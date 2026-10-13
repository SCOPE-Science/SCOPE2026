# Exact witness verification for the characteristic-two family (1)(a).
# The general exhaustion proof is in RESULT.md; this script checks the two separators.

def add(*xs):
    r = 0
    for x in xs:
        r ^= (x & 1)
    return r

def sq(x):
    return x & 1

def obstruction_values(lam,a,b,c,d,e):
    printed = add(sq(lam),a,b,c,d,e)
    at_y = add(sq(b),a)
    at_z = add(sq(d),e)
    corrected = add(sq(lam),sq(b),sq(d),a,b,c,d,e)
    return printed, at_y, at_z, corrected

# Printed-admissible but singular.
p1=(1,0,1,0,0,1)
assert obstruction_values(*p1)==(1,1,1,0)
lam,a,b,c,d,e=p1
x=y=z=1; w=0
F=add(sq(w), add(sq(x),y*z)*w, lam*x*y*z*add(y,z),
      a*y**4,b*y**3*z,c*y**2*z**2,d*y*z**3,e*z**4)
Fw=add(sq(x),y*z)
Fx=lam*y*z*add(y,z)
Fy=add(z*w,lam*x*z**2,b*y**2*z,d*z**3)
Fz=add(y*w,lam*x*y**2,b*y**3,d*y*z**2)
assert (F,Fw,Fx,Fy,Fz)==(0,0,0,0,0)

# Printed-excluded but smooth by the general exhaustion criterion.
p2=(1,0,1,1,0,1)
assert obstruction_values(*p2)==(0,1,1,1)

print('VERIFY_OK exact_obstructions=b^2+a,d^2+e,lambda^2+b^2+d^2+a+b+c+d+e witnesses=separate_printed_condition')
