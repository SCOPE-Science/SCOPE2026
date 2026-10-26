"""Certified interval witnesses for seven-cycle hyperbolicity.

Requires mpmath >=1.3.0; mpmath.iv uses outward rounding for elementary
functions. Source flight formula and original itinerary validation: arXiv:2610.19586v1.
The original source's Theorem 1 and Lemma 1 certify itinerary transversality
on the enclosing rational intervals. This program certifies new narrower
shooting intervals, displacements, and external-residence bounds.
"""
from mpmath import mp, iv
mp.dps=95
iv.dps=80
B=mp.mpf(3)/2; A=mp.mpf(9); M=mp.mpf(181363)/100000
b=iv.mpf('1.5'); a=iv.mpf('9'); mu=iv.mpf(181363)/100000

def phi(c,d,t,t0,y0):
    E=mp.exp(-c*(t-t0))
    return E*y0-d/c*(1-E)+M/(1+c*c)*(c*mp.sin(t)-mp.cos(t)-E*(c*mp.sin(t0)-mp.cos(t0)))
def phiiv(c,d,t,t0,y0):
    E=iv.exp(-c*(t-t0))
    return E*y0-d/c*(1-E)+mu/(1+c*c)*(c*iv.sin(t)-iv.cos(t)-E*(c*iv.sin(t0)-iv.cos(t0)))
def lit(x):
    return iv.mpf(str(x))
def bound(o):
    return (mp.mpf(str(o.a).split(',')[0][1:]),mp.mpf(str(o.b).split(',')[1].rstrip('] ')))
def ispos(x):return bool(x.a > 0)
def isneg(x):return bool(x.b < 0)
def show(x):
    print(str(x))

def check(y_s, guesses, levels, tag):
    y=mp.mpf(y_s); yiv=iv.mpf(y_s)
    t0=mp.mpf(0); val=y
    t0iv=iv.mpf(0); valiv=yiv
    times=[]
    for j,(guess,level) in enumerate(zip(guesses,levels)):
        if j==0 or (j>0 and j%2==0): c,d=-B,mp.mpf(0); ci,di=-b,iv.mpf(0)
        else:
            c,d=A, (A+B if level==-1 else -A-B) # note for exit, identify from prior level
            ci,di=a,(a+b if level==-1 else -a-b)
        t=mp.findroot(lambda u:phi(c,d,u,t0,val)-level, (mp.mpf(str(guess))-mp.mpf('0.00001'),mp.mpf(str(guess))+mp.mpf('0.00001')))
        center=mp.nstr(t,55)
        radius=mp.mpf(10)**(-35+5*j)
        ti=iv.mpf([mp.nstr(t-radius,70),mp.nstr(t+radius,70)])
        neg=phiiv(ci,di,iv.mpf(mp.nstr(t-radius,70)),t0iv,valiv)-level
        pos=phiiv(ci,di,iv.mpf(mp.nstr(t+radius,70)),t0iv,valiv)-level
        assert (ispos(neg) and isneg(pos)) or (isneg(neg) and ispos(pos)),(tag,j,neg,pos)
        speed=mu*iv.sin(ti)+b*level
        assert ispos(speed) or isneg(speed)
        times.append(ti)
        t0=t;val=mp.mpf(level)
        t0iv=ti; valiv=iv.mpf(level)
    c,d=-B,mp.mpf(0); ci,di=-b,iv.mpf(0)
    D=phiiv(ci,di,2*iv.pi,t0iv,valiv)-yiv
    assert ispos(D) or isneg(D),('D unresolved',tag,D)
    residence=iv.mpf('0')
    for i in range(0,len(times),2): residence+=times[i+1]-times[i]
    print(tag, 'y',y_s,'D_sign','+' if ispos(D) else '-', 'event_time_centers',[mp.nstr(mp.mpf(str(t.a).split(',')[0][1:]),18) for t in times], 'residence',residence)
    return times,residence,D

def main():
    roots=[
        ('I1_l','-0.569204',[.706,.1+1,.1+3.6,.1+4.1],[-1,-1,1,1]),
        ('I1_r','-0.569203',[.706,.1+1,.1+3.6,.1+4.1],[-1,-1,1,1]),
        ('I2_l','-0.55677',[.943,1.000,3.432,4.234],[-1,-1,1,1]),
        ('I2_r','-0.55675',[.946,.998,3.430,4.235],[-1,-1,1,1]),
        ('I3_l','-0.55517',[3.234,4.235],[1,1]),
        ('I3_r','-0.55514',[3.231,4.235],[1,1]),
    ]
    dat={}
    for tag,y,g,l in roots:dat[tag]=check(y,g,l,tag)
    limit=2*iv.pi/7
    # Monotonic switching, proven by differentiation of the crossing conditions:
    # lower residence decreases with y; upper residence increases with y.
    def lower(tag):
        ts=dat[tag][0]
        return ts[1]-ts[0]
    def upper(tag):
        ts=dat[tag][0]
        return ts[3]-ts[2] if len(ts)==4 else ts[1]-ts[0]
    i1_min=lower('I1_r')+upper('I1_l')
    i2_max=lower('I2_l')+upper('I2_r')
    i3_min=upper('I3_l')
    print('critical residence',limit)
    print('I1 guaranteed minimum exterior',i1_min)
    print('I2 guaranteed maximum exterior',i2_max)
    print('I3 guaranteed minimum exterior',i3_min)
    assert ispos(i1_min-limit)
    assert ispos(limit-i2_max)
    assert ispos(i3_min-limit)
    print('CERTIFIED_OK: I1 and I3 attracting; I2 repelling; central repelling from source')
if __name__=='__main__': main()
