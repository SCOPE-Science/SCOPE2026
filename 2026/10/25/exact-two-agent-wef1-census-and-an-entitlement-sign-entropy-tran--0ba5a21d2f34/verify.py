"""Independent exact-arithmetic verification of two-agent mixed-unit WEF1 formulas."""
from fractions import Fraction
from math import comb
from itertools import product

def direct(bits, values, a, b):
    v=[sum(values[j] for j in range(len(values)) if bits[j]==agent) for agent in (0,1)]
    bundles=[[values[j] for j in range(len(values)) if bits[j]==agent] for agent in (0,1)]
    weights=(a,b)
    for i,j in ((0,1),(1,0)):
        if Fraction(v[i],weights[i]) >= Fraction(v[j],weights[j]): continue
        okay=False
        for item in bundles[j]:
            if item>0 and Fraction(v[i],weights[i]) >= Fraction(v[j]-item,weights[j]): okay=True
        for item in bundles[i]:
            if item<0 and Fraction(v[i]-item,weights[i]) >= Fraction(v[j],weights[j]): okay=True
        if not okay: return False
    return True

def criterion(bits,values,a,b):
    p=values.count(1); q=values.count(-1)
    s=sum(1 for j in range(len(values)) if bits[j]==0 and values[j]==1)
    t=sum(1 for j in range(len(values)) if bits[j]==0 and values[j]==-1)
    x=s-t
    alpha=Fraction(a,a+b); theta=alpha*(p-q)
    if x==theta:return True
    if x<theta:
        dist=theta-x
        return (t>0 and dist<=1-alpha) or (p-s>0 and dist<=alpha)
    dist=x-theta
    return (q-t>0 and dist<=alpha) or (s>0 and dist<=1-alpha)

def closed_count(p,q,a,b):
    m=p+q
    alpha=Fraction(a,a+b)
    beta=1-alpha
    z=Fraction(q)+alpha*(p-q)
    def C(n,k):
        return comb(n,k) if 0<=k<=n else 0
    k0=z.numerator//z.denominator
    if z==k0:return C(m,k0)
    k1=k0+1
    f=z-k0
    d=1-f
    total=0
    if f<=min(alpha,beta):
        total+=C(m,k0)
    elif alpha>beta and f<=alpha:
        total+=C(m,k0)-C(q,k0-p)
    elif beta>alpha and f<=beta:
        total+=C(m,k0)-C(p,k0-q)
    if d<=min(alpha,beta):
        total+=C(m,k1)
    elif alpha>beta and d<=alpha:
        total+=C(m,k1)-C(p,k1)
    elif beta>alpha and d<=beta:
        total+=C(m,k1)-C(q,k1)
    return total

def main():
    checks=0
    weights=((1,1),(1,2),(2,1),(3,7),(7,3),(2,5),(1,20))
    for m in range(1,12):
        for p in range(m+1):
            vals=(1,)*p+(-1,)*(m-p)
            for a,b in weights:
                assert closed_count(p,m-p,a,b) == sum(criterion(bits,vals,a,b) for bits in product((0,1),repeat=m)), (m,p,a,b,closed_count(p,m-p,a,b))
                for bits in product((0,1),repeat=m):
                    got=direct(bits,vals,a,b)
                    exp=criterion(bits,vals,a,b)
                    assert got==exp,(m,p,a,b,bits,got,exp)
                    checks+=1
    for m in range(1,12):
        for p in range(m+1):
            vals=(1,)*p+(-1,)*(m-p)
            actual=sum(direct(bits,vals,1,1) for bits in product((0,1),repeat=m))
            expect=comb(m,m//2)*(1 if m%2==0 else 2)
            assert actual==expect,(m,p,actual,expect)
    for r in range(1,6):
        vals=(1,)*r+(-1,)*r
        actual=sum(direct(bits,vals,1,9) for bits in product((0,1),repeat=2*r))
        assert actual==comb(2*r,r)
    print('Verified exact WEF1 criterion on',checks,'labeled assignments across all sign counts and seven weight ratios; equal-weight cancellation counts and zero-total arbitrary-weight counts pass.')
if __name__=='__main__':main()
