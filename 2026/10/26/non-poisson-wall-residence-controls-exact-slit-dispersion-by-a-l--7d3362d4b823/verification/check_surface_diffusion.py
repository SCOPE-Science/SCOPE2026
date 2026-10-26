#!/usr/bin/env python3
"""Reproduce finite-state generator identities and renewal diffusion predictions.
The Monte Carlo implementation samples physical velocity segments, not the formula.
Standard-library Python 3; run: python nonpoisson_slit_verifier.py
"""
import math
import random

SEED = 314159265
R = random.Random(SEED)


def formula(width, vbulk, tumble, vsurf, flip_decay, mean_wall, laplace):
    b = 2.0 * width / vbulk
    phi = b / (b + mean_wall)
    return (phi * vbulk*vbulk/(2.0*tumble) +
            (1.0-phi)*vsurf*vsurf/flip_decay *
            (1.0-(1.0-laplace)/(flip_decay*mean_wall)))


def generator_test(width, vbulk, tumble):
    h=width/2.0
    for j in range(31):
        y=-h+(j/30.0)*width
        c=tumble*(h*h-y*y)/(vbulk*vbulk)+2*h/vbulk
        dc=-2*tumble*y/(vbulk*vbulk)
        up=c-2*y/vbulk
        down=c+2*y/vbulk
        horiz=c+2/tumble
        avg=(up+down+2*horiz)/4
        Lu=vbulk*(dc-2/vbulk)+tumble*(avg-up)
        Ld=-vbulk*(dc+2/vbulk)+tumble*(avg-down)
        Lh=tumble*(avg-horiz)
        for z in (Lu,Ld,Lh):
            assert abs(z+1) < 1e-11, (j,z)
        if j==0:assert abs(up-2*width/vbulk)<1e-12
        if j==30:assert abs(down-2*width/vbulk)<1e-12
    # The horizontal velocity corrector has zero boundary values and the
    # following two generator identities for each cardinal state.
    velocities=(vbulk,-vbulk,0.0,0.0)
    mean_v=sum(velocities)/4
    mean_v2=sum(z*z for z in velocities)/4
    for vx in velocities:
        q_v=tumble*(mean_v-vx)
        q_v2=tumble*(mean_v2-vx*vx)
        assert abs(q_v+tumble*vx)<1e-12
        assert abs(q_v2-tumble*(vbulk*vbulk/2-vx*vx))<1e-12


def physical_cycle(width, vbulk, tumble, vsurf, flip_decay, dwell):
    remaining=dwell
    direction=1 if R.random()<.5 else -1
    surface_dx=0.0
    while remaining>0:
        flight=R.expovariate(flip_decay/2)
        dt=min(remaining,flight)
        surface_dx+=direction*vsurf*dt
        remaining-=dt
        if flight<dt+1.e-13: direction=-direction
    vertical=-width/2 if R.random()<.5 else width/2
    mode=2 if vertical<0 else 3 # R=0,L=1,U=2,D=3
    bulk_dx=0.0
    bulk_time=0.0
    while True:
        flight=R.expovariate(tumble)
        time_to_wall = ((width/2-vertical)/vbulk if mode==2
                        else (vertical+width/2)/vbulk if mode==3
                        else math.inf)
        if time_to_wall <= flight:
            bulk_time += time_to_wall
            break
        bulk_time+=flight
        if mode==0:bulk_dx+=vbulk*flight
        elif mode==1:bulk_dx-=vbulk*flight
        elif mode==2:vertical+=vbulk*flight
        else:vertical-=vbulk*flight
        mode=R.randrange(4)
    return surface_dx,bulk_dx,bulk_time


def run():
    width=1.0; vbulk=1.0; tumble=1.5
    vsurf=1.2; flip_decay=1.3; m=1.1
    generator_test(width,vbulk,tumble)
    phi=(2*width/vbulk)/(2*width/vbulk+m)
    mu=1/m
    exp_l=mu/(mu+flip_decay)
    published=phi*vbulk*vbulk/(2*tumble)+(1-phi)*vsurf*vsurf/(flip_decay+mu)
    assert abs(formula(width,vbulk,tumble,vsurf,flip_decay,m,exp_l)-published)<1e-14
    laws=[
      ('fixed',lambda:m,math.exp(-flip_decay*m),m*m),
      ('Gamma(2)',lambda:R.expovariate(2/m)+R.expovariate(2/m),(1+flip_decay*m/2)**-2,1.5*m*m),
      ('exponential',lambda:R.expovariate(1/m),1/(1+flip_decay*m),2*m*m),
    ]
    p=.8; lo=.05; hi=(m-p*lo)/(1-p)
    laws.append(('two-point',lambda:lo if R.random()<p else hi,
                p*math.exp(-flip_decay*lo)+(1-p)*math.exp(-flip_decay*hi),
                p*lo*lo+(1-p)*hi*hi))
    prev=-math.inf
    n=65000
    for name,sampler,lap,second in laws:
        d=formula(width,vbulk,tumble,vsurf,flip_decay,m,lap)
        assert d>prev, (name,'not strictly increasing in example sequence')
        prev=d
        recovered=1-flip_decay*m + flip_decay*flip_decay*m*(d-phi*vbulk*vbulk/(2*tumble))/((1-phi)*vsurf*vsurf)
        assert abs(recovered-lap)<1e-13
        # Check the finite-persistence and ballistic-surface limits.
        slow=formula(width,vbulk,tumble,vsurf,1e-5,m,
                     1-1e-5*m+.5*1e-10*second) # truncated diagnostic
        ballistic=phi*vbulk*vbulk/(2*tumble)+(1-phi)*vsurf*vsurf*second/(2*m)
        assert abs(slow-ballistic)<0.0004, (name,slow,ballistic)
        sx2=0.0; sy2=0.0; sc2=0.0; sb=0.0; ss=0.0
        for _ in range(n):
            s=sampler()
            yy,xx,b=physical_cycle(width,vbulk,tumble,vsurf,flip_decay,s)
            sx2+=xx*xx;sy2+=yy*yy;sc2+=(xx+yy)**2
            sb+=b;ss+=s
        simd=sc2/(2*(sb+ss))
        predicted_bulk_x2=(vbulk*vbulk/tumble)*(2*width/vbulk)
        predicted_surface_x2=(2*vsurf*vsurf/flip_decay)*(m-(1-lap)/flip_decay)
        assert abs((sx2/n)/predicted_bulk_x2-1)<0.06,(name,'bulk',sx2/n,predicted_bulk_x2)
        assert abs((sy2/n)/predicted_surface_x2-1)<0.06,(name,'surface',sy2/n,predicted_surface_x2)
        assert abs(simd/d-1)<0.06,(name,'total',simd,d)
        assert abs(sb/n-2*width/vbulk)<0.09,(name,'bulk duration',sb/n)
        print(f'{name}: analytic D={d:.7f}; sampled D={simd:.7f}; '
              f'bulk mean={sb/n:.5f}, sample size={n}')
    assert formula(width,vbulk,tumble,vsurf,flip_decay,m,math.exp(-flip_decay*m)) < published
    print('PASS: Poisson-generator checks, original exponential limit, convex order,')
    print('Laplace-law reconstruction, ballistic limit, 4 full physical simulations.')

if __name__=='__main__': run()
