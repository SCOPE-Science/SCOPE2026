"""Exact-rational checks for the parameterized starlike Hankel phase theorem.

Run: python3 CHECK.py
No third-party packages. These finite computations supplement, but do not
replace, the all-parameter analytical proof in RESULT.md.
"""
from fractions import Fraction as Q

count = 0

def check(condition, message):
    global count
    if not condition:
        raise AssertionError(message)
    count += 1


def div_series(num, den, order):
    out = [Q(0)] * (order + 1)
    for j in range(order + 1):
        v = num[j] if j < len(num) else Q(0)
        for k in range(1, min(j, len(den)-1) + 1):
            v -= den[k] * out[j-k]
        out[j] = v / den[0]
    return out


def independent_coefficients(c, t, x, y):
    # A Schur function: omega(z) = z (t + z xi(z))/(1+t z xi(z)),
    # xi(z)=(x+y z)/(1+x y z), with all parameters real in [-1,1].
    # The rational numerator and denominator below are expanded independently.
    w = div_series([Q(0),t,t*x*y+x,y], [Q(1),x*y+t*x,t*y],3)
    p1 = 2*w[1]
    p2 = 2*(w[2]+w[1]*w[1])
    p3 = 2*(w[3]+2*w[1]*w[2]+w[1]**3)
    g1 = c*p1
    g2 = c*(p1*g1+p2)/2
    g3 = c*(p1*g2+p2*g1+p3)/3
    return g1,g2,g3,w


def closed_coefficients(c,t,x,y):
    v=(1-t*t)*x
    w3=(1-t*t)*((1-x*x)*y-t*x*x)
    a2=2*c*t
    a3=c*v+c*(1+2*c)*t*t
    a4=2*c*w3/3+(4*c/3+2*c*c)*t*v+(2*c/3+2*c*c+4*c**3/3)*t**3
    return a2,a3,a4,v,w3


def maximum(c,mu):
    B=1+2*c
    return c*c*max(Q(1),B*(B-Q(4,3)*mu*(1+c)))

# Exact coefficient reconstruction and phase-law checks on rational grids.
for c in [Q(1,8),Q(1,3),Q(1,2),Q(3,4),Q(1)]:
    for mu in [Q(0),Q(1,5),Q(1,2),Q(3,4),Q(1)]:
        B=1+2*c
        cutoff=3*c/B
        K=B*(Q(4,3)*mu*(1+c)-B)
        A=2*((Q(4,3)+2*c)*mu-B)
        M=max(Q(1),abs(K))
        H=abs(A)+Q(4,3)*mu
        check(H<=2*M,'exact modal coefficient envelope')
        check(maximum(c,mu)==c*c*M,'absolute branch matches sharp envelope')
        check((K<=-1)==(mu<=cutoff),'phase threshold condition')
        if mu<cutoff:
            check(maximum(c,mu)==c*c*(-K),'Koebe branch')
        if mu>cutoff:
            check(maximum(c,mu)==c*c,'odd branch')
        for t in [Q(0),Q(1,6),Q(1,3),Q(2,3),Q(5,6),Q(1)]:
            for x in [-Q(1),-Q(1,2),Q(0),Q(1,3),Q(1)]:
                for y in [-Q(1),Q(0),Q(1)]:
                    a2,a3,a4,w=independent_coefficients(c,t,x,y)
                    b2,b3,b4,v,w3=closed_coefficients(c,t,x,y)
                    check((a2,a3,a4)==(b2,b3,b4),'coefficient reconstruction')
                    check(w[2]==v and w[3]==w3,'Schur coefficients')
                    direct=mu*a2*a4-a3*a3
                    alt=c*c*(K*t**4+A*t*t*v-v*v+Q(4,3)*mu*t*w3)
                    check(direct==alt,'functional identity')
                    check(abs(direct)<=maximum(c,mu),'tested rational Schur member')
        # Both extremal constructions, at every parameter pair.
        odd=independent_coefficients(c,Q(0),Q(1),Q(0))
        koebe=independent_coefficients(c,Q(1),Q(0),Q(0))
        oddval=mu*odd[0]*odd[2]-odd[1]**2
        kv=mu*koebe[0]*koebe[2]-koebe[1]**2
        check(oddval==-c*c,'odd extremal value')
        check(kv==c*c*K,'Koebe extremal value')
        check(max(abs(oddval),abs(kv))==maximum(c,mu),'exact endpoint attainment')

# Direct, strict comparison with the October 2026 bound for interior alpha and mu<1.
for c in [Q(1,8),Q(1,3),Q(1,2),Q(3,4)]:
    for mu in [Q(0),Q(1,5),Q(1,2),Q(3,4),Q(19,20)]:
        check(maximum(c,mu)<c*c*(9-8*mu),'strict improvement')
print(f'PASS: {count} exact-rational assertions')
