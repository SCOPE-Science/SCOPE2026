import mpmath as mp
mp.mp.dps=80
iv=mp.iv
ROOT_LO=mp.mpf('1.8086448'); ROOT_HI=mp.mpf('1.8086449')
LEFT=mp.mpf('0.1'); RIGHT=mp.pi-mp.mpf('0.1')

def sh(x): return (iv.exp(x)-iv.exp(-x))/2
def ch(x): return (iv.exp(x)+iv.exp(-x))/2

def dF_iv(a,b):
    t=iv.mpf([str(a),str(b)])
    c=iv.cos(t); s=iv.sin(t); SH=sh(s); CH=ch(s)
    B=iv.cos(c)*SH
    Ap=-iv.cos(c)*s*CH+iv.sin(c)*SH*c
    Bp=iv.sin(c)*s*SH+iv.cos(c)*CH*c
    cot=iv.cos(t/2)/iv.sin(t/2)
    cotp=-iv.mpf('0.5')/(iv.sin(t/2)**2)
    return iv.mpf('0.5')*(Ap-Bp*cot-B*cotp)

def d2F_iv(a,b):
    t=iv.mpf([str(a),str(b)])
    z=iv.exp(iv.j*t)
    N=(1-z)*iv.cos(z)+iv.sin(z)
    x1=N/(1-z)**2
    x2=-iv.sin(z)/(1-z)+2*N/(1-z)**3
    return iv.re(-z*x1-z*z*x2)

def lo(x): return float(x.a)
def hi(x): return float(x.b)

def certify(a,b,neg):
    stack=[(mp.mpf(a),mp.mpf(b))]; n=0; minw=mp.inf
    while stack:
        x,y=stack.pop(); val=dF_iv(x,y); n+=1
        if (hi(val)<0 if neg else lo(val)>0):
            minw=min(minw,y-x); continue
        if y-x < mp.mpf('1e-8'):
            raise RuntimeError(('uncertified',x,y,val))
        m=(x+y)/2; stack.append((x,m)); stack.append((m,y))
    return n,minw

left=certify(LEFT,ROOT_LO,True)
right=certify(ROOT_HI,RIGHT,False)
sec=d2F_iv(ROOT_LO,ROOT_HI)
assert lo(sec)>0, sec

def dF(t):
    z=mp.e**(1j*t); N=(1-z)*mp.cos(z)+mp.sin(z)
    return mp.re(1j*z*N/(1-z)**2)
def F(t):
    z=mp.e**(1j*t); return mp.re(1+mp.sin(z)/(1-z))
root=mp.findroot(dF,(ROOT_LO,ROOT_HI)); assert ROOT_LO<root<ROOT_HI
mu=F(root)
# Exact endpoint expansions: F'(t)/t -> -sin(1)/2-cos(1)/3 at 0+;
# F'(pi-s)/s -> sin(1)/2 at pi-. They bridge small endpoint arcs.
L0=-mp.sin(1)/2-mp.cos(1)/3; Lpi=mp.sin(1)/2
assert L0<0 and Lpi>0
# Coarse endpoint-arc values are far above the minimum.
assert F(mp.mpf('0.1'))>mp.mpf('0.8') and F(mp.pi-mp.mpf('0.1'))>mp.mpf('0.55')
print('VERIFY_OK')
print('left_boxes',left[0],'min_width',mp.nstr(left[1],8))
print('right_boxes',right[0],'min_width',mp.nstr(right[1],8))
print('root_second_derivative_interval',sec)
print('root_bracket',ROOT_LO,ROOT_HI)
print('root',mp.nstr(root,50))
print('mu',mp.nstr(mu,50))
print('endpoint_ratio_limits',mp.nstr(L0,30),mp.nstr(Lpi,30))
print('endpoint_arc_values',mp.nstr(F(mp.mpf('0.1')),30),mp.nstr(F(mp.pi-mp.mpf('0.1')),30))
