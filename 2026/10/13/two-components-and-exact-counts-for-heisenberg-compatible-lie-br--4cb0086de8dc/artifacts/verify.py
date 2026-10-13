"""Replay: the fixed Heisenberg compatible-Lie-bracket fiber."""
import sympy as sp
from itertools import product

symbols=sp.symbols('a b c d e f g h i')
a,b,c,d,e,f,g,h,i=symbols
V=[sp.eye(3)[:,k] for k in range(3)]

def oper(x,y,ops):
    return sp.expand((x[0]*y[1]-x[1]*y[0])*ops[0]
        +(x[1]*y[2]-x[2]*y[1])*ops[1]
        +(x[2]*y[0]-x[0]*y[2])*ops[2])

first=[sp.Matrix([0,0,1]),sp.zeros(3,1),sp.zeros(3,1)]
second=[sp.Matrix([a,b,c]),sp.Matrix([d,e,f]),sp.Matrix([g,h,i])]

def jac(ops):
    x,y,z=V
    return sp.simplify(oper(oper(x,y,ops),z,ops)
        +oper(oper(y,z,ops),x,ops)
        +oper(oper(z,x,ops),y,ops))

def mixed(first,second):
    x,y,z=V
    return sp.simplify(
        oper(oper(x,y,first),z,second)
       +oper(oper(y,z,first),x,second)
       +oper(oper(z,x,first),y,second)
       +oper(oper(x,y,second),z,first)
       +oper(oper(y,z,second),x,first)
       +oper(oper(z,x,second),y,first))

assert mixed(first,second)==sp.Matrix([0,0,g-e])
assert jac(second)==sp.Matrix([-a*e+b*d-d*i+f*g,-a*h+b*g-e*i+f*h,-a*i+b*f-c*e+c*g])
assert sp.simplify(jac(second).subs(g,e)-sp.Matrix([
    e*(f-a)+d*(b-i), h*(f-a)+e*(b-i), b*(f-a)+a*(b-i)]))==sp.zeros(3,1)

for q in (3,5,7):
    # Enumerate all coefficients except the free c, independently of the fiber argument.
    count=0
    nonzero=0
    rank1=0
    for aa,bb,dd,ee,ff,hh,ii in product(range(q),repeat=7):
        uu=(ff-aa)%q; vv=(bb-ii)%q
        if (ee*uu+dd*vv)%q or (hh*uu+ee*vv)%q or (bb*uu+aa*vv)%q:
            continue
        count+=q
        if uu or vv: nonzero+=q
        else:
            if (ee*ee-dd*hh)%q==0 and (ee*aa-dd*bb)%q==0 and (hh*aa-ee*bb)%q==0:
                rank1+=q
    assert count==q**6+q**5-q**3,(q,count)
    assert nonzero==(q*q-1)*q**3,(q,nonzero)
    assert rank1==q**4+q**3-q**2,(q,rank1)
    print('field',q,'total',count,'nonzero_parameters',nonzero,'intersection',rank1)

# A separate complete direct enumeration of all 3^9 alternating bracket tables.
q=3
direct=0
for aa,bb,cc,dd,ee,ff,gg,hh,ii in product(range(q),repeat=9):
    # The mixed Jacobi identity is independently computed from the original coefficients.
    if (gg-ee)%q: continue
    if (-aa*ee+bb*dd-dd*ii+ff*gg)%q: continue
    if (-aa*hh+bb*gg-ee*ii+ff*hh)%q: continue
    if (-aa*ii+bb*ff-cc*ee+cc*gg)%q: continue
    direct+=1
assert direct==3**6+3**5-3**3
print('direct_3_power_9',direct)
print('VERIFY_OK')
