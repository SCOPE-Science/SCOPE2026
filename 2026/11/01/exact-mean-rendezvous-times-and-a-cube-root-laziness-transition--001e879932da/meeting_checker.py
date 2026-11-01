"""Exact finite-state checks for synchronous lazy-walk meeting on complete bipartite graphs.

Run: python3 meeting_checker.py
Requires only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product


def expectation_formula(a, b, s):
    t = a+b
    return 1/(2*s*(1-s)) + F(4*a*b-3*t+2, 1)/( (1-s*s)*(t+s-1) ) + s*(t-2)/((1-s*s)*(t+s-1))


def solve_system(m, rhs):
    n = len(m)
    aug = [list(m[i]) + [rhs[i]] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k,n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        d = aug[k][k]
        aug[k] = [v/d for v in aug[k]]
        for i in range(n):
            if i != k and aug[i][k]:
                f = aug[i][k]
                aug[i] = [aug[i][j]-f*aug[k][j] for j in range(n+1)]
    return [aug[i][-1] for i in range(n)]


def direct_first_meeting_mean(a,b,s):
    n=a+b
    states = [(i,j) for i in range(n) for j in range(n) if i!=j]
    lookup = {k:v for v,k in enumerate(states)}
    def next_states(x):
        neigh = range(a,n) if x<a else range(a)
        d = b if x<a else a
        return [(x,s)] + [(y,(1-s)/d) for y in neigh]
    kernels=[next_states(i) for i in range(n)]
    size=len(states)
    mat=[[F(i==j) for j in range(size)] for i in range(size)]
    for row,(x,y) in enumerate(states):
        for nx,px in kernels[x]:
            for ny,py in kernels[y]:
                if nx!=ny:
                    mat[row][lookup[(nx,ny)]]-=px*py
    ans=solve_system(mat,[F(1)]*size)
    return ans[lookup[(0,a)]]


def lumped_mean(a,b,s):
    u=1-s;v=s*u
    q=[[s*s+u*u,v*(a-1)/a,v*(b-1)/b],
       [2*v,s*s,u*u*(b-1)/b],
       [2*v,u*u*(a-1)/a,s*s]]
    mat=[[F(i==j)-q[i][j] for j in range(3)] for i in range(3)]
    return solve_system(mat,[F(1)]*3)[0]


def check():
    assertions=0
    for a,b in product(range(1,5),repeat=2):
        for s in [F(1,5),F(1,3),F(1,2),F(2,3),F(4,5)]:
            f=expectation_formula(a,b,s)
            if a+b<=6:
                d=direct_first_meeting_mean(a,b,s)
                assert d==f,(a,b,s,d,f)
                assertions+=1
            # Three-state formula still valid if the unoccupied same-part class has zero size.
            l=lumped_mean(a,b,s)
            assert l==f,(a,b,s,l,f)
            assertions+=1
    # Check the exact derivative sign pattern and a unique numerical minimum.
    for a,b in product(range(1,19),repeat=2):
        x=a-1;y=b-1;t=a+b;p=a*b
        cs=[-(t-1)**2,
            -2*(t-1)*(3*t-2),
            -(10*x*x+28*x*y+34*x+10*y*y+34*y+23),
            16*x*x*y+6*x*x+16*x*y*y-4*x*y-22*x+6*y*y-22*y-24,
            48*x*x*y+35*x*x+48*x*y*y+94*x*y+40*x+35*y*y+40*y+8,
            4*(3*t-2)*(4*p-t),
            4*t*(4*p-t)]
        assert all(v<0 for v in cs[:3]) and all(v>0 for v in cs[4:])
        assert sum(cs[i]*F(1,1)**i for i in range(7)) >= 0  # s=1/2 corresponds to z=1
        assertions+=2
    # Asymptotic calibration: the leading constants are verified numerically, not proved by it.
    for n in (1000, 10000, 100000):
        h=n/2
        s=(16*h)**(-1/3)
        mean=float(expectation_formula(n,n,s))
        approx=4*h+3*(h/4)**(1/3)
        assert abs(mean-approx)<3
        assertions+=1
    print(f"PASS: {assertions-3} exact/algebraic assertions and 3 numerical asymptotic diagnostics")


if __name__=='__main__':
    check()
