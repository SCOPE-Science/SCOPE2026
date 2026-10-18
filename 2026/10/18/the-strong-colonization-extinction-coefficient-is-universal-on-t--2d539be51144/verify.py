"""Exact finite-graph combinatorics and independent Markov-chain checks.
Scientific claim: leading high-colonization persistence of homogeneous patch occupancy.
Uses only Python's standard library; run: python3 verify.py.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb


def cut(mask, edges):
    return sum(bool(mask & (1 << u)) != bool(mask & (1 << v)) for u, v in edges)


def graph_connected(n, edges):
    seen={0}
    while True:
        old=len(seen)
        for a,b in edges:
            if a in seen: seen.add(b)
            if b in seen: seen.add(a)
        if len(seen)==old:return len(seen)==n


def cut_coefficient(n, edges):
    """Exact extinction escape coefficient via *subset* recursion."""
    full=(1<<n)-1
    f=[Fraction(0) for _ in range(1<<n)]
    f[0]=Fraction(1)
    for size in range(1,n):
        for mask in range(1,full):
            if mask.bit_count()!=size:continue
            boundary=cut(mask, edges)
            assert boundary>0
            f[mask]=sum((f[mask^(1<<v)] for v in range(n) if mask>>v&1),Fraction(0))/boundary
    return sum((f[full^(1<<v)] for v in range(n)),Fraction(0))


def permutation_coefficient(n,edges):
    """Independent ordering sum."""
    total=Fraction(0)
    for order in permutations(range(n)):
        mask=(1<<n)-1
        weight=Fraction(1)
        for v in order[:-1]:
            mask^=1<<v
            weight/=cut(mask,edges)
        total+=weight
    return total


def prufer_tree(n,seq):
    degree=[1]*n
    for a in seq:degree[a]+=1
    edges=[]
    for a in seq:
        leaf=next(i for i in range(n) if degree[i]==1)
        edges.append((min(a,leaf),max(a,leaf)))
        degree[leaf]-=1;degree[a]-=1
    leaves=[i for i in range(n) if degree[i]==1]
    edges.append(tuple(leaves))
    return tuple(sorted(edges))


def mean_extinction(n, edges, colonization):
    """Independent first-step CTMC solution at integer rates, exactly over rationals."""
    full=(1<<n)-1
    a=[[Fraction(0) for _ in range(full+1)] for _ in range(full)]
    for mask in range(1,full+1):
        row=a[mask-1]
        row[-1]=Fraction(1)
        for v in range(n):
            bit=1<<v
            if mask & bit:
                row[mask-1]+=1
                if mask^bit:row[(mask^bit)-1]-=1
            else:
                infected_nbr=sum((mask>>a_&1) if b_==v else (mask>>b_&1) if a_==v else 0
                                for a_,b_ in edges)
                rate=colonization*infected_nbr
                row[mask-1]+=rate
                row[(mask|bit)-1]-=rate
    # Fraction Gauss-Jordan elimination
    for j in range(full):
        pivot=next(k for k in range(j,full) if a[k][j])
        a[j],a[pivot]=a[pivot],a[j]
        d=a[j][j]
        for col in range(j,full+1):a[j][col]/=d
        for k in range(full):
            if k==j:continue
            d=a[k][j]
            if not d:continue
            for col in range(j,full+1):a[k][col]-=d*a[j][col]
    return a[full-1][-1]


def main():
    tree_count=0
    for n in range(2,7):
        for seq in product(range(n),repeat=n-2):
            edges=prufer_tree(n,seq)
            assert cut_coefficient(n,edges)==2**(n-1)
            tree_count+=1
    print('Exact tree cut-coefficients checked:',tree_count)
    ucount=0; cycle_counts={}
    for n in range(3,6):
        for edges in combinations(combinations(range(n),2),n):
            if not graph_connected(n,edges):continue
            # connected n edges => unicyclic; strip leaves to find cycle length.
            deg=[0]*n
            for a,b in edges:deg[a]+=1;deg[b]+=1
            alive=set(range(n))
            while any(deg[v]==1 for v in alive):
                leaves=[v for v in alive if deg[v]==1]
                for v in leaves:alive.remove(v)
                for a,b in edges:
                    if a in leaves and b in alive:deg[b]-=1
                    if b in leaves and a in alive:deg[a]-=1
            ell=len(alive)
            assert ell>=3
            expected=Fraction(2**(n-ell)*comb(2*ell-2,ell-1),2**(ell-1))
            assert cut_coefficient(n,edges)==expected
            ucount+=1
            cycle_counts[(n,ell)]=cycle_counts.get((n,ell),0)+1
    print('Exact unicyclic cut-coefficients checked:',ucount,sorted(cycle_counts.items()))
    samples={
        'P5':(5,((0,1),(1,2),(2,3),(3,4))),
        'S5':(5,((0,1),(0,2),(0,3),(0,4))),
        'triangle_tail':(5,((0,1),(1,2),(2,0),(0,3),(3,4))),
        'square_tail':(5,((0,1),(1,2),(2,3),(3,0),(0,4))),
        'C5':(5,((0,1),(1,2),(2,3),(3,4),(4,0))),
        'K4':(4,tuple(combinations(range(4),2))),
    }
    for label,(n,edges) in samples.items():
        c=cut_coefficient(n,edges)
        assert c==permutation_coefficient(n,edges)
        leading=1/c
        t20=mean_extinction(n,edges,20)
        t60=mean_extinction(n,edges,60)
        rel20=t20/(20**(n-1)*leading)
        rel60=t60/(60**(n-1)*leading)
        print(label,'R=',c,'asymptotic E/lambda^(n-1)=',leading,
              'ratios(lambda20,60)=',round(float(rel20),9),round(float(rel60),9))
        assert float(rel20)>0.97 and float(rel60)>0.97
        assert abs(float(rel60)-1)<abs(float(rel20)-1)
    print('All exact coefficients, independent permutation sums, and CTMC checks passed.')
if __name__=='__main__':main()
