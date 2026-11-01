"""Exact small-ring tests for the Fourier spectrum of determinant-zero 2x2 matrices.
Uses only Python standard library; cyclotomic quotient test, never floating point.
"""
from itertools import product

def expected(q,k,m_val,det_val):
    if m_val==k:
        return q**(3*k)+q**(3*k-1)-q**(2*k-1)
    if det_val+2*m_val<k-1:
        return 0
    if det_val+m_val<k:
        return -q**(2*k-1)
    return q**(2*k-1)*(q**(m_val+1)-1)

def valuation(n,p,k):
    if not n:
        return k
    i=0
    while i<k and n%p==0:
        i+=1;n//=p
    return i

def cyclic(p,k):
    n=p**k
    mats=list(product(range(n),repeat=4))
    cone=[x for x in mats if (x[0]*x[3]-x[1]*x[2])%n==0]
    rank=0
    for u,v,w,z in mats:
        m=(u,v,w,z)
        e=min(valuation(a,p,k) for a in m)
        d= k-e if e<k else 0
        if e<k:
            x=tuple(a//p**e for a in m)
            d=valuation(x[0]*x[3]-x[1]*x[2],p,k-e)
        expected_v=expected(p,k,e,d)
        counts=[0]*n
        for a,b,c,dd in cone:
            t=(u*a+v*b+w*c+z*dd)%n
            counts[t]+=1
        counts[0]-=expected_v
        # Phi_{p^k}(X)=1+X^{p^(k-1)}+...+X^{(p-1)p^(k-1)}.
        step=n//p
        for h in range(step):
            assert len({counts[h+i*step] for i in range(p)})==1,(p,k,m,expected_v,counts)
        if expected_v:rank+=1
    R1=(p-1)*(p+1)**2;L=k//2
    predicted=p**(4*(k-L))+R1*sum(p**(3*k-2-2*j) for j in range(L))
    assert rank==predicted,(p,k,rank,predicted)
    print('EXACT_CYCLIC_OK',p,k,'size',len(mats),'cone',len(cone),'rank',rank)

def dual_numbers_f2():
    # a+bt, t^2=0: encoded as a+2b, operations in F_2[t]/(t^2).
    def mul(x,y):return ((x&1)*(y&1)) | (((((x&1)*((y>>1)&1))^(((x>>1)&1)*(y&1))))<<1)
    def dot(m,x):
        r=0
        for a,b in zip(m,x):r^=mul(a,b)
        return (r>>1)&1  # psi(a+bt)=(-1)^b
    mats=list(product(range(4),repeat=4))
    cone=[x for x in mats if mul(x[0],x[3])==mul(x[1],x[2])]
    rank=0
    for m in mats:
        val=2 if all(z==0 for z in m) else (1 if all(z%2==0 for z in m) else 0)
        if val<2:
            if val==1:
                red=tuple((x>>1)&1 for x in m)
            else:
                red=m
            det=mul(red[0],red[3])^mul(red[1],red[2])
            # determinant valuation modulo t^{2-val}
            d=2-val if det==0 else (1 if det%2==0 else 0)
        else:d=0
        predicted=expected(2,2,val,d)
        actual=sum(-1 if dot(m,x) else 1 for x in cone)
        assert actual==predicted,(m,actual,predicted)
        if actual:rank+=1
    assert rank==160,(rank,160)
    print('EXACT_NONCYCLIC_OK F2[t]/(t^2) size',len(mats),'cone',len(cone),'rank',rank)

if __name__=='__main__':
    for p,k in [(2,1),(2,2),(2,3),(3,1),(3,2)]:cyclic(p,k)
    dual_numbers_f2()
    print('ALL_EXACT_DETERMINANTAL_CHECKS_OK')
