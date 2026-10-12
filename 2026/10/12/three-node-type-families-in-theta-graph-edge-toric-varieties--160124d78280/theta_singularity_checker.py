#!/usr/bin/env python3
"""Exact support-stratum Jacobian tests for theta graph edge toric varieties.

Constructs the three defining minors from alternating edge products. For
small path triples, enumerates all coordinate-zero supports. On each nonempty
support stratum it computes projective codimension and exact Jacobian rank at
a torus representative with all nonzero coordinates equal to one.
"""
from itertools import product, combinations
from math import comb


def build(r):
    groups=[]
    e=0
    for ri in r:
        groups.append((list(range(e,e+ri)),list(range(e+ri,e+2*ri))))
        e +=2*ri
    return groups,e


def jacobian_rank_3xn(rows):
    # Rank at least two iff some two rows have a nonzero 2x2 determinant.
    if not any(any(a for a in row) for row in rows): return 0
    for u,v in combinations(rows,2):
        for j in range(len(u)):
            for k in range(j+1,len(u)):
                if u[j]*v[k] != u[k]*v[j]: return 2
    return 1


def pattern_data(r,mask):
    gs,E=build(r)
    nonzero=[];zero_counts=[]
    for top,bot in gs:
        a=sum(bool(mask & (1<<z)) for z in top)
        b=sum(bool(mask & (1<<z)) for z in bot)
        zero_counts.append((a,b));nonzero.append((a==0,b==0))
    # A monomial pair f_ij can vanish on the coordinate stratum either if
    # both terms vanish, or if both survive and impose one torus equation.
    for i,j in combinations(range(3),2):
        a=nonzero[i][0] and nonzero[j][1]
        b=nonzero[i][1] and nonzero[j][0]
        if a != b: return None
    # Nonzero-entry rectangle U x V, and the torus equations among entries.
    active_cols=[i for i in range(3) if any(nonzero[i])]
    active_rows=[z for z in range(2) if any(nonzero[i][z] for i in range(3))]
    q=max(0,(len(active_cols)-1)*(len(active_rows)-1))
    z=mask.bit_count(); codim=z+q-2
    if z==E: return None  # all coordinates zero is excluded projectively
    # gradient of f_ij=A_i B_j - B_i A_j at 0/1 representative
    def mon(indices): return int(all(not(mask & (1<<j)) for j in indices))
    vals=[[mon(x) for x in pair] for pair in gs]
    def dm(indices,k):
        return int(k in indices and all((j==k or not(mask & (1<<j))) for j in indices))
    rows=[]
    for i,j in combinations(range(3),2):
        deriv=[]
        for k in range(E):
            deriv.append(dm(gs[i][0],k)*vals[j][1]+vals[i][0]*dm(gs[j][1],k)
                         -dm(gs[i][1],k)*vals[j][0]-vals[i][1]*dm(gs[j][0],k))
        rows.append(deriv)
    rank=jacobian_rank_3xn(rows)
    return codim,rank,tuple(zero_counts),tuple(vals)


def classify(r):
    gs,E=build(r)
    singular_dim3=[];wrong=[];scanned=0;min_codim=E
    for mask in range(1<<E):
        z=mask.bit_count()
        if z>5: continue   # all possible codimension <=3 singular strata have z<=5
        v=pattern_data(r,mask)
        if v is None: continue
        codim,rank,counts,vals=v
        scanned+=1
        if codim<3 and rank!=2: wrong.append((mask,'codim<3 singular',codim,rank))
        if codim==3 and rank<2: singular_dim3.append((mask,counts,vals))
        if rank<2: min_codim=min(min_codim,codim)
    cs=[comb(x,2) for x in r]
    N1=sum(c*c for c in cs)
    N2=2*sum(cs[i]*cs[j]*r[3-i-j] for i,j in combinations(range(3),2))
    N3=2*r[0]*r[1]*r[2]*sum(cs)
    exp=N1+N2+N3
    if wrong or len(singular_dim3)!=exp:
        raise AssertionError((r,E,wrong[:3],len(singular_dim3),exp,N1,N2,N3))
    return scanned,len(singular_dim3),(N1,N2,N3),min_codim


def main():
    checked=0;total=0
    for r in product(range(1,5),repeat=3):
        if tuple(sorted(r))!=r or sum(r)>7: continue
        scanned,got,counts,codim=classify(r)
        if any(k>=2 for k in r): assert codim==3,(r,codim)
        checked+=1;total+=scanned
        print(f'arms={r} strata={scanned} codim3={got} types={counts} min_sing_codim={codim}')
    print(f'VERIFY_OK triples={checked} nonempty_strata_checked={total}')

if __name__=='__main__':main()
