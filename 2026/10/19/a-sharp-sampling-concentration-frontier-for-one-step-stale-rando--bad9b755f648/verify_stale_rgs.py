"""Exact finite checks for one-step stale randomized coordinate relaxation.

Uses only Python's standard library. It validates the conditional quadratic
identity and exact enumeration of short random-update trajectories; universal
statements are established by the accompanying algebraic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def params(n, beta):
    p = F(1, n)
    t = beta * p / (1 + beta * p)
    c = (beta * beta * p + 2 * t) / 2
    eta = (beta * beta * p - 2 * t) / 2
    assert c > t*t
    return t, c, eta


def energy(cur, prev, t, c):
    return (sum(x*x for x in cur) -
            2*t*sum(x*y for x,y in zip(cur,prev)) +
            c*sum(y*y for y in prev))


def advance(cur, prev, beta, i):
    nxt = list(cur)
    nxt[i] -= beta * prev[i]
    return tuple(nxt), tuple(cur)


def one_step(n, beta, cur, prev):
    t,c,eta = params(n,beta)
    lhs = sum((energy(*advance(cur,prev,beta,i),t,c)
               for i in range(n)), F(0)) / n
    rhs = energy(cur,prev,t,c) + eta * (
        sum(x*x for x in cur) + sum(y*y for y in prev))
    assert lhs == rhs, (n,beta,cur,prev,lhs,rhs)
    assert (eta > 0) == (beta * (1 + beta/F(n)) > 2)
    assert (eta < 0) == (beta * (1 + beta/F(n)) < 2)
    return 1


def enumerate_moments(n,beta,cur,prev,steps):
    t,c,eta = params(n,beta)
    # Exact average over all n**steps equiprobable coordinate sequences.
    states = [(cur,prev)]
    energies = [energy(cur,prev,t,c)]
    for j in range(steps):
        states = [advance(x,y,beta,i) for x,y in states for i in range(n)]
        avg = sum((energy(x,y,t,c) for x,y in states),F(0)) / len(states)
        old_avg = energies[-1]
        old_states = ([(cur,prev)] if j==0 else None)
        # Compute exact drift using the states one level earlier: this
        # agrees with conditional drift and avoids probabilistic simulation.
        ee = sum((sum(x*x for x in x1)+sum(y*y for y in y1)
                  for x1,y1 in states),F(0)) / len(states)
        assert avg >= 0
        energies.append(avg)
    return energies


def heterogeneous_check(probs, beta, diag, cur, prev):
    assert sum(probs) == 1 and min(probs) > 0
    n = len(probs)
    blocks = [params(F(1, 1) / prob, beta) for prob in probs]
    def weighted_energy(x, y):
        return sum(diag[i]*(x[i]*x[i]-2*blocks[i][0]*x[i]*y[i]
                  +blocks[i][1]*y[i]*y[i]) for i in range(n))
    lhs = sum(probs[i]*weighted_energy(*advance(cur,prev,beta,i))
              for i in range(n))
    rhs = weighted_energy(cur,prev) + sum(
        diag[i]*blocks[i][2]*(cur[i]*cur[i]+prev[i]*prev[i])
        for i in range(n))
    assert lhs == rhs
    assert (all(blocks[i][2] < 0 for i in range(n)) ==
            (beta*(1+beta*max(probs)) < 2))
    return 1


def main():
    ncheck=0
    betas=[F(1,10),F(1,4),F(1,2),F(1),F(6,5),F(3,2),F(2),F(3)]
    for n in range(2,12):
        for beta in betas:
            for seed in range(11):
                cur=tuple(F((seed+3)*(i+1)-7,seed+i+4) for i in range(n))
                prev=tuple(F((seed+5)*(i+2)-11,seed+i+7) for i in range(n))
                ncheck+=one_step(n,beta,cur,prev)
            crit=4/(1+sqrt(1+8/n))
            assert abs(crit*(1+crit/n)-2) < 2e-14
            assert 1<crit<2
    # Multi-step enumeration compared with the exact three-moment recursion.
    for n in range(2,5):
      for beta in [F(1,4),F(1),F(3,2)]:
        cur=tuple(F(i+1,i+2) for i in range(n))
        prev=tuple(F(2*i+1,i+3) for i in range(n))
        t,c,_=params(n,beta)
        U=sum(x*x for x in cur)
        V=sum(x*y for x,y in zip(cur,prev))
        W=sum(y*y for y in prev)
        energies=enumerate_moments(n,beta,cur,prev,steps=5)
        for j in range(6):
            assert energies[j] == U-2*t*V+c*W
            U,V,W=U-2*beta*V/n+beta*beta*W/n, U-beta*V/n, U
            ncheck+=1
    for n in range(2,8):
      weights=[F((i+1)*(i+2)) for i in range(n)]
      total=sum(weights)
      probs=[w/total for w in weights]
      diag=[F(i+2,i+1) for i in range(n)]
      for beta in betas:
        for seed in range(9):
          cur=tuple(F(i+1+seed,i+2) for i in range(n))
          prev=tuple(F(2*i+3-seed,i+4) for i in range(n))
          ncheck+=heterogeneous_check(probs,beta,diag,cur,prev)
    # A rational exact stationary case at n=1, beta=1, and the simple
    # two-dimensional threshold straddling check.
    t,c,eta=params(1,F(1))
    assert eta==0 and c>t*t
    assert params(2,F(6,5))[2]<0<params(2,F(5,4))[2]
    print('PASS: {} exact conditional/recurrence checks'.format(ncheck))

if __name__ == '__main__':
    main()
