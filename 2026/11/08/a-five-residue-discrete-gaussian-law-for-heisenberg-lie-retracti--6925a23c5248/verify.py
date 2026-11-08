"""Standalone finite checks for the rank statistics of Heisenberg Lie retractions.
Execute: python3 verify.py. Uses only Python's standard library.
"""
from collections import Counter
from itertools import product
from math import prod


def rank_mod(columns, q):
    if not columns:
        return 0
    n=len(columns[0]); a=[[col[i] for col in columns] for i in range(n)]
    r=0
    for j in range(len(columns)):
        pivot=next((i for i in range(r,n) if a[i][j]%q),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,q)
        a[r]=[(inv*x)%q for x in a[r]]
        for i in range(n):
            if i==r:continue
            f=a[i][j]
            a[i]=[(x-f*y)%q for x,y in zip(a[i],a[r])]
        r+=1
    return r


def symp(x,y,m,q):
    return sum(x[i]*y[m+i]-x[m+i]*y[i] for i in range(m))%q


def predicted(m,q):
    # Integer exact isotropic count using flag choices.
    out=Counter({0:1,2*m+1:1})
    for r in range(1,m+1):
        numer=prod(q**(2*(m-i))-1 for i in range(r))
        denom=prod(q**(r-i)-1 for i in range(r))
        assert numer%denom==0
        out[r]=(numer//denom)*q**(r*(2*m-r+1))
    return out


def brute_heisenberg3(q):
    # Enumerate every 3x3 linear map, test the algebra homomorphism
    # using its three basis vectors, then test P squared = P.
    e=[(1,0,0),(0,1,0),(0,0,1)]
    out=Counter()
    for data in product(range(q),repeat=9):
        cols=[tuple(data[3*j:3*j+3]) for j in range(3)]
        def apply(v):
            return tuple(sum(v[j]*cols[j][i] for j in range(3))%q for i in range(3))
        # Bracket on the basis: [p,h]=z, all other basic brackets zero.
        def bracket(v,w):
            return (0,0,(v[0]*w[1]-v[1]*w[0])%q)
        if any(apply(bracket(e[i],e[j]))!=bracket(cols[i],cols[j])
               for i in range(3) for j in range(3)): continue
        if any(apply(col)!=col for col in cols): continue
        out[rank_mod(cols,q)]+=1
    return out


def brute_symplectic4_binary():
    # Exhaust every 4x4 induced map, central scalar and central row;
    # direct bracket and composition tests on the resulting 5x5 maps.
    n=4; allcols=list(product((0,1),repeat=n));out=Counter()
    basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    for cols in product(allcols,repeat=n):
        def apply(v):
            return tuple(sum(v[j]*cols[j][i] for j in range(n))%2 for i in range(n))
        if any(apply(col)!=col for col in cols): continue
        for c in (0,1):
            if any(symp(cols[i],cols[j],2,2)!=(c*symp(basis[i],basis[j],2,2))%2
                   for i in range(n) for j in range(n)): continue
            for phi in allcols:
                if not all((sum(phi[i]*cols[j][i] for i in range(n)) + c*phi[j])%2==phi[j]
                           for j in range(n)): continue
                fullcols=[cols[j]+(phi[j],) for j in range(n)]+[(0,0,0,0,c)]
                out[rank_mod(fullcols,2)]+=1
    return out


def normalized_weights(m,q):
    from math import log
    # Exact enormous integers are avoided by subtracting the largest log weight.
    rows=predicted(m,q)
    logs={r: __import__('math').log(v) for r,v in rows.items()}
    h=max(logs.values()); ws={r:__import__('math').exp(v-h) for r,v in logs.items()}
    den=sum(ws.values());return {r:w/den for r,w in ws.items()}


def theta_distribution(m,q,lo=-20,hi=20):
    from math import floor
    x=(8*m+3)/10; a=floor(x); delta=x-a
    v={j:q**(-2.5*(j-delta)**2) for j in range(lo,hi+1)}
    s=sum(v.values()); return a,{j:w/s for j,w in v.items()}


def test():
    for q in (2,3):
        actual=brute_heisenberg3(q)
        expect=predicted(1,q)
        assert actual==expect,(q,actual,expect)
        print('DIRECT_H3_OK',q,dict(sorted(actual.items())))
    actual=brute_symplectic4_binary(); expect=predicted(2,2)
    assert actual==expect,(actual,expect)
    print('DIRECT_H5_BINARY_OK',dict(sorted(actual.items())))
    for m in (10,20,40):
        p=normalized_weights(m,2);a,theta=theta_distribution(m,2)
        error=sum(abs(p.get(a+j,0)-w) for j,w in theta.items())
        assert error<(0.04 if m==10 else (0.004 if m==20 else 0.0002)),(m,error)
        assert abs(sum(r*v for r,v in p.items())/m-0.8)<0.08
        print('DISCRETE_GAUSSIAN_OK',m,'L1_error',round(error,10))
    print('VERIFY_OK')


if __name__=='__main__':test()
