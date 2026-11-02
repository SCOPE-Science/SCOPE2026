"""Independent finite-ring checks for the Q_(2k) Kirillov elementary divisors."""
from itertools import product
from collections import Counter


def matrix(vals,n,mod):
    M=[[0]*n for _ in range(n)]
    for i in range(2,n):
        v=vals[i]
        M[0][i-1]=v%mod
        M[i-1][0]=(-v)%mod
    for i in range(2,n//2+1):
        v=(-1)**(i+1)*vals[-1]
        M[i-1][n-i]=v%mod
        M[n-i][i-1]=(-v)%mod
    return M


def valuation(x,p,s):
    if x==0: return s
    i=0
    while x%p==0:
        i+=1;x//=p
    return i


def smith_valuations(M,p,s):
    """Independent Smith elimination over Z/(p^s); no skew-form assumptions."""
    a=[row[:] for row in M]
    n=len(a); mod=p**s; out=[]
    for t in range(n):
        candidates=[(valuation(a[i][j],p,s),i,j)
                    for i in range(t,n) for j in range(t,n)]
        v,i,j=min(candidates)
        if v==s:
            out.extend([s]*(n-t));break
        a[t],a[i]=a[i],a[t]
        for row in a: row[t],row[j]=row[j],row[t]
        u=(a[t][t]//p**v)%(p**(s-v))
        ui=pow(u,-1,p**(s-v))
        for i in range(t+1,n):
            c=(a[i][t]//p**v*ui)%(p**(s-v))
            if c:
                for j in range(t,n):a[i][j]=(a[i][j]-c*a[t][j])%mod
        for j in range(t+1,n):
            c=(a[t][j]//p**v*ui)%(p**(s-v))
            if c:
                for i in range(t,n):a[i][j]=(a[i][j]-c*a[i][t])%mod
        assert all(a[i][t]==0 for i in range(t+1,n))
        assert all(a[t][j]==0 for j in range(t+1,n))
        out.append(v)
    return sorted(out)


def expected(vals,n,p,s):
    b=min(valuation(x,p,s) for x in vals[2:])
    a=valuation(vals[-1],p,s)
    assert b<=a
    return sorted([b,b]+[a,a]*(n//2-2)+[s,s]),(s-b)+(n//2-2)*(s-a)


def poly_formula(n,p,s):
    r=n-3; raw=Counter({0:p**(2*s)})
    for b in range(s):
        raw[s-b]+=p**(2*s)*(p**(r*(s-b))-p**(r*(s-b-1)))
    for a in range(s):
        zcount=(p-1)*p**(s-a-1)
        raw[(n//2-1)*(s-a)]+=p**(2*s)*zcount*p**(r*(s-a))
        for b in range(a):
            raw[(s-b)+(n//2-2)*(s-a)]+=p**(2*s)*zcount*(p**(r*(s-b))-p**(r*(s-b-1)))
    return raw


def test_integer_ring(n,p,s):
    mod=p**s; observed=Counter()
    for vals in product(range(mod),repeat=n):
        predicted,e=expected(vals,n,p,s)
        actual=smith_valuations(matrix(vals,n,mod),p,s)
        assert actual==predicted, (n,p,s,vals,actual,predicted)
        observed[e]+=1
    assert observed==poly_formula(n,p,s),(n,p,s,observed,poly_formula(n,p,s))
    assert sum(c*p**(0) for c in observed.values())==mod**n
    return f'Z/{mod}Z n={n} strata={sorted(observed.items())}'


def rank_mod_p(M,p):
    a=[row[:] for row in M]; n=len(a);m=len(a[0]);r=0
    for j in range(m):
        pivot=next((i for i in range(r,n) if a[i][j]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        z=pow(a[r][j],-1,p)
        a[r]=[(x*z)%p for x in a[r]]
        for i in range(n):
            if i!=r and a[i][j]:
                f=a[i][j]
                a[i]=[(x-f*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r


def test_poly_ring(n,p,s):
    ring=list(product(range(p),repeat=s))
    N=p**s; observed=Counter()
    # Ring matrices assembled directly from original structure constants.
    for idx in product(range(N),repeat=n):
        vals=[ring[i] for i in idx]
        expanded=[[0]*(n*s) for _ in range(n*s)]
        for i,j,idx_v,sign in entries(n):
            v=vals[idx_v]
            for shift in range(s):
                for h in range(s-shift):
                    expanded[i*s+h+shift][j*s+shift]=(expanded[i*s+h+shift][j*s+shift]+sign*v[h])%p
        actual_rank=rank_mod_p(expanded,p)
        aval=next((h for h in range(s) if vals[-1][h]),s)
        bval=min(next((h for h in range(s) if x[h]),s) for x in vals[2:])
        e=(s-bval)+(n//2-2)*(s-aval)
        assert actual_rank==2*e,(n,p,s,idx,actual_rank,e)
        observed[e]+=1
    assert observed==poly_formula(n,p,s),(n,p,s,observed,poly_formula(n,p,s))
    return f'F_{p}[t]/(t^{s}) n={n} strata={sorted(observed.items())}'


def entries(n):
    for i in range(2,n):
        yield 0,i-1,i,1
        yield i-1,0,i,-1
    for i in range(2,n//2+1):
        c=(-1)**(i+1)
        yield i-1,n-i,n-1,c
        yield n-i,i-1,n-1,-c


def gf4_mul(a,b):
    a0,a1=a&1,(a>>1)&1
    b0,b1=b&1,(b>>1)&1
    return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1)


def test_gf4_poly_ring(n,s):
    ring=list(product(range(4),repeat=s))
    observed=Counter();cols=n*s*2
    for idx in product(range(4**s),repeat=n):
        vals=[ring[i] for i in idx]
        expanded=[[0]*cols for _ in range(cols)]
        for i,j,idx_v,sign in entries(n):
            v=vals[idx_v]
            for shift in range(s):
                for basis in range(2):
                    for h in range(s-shift):
                        result=gf4_mul(v[h],1<<basis)
                        # Characteristic two: sign has no effect.
                        for bit in range(2):
                            expanded[2*(i*s+h+shift)+bit][2*(j*s+shift)+basis]^=(result>>bit)&1
        actual_rank=rank_mod_p(expanded,2)
        aval=next((h for h in range(s) if vals[-1][h]),s)
        bval=min(next((h for h in range(s) if x[h]),s) for x in vals[2:])
        e=(s-bval)+(n//2-2)*(s-aval)
        assert actual_rank==4*e,(n,s,idx,actual_rank,e)
        observed[e]+=1
    assert observed==poly_formula(n,4,s)
    return f'F_4[t]/(t^{s}) n={n} strata={sorted(observed.items())}'


def main():
    checks=[]
    for n,p,s in [(4,2,1),(6,2,1),(8,2,1),(4,3,1),(6,3,1),
                   (4,2,2),(6,2,2),(4,2,3),(4,3,2),
                   (4,2,4)]:
        checks.append(test_integer_ring(n,p,s))
    for n,p,s in [(4,2,2),(6,2,2),(4,2,3),(4,3,2)]:
        checks.append(test_poly_ring(n,p,s))
    for n,s in [(4,1),(6,1),(4,2)]:
        checks.append(test_gf4_poly_ring(n,s))
    for c in checks:print(c)
    print('FILIFORM_Q_CHAIN_KIRILLOV_OK',len(checks))

if __name__=='__main__':main()
