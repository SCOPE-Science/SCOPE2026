"""Exact rational checks for a two-oscillator heat-flow optimization theorem.

Only Python's standard library is required. The algebraic proof of the
all-parameter statements is given in RESULT.md; finite tests are checks only.
"""
from fractions import Fraction as Q


def solve(matrix, rhs):
    n = len(rhs)
    z = [list(map(Q, row)) + [Q(rhs[i])] for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if z[i][j]), None)
        if pivot is None:
            raise ArithmeticError("singular linear system")
        z[j], z[pivot] = z[pivot], z[j]
        scale = z[j][j]
        z[j] = [x / scale for x in z[j]]
        for i in range(n):
            if i != j:
                factor = z[i][j]
                if factor:
                    z[i] = [x - factor*y for x, y in zip(z[i], z[j])]
    return [row[-1] for row in z]


def stationary_covariance(u, v, k, g, h, t1, t2):
    u,v,k,g,h,t1,t2 = map(Q, (u,v,k,g,h,t1,t2))
    a,b = u+k, v+k
    drift = [[Q(0), Q(0), Q(1), Q(0)],
             [Q(0), Q(0), Q(0), Q(1)],
             [-a, k, -g, Q(0)],
             [k, -b, Q(0), -h]]
    noise = [[Q(0) for _ in range(4)] for _ in range(4)]
    noise[2][2], noise[3][3] = 2*g*t1, 2*h*t2
    pairs = [(i,j) for i in range(4) for j in range(i,4)]
    eqs, rhs = [], []
    for i,j in pairs:
        row = []
        for p,q in pairs:
            def coeff(t,s):
                return Q((t==p and s==q) or (t==q and s==p))
            row.append(sum(drift[i][w]*coeff(w,j) + drift[j][w]*coeff(i,w)
                           for w in range(4)))
        eqs.append(row)
        rhs.append(-noise[i][j])
    ans = solve(eqs,rhs)
    covariance = [[Q(0) for _ in range(4)] for _ in range(4)]
    for (i,j),v0 in zip(pairs,ans): covariance[i][j]=covariance[j][i]=v0
    return covariance


def analytic_current(u,v,k,g,h,t1,t2):
    u,v,k,g,h,t1,t2=map(Q,(u,v,k,g,h,t1,t2))
    a,b=u+k,v+k
    return k*k*(t1-t2) / ((a-b)**2/(g+h) + k*k*(g+h)/(g*h) + a*h+b*g)


def optimal_share(u,v,k,budget):
    a,b=float(u+k),float(v+k)
    kk=float(k*k)
    G=float(budget)
    def deriv(p):
        return kk*(2*p-1)/(p*p*(1-p)*(1-p))+G*G*(b-a)
    left,right=1.e-12,1.-1.e-12
    assert deriv(left)<0<deriv(right)
    for _ in range(100):
        mid=(left+right)/2
        if deriv(mid)<0:left=mid
        else:right=mid
    return (left+right)/2


def main():
    examples = [
        (1, 3, 2, 2, 3, 5, 1),
        (3, 1, 1, 3, 2, 10, 3),
        (2, 2, 1, 1, 4, 4, 2),
        (1, 10, 3, 7, 1, 7, 0),
        (8, 3, 2, 5, 9, 10, 6),
        (4, 7, 5, 8, 1, 11, 2),
        (17, 1, 4, 1, 8, 1, 0),
        (2, 11, 1, 19, 7, 17, 2),
    ]
    for args in examples:
        u,v,k,g,h,t1,t2=map(Q,args)
        c=stationary_covariance(*args)
        measured=g*(t1-c[2][2])
        same_flux=k*c[0][3]
        opposite=h*(c[3][3]-t2)
        prediction=analytic_current(*args)
        assert measured == same_flux == opposite == prediction,(args,measured,same_flux,opposite,prediction)
        assert c[0][2]==c[1][3]==Q(0) and c[0][3]==-c[1][2]
    for u,v,k,G in [(3,8,2,10),(8,3,2,10),(3,3,2,10),(2,30,1,100),(30,2,1,100),(1,5,4,2)]:
        p=optimal_share(u,v,k,G)
        if u==v: assert abs(p-.5)<1e-12
        else: assert (p-.5)*(u-v)>0
        best=float(analytic_current(Q(u),Q(v),Q(k),Q(str(p*G)),Q(str((1-p)*G)),Q(3),Q(1)))
        for fraction in (.01,.05,.1,.2,.35,.5,.65,.8,.9,.95,.99):
            trial=float(analytic_current(Q(u),Q(v),Q(k),Q(str(G*fraction)),Q(str(G*(1-fraction))),Q(3),Q(1)))
            assert best >= trial-1e-10
    print('PASS: 8 exact-rational stationary covariance/current checks, 6 optimality grids')


if __name__=='__main__':main()
