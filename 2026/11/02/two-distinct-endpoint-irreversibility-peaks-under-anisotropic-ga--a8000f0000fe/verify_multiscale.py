"""Exact rational certificate for two-mode Gaussian endpoint Jeffreys rate."""
from fractions import Fraction as Q

K = 250

def certified_component(q, u, cutoff=K):
    q, u = Q(q), Q(u)
    a = 1-q
    c = a*a / (2*q)
    val = 1 + (a-2)*u*(u+2)/(u+1)**2
    z = Q(1)
    for n in range(2,cutoff+1):
        val += q*q*z*u*(u+2*n)/(u+n)**2
        z *= a
    low = c*val
    # Exact bound: positive tail <= (1-q)^(K+1)/2.
    high = low + a**(cutoff+1)/2
    return low, high

def certify():
    expected={1:1,3:-1,20:1,200:-1}
    out=[]
    for r,sign in expected.items():
        a,b=certified_component(Q(1,2),Q(r))
        c,d=certified_component(Q(9,10),Q(r,100))
        lo,hi=a+c,b+d
        assert lo > 0 if sign==1 else hi < 0, (r,float(lo),float(hi))
        out.append((r, float(lo),float(hi)))
    return out

if __name__ == '__main__':
    print('Proof by rational series truncation and positive geometric tail')
    for r,lo,hi in certify():
        print('r=',r,' derivative in [',format(lo,'.12g'),',',format(hi,'.12g'),']')
    print('PASS: four strict sign bounds with exact Fraction arithmetic; K=',K)
