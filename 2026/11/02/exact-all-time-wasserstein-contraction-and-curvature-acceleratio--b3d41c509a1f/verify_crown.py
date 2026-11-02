"""Exact-rational checks for the crown-graph heat/Wasserstein theorem.
Run with Python 3 standard library: python verify_crown.py.
Test points are t=log b, b in {2,3,5}; proof for all times is analytical.
"""
from fractions import Fraction as F


def index(side, i, n):
    return i if side == 0 else n + i


def metric(x, y, n):
    if x == y:
        return 0
    if (x < n) == (y < n):
        return 2
    return 3 if x % n == y % n else 1


def row(n, b, side, i):
    alpha, beta, gamma = (F(1, b ** (n-2)), F(1, b ** n),
                          F(1, b ** (2*n-2)))
    u, v = (alpha + beta) / 2, (alpha - beta) / 2
    common_same, common_opposite = (1+gamma)/ (2*n), (1-gamma)/(2*n)
    return [((common_same + u*(F(int(i==k))-F(1,n))) if s==side else
             (common_opposite - v*(F(int(i==k))-F(1,n))))
            for s in range(2) for k in range(n)]


def plans_and_dual(n, x, y, alpha, beta, gamma):
    # x<y in standard vertex ordering; edge/matched x=A_i,y=B_j.
    u, v, c = (alpha+beta)/2, (alpha-beta)/2, (alpha-gamma)/n
    px, py, i, j = x//n, y//n, x%n, y%n
    plan = []
    dual = None
    if px == py:
        a, b = index(px, i, n), index(px, j, n)
        oa, ob = index(1-px, i, n), index(1-px, j, n)
        plan = [(a, b, u), (ob, oa, v)]
        dual = [F(1) for _ in range(2*n)]
        dual[a] = dual[ob] = F(2)
        dual[b] = dual[oa] = F(0)
        expected = 2*alpha
    elif i==j:
        other = [k for k in range(n) if k!=i]
        plan = [(x,y,alpha-c)] + [(index(1,jj,n),index(0,other[(l+1)%len(other)],n),c)
                                     for l,jj in enumerate(other)]
        dual = [F(1) for _ in range(n)] + [F(2) for _ in range(n)]
        dual[x]=F(3)
        dual[y]=F(0)
        expected = 3*alpha+(n-4)*c
    else:
        other = [k for k in range(n) if k not in (i,j)]
        plan = [(index(0,i,n),index(1,j,n),u-c),
                (index(0,j,n),index(1,i,n),v-c)]
        plan += [(index(1,jj,n),index(0,other[(l+1)%len(other)],n),c)
                 for l,jj in enumerate(other)]
        expected = alpha+(n-4)*c
    return plan, dual, expected


def run():
    counts=0
    for n in range(5,15):
        for b in (2,3,5):
            alpha,beta,gamma = F(1,b**(n-2)),F(1,b**n),F(1,b**(2*n-2))
            c=(alpha-gamma)/n
            assert c>0 and (alpha-beta)/2>=c
            rows=[row(n,b,s,i) for s in range(2) for i in range(n)]
            for k in range(2*n):
                assert sum(rows[k])==1 and all(z>=0 for z in rows[k]); counts+=1
            for x in range(2*n):
                for y in range(x+1,2*n):
                    signed=[rows[x][k]-rows[y][k] for k in range(2*n)]
                    plan, dual, expected=plans_and_dual(n,x,y,alpha,beta,gamma)
                    inflow=[F(0)]*(2*n); outflow=[F(0)]*(2*n)
                    cost=F(0)
                    for a,z,mass in plan:
                        assert mass>=0 and signed[a]>0 and signed[z]<0
                        assert a!=z
                        outflow[a]+=mass; inflow[z]+=mass
                        cost+=mass*metric(a,z,n)
                    for k in range(2*n):
                        assert outflow[k]-inflow[k]==signed[k]
                    assert cost==expected
                    if dual is not None:
                        assert all(abs(dual[a]-dual[z])<=metric(a,z,n)
                                   for a in range(2*n) for z in range(2*n))
                        assert sum(signed[k]*dual[k] for k in range(2*n))==cost
                    else:
                        assert cost==sum(s for s in signed if s>0)
                    assert cost/F(metric(x,y,n))<=alpha+(n-4)*c
                    counts+=1
            assert alpha+(n-4)*c == (2*(n-2)*alpha-(n-4)*gamma)/n
    print('CHECK_OK exact_rational_pair_and_transport_checks=',counts,
          'orders=5..14 bases=2,3,5')

if __name__=='__main__':
    run()
