"""Independent finite checks for the bidirected friendship multipath theorem.

Run: python3 verify.py
No third-party packages. The proof for all integers n is in RESULT.md;
finite computations are consistency checks, not a substitute for induction.
"""
from collections import Counter, defaultdict, deque
from itertools import product


def arcs(n):
    return [e for i in range(n)
            for e in ((0,2*i+1),(2*i+1,0),(0,2*i+2),(2*i+2,0),
                      (2*i+1,2*i+2),(2*i+2,2*i+1))]


def admissible(arc_list, face):
    chosen = [arc_list[i] for i in range(len(arc_list)) if face >> i & 1]
    if len(set(s for s,t in chosen)) != len(chosen):
        return False
    if len(set(t for s,t in chosen)) != len(chosen):
        return False
    out = dict(chosen)
    for v in out:
        seen = set()
        while v in out:
            if v in seen:
                return False
            seen.add(v)
            v = out[v]
    return True


def enumerate_faces(n):
    al = arcs(n)
    central = [(), *((6*i+j,) for i in range(n) for j in (0,1,2,3))]
    central.extend((u,v) for u in range(len(al)) if al[u][0] == 0
                   for v in range(len(al)) if al[v][1] == 0
                   if al[u][1] != al[v][0])
    found = {0}
    for outer in product((None,4,5),repeat=n):
        mask = sum(1 << (6*i+o) for i,o in enumerate(outer) if o is not None)
        for mid in central:
            f = mask | sum(1 << k for k in mid)
            if admissible(al, f):
                found.add(f)
    return al,found


def matched_partner(n, al, face):
    central = [j for j,e in enumerate(al)
               if (face >> j) & 1 and 0 in e]
    free_arms = list(range(n))
    if len(central) == 1 or (len(central) == 2 and central[0]//6 != central[1]//6):
        arm = central[0]//6
        # Exactly one exterior arc on this arm remains compatible.
        options = [6*arm + j for j in (4,5)
                   if admissible(al, face | (1 << (6*arm+j)))
                   or (face & (1 << (6*arm+j))) and
                   admissible(al, face & ~(1 << (6*arm+j)))]
        assert len(options) == 1, (n,face,central,options)
        return face ^ (1 << options[0])
    if len(central) == 2:
        assert central[0]//6 == central[1]//6
        free_arms.remove(central[0]//6)
    # Lexicographic matching for joins of two-point sets.
    for arm in free_arms:
        p,q = 6*arm+4,6*arm+5
        if face >> q & 1:
            continue
        return face ^ (1 << p)
    return None


def test(n):
    al,fs = enumerate_faces(n)
    # Independently confirm the matching covers precisely the enumerated faces.
    assert 0 in fs and all(admissible(al,f) for f in fs)
    pairs={}; critical=[]
    for f in fs - {0}:
        g=matched_partner(n,al,f)
        if g is None or g==0:
            critical.append(f)
        else:
            assert g in fs and (f ^ g).bit_count()==1
            assert matched_partner(n,al,g)==f
            pairs[f]=g
    assert all(pairs.get(v)==u for u,v in pairs.items())
    crit_counts=Counter(f.bit_count()-1 for f in critical)
    expected={0:1,n-1:1,n:2*n} if n>=3 else ({0:1,1:1,2:4} if n==2 else {0:2,1:2})
    assert crit_counts==expected, (n,crit_counts,expected)
    # Exact exhaustive Hasse-cover orientation and Kahn acyclicity check.
    indexed=sorted(fs-{0}); index={f:k for k,f in enumerate(indexed)}
    nexts=[[] for _ in indexed]; indeg=[0]*len(indexed)
    cover_edges=0
    for f in indexed:
        i=index[f];x=f
        while x:
            bit=x&-x;g=f^bit;x-=bit
            if not g:continue
            cover_edges+=1
            j=index[g]
            if pairs.get(g)==f:
                nexts[j].append(i);indeg[i]+=1
            else:
                nexts[i].append(j);indeg[j]+=1
    todo=deque(i for i,d in enumerate(indeg) if d==0)
    done=0
    while todo:
        i=todo.popleft();done+=1
        for j in nexts[i]:
            indeg[j]-=1
            if indeg[j]==0:todo.append(j)
    assert done==len(indexed),('directed matching cycle',n,len(indexed)-done)
    # Each of the 2n oriented three-cycles on a petal, joined with
    # opposite-edge zero-cycles on other petals, yields a nonzero n-cycle.
    # Their distinguished (same-petal central-pair) n-faces are disjoint.
    if n>=2:
        distinguished=[]
        for i in range(n):
            for out_offset,in_offset in ((0,3),(2,1)):
                central=(1<<(6*i+out_offset)) | (1<<(6*i+in_offset))
                facet=central | sum(1<<(6*j+5) for j in range(n) if j!=i)
                assert facet in fs and facet.bit_count()==n+1
                assert matched_partner(n,al,facet) is None
                distinguished.append(facet)
        assert len(set(distinguished))==2*n
        # A larger face containing such a facet would have 2 central arcs
        # and a third exterior arc on the same petal: impossible.
        for f in distinguished:
            for k in range(6*n):
                if not(f>>k&1):
                    assert (f|(1<<k)) not in fs
    return len(fs)-1, sum(len(v) for v in nexts),len(pairs)//2,sorted(crit_counts.items()),cover_edges

if __name__=='__main__':
    for n in range(1,7):
        nonempty,oriented_edges,npairs,crit,covers=test(n)
        print('n=%d faces=%d matched_pairs=%d critical=%s Hasse_covers=%d acyclic=yes' %
              (n,nonempty,npairs,crit,covers))
    print('ALL_CHECKS_PASSED')
