from fractions import Fraction as F

# Sparse polynomial in (a,s): keys are exponent pairs (ea, es).
def add(p,q):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,F(0))+v
        if r[k]==0: del r[k]
    return r

def mul(p,q):
    r={}
    for (i,j),v in p.items():
        for (k,l),w in q.items():
            key=(i+k,j+l)
            r[key]=r.get(key,F(0))+v*w
    return {k:v for k,v in r.items() if v}

def scale(p,c): return {k:v*c for k,v in p.items() if v*c}

ONE={(0,0):F(1)}
A={(1,0):F(1)}
S={(0,1):F(1)}
S2=mul(S,S)
# beta = 1-a-a/(3s); clear denominators by representing B3s=3s*beta=3s-3as-a.
B3s=add(scale(S,F(3)), add(scale(mul(A,S),F(-3)), scale(A,F(-1))))
# g = a + 2b/3 - 2a^2/3 - ab - 2b^2/5.
# Verify after multiplying by 45 s^2, using b=B3s/(3s).
left={}
left=add(left, scale(mul(A,S2),F(45)))
left=add(left, scale(mul(B3s,S),F(10)))
left=add(left, scale(mul(mul(A,A),S2),F(-30)))
left=add(left, scale(mul(mul(A,B3s),S),F(-15)))
left=add(left, scale(mul(B3s,B3s),F(-2)))
left=add(left, scale(S2,F(-12)))  # subtract 45 s^2 * 4/15
rhs=mul(A, add(scale(S2,F(6)), add(scale(S,F(2)), scale(mul(A, add(scale(S2,F(3)), add(scale(S,F(-3)), scale(ONE,F(2))))),F(-1)))))
assert left==rhs, (left,rhs)

assert F(246,875)-F(4,15)==F(38,2625)
assert F(2,1)/F(38,2625)==F(2625,19)
# Check the polynomial identity for the alpha=3/2 lower reduction.
# 6s^2+2s-(3/2)(3s^2-3s+2)=(3s^2+13s-6)/2.
lhs=add(scale(S2,F(6)), add(scale(S,F(2)), add(scale(add(scale(S2,F(3)), add(scale(S,F(-3)), scale(ONE,F(2)))),F(-3,2)), {})))
rhs2=add(scale(S2,F(3,2)), add(scale(S,F(13,2)), scale(ONE,F(-3))))
assert lhs==rhs2, (lhs,rhs2)
print('VERIFY_OK')
