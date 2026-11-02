import math, cmath
from math import gcd

def area(pts):
    return abs(sum((a.conjugate()*b).imag for a,b in zip(pts,pts[1:]+pts[:1])))/2

def polygon(q,p):
    theta=2*math.pi*p/q
    lam=cmath.exp(1j*theta)
    h=0.5*math.tan(theta/2)
    center=lam/(1+lam)
    # normals in coordinates delta: Re(conj(n)*delta)<=h
    normals=[]
    for j in range(q//2):
        a=lam**(2*j)
        normals.append(-1j*a.conjugate()) # verify Im(a*delta) > -h means -Im(a*delta)<h, normal n=-1j*conj(a)
        a=lam**(2*j+1)
        normals.append(1j*a.conjugate())
    # identity: Im(a d) = Re(-i*a*d) = Re(conj(i*conj(a))*d)
    # so for Im(a d) <=h outward normal n=i*conj(a); correct
    # dedupe by angle
    by={round(cmath.phase(n)%(2*math.pi),9): n for n in normals}
    ns=sorted(by.values(),key=lambda n:cmath.phase(n)%(2*math.pi))
    verts=[]
    for a,b in zip(ns,ns[1:]+ns[:1]):
        # solve x dot a=h, x dot b=h => vertex (a+b)*h/(1+a dot b)
        dot=(a.conjugate()*b).real
        verts.append(h*(a+b)/(1+dot))
    return theta,lam,h,center,ns,verts

def F(z,lam):return lam*(z-1 if z.imag>=0 else z+1)

for q in range(4,36,2):
    for p in range(1,q//2):
        if gcd(p,q)!=1:continue
        theta,lam,h,center,ns,verts=polygon(q,p)
        N=q if q%4==0 else q//2
        assert len(ns)==N,(q,p,len(ns),N)
        expected=N*h*h*math.tan(math.pi/N)
        observed=area(verts)
        assert abs(observed-expected)<1e-8*max(1,expected),(q,p,observed,expected)
        assert abs(F(center,lam)+center)<1e-10
        for offset in [0, 0.2*h+0.05j*h,-0.11*h+0.13j*h]:
            z=center+offset
            for k in range(q):
                assert z.imag*(1 if k%2==0 else -1)>1e-8, (q,p,k,z,center)
                z=F(z,lam)
            assert abs(z-(center+offset))<1e-8,(q,p,z,center,offset)
        if q<=14:print('q=',q,'p=',p,'sides=',N,'inradius=',round(h,7),'area=',round(observed,7))
print('all passed')
