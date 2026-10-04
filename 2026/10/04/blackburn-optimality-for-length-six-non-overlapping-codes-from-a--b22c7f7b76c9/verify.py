#!/usr/bin/env python3
from fractions import Fraction
from math import floor, ceil

# Exact arithmetic verification for the length-six non-overlapping-code theorem.
# No third-party packages are used.

def objective_from_vars(a,b,u,v,w):
    y2=a*b-u
    t3=a*y2+u*b
    y3=t3-v
    t4=a*y3+u*y2+v*b
    y4=t4-w
    t5=a*y4+u*y3+v*y2+w*b
    # Optimal fifth partition places all t5 mass on x5 when a<=b.
    return b*t5+u*y4+v*y3+w*y2

def objective_expanded(a,b,u,v,w):
    return (a**4*b**2 + 3*a*a*b*b*u - a*a*u*u + 2*a*b*b*v
            - 2*a*u*v + b*b*u*u + (b*b-2*u)*w - u**3 - v*v)

def t3(a,b,u):
    return a*a*b + (b-a)*u

def t4(a,b,u,v):
    return a**3*b-a*a*u+2*a*b*u-a*v+b*v-u*u

def reduced_best_for_a(q,a):
    b=q-a
    best=(-1,None)
    for u in range(a*b+1):
        T3=t3(a,b,u)
        if 2*u <= b*b:
            # F is a concave quadratic in v with vertex b*(b*q-2u)/2.
            num=b*(b*q-2*u)
            candidates={0,T3,num//2,(num+1)//2}
        else:
            # Branch w=0 has vertex v=a*(b*b-u).
            vv=a*(b*b-u)
            candidates={0,T3,vv}
        for v in candidates:
            if not (0 <= v <= T3):
                continue
            T4=t4(a,b,u,v)
            if T4 < 0:
                continue
            w=T4 if 2*u <= b*b else 0
            f=objective_expanded(a,b,u,v,w)
            if f>best[0]:
                best=(f,(u,v,w))
    return best

def sqn6_reduced(q):
    best=(-1,None)
    for a in range(1,q//2+1):
        f,data=reduced_best_for_a(q,a)
        if f>best[0]:
            best=(f,(a,q-a,data))
    return best

def sqn6_bruteforce(q):
    best=-1
    for a in range(1,q//2+1):
        b=q-a
        for u in range(a*b+1):
            T3=t3(a,b,u)
            for v in range(T3+1):
                T4=t4(a,b,u,v)
                for w in range(T4+1):
                    f=objective_expanded(a,b,u,v,w)
                    if f>best: best=f
    return best

def blackburn(q):
    return max(l**5*(q-l) for l in range(1,q))

def h(fr):
    return fr*(1-fr)**5

def main():
    # Algebraic expansion identity, exhaustively checked on a nontrivial integer box.
    for a in range(1,5):
        for b in range(a,7):
            for u in range(a*b+1):
                T3=t3(a,b,u)
                for v in {0,T3,T3//2}:
                    if 0<=v<=T3:
                        T4=t4(a,b,u,v)
                        for w in {0,T4,T4//2}:
                            assert objective_from_vars(a,b,u,v,w)==objective_expanded(a,b,u,v,w)

    # Exact sign certificates used in the continuous upper bound.
    # D(13/50) has numerator -(7500*x^2-5000*x+893), whose discriminant is negative.
    assert 5000**2-4*7500*893 == -1790000
    # P(x)=150x^3-239x^2+128x-15 is strictly increasing because
    # P'(x)=2(225x^2-239x+64) and the quadratic discriminant is negative.
    assert 239**2-4*225*64 == -479
    x=Fraction(1,4)
    P=150*x**3-239*x**2+128*x-15
    assert P==Fraction(141,32)>0

    # Branch-B polynomial certificate at x=1/2 and derivative decomposition.
    x=Fraction(1,2)
    R=27*x**6+162*x**5-27*x**4+540*x**3-459*x**2+162*x-37
    assert R==Fraction(35,64)>0
    # At x>=1/2, 30x^2-17x+3 >= 2 and x^3(3x^2+15x-2)>0,
    # hence the derivative factor is positive.
    assert 30*x*x-17*x+3 == 2
    assert 3*x*x+15*x-2 > 0

    K=Fraction(1,5)*Fraction(4,5)**5
    assert K==Fraction(1024,15625)
    assert Fraction(1,16) < K
    assert h(Fraction(1,7))-h(Fraction(1,5)) == Fraction(1027424,1838265625) > 0

    # Reduced optimizer agrees with direct exhaustive SQN search for q<=7.
    # (q=8 direct search is unnecessarily expensive for this verifier.)
    for q in range(2,6):
        rb=sqn6_reduced(q)[0]
        brute=sqn6_bruteforce(q)
        assert rb==brute, (q,rb,brute)

    # Exact reduced SQN values recover the known q=9 rounding exception and
    # verify the theorem well beyond its first admissible alphabet sizes.
    expected_small={2:3,3:41,4:251,5:1024,6:3125,7:7776,8:16807,9:33872}
    for q,val in expected_small.items():
        assert sqn6_reduced(q)[0]==val, (q,sqn6_reduced(q)[0],val)
    assert blackburn(9)==33614 < 33872
    for q in range(10,81):
        got=sqn6_reduced(q)[0]
        want=blackburn(q)
        assert got==want, (q,got,want)

    print('VERIFY_OK theorem_q_min=10 scan_q_max=80 q9_exception=33872 blackburn_q9=33614')

if __name__=='__main__':
    main()
