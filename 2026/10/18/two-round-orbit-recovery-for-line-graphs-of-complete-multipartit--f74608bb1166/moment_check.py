"""Independent polynomial and orbit-count verification via exact integer arithmetic."""
from collections import Counter
from itertools import combinations_with_replacement

def moments(sizes, i, j):
    N=sum(sizes); Q=sum(x*x for x in sizes)
    a,b=sizes[i],sizes[j]
    degree=2*N-a-b-2
    weighted_neighbour_degree=sum(sizes[k]*(2*N-a-sizes[k]-2) for k in range(len(sizes)) if k!=i)
    weighted_neighbour_degree+=sum(sizes[k]*(2*N-b-sizes[k]-2) for k in range(len(sizes)) if k!=j)
    weighted_neighbour_degree-=2*degree
    closed=4*N*N-8*N-2*Q+4+(4-3*N)*(a+b)+2*(a*a+b*b)
    assert weighted_neighbour_degree==closed
    return degree,closed

def verify():
    configs=0; comparisons=0; max_r=0
    # Nondecreasing size vectors. The proof uses no finite bound.
    for r in range(2,8):
        for sizes in combinations_with_replacement(range(1,8),r):
            sigs={}; sums={}; types={}; pairs=[]
            for i in range(r):
                for j in range(i+1,r):
                    typ=tuple(sorted((sizes[i],sizes[j])))
                    m=moments(sizes,i,j)
                    assert m not in sigs or sigs[m]==typ
                    sigs[m]=typ
                    pairs.append((typ,m))
            for k,(typ,m) in enumerate(pairs):
                for typ2,m2 in pairs[:k]:
                    assert (m==m2)==(typ==typ2)
                    comparisons+=1
            configs+=1
            max_r=max(max_r,r)
    print(f'PASS integer moment signatures: size tuples={configs}, tested edge-type pair comparisons={comparisons}, maximum parts={max_r}')

if __name__=='__main__':verify()
