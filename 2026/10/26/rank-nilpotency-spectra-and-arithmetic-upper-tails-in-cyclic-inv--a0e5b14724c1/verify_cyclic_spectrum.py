"""Reproduce rank/nilpotency-index census for cyclic restrictions.
Independent exhaustive domain/map enumeration vs weighted transfer matrices.
Run: python3 verify_cyclic_spectrum.py
"""
from collections import Counter
from math import gcd, comb


def phi(n):
    return sum(gcd(j,n)==1 for j in range(1,n+1))


def monomial_multiply(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():out[i+j]=out.get(i+j,0)+x*y
    return {i:x for i,x in out.items() if x}


def monomial_sum(a,b):
    c=dict(a)
    for j,y in b.items():c[j]=c.get(j,0)+y
    return {j:v for j,v in c.items() if v}


def weighted_cycle(d,t):
    # States 0,...,t-1 hold the number of consecutive ones since last zero.
    mat=[[{} for j in range(t)] for i in range(t)]
    for i in range(t):
        mat[i][0]=monomial_sum(mat[i][0],{0:1})
        if i<t-1:mat[i][i+1]=monomial_sum(mat[i][i+1],{1:1})
    acc=[[{0:1} if i==j else {} for j in range(t)] for i in range(t)]
    for _ in range(d):
        nxt=[[{} for j in range(t)] for i in range(t)]
        for i in range(t):
            for j in range(t):
                for k in range(t):
                    if acc[i][k] and mat[k][j]:
                        nxt[i][j]=monomial_sum(nxt[i][j],monomial_multiply(acc[i][k],mat[k][j]))
        acc=nxt
    out={}
    for i in range(t):out=monomial_sum(out,acc[i][i])
    return out


def spectrum_cdf(n,t):
    ans={0:1-n}
    for d in range(1,n+1):
        if n%d:continue
        b=weighted_cycle(d,t)
        powered={0:1}
        for _ in range(n//d):powered=monomial_multiply(powered,b)
        ans=monomial_sum(ans,{r:phi(d)*v for r,v in powered.items()})
    return {r:v for r,v in ans.items() if v}


def brute_index(n,k,domain):
    if not domain:return 1
    current=domain
    for t in range(1,n+2):
        if current==0:return t
        nxt=0
        for i in range(n):
            if current>>i&1 and domain>>((i+k)%n)&1:
                nxt|=1<<((i+k)%n)
        current=nxt
    return None


def brute_spectrum(n):
    out=Counter({(1,0):1})
    for k in range(n):
        for mask in range(1,1<<n):
            t=brute_index(n,k,mask)
            if t is not None:out[(t,mask.bit_count())]+=1
    return out


def check():
    for n in range(2,11):
        actual=brute_spectrum(n)
        for t in range(1,n+1):
            expected=spectrum_cdf(n,t)
            observed=Counter()
            for (j,r),count in actual.items():
                if j<=t:observed[r]+=count
            assert dict(observed)==expected,(n,t,observed,expected)
            if 2*t>n:
                if t==n:
                    upper={n-1:n*phi(n)}
                else:
                    upper={t-1+j:n*phi(n)*comb(n-t-1,j) for j in range(n-t)}
                exact={r:count for (j,r),count in actual.items() if j==t}
                assert exact==upper,(n,t,exact,upper)
        assert sum(actual.values())==1-n+sum(phi(d)*(2**d-1)**(n//d) for d in range(1,n+1) if n%d==0)
        print('n=',n,'nilpotent=',sum(actual.values()),'max-index=',sum(c for (t,r),c in actual.items() if t==n))
    print('VERIFY_OK')

if __name__=='__main__':check()
