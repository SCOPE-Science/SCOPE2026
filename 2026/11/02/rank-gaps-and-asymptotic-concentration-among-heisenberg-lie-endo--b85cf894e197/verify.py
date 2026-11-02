"""Independent exhaustive small-field test and exact formula for Heisenberg Lie algebra endomorphism ranks. Only prime fields are enumerated directly."""
from itertools import product
from math import prod

def rank_mod(M,p):
    a=[list(map(lambda x:x%p,row)) for row in M]
    if not a:return 0
    n=len(a);w=len(a[0]);r=0
    for j in range(w):
        piv=next((i for i in range(r,n) if a[i][j]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        iv=pow(a[r][j],-1,p)
        a[r]=[(x*iv)%p for x in a[r]]
        for i in range(n):
            if i!=r and a[i][j]:
                t=a[i][j]
                a[i]=[(a[i][z]-t*a[r][z])%p for z in range(w)]
        r+=1
        if r==n:break
    return r

def gauss(n,k,q):
    if not(0<=k<=n):return 0
    a=b=1
    for i in range(k):
        a*=q**(n-i)-1;b*=q**(k-i)-1
    assert a%b==0
    return a//b

def formula(m,q):
    N=[0]*(2*m+2)
    for r in range(m+1):
        I=gauss(m,r,q)*prod(q**j+1 for j in range(m-r+1,m+1))
        A=I*prod(q**(2*m)-q**i for i in range(r))
        N[r]+=A*q**r
        N[r+1]+=A*(q**(2*m)-q**r)
    sp=q**(m*m)*prod(q**(2*i)-1 for i in range(1,m+1))
    N[2*m+1]+=q**(2*m)*(q-1)*sp
    return N

def brute(m,q):
    # Enumerate every A and every ell, c is forced by A as soon as m>=1.
    d=2*m;n=2*m+1;dist=[0]*(n+1)
    assert q in (2,3)
    # Standard symplectic [x_i,y_i]=z, others zero.
    def pairing(u,v):
        return sum(u[i]*v[m+i]-u[m+i]*v[i] for i in range(m))%q
    for entries in product(range(q),repeat=d*d):
        cols=[entries[j::d] for j in range(d)] # row major transpose to columns
        c=pairing(cols[0],cols[m])
        if any(pairing(cols[i],cols[j])!=(c if (i<m and j==m+i) else -c if (j<m and i==m+j) else 0)%q for i in range(d) for j in range(d)):
            continue
        ar=rank_mod([entries[d*i:d*(i+1)] for i in range(d)],q)
        for ell in product(range(q),repeat=d):
            F=[list(entries[d*i:d*(i+1)])+[0] for i in range(d)]
            F.append(list(ell)+[c])
            dist[rank_mod(F,q)]+=1
    return dist

def test():
    for m,q in [(1,2),(1,3),(2,2)]:
        pred=formula(m,q)
        obs=brute(m,q)
        assert obs==pred,(m,q,pred,obs)
        print('PASS m=',m,'q=',q,'spectrum=',pred)
    for m in [3,4,6,8,10]:
        N=formula(m,2)
        assert N[0]==1
        assert all(N[k]==0 for k in range(m+2,2*m+1))
        den=sum(N)
        print('m',m,'scaled deficiency',float((1-N[m+1]/den)*2**m))
    print('VERIFY_OK')
if __name__=='__main__': test()
