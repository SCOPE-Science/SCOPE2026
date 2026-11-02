from math import comb, factorial
from itertools import combinations
from collections import Counter

def falling(n,k):
    t=1
    for j in range(k):t*=n-j
    return t

def stir2(n,k):
    a=[[0]*(n+1) for i in range(n+1)];a[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):a[i][j]=a[i-1][j-1]+j*a[i-1][j]
    return a[n][k] if 0<=k<=n else 0

def opt(m,n):
    assert 2<=m<=n
    if n>=m+4:return m,n**m
    if n==m+3:return m,n**m+m*(m-1)*comb(n,2)*falling(n-2,m-2)
    if n==m+2:return m-1,m*falling(n,m-1)
    if n==m+1:return m-1,m*(falling(n,m-1)+comb(m-1,2)*falling(n,m-2))
    row=sum(comb(m,b)*factorial(b)*stir2(m-1,b) for b in range(max(1,m-3),m))
    return m-1,2*m*row-m*m*factorial(m-1)

def q_poly(a,b):
    if a==0 or b==0: return {0:1} if a==b==0 else {}
    out=Counter()
    for i in range(a+1):
        for j in range(b+1):
            sign=(-1)**(i+j)*comb(a,i)*comb(b,j)
            if not sign: continue
            area=(a-i)*(b-j)
            for k in range(area+1):out[k]+=sign*comb(area,k)
    return {k:v for k,v in out.items() if v}

def safe(r,c):
    return not ((r>=2 and c>=2) or (r==1 and c>=4) or (c==1 and r>=4))

def polynomial_formula(m,n):
    out=Counter()
    for a in range(m+1):
        for b in range(n+1):
            if not safe(m-a,n-b): continue
            for k,v in q_poly(a,b).items():out[k]+=comb(m,a)*comb(n,b)*v
    return {k:v for k,v in out.items() if v}

def cycle_masks(m,n):
    cells=list(range(m*n))
    adj=[set() for _ in cells]
    for i in cells:
        for j in cells:
            if i!=j and (i//n==j//n or i%n==j%n):adj[i].add(j)
    c=set()
    for a,b,c0,d in combinations(cells,4):
        quadruple=[a,b,c0,d]
        # every 4-cycle uses 4 distinct vertices and is a subgraph (not necessarily induced)
        if any(b1 in adj[a1] and c1 in adj[b1] and d1 in adj[c1] and a1 in adj[d1]
                for a1 in quadruple for b1 in quadruple if b1!=a1
                for c1 in quadruple if c1!=a1 and c1!=b1
                for d1 in quadruple if d1!=a1 and d1!=b1 and d1!=c1):
            c.add(sum(1<<x for x in quadruple))
    closed=[1<<i|sum(1<<j for j in adj[i]) for i in cells]
    return list(c),closed

def brute(m,n):
    cyc,closed=cycle_masks(m,n)
    N=m*n;mask=(1<<N)-1;out=Counter()
    cover=[0]*(1<<N)
    for S in range(1<<N):
        if S:
            b=S&-S;cover[S]=cover[S^b]|closed[b.bit_length()-1]
        residual=mask^cover[S]
        if not any(residual & cycle == cycle for cycle in cyc):
            out[S.bit_count()]+=1
    return dict(out),len(cyc)

if __name__=='__main__':
    for m,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(3,6),(3,7),(4,4),(4,5)]:
        b,c=brute(m,n)
        f=polynomial_formula(m,n)
        minimum,cnt=opt(m,n)
        assert b==f,(m,n,b,f)
        assert min(b)==minimum and b[minimum]==cnt,(m,n,b,minimum,cnt)
        print((m,n),'C4 cycles',c,'min',minimum,'minimum sets',cnt,'poly',b)
    for m in range(2,9):
        for n in range(m,m+8):
            f=polynomial_formula(m,n); t,c=opt(m,n)
            assert f[t]==c and min(f)==t,(m,n,t,c)
    print('VERIFY_OK')
