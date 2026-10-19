"""Finite exact checks of inverse-graph fourth-moment convolution identities.

The theorem is proven analytically. This script checks split square-zero and
non-split prime-square examples with Gaussian-integer inputs.
Finite tests do not constitute an infinite proof.
"""
from itertools import product
from random import Random


def add(u, v): return (u[0] + v[0], u[1] + v[1])
def mul(u, v): return (u[0]*v[0]-u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def abs2(u): return u[0]*u[0] + u[1]*u[1]
ZERO = (0, 0)


def group(p, d): return list(product(range(p), repeat=d))
def plus(u, v, p): return tuple((a+b)%p for a,b in zip(u,v))
def neg(u,p): return tuple(-a%p for a in u)


def trial(p, d, seed, nonsplit=False):
    rng = Random(seed)
    V = group(p, d)
    U = list(range(1,p))
    f = {(a,b):(rng.randint(-2,2),rng.randint(-2,2)) for a in U for b in V}
    B = {a:sum(abs2(f[a,b]) for b in V) for a in U}
    def conv(a,c):
        return {s:sum_gauss(mul(f[a,b],f[c,plus(s,neg(b,p),p)]) for b in V) for s in V}
    def sum_gauss(it):
        z = ZERO
        for u in it:z=add(z,u)
        return z
    def rep(a):
        return a if a<=(p-1)//2 else (a-p)%(p*p)
    def h(a,b):
        if nonsplit:
            assert d==1
            x=(rep(a)+p*b[0])%(p*p)
            return (x, pow(x,-1,p*p))
        ai=pow(a,-1,p)
        return (a, b, ai, tuple((-ai*ai*x)%p for x in b))
    def pair_sum(x,y):
        if nonsplit: return ((x[0]+y[0])%(p*p),(x[1]+y[1])%(p*p))
        return ( (x[0]+y[0])%p, plus(x[1],y[1],p), (x[2]+y[2])%p, plus(x[3],y[3],p))
    rows = [(h(a,b),f[a,b]) for a in U for b in V]
    sums = {}
    for x,u in rows:
        for y,v in rows:
            z=pair_sum(x,y)
            sums[z]=add(sums.get(z,ZERO),mul(u,v))
    direct = sum(abs2(t) for t in sums.values())
    ans = sum(sum(abs2(x) for x in conv(a,a).values()) for a in U)
    for a in U:
        for c in U:
            if a<c and c!=p-a:
                ans += 4*B[a]*B[c]
    antipodal=[]
    for a in U:
        if a<p-a:
            cc=conv(a,p-a);antipodal.append(cc)
            ans+=4*sum(abs2(x) for s,x in cc.items() if s!=(0,)*d)
    ans+=4*abs2(sum_gauss(c[(0,)*d] for c in antipodal))
    assert direct==ans,(p,d,seed,direct,ans)
    assert 2*direct<=3*(p**d)*sum(B.values())**2,(p,d,seed)
    return direct,ans

def extremizer(p,d,nonsplit=False):
    V=group(p,d);Q=len(V);a=1
    coeff={(c,b):1 for c in [a,p-a] for b in V}
    E={}
    for (c,b),u in coeff.items():
        for (e,t),v in coeff.items():
            if nonsplit:
                assert d==1
                rc=c if c<=(p-1)//2 else (c-p)%(p*p)
                re=e if e<=(p-1)//2 else (e-p)%(p*p)
                x=(rc+p*b[0])%(p*p);y=(re+p*t[0])%(p*p)
                k=((x+y)%(p*p),(pow(x,-1,p*p)+pow(y,-1,p*p))%(p*p))
            else:
                ci=pow(c,-1,p);ei=pow(e,-1,p)
                k=((c+e)%p, plus(b,t,p), (ci+ei)%p, plus(tuple((-ci*ci*x)%p for x in b),tuple((-ei*ei*x)%p for x in t),p))
            E[k]=E.get(k,0)+u*v
    energy=sum(x*x for x in E.values());N=2*Q
    assert 2*energy==3*Q*N*N,(p,d,energy,N)
    return energy,N

if __name__=='__main__':
    for p,d in [(3,1),(5,1),(7,1),(3,2)]:
        for seed in range(7):trial(p,d,seed)
        en,n=extremizer(p,d)
        print(f"p={p} d={d} |radical|={p**d} random_identity_tests=7 equality_energy={en} source_size={n}")
    for p in [3,5,7]:
        for seed in range(7): trial(p,1,seed,nonsplit=True)
        en,n=extremizer(p,1,nonsplit=True)
        print(f'Z/{p*p}Z |radical|={p} random_identity_tests=7 equality_energy={en} source_size={n}')
    print('PASS finite exact identity and sharpness tests (not an infinite proof)')
