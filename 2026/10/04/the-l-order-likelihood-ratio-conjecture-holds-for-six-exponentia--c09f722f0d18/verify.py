import math, random

def vals(x):
    # stable enough on stress-test domain x>=0.03
    e=math.exp(x); q=e-1.0
    b=x/q
    bp=(e*(1.0-x)-1.0)/(q*q)
    d=x+b
    dp=1.0+bp
    return b,bp,d,dp

def g(x1,y):
    bx,bpx,dx,dpx=vals(x1)
    by,bpy,dy,dpy=vals(y)
    return by*dpy+bpy*(dy-dx)

def P(a,c,x,y):
    bx,bpx,dx,dpx=vals(x)
    by,bpy,dy,dpy=vals(y)
    return bx*dpx+a*by*dpy+c*bpy*(dy-dx)

def U(xs):
    bs=[]; ds=[]
    for x in xs:
        b,bp,d,dp=vals(x); bs.append(b); ds.append(d)
    return sum(b*d for b,d in zip(bs,ds))/sum(bs)

def grad_dir(xs,v,h=1e-6):
    # centered directional difference only for stress checking.
    scale=max(1.0,max(xs))
    hh=h/scale
    xp=[x+hh*w for x,w in zip(xs,v)]
    xm=[x-hh*w for x,w in zip(xs,v)]
    if min(xm)<=0: return None
    return (U(xp)-U(xm))/(2*hh)

# Published Lemma A.2 parameter pairs newly used in the n=6 argument.
grid=[0.03,0.05,0.1,0.2,0.5,1.0,2.0,4.0,7.0,12.0]
mn=1e99
for p in (3,4,5):
    a=p-1
    for x in grid:
      for y in grid:
        z=P(a,a,x,y); mn=min(mn,z)
        if z < -2e-12:
            raise SystemExit(f'P_FAIL {p} {x} {y} {z}')

# Algebraic identity P_{p-1,p-1}(x1,y)=G(x1)+(p-1)G(y).
for p in (3,4,5):
  for x in grid:
    for y in [z for z in grid if z>=x]:
      lhs=P(p-1,p-1,x,y)
      rhs=g(x,x)+(p-1)*g(x,y)
      if abs(lhs-rhs)>2e-12*(1+abs(lhs)):
          raise SystemExit('IDENTITY_FAIL')

# Random ordered six-tuples: all three full-support new sign patterns.
rng=random.Random(20261003)
md=1e99
for _ in range(20000):
    xs=sorted(math.exp(rng.uniform(math.log(0.04),math.log(10.0))) for _ in range(6))
    for p in (3,4,5):
        v=[1.0]*p+[-1.0]*(6-p)
        d=grad_dir(xs,v)
        if d is not None:
            md=min(md,d)
            if d < -2e-7:
                raise SystemExit(f'DIR_FAIL {p} {xs} {d}')
print('VERIFY_OK')
print('min_P_grid',repr(mn))
print('min_directional_stress',repr(md))
