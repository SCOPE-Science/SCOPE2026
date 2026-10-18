#!/usr/bin/env python3
"""Independent finite-field and coefficient tests for Cartesian Hermitian sampling.
Pure Python, standard library only. Finite tests supplement the general proof.
"""
from math import comb
PRIME=1009

def rank_mod(M,p=PRIME):
    a=[[int(v)%p for v in row] for row in M]
    R=len(a); C=len(a[0]); pivot=0
    for col in range(C):
        j=next((i for i in range(pivot,R) if a[i][col]),None)
        if j is None: continue
        a[pivot],a[j]=a[j],a[pivot]
        inv=pow(a[pivot][col],p-2,p)
        a[pivot]=[(v*inv)%p for v in a[pivot]]
        for i in range(pivot+1,R):
            if a[i][col]:
                c=a[i][col]
                a[i]=[(u-c*v)%p for u,v in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==R:break
    return pivot

def cmul(u,v):return (u[0]*v[0]-u[1]*v[1])%PRIME,(u[0]*v[1]+u[1]*v[0])%PRIME

def gram_rows(m,X,Y):
    rows=[]
    for x in X:
        for y in Y:
            powers=[(1,0)]
            for j in range(1,m):powers.append(cmul(powers[-1],(x%PRIME,y%PRIME)))
            col=[]
            for j in range(m):
                z=cmul(powers[j],(powers[j][0],-powers[j][1]))
                col.append(z[0])
                for k in range(j+1,m):
                    w=cmul(powers[j],(powers[k][0],-powers[k][1]))
                    col.extend((2*w[0],-2*w[1]))
            assert len(col)==m*m
            rows.append(col)
    return rows

def binomial_block(r,k):
    return [[comb(r,(r+h-s)//2) if (r+h-s)%2==0 and 0 <= (r+h-s)//2 <= r else 0 for s in range(k)] for h in range(k)]

def test():
    for m in range(2,11):
        for pattern in range(2):
            if pattern==0:
                X=list(range(m));Y=[3*j+2 for j in range(m)]
            else:
                X=[j*j+j for j in range(m)];Y=[2*j*j+3*j+5 for j in range(m)]
            rk=rank_mod(gram_rows(m,X,Y))
            expected=m*m if m%2 else m*m-m//2
            assert rk==expected,(m,pattern,rk,expected)
            print('grid',m,pattern,'rank',rk,'nullity',m*m-rk)
        for r in range(1,m):
            k=m-r
            rk=rank_mod(binomial_block(r,k))
            expected=k-1 if r%2 and k%2 else k
            assert rk==expected,(m,r,k,rk,expected)
            print('block',m,r,k,'rank',rk)
    print('PASS finite-field test for m=2..10, two arbitrary grid families, all middle-coefficient blocks.')

if __name__=='__main__':test()
