"""Independent finite enumeration of graded algebra retractions of equal-exponent truncated complete intersections.
Run: python check_retractions.py. Standard library only. All objects are finite and all arithmetic is exact.
"""
from itertools import product
from math import comb


def field(q):
    if q == 4:
        add=lambda a,b: a^b
        def mul(a,b):
            v=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1):
                        v ^= 1 << (i+j)
            if v&8: v ^= 0b1100  # x^3=x(x+1)=x^2+x
            if v&4: v ^= 0b111  # x^2=x+1
            return v
        return add,mul,2
    assert q in (2,3,5)
    return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q,q


def truncated_mul(A,B,n,d,add,mul):
    out={}
    for e,a in A.items():
        for f,b in B.items():
            ef=tuple(e[i]+f[i] for i in range(n))
            if any(x>=d for x in ef): continue
            c=add(out.get(ef,0),mul(a,b))
            if c: out[ef]=c
            elif ef in out: del out[ef]
    return out


def linear_power(column,n,d,add,mul):
    one={(0,)*n:1}
    v={tuple(1 if j==i else 0 for j in range(n)):a
       for i,a in enumerate(column) if a}
    z=one
    for _ in range(d): z=truncated_mul(z,v,n,d,add,mul)
    return z


def matrix_product_is(M,n,add,mul):
    for i in range(n):
        for j in range(n):
            v=0
            for k in range(n): v=add(v,mul(M[i*n+k],M[k*n+j]))
            if v!=M[i*n+j]:return False
    return True


def rank(M,n,add,mul,q):
    if q == 4:
        inv={1:1,2:3,3:2}
    else:
        inv={a:pow(a,-1,q) for a in range(1,q)}
    v=[list(M[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for j in range(n):
        k=next((i for i in range(r,n) if v[i][j]),None)
        if k is None: continue
        v[r],v[k]=v[k],v[r]
        t=inv[v[r][j]]
        v[r]=[mul(x,t) for x in v[r]]
        for i in range(r+1,n):
            if v[i][j]:
                f=v[i][j]
                # Subtraction equals addition in char 2.
                if q == 4 or q==2: v[i]=[add(a,mul(f,b)) for a,b in zip(v[i],v[r])]
                else: v[i]=[add(a,q-mul(f,b)) for a,b in zip(v[i],v[r])]
        r+=1
        if r==n:break
    return r


def gaussian(n,r,q):
    a=b=1
    for i in range(r):a*=q**(n-i)-1;b*=q**(r-i)-1
    return a//b


def full_predicted(n,q,d):
    rdict={}
    _,_,p=field(q)
    val=d
    while val>1 and val%p==0:val//=p
    for r in range(n+1):
        if val==1:
            a=1
            for j in range(r):a*=q**n-q**j
            rdict[r]=gaussian(n,r,q)*a
        else:
            rdict[r]=comb(n,r)*sum((-1)**j*comb(r,j)*(1+(r-j)*(q-1))**n for j in range(r+1))
    return rdict

def predicted(n,q,d):
    p=field(q)[2]
    ispp=False
    val=d
    while val>1 and val%p==0:val//=p
    ispp=(val==1)
    if ispp:
        return {r:gaussian(n,r,q)*q**(r*(n-r)) for r in range(n+1)},'Frobenius'
    return {r:comb(n,r)*(1+r*(q-1))**(n-r) for r in range(n+1)},'monomial'


def run(q,n,d):
    add,mul,p=field(q)
    allowed=[]
    for c in product(range(q),repeat=n):
        if not linear_power(c,n,d,add,mul):allowed.append(c)
    histogram={r:0 for r in range(n+1)}
    full_histogram={r:0 for r in range(n+1)}
    matrices=0
    first=None
    for cols in product(allowed,repeat=n):
        M=tuple(cols[j][i] for i in range(n) for j in range(n))
        matrices+=1
        rk=rank(M,n,add,mul,q)
        full_histogram[rk]+=1
        if matrix_product_is(M,n,add,mul):
            histogram[rk]+=1
            if first is None:first=M
    want,regime=predicted(n,q,d)
    assert histogram==want,(q,n,d,regime,histogram,want)
    full_want=full_predicted(n,q,d)
    assert full_histogram==full_want,(q,n,d,regime,full_histogram,full_want)
    print('PASS',f'q={q}',f'n={n}',f'd={d}',regime,
          'relation_columns='+str(len(allowed)), 'homomorphisms='+str(matrices),
          'retractions='+str(sum(histogram.values())),
          'full_rank_histogram='+str([full_histogram[r] for r in range(n+1)]),
          'rank_histogram='+str([histogram[r] for r in range(n+1)]))

if __name__=='__main__':
    cases=[(2,2,2),(2,2,3),(2,2,4),(2,3,2),(2,3,3),(2,3,4),
           (3,2,2),(3,2,3),(3,3,2),(3,3,3),
           (4,2,2),(4,2,3),(4,2,4),(4,3,2),(4,3,3),(4,3,4),
           (5,2,2),(5,2,5)]
    for q,n,d in cases:run(q,n,d)
    print('ALL_EXACT_CHECKS_PASSED',len(cases))
