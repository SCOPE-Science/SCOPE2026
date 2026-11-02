"""Exact-rational checks for three-habitat common-catastrophe occupancy.

This standalone script uses only Python's standard library. Finite checks
are supplemental; the universal statement has an algebraic proof.
"""
from fractions import Fraction as F
from itertools import product

assertions = 0


def check(x, label):
    global assertions
    assertions += 1
    if not x:
        raise AssertionError(label)


def stationary_by_elimination(c, e, k, d, r):
    # Generator rows are origin states; transitions are counted exactly.
    Q = [[F(0) for _ in range(4)] for _ in range(4)]
    for j in range(4):
        if j < 3: Q[j][j+1] += (3-j)*(c+j*d)
        if j > 0: Q[j][j-1] += j*(e+(1-r)*k)
        if j > 0: Q[j][0] += r*k
        Q[j][j] = -sum(Q[j][z] for z in range(4) if j != z)
    B = [[Q[j][i] for j in range(4)] + [F(0)] for i in range(3)]
    B.append([F(1),F(1),F(1),F(1),F(1)])
    # Exact Gauss-Jordan elimination on stationary equations.
    for i in range(4):
        z = next(j for j in range(i,4) if B[j][i] != 0)
        B[i], B[z] = B[z], B[i]
        p = B[i][i]
        B[i] = [v/p for v in B[i]]
        for j in range(4):
            if j != i:
                f = B[j][i]
                B[j] = [v - f*w for v,w in zip(B[j],B[i])]
    ans = [B[i][4] for i in range(4)]
    check(sum(ans) == 1 and all(v > 0 for v in ans), 'unique positive equilibrium')
    return ans


def formula(c,e,k,d,r):
    s=c+e+k
    A=6*(s**3+3*c*d*s+2*c*d*d)
    B=k*(4*d*d+8*d*(e+k)-7*s*s)
    C=2*k*k*(s-2*d)
    denominator=A+B*r+C*r*r
    numerator=6*c*(c+d)*(c+2*d)
    H=7*s*s-4*d*d-8*d*(e+k)-4*k*r*(s-2*d)
    return numerator/denominator, numerator*k*H/(denominator*denominator), denominator, H


def run():
    rates=[F(1,3),F(1,2),F(1),F(2),F(3)]
    params=[F(1,5),F(1,4),F(1,2),F(3,4),F(1)]
    for c,e,k in product(rates,rates,rates):
        for d in [F(0),F(1,3),F(1),F(5,2),F(4),F(8)]:
            for r in params:
                x=stationary_by_elimination(c,e,k,d,r)
                direct=x[3]
                theoretical,derivative,den,H=formula(c,e,k,d,r)
                check(direct == theoretical, 'joint occupancy exact')
                check(den>0, 'positive partition denominator')
                check((derivative>0) == (H>0), 'derivative sign')
                check((derivative<0) == (H<0), 'derivative sign negative')
    # Exact natural nonmonotone witness c=e=k=1, d=5/2.
    c=e=k=F(1);d=F(5,2)
    left=formula(c,e,k,d,F(0))[0]
    midpoint=formula(c,e,k,d,F(1,4))[0]
    right=formula(c,e,k,d,F(1))[0]
    check(left==F(21,62),'left endpoint')
    check(midpoint==F(504,1489),'strict interior minimum')
    check(right==F(63,185),'right endpoint')
    check(midpoint<left and midpoint<right,'interior minimum strict')
    check(formula(c,e,k,d,F(1,4))[1]==0,'zero derivative at 1/4')
    print('VERIFY_OK assertions=',assertions)
    print('witness:',left,midpoint,right)

if __name__=='__main__':
    run()
