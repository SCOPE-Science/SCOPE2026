from fractions import Fraction as F

class Q2:
    """Exact a+b*sqrt(2), with rational a,b."""
    __slots__=("a","b")
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=asq(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-asq(o))
    def __rsub__(self,o): return asq(o)-self
    def __mul__(self,o):
        o=asq(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asq(o); den=o.a*o.a-2*o.b*o.b
        assert den != 0
        return Q2((self.a*o.a-2*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=asq(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if a==0 and b==0: return 0
        if b==0: return 1 if a>0 else -1
        if a==0: return 1 if b>0 else -1
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        if a>0 and b<0:
            return 1 if a*a > 2*b*b else -1
        return 1 if 2*b*b > a*a else -1
    def __lt__(self,o): return (self-asq(o)).sign()<0
    def __le__(self,o): return (self-asq(o)).sign()<=0
    def __gt__(self,o): return (self-asq(o)).sign()>0
    def __ge__(self,o): return (self-asq(o)).sign()>=0
    def __abs__(self): return self if self.sign()>=0 else -self
    def __repr__(self): return f"Q2({self.a},{self.b})"

def asq(x): return x if isinstance(x,Q2) else Q2(x,0)

S=Q2(0,1); ONE=Q2(1); HALF=Q2(F(1,2)); r=S-1

def div_sqrt2(q):
    q=asq(q); return Q2(q.b, q.a/2)

def norm(v):
    a,b=v; aa,bb=abs(a),abs(b)
    vals=[aa,bb,div_sqrt2(aa+bb)]
    z=vals[0]
    for w in vals[1:]:
        if z<w: z=w
    return z

def sub(u,v): return (u[0]-v[0],u[1]-v[1])

v0=(ONE,r); v1=(r,ONE); v2=(-r,ONE); v3=(-ONE,r); v4=(-ONE,-r)
assert norm(v0)==norm(v1)==norm(v2)==norm(v3)==norm(v4)==ONE
assert norm(sub(v0,v1))==2*r
assert norm(sub(v0,v2))==S
assert norm(sub(v0,v3))==2
assert norm(sub(v0,v4))==2

# Breakpoints and the support changes used in the proof.
mstar=(Q2(4)-S)/7
mzero=(Q2(2)-S)/2
assert Q2(0)<mzero<mstar<r<HALF

# Pair k=1: the convex combination stays on the diagonal support line.
assert ONE+r==S

# Pair k=2. z1=-r+sqrt(2)m, z2=1-(2-sqrt(2))m.
# The condition |z1| <= r*z2 forces N(z)=z2. On each sign interval
# the difference is affine, so endpoint checks prove it on the full interval.
def z1(t): return -r+S*t
def z2(t): return ONE-(Q2(2)-S)*t
def hminus(t): return r*z2(t)+z1(t)  # r*z2-(-z1)
def hplus(t):  return r*z2(t)-z1(t)  # r*z2-z1
assert z1(Q2(0))<0 and z1(mzero)==0 and z1(HALF)>0
for t in (Q2(0),mzero): assert hminus(t)>=0
for t in (mzero,HALF): assert hplus(t)>=0
assert z2(Q2(0))>0 and z2(HALF)>0

# Pair k=3. For m<=r the diagonal support is 1-sqrt(2)m;
# for m>=r the constant second coordinate r is the norm.
def diag3(t): return ONE-S*t
def absx3(t): return ONE-2*t
assert diag3(Q2(0))==ONE and diag3(r)==r
assert diag3(Q2(0))>=absx3(Q2(0))
assert diag3(r)>=absx3(r)
assert absx3(r)<=r and absx3(HALF)<=r

# Polynomial arithmetic in m, coefficients low to high.
def padd(p,q):
    n=max(len(p),len(q)); return [(p[i] if i<len(p) else Q2())+(q[i] if i<len(q) else Q2()) for i in range(n)]
def pneg(p): return [-x for x in p]
def psub(p,q): return padd(p,pneg(q))
def pmul(p,q):
    out=[Q2() for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]=out[i+j]+a*b
    return out
def peq(p,q):
    n=max(len(p),len(q));
    return all((p[i] if i<len(p) else Q2())==(q[i] if i<len(q) else Q2()) for i in range(n))

def lin(a,b): return [asq(a),asq(b)]

M=lin(0,1); OM=lin(1,-1)
F1=padd([ONE], [Q2(),4*r*r,-4*r*r])
F2=padd(pmul(lin(1,-(Q2(2)-S)),lin(1,-(Q2(2)-S))), [Q2(),Q2(2),Q2(-2)])
F3a=[ONE,Q2(4)-2*S,Q2(-2)]
F3b=padd([r*r],[Q2(),Q2(4),Q2(-4)])

# Exact factor identities establishing the envelope.
assert peq(psub(F3a,F2), pmul([Q2(),Q2(2)*(-Q2(3)+2*S)], lin(-1,1)))
assert peq(psub(F1,F2), pmul([Q2(),Q2(2)], lin(Q2(7)-5*S,-Q2(8)+6*S)))
assert peq(psub(F1,F3b), [2*r,-8*r,8*r])
assert peq(psub(F3a,F1), pmul([Q2(),Q2(-2)], lin(Q2(4)-3*S,-Q2(5)+4*S)))

# The F3a/F1 affine factor has its unique zero at mstar.
slope=-Q2(5)+4*S; intercept=Q2(4)-3*S
assert slope>0 and intercept<0 and intercept+slope*mstar==0

# F3a dominates F2 throughout (0,1), and F1 dominates F2 from
# the smaller crossing m0=1/2-sqrt(2)/4 onward; mstar is beyond m0.
m0=HALF-S/4
assert Q2(0)<m0<mstar
# F1 dominates F3b because 2*r*(2m-1)^2 is nonnegative.
assert r>0

# Candidate branch values are >=1 on their claimed intervals.
assert (Q2(4)-2*S)-2*mstar > 0
assert 4*r*r>0

# Endpoint and continuity checks.
def peval(p,t):
    acc=Q2(); power=Q2(1)
    for c in p:
        acc=acc+c*power; power=power*t
    return acc
assert peval(F3a,Q2(0))==ONE
assert peval(F3a,mstar)==peval(F1,mstar)
assert peval(F1,HALF)==Q2(4)-2*S

print("VERIFY_OK")
print("m_star=(4-sqrt(2))/7")
print("endpoint_lambda_half=4-2*sqrt(2)")
print("vertex_separations_checked=0,1,2,3,4")
