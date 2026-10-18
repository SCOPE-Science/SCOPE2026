"""Reproducibility checks for a degree-two cyclic positive-definite optimizer face.
This finite checker corroborates, but does not replace, the analytic proof.
Run: python check.py  (Python standard library only).
"""
import math
from itertools import combinations

def trig(N,j):
    q=2*math.pi*j/N
    return math.cos(q),math.sin(q)

def sample(N,a,b,t1,t2):
    return [1+2*a*trig(N,j)[0]+2*b*(2*trig(N,j)[0]**2-1)
            +2*t1*trig(N,j)[1]+4*t2*trig(N,j)[0]*trig(N,j)[1]
            for j in range(N)]

def brackets(N):
    xs=sorted(set(round(trig(N,j)[0],14) for j in range(N)))
    return max(x for x in xs if x<-.5-1e-11),min(x for x in xs if x>-.5+1e-11)

def get_face(N):
    # Completely independent half-plane enumeration on the 2D optimal affine slice.
    assert N%3==0
    half=[]
    for j in range(N):
        x,y=trig(N,j)
        if abs(x+.5)<1e-10:continue
        sg=1 if x>-.5 else -1
        half.append((2*sg*(1-x),-2*sg*y,sg))
    pts=[]
    for (a,b,c),(d,e,f) in combinations(half,2):
        det=a*e-b*d
        if abs(det)<1e-10:continue
        X=(c*e-b*f)/det;Y=(a*f-c*d)/det
        if all(A*X+B*Y<=C+2e-9 for A,B,C in half):
            if not any(abs(X-p)<1e-8 and abs(Y-q)<1e-8 for p,q in pts):pts.append((X,Y))
    return pts

num=0
for N in range(5,301):
    u,v=brackets(N)
    if N%3:
        M=(1-u)*(1-v)/(.5+u*v)
        b=1/(2+4*u*v)
        a=-(u+v)/(1+2*u*v)
        values=sample(N,a,b,0,0)
        assert min(values)>-2e-11,(N, min(values))
        assert sum(abs(v) for v in values if abs(v)<2e-8)>=0
        assert abs(1+2*a+2*b-M)<3e-10
        # Independently enumerate all real-even feasible vertices and compare objectives.
        rows=[(2*trig(N,j)[0],2*(2*trig(N,j)[0]**2-1)) for j in range(N)]
        for (A,B),(D,E) in combinations(rows,2):
            det=A*E-B*D
            if abs(det)<1e-10:continue
            p=(-E+B)/det;q=(-A+D)/det
            if all(1+U*p+V*q>=-2e-9 for U,V in rows):
                assert 1+2*p+2*q<=M+2e-8,(N,p,q,M)
        num+=1
    else:
        theta=2*math.pi/N
        C=math.cos(theta);S=math.sin(theta)
        U=math.cos(2*math.pi/3+theta)
        V=math.cos(2*math.pi/3-theta)
        L=1/(2*(1-U));R=1/(2*(1-V))
        B=C/(1+2*C);T=S/(1+2*C)
        expected=[(L,0),(R,0),(B,T),(B,-T)]
        for b,t in expected:
            vals=sample(N,1-b,b,t,t)
            assert min(vals)>-2e-9,(N,b,t,min(vals))
            assert abs(vals[0]-3)<2e-9
        found=get_face(N)
        for z in found:
            assert any(abs(z[0]-p)<1e-7 and abs(z[1]-q)<1e-7 for p,q in expected),(N,z,expected)
        if N==6:
            assert len(found)==3
        else:
            assert len(found)==4,(N,len(found))
        num+=1
print('PASS:',num,'cyclic orders; exact vertex-enumeration structures and sampled positivity corroborated')
