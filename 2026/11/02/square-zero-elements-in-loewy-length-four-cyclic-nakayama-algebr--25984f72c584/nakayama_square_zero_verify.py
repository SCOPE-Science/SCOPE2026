#!/usr/bin/env python3
"""Finite-field checks for square-zero elements in cyclic Loewy-length-four path algebras."""
from itertools import product
from collections import Counter


def mul(x,y,q):
    if q == 4:
        t = 0
        for i in range(2):
            if (y >> i) & 1:
                t ^= x << i
        if t & 8:
            t ^= 0b1100
        if t & 4:
            t ^= 0b0111
        return t
    return x*y%q


def add(x,y,q):
    return x ^ y if q == 4 else (x+y)%q


def path_product_square(a,b,n,q):
    """Multiply path-basis elements directly, collecting degrees two and three."""
    paths = [(i,1,a[i]) for i in range(n) if a[i]]
    paths += [(i,2,b[i]) for i in range(n) if b[i]]
    out = {}
    for i,d,x in paths:
        for j,e,y in paths:
            if d+e<4 and (i+d)%n==j:
                key=(i,d+e)
                out[key]=add(out.get(key,0),mul(x,y,q),q)
    return all(x==0 for x in out.values())


def matrix_rank(rows,q):
    a=[row[:] for row in rows]
    r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        piv=a[r][c]
        for i in range(r+1,len(a)):
            if a[i][c]:
                ratio=next(z for z in range(1,q) if mul(z,piv,q)==a[i][c])
                for j in range(c,len(a[0])):
                    a[i][j]=add(a[i][j], mul(ratio,a[r][j],q) if q==4 else -mul(ratio,a[r][j],q),q)
        r+=1
    return r


def transfer_count(n,q):
    w_num=q-1
    # Count with integral weights by replacing T with q^2*T.
    states=((0,0,0),(0,0,1),(0,1,0),(1,0,0),(1,0,1))
    T=[[0]*5 for _ in states]
    for i,(a,b,c) in enumerate(states):
        for d in (0,1):
            if c*d:continue
            ss=(b,c,d)
            if ss in states:
                j=states.index(ss)
                # q^2 * (w^d * q^(d*(a+b))).
                T[i][j]=(q*q) if not d else (q-1)*q**(a+b)
    P=[[int(i==j) for j in range(5)] for i in range(5)]
    for _ in range(n):
        P=[[sum(P[i][k]*T[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    return sum(P[i][i] for i in range(5))


def support_count(n,q):
    tot=0
    for bits in product((0,1),repeat=n):
        if any(bits[i] and bits[(i+1)%n] for i in range(n)):continue
        s=sum(bits)
        t2=sum(bits[i]*bits[(i+2)%n] for i in range(n))
        t3=sum(bits[i]*bits[(i+3)%n] for i in range(n))
        rank=2*s-t2-t3
        assert 0<=rank<=n
        tot+=(q-1)**s*q**(2*n-rank)
    return tot


def recurrence_values(q,N):
    b={1:q**2,2:q**3*(3*q-2),3:q**5*(4*q-3),4:q**6*(3*q*q-2)}
    for n in range(5,N+1):
        b[n]=q*q*b[n-1]+q**3*(q-1)*b[n-2]-q**6*(q-1)**2*b[n-4]
    return b


def direct_count(n,q):
    bvals=list(product(range(q),repeat=n))
    b_good=0
    rank_cases=0
    for a in product(range(q),repeat=n):
        S={i for i,v in enumerate(a) if v}
        if any((i+1)%n in S for i in S):continue
        t2=sum((i+2)%n in S for i in S)
        t3=sum((i+3)%n in S for i in S)
        predicted=2*len(S)-t2-t3
        M=[[add(a[i] if j==(i+1)%n else 0, a[(i+2)%n] if j==i else 0,q) for j in range(n)] for i in range(n)]
        actual=matrix_rank(M,q)
        assert actual==predicted,('rank',n,q,a,predicted,actual)
        rank_cases+=1
        for b in bvals:
            if path_product_square(a,b,n,q):b_good+=1
    return b_good*q**n,rank_cases


def run():
    configurations=((3,2),(4,2),(5,2),(6,2),(7,2),
                    (3,3),(4,3),(5,3),(4,4),(3,4),(4,5))
    for n,q in configurations:
        actual,rank_cases=direct_count(n,q)
        expected=transfer_count(n,q)
        via_support=support_count(n,q)
        via_recurrence=recurrence_values(q,n)[n]
        assert actual==expected==via_support==via_recurrence,(n,q,actual,expected,via_support,via_recurrence)
        print('CASE',n,q,'count',actual,'rank_support_cases',rank_cases)
    for q in (2,3,4,5,7,9):
        seq=recurrence_values(q,15)
        for n in range(3,16):
            assert seq[n]==transfer_count(n,q)==support_count(n,q)
        print('RECURRENCE',q,'n3_to_15_OK')
    print('CYCLIC_NAKAYAMA_LENGTH4_SQUARE_ZERO_OK',len(configurations),'6x13')

if __name__=='__main__':
    run()
