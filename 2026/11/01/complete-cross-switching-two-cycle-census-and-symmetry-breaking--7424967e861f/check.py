"""Standalone symbolic and numerical spot checks of the symmetric CNV two-cycle theorem.
Run: python check.py. No external file dependencies besides sympy.
"""
import sympy as s
u,m,b=s.symbols('u m b',positive=True,real=True)
x=s.symbols('x',real=True)
F=lambda z: m*z*(z-s.Rational(1,2))*(1-z)
B=4*u+m*u/s.Integer(2)-2*m*u**3
L=s.Rational(1,2)-u
R=s.Rational(1,2)+u
left=L+F(L)+b/2
right=R+F(R)-b/2
assert s.simplify(left-R - (b-B)/2)==0
assert s.simplify(right-L - (B-b)/2)==0
assert s.simplify(F(1-x)+F(x))==0
D=s.factor(s.diff(x+F(x),x).subs(x,L))
assert s.simplify(D-(1+m*(s.Rational(1,4)-3*u*u)))==0
assert s.factor(s.diff(B,u)-2*(D+1))==0
ustar=s.sqrt((m+8)/(12*m)); bstar=(m+8)**s.Rational(3,2)/(6*s.sqrt(3*m))
assert s.simplify(B.subs(u,ustar)-bstar)==0
assert s.simplify(s.diff(B,u).subs(u,ustar))==0
assert s.simplify(D.subs(u,ustar)+1)==0
assert s.simplify((B-2)+(2*u-1)*(2*m*u*u+m*u-4)/2)==0
u0=(s.sqrt(1+32/m)-1)/4
assert s.simplify(B.subs(u,u0)-2)==0
um=s.sqrt(s.Rational(1,12)); bflip=(m+12)/(6*s.sqrt(3))
assert s.simplify(B.subs(u,um)-bflip)==0
mucrit=12*(s.sqrt(3)-1)
assert s.simplify(bflip.subs(m,mucrit)-2)==0
for mv,bv,expect in [(2,s.Rational(3,2),1),(4,2,0),(6,s.Rational(203,100),2),(12,s.Rational(21,10),2),(12,s.Rational(12,5),2),(12,3,0),(6,2,1)]:
    z=s.symbols('z',real=True)
    eq=s.Poly(B.subs({m:mv,u:z})-bv,z)
    roots=s.polys.polytools.intervals(eq,eps=s.Rational(1,10**12))
    admissible=[]
    for (lo,hi),mult in roots:
        c=float((lo+hi)/2)
        if 0<c<.5:admissible.append(c)
    assert len(admissible)==expect,(mv,bv,admissible,expect)
    for z0 in admissible:
        xx=.5-z0;yy=.5+z0
        gl=xx+float(F(xx).subs(m,mv))+float(bv)/2
        gr=yy+float(F(yy).subs(m,mv))-float(bv)/2
        assert abs(gl-yy)<1e-9 and abs(gr-xx)<1e-9
        multiplier=float((1+mv*(.25-3*z0*z0))**2)
        if mv==6 and float(bv)>2:
            assert (multiplier<1 if z0==min(admissible) else multiplier>1)
        if mv==12 and bv==s.Rational(21,10):
            assert multiplier>1
        if mv==12 and bv==s.Rational(12,5):
            assert (multiplier<1 if z0==min(admissible) else multiplier>1)
print('SYMBOLIC_IDENTITIES_OK; EXACT_RATIONAL_ROOT_COUNTS_OK; LOCAL_STABILITY_SAMPLES_OK')
# Full crossing-cycle nonsymmetric branch: r,v positive, r != v.
r,v,t=s.symbols('r v t',positive=True)
Gminus=(s.Rational(1,2)-r)+F(s.Rational(1,2)-r)+b/2
Gplus=(s.Rational(1,2)+v)+F(s.Rational(1,2)+v)-b/2
E1=s.factor(Gminus-(s.Rational(1,2)+v))
E2=s.factor(Gplus-(s.Rational(1,2)-r))
assert s.simplify((E1+E2)/m - (v-r)*(s.Rational(1,4)-r*r-r*v-v*v))==0
# The pair also satisfies E1=E2=0 when r^2+rs+v^2=1/4 and b=2(r+v)(1+m*r*v).
bnew=2*(r+v)*(1+m*r*v)
assert s.simplify(s.rem(E1.subs(b,bnew),r*r+r*v+v*v-s.Rational(1,4),r))==0
assert s.simplify(s.rem(E2.subs(b,bnew),r*r+r*v+v*v-s.Rational(1,4),r))==0
bt=2*t*(1+m*(t*t-s.Rational(1,4)))
crit=(m+12)/(6*s.sqrt(3))
assert s.simplify(bt.subs(t,s.Rational(1,2))-1)==0
assert s.simplify(bt.subs(t,1/s.sqrt(3))-crit)==0
assert s.simplify(s.diff(bt,t)-2*(1+m*(3*t*t-s.Rational(1,4))))==0
# Period-two multiplier for nonsymmetric pairs, in t-coordinate.
lam=s.factor((1+m*(s.Rational(1,4)-3*r*r))*(1+m*(s.Rational(1,4)-3*v*v)))
lamt=s.factor((1+m/4)**2-3*m*(1+m/4)*(s.Rational(1,2)-t*t)+9*m*m*(t*t-s.Rational(1,4))**2)
assert s.factor(lamt-1)==m*(3*t*t-1)*(12*m*t*t-m+4)/4
for mv,bv,expected in [(2,s.Rational(9,10),0),(2,s.Rational(11,10),2),(2,s.Rational(3,2),0),(6,s.Rational(13,10),2),(12,s.Rational(21,10),2),(12,s.Rational(12,5),0)]:
    p=s.Poly(bt.subs({m:mv,t:t})-bv,t)
    intervals=s.polys.polytools.intervals(p,eps=s.Rational(1,10**12))
    ts=[float((iv[0][0]+iv[0][1])/2) for iv in intervals if 0.5<float((iv[0][0]+iv[0][1])/2)<3**(-.5)]
    assert 2*len(ts)==expected,(mv,bv,ts,expected)
    for tt in ts:
        disc=(1-3*tt*tt)**.5
        rr=(tt+disc)/2; ss=(tt-disc)/2
        for r0,s0 in [(rr,ss),(ss,rr)]:
            xx=.5-r0;yy=.5+s0
            assert abs(xx+float(F(xx).subs(m,mv))+float(bv)/2-yy)<1e-9
            assert abs(yy+float(F(yy).subs(m,mv))-float(bv)/2-xx)<1e-9
print('NONSYMMETRIC_CYCLE_IDENTITIES_AND_COUNTS_OK')
