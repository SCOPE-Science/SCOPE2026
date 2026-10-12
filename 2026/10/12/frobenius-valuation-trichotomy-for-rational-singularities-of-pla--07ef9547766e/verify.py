"""Exact coefficient-ring checks for the tangent-cone classification.

These finite-characteristic examples test algebraic identities; the general
proof uses polynomial expansions and is not inferred from the sample tests.
"""
from math import comb
from collections import defaultdict

def clean(d,p):
    return {e:c%p for e,c in d.items() if c%p}

def add(*fs,p):
    d=defaultdict(int)
    for f in fs:
        for e,c in f.items(): d[e]+=c
    return clean(d,p)

def mul(f,g,p,maxdeg):
    d=defaultdict(int)
    for (i,j),a in f.items():
        for (k,l),b in g.items():
            if i+j+k+l<=maxdeg:d[i+k,j+l]+=a*b
    return clean(d,p)

def scalar(f,a,p):
    return clean({e:a*c for e,c in f.items()},p)

def power_shift(a,r,p,axis,maxdeg):
    return clean({(i,0) if axis==0 else (0,i):comb(r,i)*pow(a,r-i,p) for i in range(min(r,maxdeg)+1)},p)

def local(p,e,r,t):
    q=p**e;s=1
    while r%(s*p)==0:s*=p
    assert r%s==0 and r%(s*p)!=0
    t=t%p; assert t
    a=pow(t,r,p); b=pow(t,r+1,p);k=(b-pow(a,-r,p))%p
    m=min(s,q)+1
    A=clean({(0,1):a,(1,0):-b,(q,0):b,(0,q):-a,(q,1):1,(1,q):-1},p)
    B=clean({(0,1):-1,(0,q):1},p)
    C=clean({(1,0):1,(q,0):-1},p)
    X=power_shift(a,r,p,0,m);Y=power_shift(b,r,p,1,m)
    E=add(mul(X,A,p,m),mul(Y,B,p,m),mul(add({(0,0):1},scalar(X,k,p),p=p),C,p,m),p=p)
    assert not {e:c for e,c in E.items() if sum(e)<m}, ('lower terms',p,q,r,t,E)
    T={ex:c for ex,c in E.items() if sum(ex)==m}
    if s<q:
        h=(r//s)%p
        expected=clean({(s+1,0):-h*pow(a,-s,p), (s,1):h*pow(a,r-s+1,p), (0,s+1):-h*pow(b,r-s,p)},p)
    elif s>q:
        expected=clean({(q,1):pow(a,r,p), (1,q):-pow(a,r,p)},p)
    else:
        h=(r//q)%p
        expected=clean({(q+1,0):-h*pow(a,-1,p), (q,1):(h+1)*pow(a,h,p),(1,q):-pow(a,h,p),(0,q+1):-h*pow(b,h-1,p)},p)
    assert T==expected,(p,q,r,t,T,expected)
    if s==q:
        h=(r//q)%p; lam=pow(t,r*r+r+1,p)
        # P_lambda(z) = -h + lambda((h+1)z-z^q-h z^{q+1})
        coefs=clean({(q+1,0):-lam*h,(q,0):-lam,(1,0):lam*(h+1),(0,0):-h},p)
        actual=clean({(j,0): v*pow(t,j,p)*pow(t,h,p) for (i,j),v in expected.items()},p)
        assert coefs==actual,(p,q,r,t,coefs,actual)
        special=(h*h+lam*(h+1))%p ==0
        z0=((h+1)*pow(h,-1,p))%p
        # confirm exact multiplicity at z0, q or q+1
        def evaluate_derivatives():
            from math import comb
            cf={j:v for (j,_),v in coefs.items()}
            shift=[sum(v*comb(j,i)*pow(z0,j-i,p) for j,v in cf.items() if j>=i)%p for i in range(q+2)]
            if special:
                assert not any(shift[:q]),(p,q,r,t,shift)
                assert shift[q]==(-lam*(h+2))%p and shift[q+1]==(-lam*h)%p
            else:
                assert shift[0]!=0
        evaluate_derivatives()
    return p,q,r,t,s,m,k, ('exception' if s==q and special else 'regular')

if __name__=='__main__':
    tests=[(2,2,2,1),(3,2,3,1),(3,2,3,2),(5,2,5,2),
    (2,1,2,1),(3,1,3,1),(5,1,5,3),(5,1,15,4),(7,1,14,1),
    (2,1,4,1),(3,1,9,1),(5,1,25,2),(3,2,27,2),
    (5,2,125,2)]
    for case in tests: print('CASE',local(*case))
    print('VERIFY_OK: exact truncated local coefficient identities and critical multiplicities in',len(tests),'cases')
