#!/usr/bin/env python3
"""Exact algebraic certificate for the two-component reshuffling phase boundary.
Requires Python 3 and SymPy >= 1.12. No network or external data.
"""
import sympy as S

h, v, w = S.symbols('h v w', real=True)
P = w*(w-1)**2*h**4 + (3*w*w-4*w+1)*h**3 + (-2*w*w+5*w-5)*h**2 + (8-2*w)*h-4
H = 224*w**7+896*w**6+96*w**5-3405*w**4+1956*w**3+350*w**2-148*w-17
A = 32*w**7+20*w**6-158*w**5-395*w**4+476*w**3+62*w**2+10*w+1
B = 16*w**6+84*w**5+369*w**4-461*w**3-59*w**2-19*w-2
q = (1-h)**2 - h*h*v*v
r1, r2 = 1-h*(1-v), 1-h*(1+v)
M_iid = 1/(1-(r1*r1+r2*r2)/2)
M_rr = (r1-r2)**2/(4*(1-q)**2)+(2-r1-r2)**2/(4*(1-q*q))
assert S.factor(M_rr/M_iid-1 -2*P.subs(w,v*v)/((2-h*(1-v*v))**2*(1+q))) == 0
print('PASS exact stationary-error ratio identity')
res=S.factor(S.resultant(P,S.diff(P,h),h))
assert S.factor(res-(-4*w**3*(w-1)**4*H))==0
sub=S.subresultants(P,S.diff(P,h),h)
assert S.factor(sub[-2]-(-2*w*(w-1)**4*(A*h+B)))==0
assert S.factor(P.subs({w:v*v,h:2/(1+v)})-4*v*v*(v-1)*(2*v-1)/(v+1)**2)==0
print('PASS resultant, subresultant and stability-boundary identities')

wa_lo=S.Rational(315146,10**6);wa_hi=S.Rational(315147,10**6)
wb_lo=S.Rational(819561,10**6);wb_hi=S.Rational(819562,10**6)
assert S.Poly(H,w).count_roots(0,1)==2
for lo,hi in [(wa_lo,wa_hi),(wb_lo,wb_hi)]:
    assert S.Poly(H,w).count_roots(lo,hi)==1
    assert H.subs(w,lo)*H.subs(w,hi)<0
print('PASS rational isolation of exactly two discriminant parameters')

def interval_poly(poly,lo,hi):
    """Rigorous rational interval evaluation of a polynomial for positive interval."""
    Q=S.Poly(poly,w)
    lb=S.Rational(0); ub=S.Rational(0)
    for (k,), c in Q.terms():
        a=c*lo**k; b=c*hi**k
        lb+=min(a,b); ub+=max(a,b)
    return (lb,ub)
for lo,hi,low_h,high_h in [
    (wa_lo,wa_hi,S.Rational(116,100),S.Rational(118,100)),
    (wb_lo,wb_hi,S.Rational(119,100),S.Rational(122,100))]:
    al,au=interval_poly(A,lo,hi)
    bl,bu=interval_poly(B,lo,hi)
    assert al>0 and bu<0
    hl=-bu/au;hu=-bl/al
    assert low_h<hl<=hu<high_h
    print('PASS certified common-root enclosure',str(low_h),'< h <',str(high_h))
# First tangency is inside admissible step range; second is outside it.
assert S.Rational(118,100) < S.Rational(2)/(1+S.Rational(57,100))
assert S.Rational(119,100) > S.Rational(2)/(1+S.Rational(90,100))
print('PASS exactly one interior discriminant event')

for sample,count in [(S.Rational(1,4),1),(S.Rational(1,2),1),
                     (S.Rational(11,20),2),(S.Rational(2,3),0),
                     (S.Rational(19,20),0)]:
    poly=S.Poly(P.subs(w,sample**2),h)
    bound=S.Rational(2)/(1+sample)
    assert poly.count_roots(0,bound) - int(poly.eval(bound)==0)==count
    print('PASS exact stable-domain root count',str(sample),count)
# Uniform curvature: the other root h=2 lies at the excluded stability boundary.
assert S.factor(P.subs(w,0)-(h-1)*(h-2)**2)==0
# Strict counterexample with unequal component curvatures.
assert S.factor((M_rr/M_iid).subs({h:S.Rational(6,5),v:S.Rational(1,2)})-S.Rational(2235,2057))==0
# Equal-curvature counterexample: eta*a=3/2 gives RR/IID=9/5.
assert S.factor((M_rr/M_iid).subs({h:S.Rational(3,2),v:0})-S.Rational(9,5))==0
print('PASS exact boundary examples and equal-curvature specialization')

# Independent exact rational checks of affine recursions for diverse stable pairs.
for av,bv,eta in [(1,1,S.Rational(1,2)),(1,1,S.Rational(3,2)),
                  (1,3,S.Rational(3,5)),(1,10,S.Rational(1,6)),
                  (3,7,S.Rational(1,4))]:
    av,bv=S.Rational(av),S.Rational(bv)
    r,t=1-eta*av,1-eta*bv
    assert abs(r)<1 and abs(t)<1
    eps=eta
    # IID stationary mean vanishes; stationary second moment recurrence.
    si=eps*eps/(1-(r*r+t*t)/2)
    m=eps*(r-t)/(2*(1-r*t))
    sr=m*m+eps*eps*(2-r-t)**2/(4*(1-r*r*t*t))
    vv=(bv-av)/(av+bv); hh=eta*(av+bv)/2
    assert S.factor(sr/si-(M_rr/M_iid).subs({v:vv,h:hh}))==0
print('PASS five exact affine-recursion cross-checks')
print('ALL CERTIFICATES PASS')
