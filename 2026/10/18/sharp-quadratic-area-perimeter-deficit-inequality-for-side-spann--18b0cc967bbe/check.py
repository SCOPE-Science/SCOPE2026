"""Finite numerical cross-checks for a sharp inscribed-polygon deficit inequality."""
import math
import random


def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    pts=sorted(set(points))
    lower=[]
    for p in pts:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def area(p):
    return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p)))/2)


def per(p):
    return sum(math.dist(p[i],p[(i+1)%len(p)]) for i in range(len(p)))


def params(p):
    n=len(p);angles=[];lengths=[]
    for i,v in enumerate(p):
        a=p[(i-1)%n];b=p[(i+1)%n]
        da=math.dist(a,v);db=math.dist(b,v); lengths.append(db)
        co=max(-1.,min(1.,((a[0]-v[0])*(b[0]-v[0])+(a[1]-v[1])*(b[1]-v[1]))/(da*db)))
        angles.append(math.acos(co))
    return angles,lengths


def mark(p,i,d,forward):
    n=len(p);v=p[i];j=(i+(1 if forward else -1))%n
    L=math.dist(v,p[j]);return (v[0]+d*(p[j][0]-v[0])/L,v[1]+d*(p[j][1]-v[1])/L)


def verify(p,gaps):
    n=len(p);theta,lengths=params(p)
    samples=[mark(p,i,gaps[i][0],False) for i in range(n)]+[mark(p,i,gaps[i][1],True) for i in range(n)]
    # All side intervals between neighboring cuts must remain feasible.
    assert all(gaps[i][1]+gaps[(i+1)%n][0] <= lengths[i]+1e-12 for i in range(n))
    H=hull(samples)
    DP=per(p)-per(H);DA=area(p)-area(H)
    ks=[math.sin(t)/(8*(1-math.sin(t/2))**2) for t in theta]
    C=1/sum(1/k for k in ks)
    us=[];vs=[];local=[]
    for (x,y),t,k in zip(gaps,theta,ks):
        d=math.sqrt(max(0,x*x+y*y-2*x*y*math.cos(t)))
        u=x+y-d;v=x*y*math.sin(t)/2
        s=math.sin(t/2);z=d/(x+y) if x+y else 1.
        us.append(u);vs.append(v)
        local.append(math.sin(t)/4*(x-y)**2*(1-z)/((z+s)*(1-s)))
    assert abs(DP-sum(us))<2e-9, (DP,us)
    assert abs(DA-sum(vs))<2e-9, (DA,vs)
    assert DA+2e-9>=C*DP*DP,(DA,C*DP*DP)
    dispersion=sum((k*u-C*DP)**2/k for u,k in zip(us,ks))
    assert abs(DA-C*DP*DP-sum(local)-dispersion)<2e-9
    return DA-C*DP*DP,DP


def main():
    polygons=[[(0,0),(5,0),(4,3),(0,2)],[(0,0),(4,0),(1,3)],[(0,0),(3,0),(5,1),(3,4),(-1,2)]]
    rng=random.Random(20261014)
    count=0
    for p in polygons:
        angles,lengths=params(p);n=len(p)
        for rep in range(600):
            # For each edge, choose a small independent fraction from either endpoint.
            gaps=[(rng.uniform(.005,.18)*lengths[(i-1)%n],rng.uniform(.005,.18)*lengths[i]) for i in range(n)]
            verify(p,gaps);count+=1
        s=[math.sin(t/2) for t in angles]
        t=min(lengths[i]/((1-s[i])/math.sin(angles[i])+(1-s[(i+1)%n])/math.sin(angles[(i+1)%n])) for i in range(n))*.1
        gaps=[(t*(1-s[i])/math.sin(angles[i]),t*(1-s[i])/math.sin(angles[i])) for i in range(n)]
        defect,dp=verify(p,gaps)
        assert dp>0 and abs(defect)<2e-9,defect
    print(f'OK: {count} random hulls; 3 attained equality configurations; exact stability identity verified.')

if __name__=='__main__':
    main()
