"""Independent numerical check of circular clipping and singular coefficients.
No finite check substitutes for the geometric proof.
"""
import math
from itertools import product

PI=math.pi
TAU=2*PI

def facets(u,v,rectangle=False):
    vec=[u,v] if rectangle else [u,v,(v[0]-u[0],v[1]-u[1])]
    out=[]
    for w in vec:
        for s in (-1,1):
            z=(s*w[0],s*w[1]); r=math.hypot(*z)
            out.append((math.atan2(z[1],z[0])%TAU,r/2))
    return out

def forbidden_length(data,r):
    iv=[]
    for phi,d in data:
        if r<=d:continue
        g=math.acos(min(1,d/r))
        lo=(phi-g)%TAU; hi=(phi+g)%TAU
        if lo<=hi: iv.append((lo,hi))
        else: iv.extend(((lo,TAU),(0,hi)))
    if not iv:return 0.
    iv.sort()
    total=0.; lo,hi=iv[0]
    for l,h in iv[1:]:
        if l>hi: total+=hi-lo;lo,hi=l,h
        else:hi=max(h,hi)
    return total+hi-lo

def deriv(data,r,area):
    return r*(TAU-forbidden_length(data,r))/area

def intersection_area(data,r,N=20000):
    # midpoint angular integration of min(r, polar_radius)^2 /2
    dtheta=TAU/N; res=0.
    for j in range(N):
        theta=(j+.5)*dtheta; z=(math.cos(theta),math.sin(theta))
        edge=min((d/max(1e-30,math.cos(theta-phi)) for phi,d in data if math.cos(theta-phi)>0))
        res+=min(r,edge)**2
    return .5*dtheta*res

def run(name,u,v,rectangle):
    area=abs(u[0]*v[1]-u[1]*v[0])
    data=facets(u,v,rectangle)
    dvals=sorted(set(round(d,12) for phi,d in data))
    print(f'{name}: area={area:.10f}; distances={dvals}; facets={len(data)}')
    for di in dvals:
        k=sum(abs(d-di)<1e-10 for phi,d in data)//2
        for eps in (1e-5,1e-7,1e-9):
            df=deriv(data,di+eps,area)-deriv(data,di-eps,area)
            estimated=-area*df/(4*math.sqrt(2*di*eps))
            print(f'  distance={di:.10f}, pair count={k}, epsilon={eps:.0e}, recovered={estimated:.7f}')
        assert abs(estimated-k)<0.002
    for r in (.1, .4, .7, 1., 1.5, 3.):
        if r>=3: expected=area
        else: expected=None
        calc=intersection_area(data,r,N=30000)
        if expected is not None:assert abs(calc-expected)<1e-6,(name,calc,expected)
        print(f'  r={r:.2f}, F={calc/area:.9f}, Fprime={deriv(data,r,area):.9f}')

if __name__=='__main__':
    run('generic oblique',(1,0),(.42,1.2),False)
    run('hexagonal',(1,0),(.5,math.sqrt(3)/2),False)
    run('rectangular',(1,0),(0,1.5),True)
    run('equal upper lengths',(1,0),(.5,1.),False)
