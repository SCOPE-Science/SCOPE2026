"""Independent exact finite-phase and trajectory checks for a three-node renewal voter cycle."""
from fractions import Fraction as F
import math
import random


def solve(rows, rhs):
    n = len(rhs)
    mat = [[F(v) for v in row] + [F(y)] for row, y in zip(rows, rhs)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if mat[r][col]), None)
        if pivot is None:
            raise AssertionError("Singular finite-phase system")
        mat[col], mat[pivot] = mat[pivot], mat[col]
        d = mat[col][col]
        mat[col] = [x / d for x in mat[col]]
        for r in range(n):
            if r == col:
                continue
            fac = mat[r][col]
            if fac:
                mat[r] = [x - fac * y for x, y in zip(mat[r], mat[col])]
    return [mat[i][-1] for i in range(n)]


def phase_system(k):
    # f_phase(x) = a_phase*x_A + b_phase*x_B + c_phase*x_C.
    # The displayed linear equations are the exact generator-harmonic identities.
    n = 3*k
    rows = []
    rhs = []
    def add(pairs, val=0):
        r = [0]*n
        for i, coef in pairs:
            r[i] += coef
        rows.append(r)
        rhs.append(val)
    def a(j): return 3*j
    def b(j): return 3*j+1
    def c(j): return 3*j+2
    for j in range(k-1):
        add([(a(j+1),k),(a(j),-k),(c(j),1)])
        add([(b(j+1),k),(b(j),-k-1)])
        add([(c(j+1),k),(c(j),-k-1),(b(j),1)])
    last=k-1
    add([(a(last),-k),(c(last),1)])
    add([(a(0),k),(b(0),k),(b(last),-k-1)])
    # The final C equation is implied by the other ones and normalization.
    add([(a(0),1),(b(0),1),(c(0),1)],1)
    ans=solve(rows,rhs)
    # Independently verify ALL generator equations, including the omitted one.
    for j in range(k-1):
        assert k*(ans[a(j+1)]-ans[a(j)])+ans[c(j)]==0
        assert k*(ans[b(j+1)]-ans[b(j)])-ans[b(j)]==0
        assert k*(ans[c(j+1)]-ans[c(j)])+ans[b(j)]-ans[c(j)]==0
    assert -k*ans[a(last)]+ans[c(last)]==0
    assert k*(ans[a(0)]+ans[b(0)]-ans[b(last)])-ans[b(last)]==0
    assert k*(ans[c(0)]-ans[c(last)])+ans[b(last)]-ans[c(last)]==0
    assert all(sum(ans[3*j:3*j+3])==1 for j in range(k))
    fresh=ans[:3]
    stationary=[sum(ans[3*j+i] for j in range(k))/k for i in range(3)]
    return fresh,stationary


def renewal_formula(k):
    phi=F(k,k+1)**k
    m=phi*F(k,k+1)
    K=1-phi+m
    fresh=[(1-phi)**2/K,phi*(1-phi)/K,m/K]
    stationary=[1-2*fresh[0],fresh[0],fresh[0]]
    return fresh,stationary


def simulate(k, stationary, runs=25000):
    rng = random.Random(314159 + 100*k + stationary)
    counts=[0,0,0]
    for _ in range(runs):
        x=[0,1,2]
        t=0.
        if stationary:
            # Equal-duration exponential stages have uniform equilibrium phase.
            remaining=rng.randrange(1,k+1)
        else:
            remaining=k
        t_a=sum(rng.expovariate(k) for _ in range(remaining))
        t_b=rng.expovariate(1)
        t_c=rng.expovariate(1)
        while len(set(x))>1:
            t=min(t_a,t_b,t_c)
            if t==t_a:
                x[0]=x[1]
                t_a=t+sum(rng.expovariate(k) for _ in range(k))
            elif t==t_b:
                x[1]=x[2]
                t_b=t+rng.expovariate(1)
            else:
                x[2]=x[0]
                t_c=t+rng.expovariate(1)
        counts[x[0]]+=1
    return [v/runs for v in counts]


def main():
    for k in range(1,13):
        from_generator=phase_system(k)
        from_renewal=renewal_formula(k)
        assert from_generator==from_renewal, (k,from_generator,from_renewal)
        print('exact Erlang shape', k, 'fresh',from_generator[0], 'stationary',from_generator[1])
    f,s=renewal_formula(2)
    assert f==[F(25,69),F(20,69),F(24,69)]
    assert s==[F(19,69),F(25,69),F(25,69)]
    assert f[0]>F(1,3)>s[0]
    for mode in (False,True):
        observed=simulate(2,mode)
        expected=[float(v) for v in (s if mode else f)]
        assert all(abs(a-b)<0.015 for a,b in zip(observed,expected)),(mode,observed,expected)
        print('trajectory simulation', 'stationary' if mode else 'fresh',observed,'expected',expected)
    print('ALL CHECKS PASSED')


if __name__=='__main__':
    main()
