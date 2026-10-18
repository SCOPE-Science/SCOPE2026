"""Exact cuboctahedral matching-complex equivariant homology verifier.

Standard Python 3 only. Computes an integral acyclic algebraic-Morse matching,
and calculates the homology character by two independent fixed-face formulas.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations


def cube_data():
    cube_edges = [(a, b) for a in range(8) for b in range(a+1, 8)
                  if (a ^ b).bit_count() == 1]
    assert len(cube_edges) == 12
    cubo_edges = [(i, j) for i in range(12) for j in range(i+1,12)
                  if set(cube_edges[i]) & set(cube_edges[j])]
    assert len(cubo_edges) == 24
    return cube_edges, cubo_edges


def all_matchings(cubo_edges):
    incid = [0]*24
    for i,(a,b) in enumerate(cubo_edges):
        for j,(c,d) in enumerate(cubo_edges):
            if {a,b} & {c,d}: incid[i] |= 1 << j
    faces = {0}
    for i in range(24):
        bit = 1 << i
        faces |= {face | bit for face in faces if not (face & incid[i])}
    return faces,incid


def acyclic_morse(faces):
    free = set(faces)
    pairs = set()
    # Lexicographic matching in reverse edge order, including the empty face.
    for i in reversed(range(24)):
        bit = 1 << i
        for low in list(free):
            high = low | bit
            if low & bit == 0 and high in free:
                pairs.add((low, high))
                free.remove(low)
                free.remove(high)
    assert len(pairs) == 1296
    assert len(free) == 57
    assert all(face.bit_count() == 4 for face in free)
    # Matching graph with all codimension-one cover edges. The reversed
    # matched Hasse edges are directed upwards; all others downwards.
    indegree = {f:0 for f in faces}
    targets = defaultdict(list)
    arrows = 0
    for high in faces:
        tmp = high
        while tmp:
            bit = tmp & -tmp
            tmp ^= bit
            low = high ^ bit
            if (low,high) in pairs:
                a,b = low,high
            else:
                a,b = high,low
            targets[a].append(b)
            indegree[b] += 1
            arrows += 1
    queue = deque(f for f,degree in indegree.items() if degree == 0)
    seen = 0
    while queue:
        face = queue.popleft(); seen += 1
        for target in targets[face]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    assert seen == len(faces), 'directed Morse cycle'
    assert arrows == 9960
    return len(pairs),len(free),arrows


def automorphisms(cube_edges,cubo_edges):
    emap_index = {edge:i for i,edge in enumerate(cube_edges)}
    cmap_index = {edge:i for i,edge in enumerate(cubo_edges)}
    axes = sorted({min(x,x^7) for x in range(8)})
    group=[]
    for p in permutations(range(3)):
        for t in range(8):
            vm = [sum(((((x >> p[i]) & 1) ^ ((t >> i) & 1)) << i)
                       for i in range(3)) for x in range(8)]
            em = [emap_index[tuple(sorted((vm[a],vm[b])))] for a,b in cube_edges]
            cm = tuple(cmap_index[tuple(sorted((em[a],em[b])))] for a,b in cubo_edges)
            ap = [axes.index(min(vm[x],vm[x]^7)) for x in axes]
            remaining=set(range(4)); cycle_lengths=[]
            while remaining:
                i=next(iter(remaining));j=i;length=0
                while j in remaining:
                    remaining.remove(j)
                    length+=1
                    j=ap[j]
                cycle_lengths.append(length)
            cycle_type=tuple(sorted(cycle_lengths,reverse=True))
            group.append((cm,cycle_type,t.bit_count()%2,p,t))
    assert len(group)==48 and len({a[0] for a in group})==48
    return group


def brute_character(faces, perm):
    trace=0
    for face in faces:
        support=[i for i in range(24) if face >> i & 1]
        images=[perm[i] for i in support]
        if set(images)!=set(support): continue
        sign_parity=sum(images[i]>images[j] for i in range(len(images))
                        for j in range(i+1,len(images)))%2
        trace+=(-1)**(len(support)+sign_parity)
    return trace


def orbit_character(cubo_edges, perm):
    """Every chosen permissible edge orbit contributes a factor -1."""
    notseen=set(range(24)); choices=[]
    while notseen:
        i=next(iter(notseen));j=i;orbit=[]
        while j in notseen:
            notseen.remove(j)
            orbit.append(j)
            j=perm[j]
        used=0;ok=True
        for k in orbit:
            a,b=cubo_edges[k]
            bmask=(1<<a)|(1<<b)
            if used & bmask: ok=False
            used|=bmask
        if ok:choices.append(used)
    def evaluate(i, used):
        if i==len(choices):return 1
        v=evaluate(i+1, used)
        if not used & choices[i]:v-=evaluate(i+1,used|choices[i])
        return v
    return evaluate(0,0)


def parity(perm):
    return (-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))


def main():
    Q,C=cube_data()
    faces,inc=all_matchings(C)
    assert len(faces)==2649
    assert dict(Counter(x.bit_count() for x in faces)) == {0:1,1:24,2:204,3:744,4:1116,5:528,6:32}
    pair_count,crit_count,arrows=acyclic_morse(faces)
    group=automorphisms(Q,C)
    class_values=defaultdict(set)
    class_multiplicity=Counter()
    for permutation,typ,eps,p,t in group:
        brute=brute_character(faces,permutation)
        orbit=orbit_character(C,permutation)
        assert brute==orbit,(typ,eps,brute,orbit)
        class_values[(typ,eps)].add(brute)
        class_multiplicity[(typ,eps)]+=1
    types=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
    sizes=[1,6,3,8,6]
    even=[57,1,13,-3,-5]
    odd=[11,3,-1,-1,-3]
    for typ,size,chi0,chi1 in zip(types,sizes,even,odd):
        assert class_multiplicity[(typ,0)]==size
        assert class_multiplicity[(typ,1)]==size
        assert class_values[(typ,0)]=={chi0}
        assert class_values[(typ,1)]=={chi1}
    # irreducible character table of S4 in above class order
    irrs={'trivial':[1,1,1,1,1],
          'sign':[1,-1,1,1,-1],
          'standard3':[3,1,-1,0,-1],
          'sign_standard3':[3,-1,-1,0,1],
          'two_dimensional':[2,0,2,-1,0]}
    even_proj=[(a+b)//2 for a,b in zip(even,odd)]
    odd_proj=[(a-b)//2 for a,b in zip(even,odd)]
    mplus={name:sum(w*x*y for w,x,y in zip(sizes,even_proj,c))/24
           for name,c in irrs.items()}
    mminus={name:sum(w*x*y for w,x,y in zip(sizes,odd_proj,c))/24
           for name,c in irrs.items()}
    assert all(m.is_integer() and m>=0 for m in list(mplus.values())+list(mminus.values()))
    assert tuple(map(int,mplus.values()))==(1,2,5,2,5)
    assert tuple(map(int,mminus.values()))==(1,2,2,2,4)
    assert sum(mplus[name]*irrs[name][0] for name in irrs)==34
    assert sum(mminus[name]*irrs[name][0] for name in irrs)==23
    print('MATCHING_F_VECTOR',tuple(Counter(x.bit_count() for x in faces)[i] for i in range(7)))
    print('ACYCLIC_MATCHING',pair_count,'CRITICAL_DEGREE3',crit_count,'HASSE_ARROWS',arrows)
    print('FULL_GROUP_48_CHARACTER_EVEN',tuple(even))
    print('FULL_GROUP_48_CHARACTER_ODD',tuple(odd))
    print('CENTRAL_EIGENRANKS',34,23,'FULL_INVARIANT_RANK',int(mplus['trivial']))
    print('EVEN_MULTIPLICITIES',mplus)
    print('ODD_MULTIPLICITIES',mminus)
    print('VERIFY_OK')

if __name__=='__main__':main()
