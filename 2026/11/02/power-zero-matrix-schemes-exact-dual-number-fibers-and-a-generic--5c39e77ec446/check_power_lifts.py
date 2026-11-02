#!/usr/bin/env python3
"""Independent finite-field checks for nilpotent matrix power lifting formulas."""
from itertools import product
from math import prod

def partitions(n, hi=None):
    if n == 0:
        yield ()
        return
    if hi is None: hi=n
    for a in range(min(n,hi), 0, -1):
        for p in partitions(n-a, a):
            yield (a,)+p

def gl(n,q):
    return prod(q**n-q**i for i in range(n))

def orbit_count(lam,q):
    n=sum(lam)
    conjugate=[sum(a>=j for a in lam) for j in range(1,max(lam)+1)]
    groups={a:lam.count(a) for a in set(lam)}
    # Exact automorphism-group order of the truncated polynomial module.
    unipotent_dim=sum(x*x for x in conjugate)-sum(t*t for t in groups.values())
    cent=q**unipotent_dim*prod(gl(t,q) for t in groups.values())
    return gl(n,q)//cent

def rank_by_partition(lam,m):
    return sum(max(0,a+b-m) for a in lam for b in lam)

def total_formula(n,m,q):
    return sum(orbit_count(p,q)*q**(n*n-rank_by_partition(p,m))
               for p in partitions(n) if max(p)<=m)

def make_field(q):
    if q==2: return lambda a,b:(a+b)%2,lambda a,b:(a*b)%2
    if q==3: return lambda a,b:(a+b)%3,lambda a,b:(a*b)%3
    if q==4:
        # F_2[z]/(z^2+z+1), encoding 0,1,z,z+1 in binary.
        def mul(a,b):
            t=0
            if b&1:t^=a
            if b&2:t^=a<<1
            if t&8:t^=0b1100
            if t&4:t^=0b111
            return t&3
        return lambda a,b:a^b,mul
    raise ValueError(q)

def matrix_table(n,q):
    add,mul=make_field(q)
    size=q**(n*n)
    powq=[q**i for i in range(n*n)]
    mats=[tuple((v//t)%q for t in powq) for v in range(size)]
    # Independent multiplication, not using the symbolic differential.
    def product(A,B):
        return sum(powq[i*n+j]*sum_term(A,B,i,j) for i in range(n) for j in range(n))
    def sum_term(A,B,i,j):
        t=0
        for h in range(n): t=add(t,mul(A[i*n+h],B[h*n+j]))
        return t
    table=[None]*size
    for v,A in enumerate(mats):
        table[v]=[product(A,B) for B in mats]
    def plus(a,b):
        A=mats[a];B=mats[b]
        return sum(powq[i]*add(A[i],B[i]) for i in range(n*n))
    return table,plus,size

def brute(n,q,exps):
    T,plus,N=matrix_table(n,q)
    counts={m:0 for m in exps}
    for a in range(N):
        for b in range(N):
            x,y=a,b
            for m in range(2,max(exps)+1):
                x,y=T[x][a],plus(T[x][b],T[y][a])
                if m in counts and x==0 and y==0:counts[m]+=1
    return counts

def rankmod(A,p):
    M=[list(map(lambda x:x%p,row)) for row in A]
    if not M:return 0
    r=0
    for c in range(len(M[0])):
        k=next((i for i in range(r,len(M)) if M[i][c]),None)
        if k is None:continue
        M[k],M[r]=M[r],M[k]
        u=pow(M[r][c],-1,p)
        M[r]=[(v*u)%p for v in M[r]]
        for i in range(r+1,len(M)):
            if M[i][c]:
                u=M[i][c];M[i]=[(v-u*w)%p for v,w in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r

def direct_pair_rank(a,b,m,p):
    ij=list(product(range(a),range(b))); rows=[]
    for target in ij:
        row=[]
        for source in ij:
            t=0
            for v in range(m):
                if (source[0]+v,source[1]+m-1-v)==target:t+=1
            row.append(t)
        rows.append(row)
    return rankmod(rows,p)

def main():
    rankcases=0
    for m in range(1,9):
        for a in range(1,m+1):
            for b in range(1,m+1):
                for p in (2,3,5):
                    got=direct_pair_rank(a,b,m,p)
                    expected=max(0,a+b-m)
                    assert got==expected,(m,a,b,p,got,expected)
                    rankcases+=1
    print('PAIR_RANK_CHECKS',rankcases,'PASS')
    for n,q,exps in ((1,2,(2,3)),(2,2,(2,3,4)),(2,3,(2,3,4)),(2,4,(2,3,4)),(3,2,(2,3,4,5,6))):
        actual=brute(n,q,exps)
        for m in exps:
            expected=total_formula(n,m,q)
            assert actual[m]==expected,(n,q,m,actual[m],expected)
        print('EXHAUSTIVE',f'n={n}',f'q={q}',f'm={exps}','counts',actual,'PASS')
    for n in range(1,10):
        for m in range(1,9):
            p=(m,)*(n//m)+((n%m,) if n%m else ())
            # Full dense-orbit tangent excess, including n<m.
            C=sum(sum(a>=j for a in p)**2 for j in range(1,max(p)+1))
            excess=C-rank_by_partition(p,m)
            r=n%m
            expected=min(r,m-r) if r else 0
            assert excess==expected,(n,m,excess,expected)
    print('DENSE_ORBIT_GENERIC_NILPOTENT_EXCESS',72,'PASS')
    print('ALL_NILPOTENT_MATRIX_POWER_LIFT_CHECKS_OK')

if __name__=='__main__':main()
