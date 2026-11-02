"""Finite reproducibility checks for the boundary-sampled triangle hull theorem.
Python 3 + NumPy are required. Monte Carlo is corroborative, not a proof.
"""
from fractions import Fraction as F
from math import factorial
import itertools
import numpy as np

def exact_ratio(n, p):
    p = [F(x) for x in p]
    N=n+2
    return F(1)- (F(1)-sum((1-x)**N for x in p)+sum(x**N for x in p))/(F((n+1)*(n+2))*p[0]*p[1]*p[2])

def conditional_ratio(m):
    return F(1) - sum(F(1,(m[(i+1)%3]+1)*(m[(i+2)%3]+1)) for i in range(3) if m[i]>0)

def multinomial_ratio(n,p):
    ans=F(0)
    for a in range(n+1):
        for b in range(n-a+1):
            c=n-a-b
            mult=factorial(n)//(factorial(a)*factorial(b)*factorial(c))
            ans+=mult*p[0]**a*p[1]**b*p[2]**c*conditional_ratio((a,b,c))
    return ans

def sample_hull_ratio(rng, n, sides, rep):
    p=np.array(sides,dtype=float)/sum(sides)
    # Valid triangle coordinates: first two sides along V0-V1 and V1-V2.
    a,b,c = np.array(sides,dtype=float)
    z=(a*a+c*c-b*b)/(2*a*c) # cosine of angle at V0 between V0V1 length a and V0V2 length c
    V=np.array([[0.,0.],[a,0.],[c*z,c*np.sqrt(1-z*z)]])
    double_area=abs(np.linalg.det(np.stack((V[1]-V[0],V[2]-V[0]))))
    vals=np.zeros(rep)
    for j in range(rep):
        edges=rng.choice(3,size=n,p=p)
        t=rng.random(n)
        pts=np.array([V[e]*(1-u)+V[(e+1)%3]*u for e,u in zip(edges,t)])
        # Andrew's monotone hull algorithm, retaining outer vertices.
        pts=sorted(map(tuple,pts))
        def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
        lo=[]
        for pt in pts:
            while len(lo)>=2 and cross(lo[-2],lo[-1],pt)<=0:lo.pop()
            lo.append(pt)
        hi=[]
        for pt in pts[::-1]:
            while len(hi)>=2 and cross(hi[-2],hi[-1],pt)<=0:hi.pop()
            hi.append(pt)
        hull=lo[:-1]+hi[:-1]
        if len(hull)>2:
            H=np.array(hull)
            vals[j]=abs(np.dot(H[:,0],np.roll(H[:,1],-1))-np.dot(H[:,1],np.roll(H[:,0],-1)))/double_area
    return vals.mean(),vals.std()/np.sqrt(rep)

def main():
    cases=[(3,[F(1,3)]*3),(4,[F(1,3)]*3),(7,[F(2,5),F(7,20),F(1,4)]),(5,[F(49,100),F(47,100),F(4,100)]),(10,[F(3,10),F(3,10),F(2,5)]),(11,[F(1,4),F(3,8),F(3,8)])]
    for n,p in cases:
        assert exact_ratio(n,p)==multinomial_ratio(n,p), (n,p)
    print('EXACT_MULTINOMIAL_VERSUS_INCLUSION_EXCLUSION_IDENTITIES_PASSED',len(cases))
    assert exact_ratio(3,[F(1,3)]*3)==F(1,6)
    assert exact_ratio(4,[F(1,3)]*3)==F(1,3)
    for n in range(3,30):
        upper=exact_ratio(n,[F(1,3)]*3)
        lower=F(n-3,n+1)+F(2,2**n*(n+1))*4 # equals 2^{2-n}/(n+1)
        lower=F(n-3,n+1)+F(4,2**n*(n+1))
        assert lower<upper
    print('SHARP_EQUALITY_FORMULAS_AND_ENDPOINT_CONSISTENCY_PASSED')
    rng=np.random.default_rng(1212026)
    for n,sides in [(3,[1,1,1]),(5,[4,5,6]),(8,[3,4,5]),(7,[3,3,4])]:
        expected=float(exact_ratio(n,[F(s,sum(sides)) for s in sides]))
        obs,se=sample_hull_ratio(rng,n,sides,3200)
        assert abs(obs-expected)<6*se+0.012,(n,sides,expected,obs,se)
    print('INDEPENDENT_EUCLIDEAN_HULL_SIMULATIONS_PASSED',4)
    # Direct numerical integration of the cubical moment identity.
    nodes,weights=np.polynomial.legendre.leggauss(40)
    t=(nodes+1)/2;w=weights/2
    for n,p in [(3,[.3333333333333333]*3),(7,[.4,.35,.25]),(9,[.45,.3,.25])]:
        t1,t2,t3=np.meshgrid(t,t,t,indexing='ij')
        q=n*np.einsum('ijk,i,j,k->', (p[0]*t1+p[1]*t2+p[2]*t3)**(n-1),w,w,w)
        exact=1-float(exact_ratio(n,[F(str(x)) for x in p]))
        assert abs(q-exact)<4e-12,(q,exact)
    print('INDEPENDENT_CUBICAL_MOMENT_QUADRATURE_PASSED')
    print('ALL_CHECKS_PASSED')
if __name__=='__main__': main()
