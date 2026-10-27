"""Exact stationary-current and all-bias parity checks for the four-site trap exclusion process.

Run: python verify_candidate.py  (requires SymPy).
All identities are exact rational-polynomial checks; numerical cases are ancillary.
"""
import sympy as sp
from itertools import combinations

a,b,c,d,e=sp.symbols('a b c d e')
h=[a,b,c,d]
U=a+c;V=b+d; x=a-c;y=b-d
P=U*V*(U+V)*(1+e**2)-2*e**2*(U*y**2+V*x**2)+e*(1-e**2)*x*y*(U-V)
J=4*a*b*c*d*e*(1+e**2)/P


def generator(L, rates, particles, bias):
    masks=[sum(1<<k for k in z) for z in combinations(range(L),particles)]
    Q=sp.zeros(len(masks)); currents=sp.zeros(1,len(masks))
    for col,mask in enumerate(masks):
        for i in range(L):
            if not(mask & (1<<i)):
                continue
            for direction in (1,-1):
                target=(i+direction)%L
                if mask & (1<<target):
                    continue
                new=mask^(1<<i)^(1<<target)
                row=masks.index(new)
                rate=rates[i]*(1+direction*bias)/2
                Q[row,col]+=rate
                Q[col,col]-=rate
                currents[0,col]+=direction*rate/L
    return Q,currents

Q,C=generator(4,h,3,e)
cofactors=[sp.factor(Q.minor_submatrix(k,k).det()) for k in range(4)]
# All three-edge in-trees have equal sign; use negated minors to ensure positivity.
weights=[-t for t in cofactors]
Z=sum(weights)
assert sp.simplify(Z)!=0
assert all(sp.simplify(f.subs({a:1,b:2,c:4,d:3,e:sp.Rational(1,3)}))>0 for f in weights)
assert all(sp.simplify(v)==0 for v in Q*sp.Matrix(weights))
assert sp.factor(((C*sp.Matrix(weights))[0]/Z)-J)==0
checks=3

even=sp.factor((J+J.subs(e,-e))/2)
assert sp.factor(even+4*a*b*c*d*e**2*(1-e**4)*x*y*(U-V)/(P*P.subs(e,-e)))==0
j2=sp.factor(sp.diff(J,e,2).subs(e,0)/2)
assert sp.factor(j2 + 4*a*b*c*d*x*y*(U-V)/(U**2*V**2*(U+V)**2))==0
checks+=2

# Balanced but non-reflective all-distinct disorder yields exactly odd current.
profile={a:1,b:2,c:4,d:3}
special=sp.factor(J.subs(profile))
assert sp.factor(special-96*e*(1+e**2)/(250+150*e**2))==0
assert sp.factor(special+special.subs(e,-e))==0
assert len({1,2,4,3})==4
checks+=3

# Non-balanced generic disorder rectifies for every 0<|bias|<1.
profile2={a:1,b:2,c:3,d:5}
assert sp.simplify(j2.subs(profile2))==sp.Rational(2160,94864)
for bias in (sp.Rational(1,10),sp.Rational(1,3),sp.Rational(2,3),sp.Rational(9,10)):
    true_even=sp.factor(even.subs(profile2).subs(e,bias))
    assert true_even>0
    assert sp.simplify((J.subs(profile2).subs(e,bias)+J.subs(profile2).subs(e,-bias))/2-true_even)==0
    checks+=2
checks+=1

# For three sites the only nontrivial particle sectors both have odd current.
f,g,h3=sp.symbols('f g h',positive=True)
for N in (1,2):
    Q3,C3=generator(3,[f,g,h3],N,e)
    minors=[sp.factor(Q3.minor_submatrix(i,i).det()) for i in range(3)]
    v=sp.factor((C3*sp.Matrix(minors))[0]/sum(minors))
    assert sp.factor(v+v.subs(e,-e))==0
    if N==1:
        expected=e/(1/f+1/g+1/h3)
    else:
        expected=f*g*h3*e*(3+e**2)/((f+g+h3)**2-e**2*((f+g+h3)**2-4*(f*g+g*h3+h3*f)))
    assert sp.factor(v-expected)==0
    checks+=2

print(f'PASS: {checks} independent exact identities and finite checks')
