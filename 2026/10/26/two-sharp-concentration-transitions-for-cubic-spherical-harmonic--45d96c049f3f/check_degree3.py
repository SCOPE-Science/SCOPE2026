"""Exact rational spot checks of the cubic-harmonic cap eigenbranch identities.

Run: python3 check_degree3.py
Only Python's standard library is required. These tests check finitely many
integer dimensions; the all-dimensional proof is the algebra in RESULT.md.
"""
from fractions import Fraction as Q

def add(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return c

def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def scale(a,k):return [Q(k)*x for x in a]
def neg(a):return scale(a,-1)
def deriv(a):return [Q(i)*a[i] for i in range(1,len(a))] or [Q(0)]
def eq(a,b):
    n=max(len(a),len(b));return (a+[0]*(n-len(a)))==(b+[0]*(n-len(b)))

def beta_moment(d,k):
    y=Q(1)
    for r in range(k):y*=Q(2*r+1,d+2*r)
    return y

def run_dimension(d):
    t=[Q(0),Q(1)]; one=[Q(1)]; omin=[Q(1),Q(-1)]; a=add(scale(t,d+2),[-1]); b=add(scale(t,d+2),[-3])
    R=[mul(t,mul(b,b)),mul(omin,mul(a,a)),mul(t,mul(omin,omin)),mul(omin,mul(omin,omin))]
    N=[Q(6*(d-1),d*(d+4)),Q(2*(d-1)*(d+1),d*(d+4)),Q((d-1)*(d+1),d*(d+2)*(d+4)),Q((d-1)*(d+1)*(d+3),d*(d+2)*(d+4))]
    q=[scale(R[i],1/N[i]) for i in range(4)]
    for i in range(4):
        val=sum(z*beta_moment(d,j) for j,z in enumerate(q[i]))
        assert val==1,(d,i,val)
    P={
      (0,1):scale(mul(a,b),Q(d*(d+4),3*(d-1)*(d+1))),
      (0,2):scale(mul(t,a),Q(d*(d+4),3*(d+1))),
      (1,2):scale(mul(omin,a),Q(d*(d+4),(d-1)*(d+1))),
      (2,3):scale(mul(omin,omin),Q(2*d*(d+2)*(d+4),(d-1)*(d+1)*(d+3)))
    }
    for (i,j),p in P.items():
        L=add(scale(mul([Q(1),-Q(d)],p),Q(1,2)),mul(mul(t,omin),deriv(p)))
        assert eq(L,add(q[j],neg(q[i]))),(d,i,j,L,q[i],q[j])
    # Positive factors imply ordering and the two universal transition points.
    assert Q(0)<Q(1,d+2)<Q(3,d+2)<Q(1)
    assert 1+(d-1)+((d-2)*(d+1)//2)+(d-1)*(d-2)*(d+3)//6==d*(d-1)*(d+4)//6
    return True

def numerical_cap_eigenvalues(d,t):
    """Independent Simpson quadrature of the four beta-normalized energy integrals."""
    import math
    n=6000
    assert n%2==0
    h=1.0/n
    beta=math.exp(math.lgamma(.5)+math.lgamma((d-1)/2)-math.lgamma(d/2))
    def vals(s):
        r=[s*((d+2)*s-3)**2,(1-s)*((d+2)*s-1)**2,
           s*(1-s)**2,(1-s)**3]
        return [x*s**(-.5)*(1-s)**((d-3)/2)/beta for x in r]
    sums=[0.0]*4
    for j in range(n+1):
        w=1 if j==0 or j==n else (4 if j%2 else 2)
        u=j*h
        s=1-(1-t)*u*u
        for i,v in enumerate(vals(s)):
            sums[i]+=w*v*2*(1-t)*u
    N=[6*(d-1)/(d*(d+4)),2*(d-1)*(d+1)/(d*(d+4)),
       (d-1)*(d+1)/(d*(d+2)*(d+4)),
       (d-1)*(d+1)*(d+3)/(d*(d+2)*(d+4))]
    return [h*sums[i]/(3*N[i]) for i in range(4)]

if __name__=='__main__':
    for d in list(range(3,101))+[101,125,150,200,500,1000]:run_dimension(d)
    for d in (3,4,5,10):
        t1,t2=1/(d+2),3/(d+2)
        v=numerical_cap_eigenvalues(d,t1)
        assert max(v[:3])-min(v[:3])<2e-7 and v[2]>v[3]
        v=numerical_cap_eigenvalues(d,t2)
        assert abs(v[0]-v[1])<2e-7 and v[1]>v[2]>v[3]
    print('PASS: rational normalizations, difference identities (104 dimensions); Simpson cap quadrature at both transitions (four dimensions).')
