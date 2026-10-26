"""Exact rational verification of a three-agent adaptive-confidence HK phase transition."""
from fractions import Fraction as Q
from itertools import product


def step(x, c, gamma, delta):
    pairs = ((0, 1), (0, 2), (1, 2))
    on = {pair: abs(x[pair[0]]-x[pair[1]]) < c[pair] for pair in pairs}
    nx = []
    for i in range(3):
        seen = [x[i]] + [x[j] for j in range(3) if j != i and on[tuple(sorted((i,j)))]]
        nx.append(sum(seen, Q(0)) / len(seen))
    nc = {pair: (c[pair] + gamma * (1-c[pair]) if on[pair] else delta*c[pair]) for pair in pairs}
    return tuple(nx), nc, on


def check_case(x, c0, gamma, delta, horizon=15):
    u, v = x[1]-x[0], x[2]-x[1]
    assert u>0 and v>0 and max(u,v)<c0<=u+v and 0<c0<1
    assert 0<gamma<=1 and 0<delta<1
    d = u+v
    m=(2*x[0]+3*x[1]+2*x[2])/7
    c = {(0,1):c0,(0,2):c0,(1,2):c0}
    activation = next((t for t in range(horizon) if (2*delta)**t > d/c0), None)
    if delta<=Q(1,2): assert activation is None
    for t in range(horizon):
        path = activation is None or t<activation
        if path:
            assert x[2]-x[0] == d/Q(2)**t
            assert x[1]-x[0] - (x[2]-x[1]) == (u-v)*(-Q(1,6))**t
            assert c[(0,2)]==c0*delta**t
            assert c[(0,1)] == 1-(1-c0)*(1-gamma)**t
            assert c[(1,2)] == 1-(1-c0)*(1-gamma)**t
            assert (2*x[0]+3*x[1]+2*x[2])/7 == m
        if activation is not None and t>=activation+1:
            assert x[0]==x[1]==x[2]
            target=m+(v-u)*(-Q(1,6))**activation/21
            assert x[0]==target
        nx, nc, on=step(x,c,gamma,delta)
        assert on[(0,1)] and on[(1,2)]
        assert on[(0,2)] == (activation is not None and t>=activation)
        x,c=nx,nc


def run():
    tests=0
    baselines=[((Q(1,10),Q(2,5),Q(4,5)),Q(1,2)),
               ((Q(1,5),Q(1,2),Q(4,5)),Q(3,5)),
               ((Q(1,10),Q(3,10),Q(9,10)),Q(7,10)),
               ((Q(1,100),Q(1,4),Q(3,4)),Q(3,5))]
    for (x,c0),gamma,delta in product(baselines,[Q(1,10),Q(1,3),Q(1)],
                                        [Q(1,5),Q(2,5),Q(1,2),Q(3,5),Q(4,5),Q(9,10)]):
        check_case(x,c0,gamma,delta,horizon=15)
        tests+=1
    x=(Q(1,10),Q(2,5),Q(4,5))
    c0=Q(1,2)
    assert min(t for t in range(20) if (Q(6,5))**t > Q(7,5))==2
    m=(2*x[0]+3*x[1]+2*x[2])/7
    assert m==Q(3,7)
    assert m+(x[2]-2*x[1]+x[0])*(-Q(1,6))**2/21==Q(463,1080)
    print(f"PASS: {tests} parameter families, 15 exact state/update comparisons each, critical equality and finite-consensus examples.")

if __name__=='__main__':
    run()
