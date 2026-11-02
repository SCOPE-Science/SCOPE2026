#!/usr/bin/env python3
"""Reproduce exact witness and finite diagnostics for ring-array arrival-time theorem.

All scientific statements and limitations appear in RESULT.md. These tests
complement, rather than replace, the all-parameter analytic proof.
"""
import math, random

RING = [(1.,0.), (0.,1.),(-1.,0.),(0.,-1.),(3./5.,4./5.)]
STATIONS = RING + [(0.,0.), (2.,0.)]

def arrival(s, pos, depth, speed, origin):
    return origin + math.sqrt((s[0]-pos[0])**2+(s[1]-pos[1])**2+depth**2)/speed

def solve(a,b):
    a = [list(map(float, row))+[float(v)] for row,v in zip(a,b)]
    n=len(b)
    for j in range(n):
        k=max(range(j,n),key=lambda i:abs(a[i][j]))
        if abs(a[k][j])<1e-14: raise ArithmeticError('singular')
        a[j],a[k]=a[k],a[j]
        q=a[j][j]
        for t in range(j,n+1): a[j][t]/=q
        for i in range(n):
            if i!=j:
                q=a[i][j]
                for t in range(j,n+1): a[i][t]-=q*a[j][t]
    return [a[i][n] for i in range(n)]

def recover(stations, arrivals):
    # t^2=(2 origin)t+u^2 r^2+B_x s_x+B_y s_y+D
    mat=[[2*t, s[0]**2+s[1]**2,s[0],s[1],1.] for s,t in zip(stations,arrivals)]
    gram=[[sum(row[j]*row[k] for row in mat) for k in range(5)] for j in range(5)]
    rhs=[sum(row[j]*t*t for row,t in zip(mat,arrivals)) for j in range(5)]
    tau,A,Bx,By,D=solve(gram,rhs)
    pos=(-Bx/(2*A),-By/(2*A))
    depth2=(D+tau*tau)/A-pos[0]*pos[0]-pos[1]*pos[1]
    return pos,math.sqrt(depth2),1./math.sqrt(A),tau

def run():
    checks=0
    # A non-centred ambiguity holds at every point of the entire unit circle.
    for j in range(720):
        th=2*math.pi*j/720
        s=(math.cos(th),math.sin(th))
        t1=arrival(s,(1.,0.),2.,1.,0.)
        t2=arrival(s,(4.,0.),math.sqrt(7.),2.,0.)
        assert abs(t1-t2)<3e-15
        checks+=1
    # Adding a station at the centre distinguishes the same two models.
    assert abs(arrival((0.,0.),(1.,0.),2.,1.,0.)-arrival((0.,0.),(4.,0.),math.sqrt(7.),2.,0.))>0.1
    checks+=1
    rng=random.Random(212345)
    for j in range(1500):
        # Vary epicentral position, positive depth, speed and origin time.
        pos=(rng.uniform(-2.1,2.1),rng.uniform(-2.1,2.1))
        depth=rng.uniform(.4,3.)
        speed=rng.uniform(.5,3.)
        origin=rng.uniform(-5.,5.)
        t=[arrival(s,pos,depth,speed,origin) for s in STATIONS]
        pr,dr,vr,tr=recover(STATIONS,t)
        scale=max(1.,abs(pos[0]),abs(pos[1]),depth,speed,abs(origin))
        err=max(abs(pr[0]-pos[0]),abs(pr[1]-pos[1]),abs(dr-depth),abs(vr-speed),abs(tr-origin))/scale
        assert err<1.e-7,(j,err,pos,depth,speed,origin,pr,dr,vr,tr)
        checks+=5
    # The centred hypocentre (often singular for ring-only designs) is covered.
    for depth in [.25,.5,1.,2.,5.]:
        for speed in [.75,1.5,3.]:
            t=[arrival(s,(0.,0.),depth,speed,-1.25) for s in STATIONS]
            pos2,d2,v2,t2=recover(STATIONS,t)
            assert max(abs(pos2[0]),abs(pos2[1]),abs(d2-depth),abs(v2-speed),abs(t2+1.25))<1e-8
            checks+=5
    print(f'PASS: {checks} deterministic exact-formula and floating-point assertions')

if __name__=='__main__': run()
