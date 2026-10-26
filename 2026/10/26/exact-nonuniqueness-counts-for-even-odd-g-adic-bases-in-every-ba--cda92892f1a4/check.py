#!/usr/bin/env python3
"""Independent finite enumeration for exact representation-count formulas."""
from itertools import combinations_with_replacement


def family(g,k):
    E=[]; O=[]
    for x in range(1,g**k):
        z=x;even=odd=0
        for j in range(k):
            d=z%g;z//=g
            even+=d*g**(2*j)
            odd+=d*g**(2*j+1)
        E.append(even);O.append(odd)
    return sorted(E+O)


def predicted(g,k):
    return (3*g-1)*(2*g-1)**(k-1)-2**(2*k-1)-5*k-1


def run():
    comparisons=0
    rows=[]
    for g in range(4,11):
        for k in range(1,4):
            N=g**(2*k)
            A=family(g,k)
            assert len(A)==2*(g**k-1)
            assert len(A)==len(set(A))
            R=[0]*N
            for i,a in enumerate(A):
                for b in A[i:]:
                    s=a+b
                    if s>=N:break
                    R[s]+=1
                    comparisons+=1
            # A direct enumeration of unordered positive summands;
            # the derived formula is evaluated separately.
            nonunique=sum(r>=2 for r in R)
            assert nonunique==predicted(g,k),(g,k,nonunique,predicted(g,k))
            assert [n for n,r in enumerate(R) if r==0]==[0,1]
            assert sum(r==1 for r in R)==N-2-predicted(g,k)
            rows.append((g,k,N,nonunique))
    for row in rows:
        print('base=%d cutoff_blocks=%d checked=%d multiple=%d'%row)
    print('CERTIFICATE_OK configurations=%d direct_summand_pairs=%d'%(len(rows),comparisons))

if __name__=='__main__': run()
