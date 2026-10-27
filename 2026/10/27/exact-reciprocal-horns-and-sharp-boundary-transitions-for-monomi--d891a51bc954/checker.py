"""Finite diagnostics for monomial Berezin-horn formula (analytical proof separate)."""
import math

checks=0

def check(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)

def R(s,a,beta):
    return a*s*(1-1/s)**beta

def Rp(s,a,beta):
    return a*(1-1/s)**(beta-1)*(1+(beta-1)/s)

def Rpp(s,a,beta):
    return a*beta*(beta-1)*(1-1/s)**(beta-2)/s**3

def Y(s,a,beta):
    v=Rp(s,a,beta)
    return R(s,a,beta)*math.sqrt(max(0,1-v*v))

def xx(s,a,beta):
    return s-R(s,a,beta)*Rp(s,a,beta)

def envelope(y,a,beta):
    y=abs(y)
    if y==0:
        return 1.0
    if a==1.0 and y>=math.sqrt(beta*(beta-1)):
        return beta
    lo=1.0
    hi=2.0
    while Y(hi,a,beta)<y:
        hi*=2
        assert hi<1e14
    for _ in range(90):
        mid=(lo+hi)*0.5
        if Y(mid,a,beta)<y:
            lo=mid
        else:
            hi=mid
    return xx(hi,a,beta)

for m in [2,3,4,7,13]:
    beta=(m+1)/2
    for a in [0.17,0.5,0.93,1.0]:
        prevY=-1; prevX=-1
        for j in range(1,151):
            s=1+10**(-4+7*j/150)
            v=Rp(s,a,beta)
            check(0<v<a+1e-12,('slope',m,a,s))
            check(v*v+R(s,a,beta)*Rpp(s,a,beta)<a*a+2e-12,('curvature',m,a,s))
            yy=Y(s,a,beta); x=xx(s,a,beta)
            check(yy>prevY and x>prevX,('envelope monotonicity',m,a,s))
            prevY,prevX=yy,x
        # verify that analytic candidate envelope equals minimum over sampled circles
        for s0 in [1.1,1.5,2,3,6,12,30]:
            y=Y(s0,a,beta)
            g=envelope(y,a,beta)
            check(abs(g-xx(s0,a,beta))<5e-9*max(1,xx(s0,a,beta)),('tangency',m,a,s0,g))
            for mult in [0.15,0.4,0.85,0.98,1,1.03,1.1,2,5,20]:
                s=1+(s0-1)*mult
                rad=R(s,a,beta)
                if rad>=y:
                    left=s-math.sqrt(max(0,rad*rad-y*y))
                    check(left>=g-2e-8*max(1,g),('left support',m,a,s0,s,y,g,left))
            # independently recover point on actual Berezin transform via w
            rt=math.sqrt(1-1/s0)
            phase=-math.acos(Rp(s0,a,beta))/(m-1)
            w=rt*complex(math.cos(phase),math.sin(phase))
            z=(1-abs(w)**2)/(1-a*(w**m)*w.conjugate())
            u=1/z
            check(abs(u.real-g)<3e-10*max(1,g) and abs(u.imag-y)<3e-10*max(1,y),('attainment',m,a,s0,u,g,y))
        if a==1.0:
            lim=math.sqrt(beta*(beta-1))
            check(Y(1000,1,beta)<lim,('endpoint below',m))
            for mult in [1,1.2,2,4]:
                y=mult*lim
                check(envelope(y,a,beta)==beta,('flat boundary',m,y))
                for s in [1.1,2,5,20,200,2000]:
                    if R(s,a,beta)>=y:
                        left=s-math.sqrt(R(s,a,beta)**2-y*y)
                        check(left>beta,('strict exclusion',m,y,s,left,beta))

# Near-tip cusp exponent, using decreasing offsets at fixed modulus.
for m,a in [(2,0.7),(3,0.4),(5,1.)]:
    beta=(m+1)/2
    for exponent in [3,4,5]:
        s=1+10**(-exponent)
        y=Y(s,a,beta)
        z=1/complex(xx(s,a,beta),y)
        ratio=abs(z.imag)/(1-z.real)**beta
        check(abs(ratio/a-1)<0.1,('cusp approximate',m,a,s,ratio))
print('PASS',checks,'finite checks')
