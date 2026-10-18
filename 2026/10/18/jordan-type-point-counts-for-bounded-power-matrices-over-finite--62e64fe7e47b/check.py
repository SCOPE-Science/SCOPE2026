"""Exact independent checks for bounded-power matrices over finite dual numbers.

Run: python check.py. Only prime fields are used in brute-force checks;
the proof, not these checks, covers every finite extension field.
"""
from itertools import product
from math import prod


def mul(A, B, n, q):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n)) % q
                 for i in range(n) for j in range(n))


def power(A, n, q, d):
    X = tuple(int(i == j) for i in range(n) for j in range(n))
    for _ in range(d):
        X = mul(X, A, n, q)
    return X


def rank(M, q):
    rows = [list(row) for row in M]
    r = 0
    for j in range(len(rows[0])):
        idx = next((i for i in range(r,len(rows)) if rows[i][j]%q), None)
        if idx is None: continue
        rows[r],rows[idx]=rows[idx],rows[r]
        c=pow(rows[r][j]%q,-1,q)
        rows[r]=[(x*c)%q for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][j]%q:
                t=rows[i][j]
                rows[i]=[(x-t*y)%q for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return r


def derivative_columns(A,n,q,d):
    powers=[tuple(int(i==j) for i in range(n) for j in range(n))]
    for _ in range(d-1):powers.append(mul(powers[-1],A,n,q))
    cols=[]
    for a in range(n):
        for b in range(n):
            E=tuple(int(i==a and j==b) for i in range(n) for j in range(n))
            Z=[0]*(n*n)
            for k in range(d):
                T=mul(mul(powers[k],E,n,q),powers[d-1-k],n,q)
                Z=[(u+v)%q for u,v in zip(Z,T)]
            cols.append(Z)
    return [list(col) for col in zip(*cols)]


def gaussian(n,r,q):
    if r<0 or r>n:return 0
    a=b=1
    for i in range(r):a*=q**(n-i)-1;b*=q**(r-i)-1
    return a//b


def gl(n,q):
    return prod(q**n-q**j for j in range(n))


def partitions_bounded(n,d):
    def rec(left,top):
        if left==0:yield ()
        else:
            for p in range(min(left,top),0,-1):
                for tail in rec(left-p,p):yield (p,)+tail
    return rec(n,d)


def jordancount(shape,q):
    n=sum(shape)
    c=sum(sum(1 for s in shape if s>=t)**2 for t in range(1,max(shape,default=0)+1))
    denom=q**c
    # Exact division using GL centralizer: q**(c-sum(m_s**2)) * product GL_{m_s}(q).
    ms=[shape.count(s) for s in set(shape)]
    central=q**(c-sum(m*m for m in ms))*prod(gl(m,q) for m in ms)
    return gl(n,q)//central


def nullity(shape,d):
    n=sum(shape)
    return n*n-sum(max(0,a+b-d) for a in shape for b in shape)


def formula(n,q,d):
    return sum(jordancount(s,q)*q**nullity(s,d) for s in partitions_bounded(n,d))


def check_pair_block_ranks():
    # Explicit matrix ranks independent of the block-count formula.
    for d in range(2,8):
        for q in (2,3,5,7):
            for a in range(1,d+1):
                for b in range(1,d+1):
                    Ja=tuple(int(i+1==j) for i in range(a) for j in range(a))
                    Jb=tuple(int(i+1==j) for i in range(b) for j in range(b))
                    cols=[]
                    pa=[tuple(int(i==j) for i in range(a) for j in range(a))]
                    pb=[tuple(int(i==j) for i in range(b) for j in range(b))]
                    for _ in range(d-1):
                        pa.append(mul(pa[-1],Ja,a,q));pb.append(mul(pb[-1],Jb,b,q))
                    for u in range(a):
                        for v in range(b):
                            Y=[[0]*b for _ in range(a)];Y[u][v]=1
                            Z=[]
                            for i in range(a):
                                for j in range(b):
                                    Z.append(sum(pa[k][i*a+h]*Y[h][t]*pb[d-1-k][t*b+j]
                                                 for k in range(d) for h in range(a) for t in range(b))%q)
                            cols.append(Z)
                    M=[list(col) for col in zip(*cols)]
                    actual=rank(M,q)
                    assert actual==max(0,a+b-d),(d,q,a,b,actual)
    print('BLOCK_RANKS_OK')


def check_counts():
    for q,n,d in [(2,1,3),(2,2,3),(3,2,3),(2,3,3),(2,3,4),(2,3,2)]:
        zero=(0,)*(n*n)
        matrices=list(product(range(q),repeat=n*n))
        direct=0
        byker=0
        for A in matrices:
            if power(A,n,q,d)!=zero:continue
            # Independent direct lift enumeration checks every second coordinate.
            ps=[tuple(int(i==j) for i in range(n) for j in range(n))]
            for _ in range(d-1):ps.append(mul(ps[-1],A,n,q))
            nvalid=0
            for B in matrices:
                Z=[0]*(n*n)
                for k in range(d):
                    U=mul(mul(ps[k],B,n,q),ps[d-1-k],n,q)
                    Z=[(v+w)%q for v,w in zip(Z,U)]
                if all(v==0 for v in Z):nvalid+=1
            direct+=nvalid
            kdim=n*n-rank(derivative_columns(A,n,q,d),q)
            assert nvalid==q**kdim,(q,n,d,A,nvalid,kdim)
            byker+=q**kdim
        predicted=formula(n,q,d)
        assert direct==byker==predicted,(q,n,d,direct,byker,predicted)
        print('BRUTE_OK',q,n,d,direct)


if __name__=='__main__':
    check_pair_block_ranks()
    check_counts()
    print('ALL_EXACT_CHECKS_PASSED')
