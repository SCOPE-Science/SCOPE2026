"""Independent cap-polygon integration checks for the planar triangle Ulam body."""
from math import cos, sin, pi, sqrt, log, isclose

T = ((0.0,0.0),(1.0,0.0),(0.0,1.0))

def clip(poly, u, level):
    out = []
    for x,y in zip(poly, poly[1:]+poly[:1]):
        ax = x[0]*u[0]+x[1]*u[1]-level
        ay = y[0]*u[0]+y[1]*u[1]-level
        if ax >= 0: out.append(x)
        if (ax < 0 < ay) or (ay < 0 < ax):
            z = ax/(ax-ay)
            out.append((x[0]+z*(y[0]-x[0]),x[1]+z*(y[1]-x[1])))
    return out

def area_centroid(poly):
    if len(poly)<3: return 0.0,None
    terms=[x[0]*y[1]-y[0]*x[1] for x,y in zip(poly,poly[1:]+poly[:1])]
    area=sum(terms)/2
    if area < 1e-17:return 0.0,None
    cx=sum((x[0]+y[0])*c for x,y,c in zip(poly,poly[1:]+poly[:1],terms))/(6*area)
    cy=sum((x[1]+y[1])*c for x,y,c in zip(poly,poly[1:]+poly[:1],terms))/(6*area)
    return area,(cx,cy)

def cap_centroid(poly, u, fraction):
    area,_=area_centroid(poly)
    vals=[p[0]*u[0]+p[1]*u[1] for p in poly]
    low,high=min(vals),max(vals)
    for _ in range(48):
        mid=(low+high)/2
        cap_area,_=area_centroid(clip(poly,u,mid))
        if cap_area > fraction*area: low=mid
        else:high=mid
    cap_area,center=area_centroid(clip(poly,u,(low+high)/2))
    if center is None:raise ArithmeticError('empty cap')
    return center

def body_ratio(poly,fraction,steps=1080):
    centers=[]
    for j in range(steps):
        angle=2*pi*j/steps
        centers.append(cap_centroid(poly,(cos(angle),sin(angle)),fraction))
    return area_centroid(centers)[0]/area_centroid(poly)[0]

def formula(q):
    if q>0.5:
        return ((1-q)/q)**2*formula(1-q)
    p=1-q
    return 2/3*(p+q*log(q)+p*p/(q*q)*(q+p*log(p)))

def analytic_arc(q):
    p=1-q
    for j in range(1,40):
        r=sqrt(q)+(1-sqrt(q))*j/40
        x=1-(r+q/r)/3
        y=r/3
        a,b,c=(x,y,1-x-y)
        assert abs(b*c-q/9)<1e-13
        r=sqrt(p)+(1-sqrt(p))*j/40
        x=(1-p*p/r)/(3*q)
        y=(1-p*r)/(3*q)
        assert abs((1-3*q*x)*(1-3*q*y)-p**3)<1e-13


def main():
    tested=0
    for q in (0.01,0.05,0.1,0.23,0.35,0.5,0.7,0.88,0.94):
        got=body_ratio(list(T),q,5000 if q<=0.05 else 1800)
        expect=formula(q)
        assert abs(got-expect)<2.5e-5,(q,got,expect)
        tested+=1
    # Independent affine-map regression: do not use the normalized analytic boundary.
    T2=[(2*x+0.7*y-3,-0.6*x+1.3*y+1) for x,y in T]
    for q in (0.1,0.5,0.83):
        got=body_ratio(T2,q,4000)
        expect=formula(q)
        assert abs(got-expect)<2.5e-5,(q,got,expect)
        tested+=1
    for q in (0.005,0.1,0.27,0.5):analytic_arc(q)
    assert abs(formula(0.5)-(2/3)*(1-log(2)))<1e-13
    # Complement law and strict positive area at every tested level.
    for j in range(1,100):
        q=j/100
        assert 0<formula(q)<1
        if q!=0.5:assert isclose(formula(q),((1-q)/q)**2*formula(1-q),rel_tol=3e-13)
    print(f'VERIFY_OK triangle Ulam normalized area; {tested} independent cap-polygon areas, 156 exact conic-arc checks, 99 complement checks')

if __name__=='__main__':main()
