"""Exact spherical-cone certificate for widths of polar cubic solids.
Requires Python 3 with sympy and numpy. All cone inequalities, rays, and
integral reductions use exact integer/radical arithmetic. Floating point
values are used solely to propose the cyclic order of already exact rays;
the proposed order is verified using exact positive determinants.
"""
import itertools, math
from collections import Counter
from fractions import Fraction as F
import numpy as np
import sympy as sp

ROT = [(2,-1,2),(2,2,-1),(-1,2,2)]
assert sp.Matrix(ROT)*sp.Matrix(ROT).T == 9*sp.eye(3)
assert sp.Matrix(ROT).det() == 27

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def neg(a): return tuple(-x for x in a)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def prim(v):
    g=math.gcd(*(abs(int(x)) for x in v))
    return tuple(int(x)//g for x in v)
def unit(v):
    z=sp.Matrix(v); return z/sp.sqrt(z.dot(z))

def chambers():
    for sig in itertools.product((-1,1),repeat=3):
        for j in range(3):
            for t in (-1,1):
                b=tuple(t*x for x in ROT[j]); H=[]
                for i in range(3): H.append(tuple(sig[i] if k==i else 0 for k in range(3)))
                for q in ROT:
                    H.extend([sub(b,q),tuple(b[k]+q[k] for k in range(3))])
                H=[h for h in H if h!=(0,0,0)]
                rays=set()
                for a,z in itertools.combinations(H,2):
                    x=cross(a,z)
                    if x==(0,0,0): continue
                    for y in (x,neg(x)):
                        if all(dot(h,y)>=0 for h in H): rays.add(prim(y))
                if len(rays)<3: continue
                V=list(rays)
                vf=np.array(V,dtype=float)
                cen=vf.sum(axis=0); cen/=np.linalg.norm(cen)
                w=vf[0]/np.linalg.norm(vf[0]); e1=w-np.dot(w,cen)*cen;e1/=np.linalg.norm(e1)
                e2=np.cross(cen,e1)
                V=sorted(V,key=lambda x:math.atan2(np.dot(x,e2),np.dot(x,e1)))
                # Finite exact check that cyclic vertices follow the same
                # positive orientation about their exact interior ray.
                interior=tuple(map(sum, zip(*V)))
                assert all(dot(h,interior)>=0 for h in H)
                assert all(dot(cross(V[i],V[(i+1)%len(V)]),interior)>0 for i in range(len(V)))
                yield sig,j,t,H,V

def certificate():
    types=Counter(); areas=[]
    expected={
        'A':(3,sp.Integer(1),sp.pi/6,sp.Rational(4,9)),
        'B':(3,sp.Rational(1,3),sp.acos(2*sp.sqrt(2)/3)-sp.pi/12,sp.Rational(1,9)+sp.sqrt(2)/18-2*sp.sqrt(3)/27),
        'C':(5,sp.Rational(5,3),2*sp.pi/3-2*sp.acos(2*sp.sqrt(2)/3),sp.Rational(2,3)+sp.sqrt(2)/9+4*sp.sqrt(3)/27),
    }
    cos_expected={
       'A':[-sp.sqrt(2)/2,-sp.sqrt(2)/2,sp.Rational(1,2)],
       'B':[-2*sp.sqrt(2)/3,-sp.sqrt(2)/2,sp.Rational(1,2)],
       'C':[2*sp.sqrt(2)/3,sp.Integer(0),sp.Integer(0),2*sp.sqrt(2)/3,sp.Rational(1,2)],
    }
    for sig,j,t,H,V in chambers():
        b=sp.Matrix([sp.Rational(t*z,3) for z in ROT[j]])
        c=sp.Matrix(sig)
        scalar=c.dot(b)
        typ={ (3,sp.Integer(1)):'A',(3,sp.Rational(1,3)):'B',(5,sp.Rational(5,3)):'C' }[(len(V),scalar)]
        types[typ]+=1
        normals=[];U=[]
        for i in range(len(V)):
            a=V[i];z=V[(i+1)%len(V)]
            active=[h for h in H if dot(h,a)==0 and dot(h,z)==0]
            assert active
            # All active planes of a genuine edge must be co-oriented.
            for h in active: assert cross(h,active[0])==(0,0,0) and dot(h,active[0])>0
            normals.append(-unit(active[0]))
            U.append(unit(a))
        actual_cos=[sp.simplify(normals[i-1].dot(normals[i])) for i in range(len(V))]
        assert sorted(actual_cos,key=float)==sorted(cos_expected[typ],key=float)
        # Exact Gauss-Bonnet angle formula; finite rational/radical cosines above
        # derive the listed symbolic area using standard acos identities.
        theta=sp.acos(2*sp.sqrt(2)/3)
        angle_replacements=[(-sp.sqrt(2)/2,3*sp.pi/4),
            (-2*sp.sqrt(2)/3,sp.pi-theta),
            (2*sp.sqrt(2)/3,theta),
            (sp.Rational(1,2),sp.pi/3),(sp.Integer(0),sp.pi/2)]
        area=2*sp.pi
        for cosine in actual_cos:
            matches=[angle for v,angle in angle_replacements if sp.simplify(cosine-v)==0]
            assert len(matches)==1
            area-=matches[0]
        want_area=expected[typ][2]
        assert sp.simplify(area-want_area)==0
        boundary=sp.Integer(0)
        for i in range(len(V)):
            a,z=U[i],U[(i+1)%len(V)]
            tcos=sp.simplify(a.dot(z))
            segment=(a+z)*sp.sqrt((1-tcos)/(1+tcos))
            normal=normals[i]
            term=-(normal.dot(b)*c.dot(segment)+normal.dot(c)*b.dot(segment))/6
            boundary+=sp.sqrtdenest(sp.simplify(term))
        boundary=sp.simplify(boundary)
        want=expected[typ][3]
        diff=sp.simplify(sp.sqrtdenest(boundary-want))
        assert diff==0,(typ,diff)
    assert types==Counter({'A':6,'B':12,'C':6}),types
    assert sp.simplify(sum(types[t]*expected[t][2] for t in types)-4*sp.pi)==0
    theta=sp.atan(1/(2*sp.sqrt(2)))
    mixed=sp.Rational(11,18)+(2+sp.sqrt(2)/3)/sp.pi-4*theta/(3*sp.pi)
    # In the aligned orientation the elementary winner-octant integral gives
    # J0 = pi/18 + 1/(3sqrt3), Jp = 1/(3sqrt2)-1/(6sqrt3),
    # E[SM]=6/pi*(J0+2Jp).
    aligned=sp.Rational(1,3)+2*sp.sqrt(2)/sp.pi
    smean=sp.Rational(3,2)
    mmean=3*sp.sqrt(2)*sp.acos(sp.Rational(1,3))/(2*sp.pi)
    c0=4*(aligned-smean*mmean)
    c1=4*(mixed-smean*mmean)
    assert float(c0)<-0.05 and float(c1)>0.027
    print('CHAMBERS_OK',dict(types),'area=4pi')
    print('ALIGNED_MIXED',sp.N(aligned,17),'TWISTED_MIXED',sp.N(mixed,17))
    print('COVARIANCES',sp.N(c0,17),sp.N(c1,17))
    return c0,c1

# Rigorous rational interval enclosure; every root, atan, and pi is bounded.
def ai(x,n): return sum(((-1)**k)*x**(2*k+1)/F(2*k+1) for k in range(n))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def negate(a):return (-a[1],-a[0])
def subtract(a,b):return add(a,negate(b))
def times(a,b):
 p=[x*y for x in a for y in b];return (min(p),max(p))
def divide(a,b):
 assert b[0]>0
 return times(a,(1/b[1],1/b[0]))
def mult(a,q):return times(a,(F(q),F(q)))
def exact(q):return (F(q),F(q))
def signs():
 root2=(F(141421356237,10**11),F(141421356238,10**11))
 assert root2[0]**2<2<root2[1]**2
 atan=lambda x:(ai(x[0],14),ai(x[1],15))
 a5=atan(exact(F(1,5)));a239=atan(exact(F(1,239)))
 pi=subtract(mult(a5,16),mult(a239,4))
 th=atan((F(1,1)/(2*root2[1]),F(1,1)/(2*root2[0])))
 assert pi[0]>F(314159,100000) and pi[1]<F(314160,100000)
 c0=add(subtract(exact(F(4,3)),mult(root2,F(9,2))),divide(times(root2,add(exact(8),mult(th,9))),pi))
 c1=add(subtract(exact(F(22,9)),mult(root2,F(9,2))),divide(add(add(exact(8),mult(root2,F(4,3))),times(subtract(mult(root2,9),exact(F(16,3))),th)),pi))
 assert c0[1]<0 and c1[0]>0
 print('RATIONAL_SIGN_CERTIFICATE_OK',*[tuple(float(v) for v in x) for x in (c0,c1)])

if __name__=='__main__':
 certificate();signs();print('VERIFY_OK')
