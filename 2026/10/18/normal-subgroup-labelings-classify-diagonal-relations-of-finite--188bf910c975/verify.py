"""Reproduce counts and multiplication checks for diagonal relations of group-semilattice products.
Runs on Python 3, standard library only.
"""
from itertools import combinations_with_replacement, permutations, product
from math import factorial


def chain_traces(n):
    """Generate all diagonal meet-closed relations on the n-chain by two prefix codes."""
    ranges = [range(n-i) for i in range(n-1)]
    for upper in product(*ranges):
        for lower in product(*ranges):
            A = {(i,i) for i in range(n)}
            for i in range(n-1):
                A.update((i,i+j) for j in range(1,upper[i]+1))
                A.update((i+j,i) for j in range(1,lower[i]+1))
            yield frozenset(A)


def full_grid_ideals(n):
    """All order ideals of the n-by-n coordinatewise ordered grid."""
    for asc in combinations_with_replacement(range(n+1),n):
        lengths = asc[::-1]
        yield frozenset((i,j) for i in range(n) for j in range(lengths[i]))


def simple_group_relation_count(n):
    ideals = tuple(full_grid_ideals(n))
    return sum(len({A.intersection(I) for I in ideals}) for A in chain_traces(n))


def direct_semigroup_test(R, mult):
    return all((mult[x[0]][y[0]], mult[x[1]][y[1]]) in R for x in R for y in R)


def table_chain_cyclic(n,p):
    S = list(product(range(n),range(p)))
    mul = [[S.index((min(x[0],y[0]),(x[1]+y[1])%p)) for y in S] for x in S]
    return S,mul


def exhaustive_binary_chain_two():
    S,mul = table_chain_cyclic(2,2)
    d = len(S)
    off = [(i,j) for i in range(d) for j in range(d) if i!=j]
    count = 0
    for state in range(1<<len(off)):
        R = {(i,i) for i in range(d)}
        R.update(off[i] for i in range(len(off)) if (state>>i)&1)
        count += direct_semigroup_test(R,mul)
    assert count==17, count


def verify_n3_fibers():
    S,mul=table_chain_cyclic(3,2)
    lookup={(i,g):k for k,(i,g) in enumerate(S)}
    count=0
    for A in chain_traces(3):
        cells=sorted(A)
        for bits in product((0,1),repeat=len(cells)):
            R=set()
            for (i,j),full in zip(cells,bits):
                for g in range(2):
                    for h in range(2):
                        if full or g==h:
                            R.add((lookup[(i,g)],lookup[(j,h)]))
            count+=direct_semigroup_test(R,mul)
    assert count==337, count


def partitions(n):
    def grow(vals):
        if len(vals)==n:
            yield tuple(vals)
        else:
            for k in range(max(vals)+2 if vals else 1):
                yield from grow(vals+[k])
    yield from grow([])


def verify_congruences():
    for n,p,expected in [(1,2,2),(2,2,5),(2,3,5),(3,2,12)]:
        S,mul=table_chain_cyclic(n,p)
        d=len(S)
        count=0
        for part in partitions(d):
            if all(part[mul[i][k]]==part[mul[j][k]]
                   for i in range(d) for j in range(d) if part[i]==part[j]
                   for k in range(d)):
                count+=1
        assert count==expected,(n,p,count,expected)


def s3_table():
    G=list(permutations(range(3)))
    mult=[[G.index(tuple(g[h[x]] for x in range(3))) for h in G] for g in G]
    return G,mult


def overgroups_of_diagonal():
    G,gmult=s3_table()
    d=len(G)
    pair=[(i,j) for i in range(d) for j in range(d)]
    mult=[[pair.index((gmult[x[0]][y[0]],gmult[x[1]][y[1]])) for y in pair] for x in pair]
    Delta=frozenset(pair.index((g,g)) for g in range(d))
    def generated(elems):
        H=set(elems)
        while True:
            expand=H | {mult[x][y] for x in H for y in H}
            if expand==H:return frozenset(H)
            H=expand
    seen={Delta}
    queue=[Delta]
    for H in queue:
        for x in range(d*d):
            if x not in H:
                K=generated(H | {x})
                if K not in seen:
                    seen.add(K)
                    queue.append(K)
    assert sorted(map(len,seen))==[6,18,36],sorted(map(len,seen))
    return G,gmult,pair,mult,sorted(seen,key=len)


def verify_s3():
    G,gmult,pair,g2mult,subgroups=overgroups_of_diagonal()
    d=len(G)
    # Directly test all possible fibers H <= G^2 that contain Delta_G,
    # rather than assuming subgroup-label monotonicity.
    S=list(product(range(2),range(d)))
    mul=[[S.index((min(x[0],y[0]),gmult[x[1]][y[1]])) for y in S] for x in S]
    valid=0
    for A in chain_traces(2):
        cells=sorted(A)
        for labels in product(range(len(subgroups)),repeat=len(cells)):
            R=set()
            for cell,lab in zip(cells,labels):
                i,j=cell
                for pidx in subgroups[lab]:
                    g,h=pair[pidx]
                    R.add((S.index((i,g)),S.index((j,h))))
            valid+=direct_semigroup_test(R,mul)
    assert valid==46,valid



def verify_diamond_congruences():
    # The four-element Boolean meet-semilattice with top 3.
    Y=tuple(range(4))
    E=[[a&b for b in Y] for a in Y]
    valid=[]
    for theta in partitions(4):
        if all(theta[E[i][k]]==theta[E[j][k]]
               for i in Y for j in Y if theta[i]==theta[j] for k in Y):
            valid.append(theta)
    predicted=0
    for theta in valid:
        k=max(theta)+1
        for bits in product((0,1), repeat=k):
            if all(bits[theta[a]]>=bits[theta[b]] for a in Y for b in Y if E[a][b]==a):
                predicted+=1
    S=list(product(Y,range(2)))
    table=[[S.index((x[0]&y[0],(x[1]+y[1])%2)) for y in S] for x in S]
    actual=0
    for part in partitions(8):
        if all(part[table[i][k]]==part[table[j][k]]
               for i in range(8) for j in range(8) if part[i]==part[j]
               for k in range(8)):
            actual+=1
    assert actual==predicted, (actual,predicted)
    print('DIAMOND_SEMILATTICE_CONGRUENCE_COUNT',actual,'PASS')

def main():
    expected=[2,17,337,12152,696076]
    for n,e in enumerate(expected,1):
        v=simple_group_relation_count(n)
        assert v==e,(n,v,e)
        assert len(tuple(chain_traces(n)))==factorial(n)**2
        print('CHAIN',n,'DIAGONAL',v,'TRACES',factorial(n)**2)
    exhaustive_binary_chain_two()
    print('DIRECT_ALL_REFLEXIVE_RELATIONS_C2xC2_OK')
    verify_n3_fibers()
    print('DIRECT_FIBER_RELATIONS_C3xC2_OK')
    verify_congruences()
    print('DIRECT_CONGRUENCE_PARTITIONS_OK')
    verify_s3()
    verify_diamond_congruences()
    print('NONABELIAN_S3_NORMAL_SUBGROUP_FIBERS_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
