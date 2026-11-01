#!/usr/bin/env python3
"""Self-contained numerical and structural checks for odd-polygon diameter limits.

The proof is analytic; finite checks here are consistency tests rather than certificates
of a general limiting theorem.
"""
import math
import random


def terms(m):
    if m < 3 or m % 2 == 0:
        raise ValueError('m must be odd and at least 3')
    p = math.sin(math.pi / (2*m))
    q = math.sin(3*math.pi / (2*m))
    return p, q, 1/(m*p*q)


def intersection_area(s, t, p, q):
    if s <= 0 or t <= 0:
        return 0.0
    if t*q <= s*p:
        return t*t/(2*p*q)
    if t*p >= s*q:
        return s*s/(2*p*q)
    return (2*q*s*t-p*(s*s+t*t))/(2*q*(q*q-p*p))


def numerical_intersection(s, t, p, q, steps=3000):
    lim = min(s/q, t/p)
    def ht(x):
        return max(0., min((s-q*x)/p,(t-p*x)/q))
    dx=lim/steps
    return dx*(0.5*(ht(0)+ht(lim)) + sum(ht(dx*k) for k in range(1,steps)))


def joint_survival(m, s, t):
    p, q, _=terms(m)
    union=(s*s+t*t)/(2*p*q)-intersection_area(s,t,p,q)
    return math.exp(-2*union/m)


def polygon_area(v):
    return abs(sum(v[i][0]*v[(i+1)%len(v)][1]-v[i][1]*v[(i+1)%len(v)][0]
                   for i in range(len(v)))/2) if len(v)>2 else 0.


def clip_halfplane(vertices, normal, threshold):
    out=[]
    for a,b in zip(vertices,vertices[1:]+vertices[:1]):
        fa=a[0]*normal[0]+a[1]*normal[1]-threshold
        fb=b[0]*normal[0]+b[1]*normal[1]-threshold
        if fa>=0:
            out.append(a)
        if (fa>=0)!=(fb>=0):
            f=fa/(fa-fb)
            out.append((a[0]+f*(b[0]-a[0]),a[1]+f*(b[1]-a[1])))
    return out


def sample_poisson(rng, mean):
    bound=math.exp(-mean)
    n=0
    product=1.0
    while product>bound:
        n+=1
        product*=rng.random()
    return n-1


def trial_limiting(m, t, rng):
    p,q,_=terms(m)
    h=t/p
    intensity=2/m
    us=[]; vs=[]
    for j in range(m):
        n=sample_poisson(rng,intensity*h*h)
        u=v=t+1
        for k in range(n):
            x,y=h*rng.random(),h*rng.random()
            u=min(u,q*x+p*y)
            v=min(v,p*x+q*y)
        us.append(u)
        vs.append(v)
    r=(m-1)//2
    return min(us[j]+vs[(j+r)%m] for j in range(m)) <=t


def uniformly_sample_point_polygon(m,rng):
    vs=[(math.cos(2*math.pi*j/m),math.sin(2*math.pi*j/m)) for j in range(m)]
    weights=[]
    for j in range(1,m-1):
        u=(vs[j][0]-vs[0][0],vs[j][1]-vs[0][1])
        w=(vs[j+1][0]-vs[0][0],vs[j+1][1]-vs[0][1])
        weights.append(abs(u[0]*w[1]-u[1]*w[0]))
    a=rng.random()*sum(weights)
    k=0
    while k<len(weights)-1 and a>weights[k]:
        a-=weights[k]; k+=1
    j=k+1
    u=math.sqrt(rng.random()); v=rng.random()
    a,b,c=(1-u,u*(1-v),u*v)
    return (a*vs[0][0]+b*vs[j][0]+c*vs[j+1][0],
            a*vs[0][1]+b*vs[j][1]+c*vs[j+1][1])


def finite_sample_deficit(m,N,rng):
    # O(N^2) check, feasible for the moderate N used here.
    pts=[uniformly_sample_point_polygon(m,rng) for _ in range(N)]
    max2=0.
    for i in range(N):
        x,y=pts[i]
        for xx,yy in pts[i+1:]:
            dist2=(x-xx)**2+(y-yy)**2
            if dist2>max2:max2=dist2
    diam=2*math.cos(math.pi/(2*m))
    return math.sqrt(N)*(diam-math.sqrt(max2))


def run():
    checks=0
    for m in (3,5,7,9,11,13):
        p,q,lam=terms(m)
        assert p<q and lam>0
        checks+=1
        verts=[(math.cos(2*math.pi*i/m),math.sin(2*math.pi*i/m)) for i in range(m)]
        r=(m-1)//2
        u=(verts[r][0]-verts[0][0],verts[r][1]-verts[0][1])
        D=math.hypot(*u)
        u=(u[0]/D,u[1]/D)
        e1=(verts[1][0]-verts[0][0],verts[1][1]-verts[0][1]);
        e2=(verts[-1][0]-verts[0][0],verts[-1][1]-verts[0][1]);
        n1=math.hypot(*e1);n2=math.hypot(*e2)
        projections=sorted((sum(a*b for a,b in zip(u,e1))/n1,
                            sum(a*b for a,b in zip(u,e2))/n2))
        assert abs(projections[0]-p)<1e-11 and abs(projections[1]-q)<1e-11
        checks+=1
        area=polygon_area(verts)
        for t in (0.003,0.007,0.012):
            cap=clip_halfplane(verts,(-u[0],-u[1]),-sum(a*b for a,b in zip(u,verts[0]))-t)
            prob=polygon_area(cap)/area
            assert abs(prob-lam*t*t)<1.e-10,(m,t,prob,lam*t*t)
            checks+=1
        for s,t in ((.23,.11),(.3,.7),(1.0,1.0),(1.,.01),(.1,1.),(1.,p/q),(1.,q/p)):
            exact=intersection_area(s,t,p,q)
            numeric=numerical_intersection(s,t,p,q)
            assert abs(exact-numeric)<8e-7, (m,s,t,exact,numeric)
            checks+=1
            P=joint_survival(m,s,t)
            assert math.exp(-lam*(s*s+t*t))-1e-12 <= P <= math.exp(-lam*max(s*s,t*t))+1e-12
            assert abs(joint_survival(m,s,t)-joint_survival(m,t,s))<1e-12
            checks+=2
        # Mean exceedance coefficient for first small-t term.
        assert abs(m*lam**2/6-1/(6*m*p*p*q*q))<1e-11
        checks+=1
    rng=random.Random(5072026)
    for m in (3,5,7):
        for threshold in (.85,1.3):
            # Uses disjoint finite domains capturing every relevant Poisson point.
            trials=2400
            success=sum(trial_limiting(m,threshold,rng) for _ in range(trials))
            assert 0<success<trials
            checks+=1
    # Restrict these finite experiments to checking basic range and convergence scale,
    # not numerical equality at fixed finite sample sizes.
    for m in (3,5):
        vals=[finite_sample_deficit(m,150,rng) for _ in range(12)]
        assert min(vals)>0 and max(vals)<8
        checks+=12
    # Compare two independent implementations at a finite sample size. The loose
    # threshold allows for ordinary finite-size bias and Monte Carlo fluctuation.
    for m in (3,5):
        threshold=1.0
        limiting=sum(trial_limiting(m,threshold,rng) for _ in range(2500))/2500
        finite=sum(finite_sample_deficit(m,320,rng)<=threshold
                   for _ in range(180))/180
        assert abs(finite-limiting)<0.16,(m,finite,limiting)
        checks+=1
    print('VERIFY_OK',checks,'deterministic and seeded checks')

if __name__ == '__main__':
    run()
