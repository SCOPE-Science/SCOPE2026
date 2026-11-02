"""Directed interval replay for the seven-cycle Floquet refinement.

Use Python 3 and mpmath >=1.3. The original source's itinerary theorem
is used to identify the first switching events inside its three rational
shooting intervals. This checker tests independent narrower endpoint
brackets, event-root enclosures, return signs, and uniform Floquet signs.
"""
import json
from pathlib import Path
from mpmath import iv

iv.dps=80
I=lambda s: iv.mpf(str(s))
MU=I('181363')/I('100000')
A=I('9'); B=I('1.5')
RADIUS=['1e-31','1e-28','1e-25','1e-20']

# exact real flow in each of the three affine regions
# for x'=a*x+b+MU*sin(t)
def flow(a,b,t,t0,x0):
    e=iv.exp(a*(t-t0))
    return e*x0 + b*(e-1)/a + MU*((-a*iv.sin(t)-iv.cos(t))-e*(-a*iv.sin(t0)-iv.cos(t0)))/(a*a+1)

def strictpos(x):
    return x.a>0

def strictneg(x):
    return x.b<0

def ev(y,record,half=False):
    ts=[]
    t0=I('0'); x0=I(y)
    targets=record['thresholds']
    assert len(targets)==len(record['event_centers'])
    for k,(target,center) in enumerate(zip(targets,record['event_centers'])):
        reg='M' if k==0 or k%2==0 else 'X'
        if len(targets)==2: reg='M' if k==0 else 'X'
        aa=B if reg=='M' else -A
        bb=I('0') if reg=='M' else I('10.5')*I(targets[k-1])
        rad=I(RADIUS[k])
        lo=I(center)-rad; hi=I(center)+rad
        th=I(target)
        lower=flow(aa,bb,lo,t0,x0)-th
        upper=flow(aa,bb,hi,t0,x0)-th
        direction = (-1 if (target==-1 and reg=='M') or (target==1 and reg=='X') else 1)
        if direction==1:
            assert strictneg(lower) and strictpos(upper), ('not upwards bracket',record['y'],k,lower,upper)
        else:
            assert strictpos(lower) and strictneg(upper), ('not downwards bracket',record['y'],k,lower,upper)
        # sign-definite vector-field velocity near event excludes tangency
        vel=B*th+MU*iv.sin(iv.mpf([lo.a,hi.b]))
        assert (strictpos(vel) if direction==1 else strictneg(vel)), ('tangency',record['y'],k,vel)
        ti=iv.mpf([lo.a,hi.b]);ts.append(ti)
        t0=ti;x0=th
    aa=B if len(targets)%2==0 else -A
    # even number of crossings, return in middle region
    assert len(targets) in (2,4)
    end=flow(aa,I('0'),(iv.pi if half else 2*iv.pi),t0,x0)
    return ts,end

def duration(ts):
    if len(ts)==4:
        return ts[1]-ts[0],ts[3]-ts[2]
    else:
        return None,ts[1]-ts[0]

def bounds_and_signs(data):
    out={}
    for label,rec in data.items():
        ts,py=ev(rec['y'],rec)
        d=py-I(rec['y'])
        if label.endswith('c'):
            # central y is tested by the half-period antipodal equation
            ts2,hp=ev(rec['y'],{'thresholds':rec['thresholds'][:2], 'event_centers':rec['event_centers'][:2], 'y':rec['y']},half=True)
            ant=hp+I(rec['y'])
            if label=='lowc': assert strictneg(ant), ('central left sign', ant)
            else: assert strictpos(ant), ('central right sign', ant)
        else:
            expect=(label.startswith('low1') or label.startswith('high2') or label.startswith('low3'))
            assert (strictpos(d) if expect else strictneg(d)), ('displacement sign',label,d)
        out[label]={'times':ts,'duration':duration(ts),'D':d}
        print(label, 'D=',d)
    rho=2*iv.pi/7
    for j in range(1,4):
        lo=out[f'low{j}']['duration'];hi=out[f'high{j}']['duration']
        if j!=3:
            # lower excursion length decreases with initial condition;
            # upper excursion length increases with initial condition.
            ext_min=hi[0]+lo[1]
            ext_max=lo[0]+hi[1]
        else:
            ext_min=lo[1];ext_max=hi[1]
        want_below=(j==1 or j==3)
        if want_below:
            assert strictpos(ext_min-rho), ('wrong attraction',j,ext_min-rho)
        else:
            assert strictneg(ext_max-rho), ('wrong repulsion',j,ext_max-rho)
        qlo=iv.exp(3*iv.pi-I('10.5')*ext_max)
        qhi=iv.exp(3*iv.pi-I('10.5')*ext_min)
        ranges={1:('0.99','1'),2:('1.5','1.53'),3:('0.33','0.34')}
        a,b=ranges[j]
        assert strictpos(qlo-I(a)) and strictneg(qhi-I(b)), ('floquet interval',j,qlo,qhi)
        print('family',j, 'exterior interval', ext_min, ext_max,'critical',rho,
              'Pprime interval',qlo,qhi)
    # Antisymmetric solution has equal lower- and upper-zone durations.
    # For the two candidate endpoints lower duration s decreases as y increases;
    # hence at unique Q fixed point duration <= s(lowc).
    c=out['lowc']['duration'][0]
    assert strictneg(c-iv.pi/7),('central Floquet',c-iv.pi/7)
    cmin=out['highc']['duration'][0]
    central_lo=iv.exp(3*iv.pi-I('21')*c)
    central_hi=iv.exp(3*iv.pi-I('21')*cmin)
    assert strictpos(central_lo-I('1.003')) and strictneg(central_hi-I('1.006'))
    print('central half-period lower-zone s <=',c,'< pi/7',iv.pi/7)
    print('central Floquet interval',central_lo,central_hi)
        # In total: two attracting pairs (j=1,3), one repelling pair (j=2)
    # plus one repelling central orbit = four sinks, three sources.
    print('PASS: seven hyperbolic periodic solutions, at least 4 attracting and 3 repelling')

if __name__=='__main__':
    data=json.loads((Path(__file__).parent/'centers.json').read_text())
    bounds_and_signs(data)
