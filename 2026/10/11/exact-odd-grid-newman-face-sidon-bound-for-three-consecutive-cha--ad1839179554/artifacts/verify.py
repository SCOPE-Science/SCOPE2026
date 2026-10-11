import math, random

def data(N):
    assert N>=5 and N%2==1
    xs=sorted(set(round(math.cos(2*math.pi*k/N),15) for k in range(N)))
    u=max(x for x in xs if x<0); v=min(x for x in xs if x>0)
    t=(u+v)/2; T=abs(t); D=(v-u)/2; w=u*v
    def F(r): return (T*T-w)*r**4+T*(1-w)*r**3+T*(1+w)*r-T*T
    lo,hi=0.0,1.0
    for _ in range(100):
        md=(lo+hi)/2
        if F(md)<0: lo=md
        else: hi=md
    R=(lo+hi)/2
    sig=1 if t>0 else -1
    rr=sig*R
    p=T*(1-R*R)/R
    s=1/(1+p); d=rr*s
    aa=(s+d)/2; cc=(s-d)/2; bb=1-s
    M=s*s*(1+p*p+w*(1-R*R))
    vals=[]
    for k in range(N):
        z=complex(math.cos(2*math.pi*k/N),math.sin(2*math.pi*k/N))
        vals.append(abs(aa+bb*z-cc*z*z)**2)
    assert max(abs(max(vals)-M), abs((aa+bb+cc)-1)) < 3e-11
    # convex certificate weight after orienting endpoints to midpoint +T
    if sig>0: l,h=u,v
    else: l,h=-v,-u
    lam=(D+T)*(D*R*R+T)/(2*D*T*(1+R*R))
    assert 0<lam<1
    # map weight back if reflected
    lam_actual=lam if sig>0 else 1-lam
    X=lam_actual*u+(1-lam_actual)*v
    Y=lam_actual*u*u+(1-lam_actual)*v*v
    det=16*(2*Y-X*X-Y*Y)
    assert det>0
    # stationarity of weighted quadratic in (a,c)
    ga=(-4*X*aa+2*X-4*Y*cc+4*aa+4*cc-2)
    gc=(4*X*cc-2*X-4*Y*aa+4*aa+4*cc-2)
    assert abs(ga)<2e-10 and abs(gc)<2e-10,(N,ga,gc)
    return M,1/math.sqrt(M),aa,bb,cc

mx=0
for N in range(5,1002,2):
    M,S,a,b,c=data(N)
    # random restricted-family checks
    rng=random.Random(N)
    for _ in range(40):
        x=rng.random(); y=rng.random()
        if x+y>1: x,y=1-x,1-y
        aa=x; cc=y; bb=1-aa-cc
        peak=0.0
        for k in range(N):
            z=complex(math.cos(2*math.pi*k/N),math.sin(2*math.pi*k/N))
            peak=max(peak,abs(aa+bb*z-cc*z*z)**2)
        if peak < M-2e-11: raise AssertionError((N,peak,M))
    alpha=math.pi/(2*N)
    scaled=(S-math.sqrt(2))*N*N
    mx=max(mx,abs(scaled-3*math.sqrt(2)*math.pi**2/16)) if N>200 else mx
print('VERIFY_OK odd_N=5..1001 random_per_N=40 asymptotic_tail_maxerr=%.3e'%mx)
for N in (5,7,9,11,101,1001):
    M,S,a,b,c=data(N); print(N, 'S=%.15f a=%.12f b=%.12f c=%.12f'%(S,a,b,c))
