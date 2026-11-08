#!/usr/bin/env python3
"""Independent numerical cross-checks for polar-area-sum contact families.
Requires Python 3 standard library only. These are finite tests, not proof.
"""
import math

PI=math.pi

def support(theta, m, t, delta=0.0):
    s=math.sin(m*theta)
    return 1.0+t*(math.sqrt(s*s+delta*delta)-delta)

def polygon_areas(m,t,N,delta=0.0):
    assert N>10 and N % (2*m)==0
    step=2*PI/N
    c=[math.cos(step*j) for j in range(N)]
    s=[math.sin(step*j) for j in range(N)]
    h=[support(step*j,m,t,delta) for j in range(N)]
    cs=math.cos(step); sn=math.sin(step)
    vertices=[]
    for j in range(N):
        k=(j+1)%N
        vertices.append(((h[j]*s[k]-h[k]*s[j])/sn, (h[k]*c[j]-h[j]*c[k])/sn))
    def area(points):
        return .5*sum(points[j][0]*points[(j+1)%len(points)][1]-points[(j+1)%len(points)][0]*points[j][1] for j in range(len(points)))
    area_outer=area(vertices)
    polar_inside=area([(c[j]/h[j],s[j]/h[j]) for j in range(N)])
    return area_outer,polar_inside

def exact_area(m,t):return PI+4*t+.5*(1-m*m)*PI*t*t

def exact_polar(t):return (PI-2*math.asin(t))/(1-t*t)**1.5-2*t/(1-t*t)

def numerical_h1(delta,N=200000):
    dt=2*PI/N
    v=w=0.0
    for j in range(N):
        a=(j+.5)*dt
        s=math.sin(2*a);c=math.cos(2*a)
        H=math.sqrt(s*s+delta*delta)
        f=H-delta
        fp=2*s*c/H
        v+=f*f
        w+=fp*fp
    return .5*dt*(w-4*v)

checks=0
for m in [2,3,4,5,6,8]:
    for t in [.015,.08,min(.17,1/(m*m-1))*.8]:
        if t<=0:continue
        a=exact_area(m,t); b=exact_polar(t)
        for N in [2400,4800,9600]:
            if N%(2*m):continue
            x,y=polygon_areas(m,t,N)
            assert abs(x-a)<.0002, (m,t,N,x,a)
            assert abs(y-b)<.0002, (m,t,N,y,b)
            checks+=2
        d=2*PI-a-b
        assert d>0,(m,t,d)
        # Expand both area formulas independently at small deformation.
        if t==.015:
            leading=(m*m-4)*PI*t*t/2+16*t**3/3
            assert abs((d-leading)/t**3)<1.0, (m,t,d,leading)
            checks+=1

for delta in [.2,.05,.01,.002]:
    val=numerical_h1(delta,N=24000)
    assert val>0 and val<9*math.sqrt(delta),(delta,val)
    checks+=1
for t in [.08,.04,.02,.01]:
    delta=t**4
    N=48000
    dt=2*PI/N
    area=PI+sum(t*(math.sqrt(math.sin(2*(j+.5)*dt)**2+delta**2)-delta) for j in range(N))*dt
    # The full support area requires the curvature/derivative term.
    totalf=totalf2=totalder2=polarsum=0.0
    for j in range(N):
        th=(j+.5)*dt
        s=math.sin(2*th);c=math.cos(2*th);H=math.sqrt(s*s+delta*delta)
        f=H-delta
        df=2*s*c/H
        totalf+=f
        totalf2+=f*f
        totalder2+=df*df
        polarsum+=1/(1+t*f)**2
    A=PI+t*totalf*dt+.5*t*t*(totalf2-totalder2)*dt
    B=.5*polarsum*dt
    D=2*PI-A-B
    assert 4.3 < D/t**3 < 5.35,(t,D/t**3)
    checks+=1
print('PASS:',checks,'independent polygon/identity/smoothing checks')
print('Exact limiting cubic coefficient:',16/3)
