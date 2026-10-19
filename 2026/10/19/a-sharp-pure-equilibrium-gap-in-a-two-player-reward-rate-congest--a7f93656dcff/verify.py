"""Independent exact-arithmetic calculations for a reward-rate game."""
from fractions import Fraction as F
from random import Random

ACTIONS = ((frozenset('BC'), frozenset('C')),
           (frozenset('BC'), frozenset('A')))


def rates(eta):
    e = F(eta)
    return {
        'A': {1: (2*e,F(2)), 2:(e,F(3))},
        'B': {1: (F(5),F(1)), 2:(F(4),F(2))},
        'C': {1: (F(6),F(1)), 2:(F(1),F(2))},
    }


def payoffs(eta, dat=None):
    dat = rates(eta) if dat is None else dat
    out = []
    for a in ACTIONS[0]:
        row = []
        for b in ACTIONS[1]:
            congest = {k: int(k in a) + int(k in b) for k in 'ABC'}
            vals = []
            for chosen in [a,b]:
                rewards = sum((dat[k][congest[k]][0] for k in chosen),F(0))
                times = sum((dat[k][congest[k]][1] for k in chosen),F(0))
                vals.append(rewards / times)
            row.append(tuple(vals))
        out.append(tuple(row))
    return tuple(out)


def pure_nash(matrix):
    stable = []
    for i in (0,1):
        for j in (0,1):
            if matrix[i][j][0] >= matrix[1-i][j][0] and matrix[i][j][1] >= matrix[i][1-j][1]:
                stable.append((i,j))
    return stable


def test():
    for eta in [F(1,2),F(5,4),F(3,2),F(7,4),F(2),F(3)]:
        m=payoffs(eta)
        assert m==(((F(5,4),F(5,4)),(F(11,2),eta)),((F(1,2),F(2)),(F(6),eta)))
        assert pure_nash(m)== ([(0,0)] if eta<=F(5,4) else ([] if eta<F(2) else [(1,1)]))
        for res,tab in rates(eta).items():
            assert tab[1][0]>tab[2][0]>0 and 0<tab[1][1]<tab[2][1]
    eta=F(3,2)
    m=payoffs(eta)
    gains=(m[0][1][1]-m[0][0][1],m[1][1][0]-m[0][1][0],
           m[1][0][1]-m[1][1][1],m[0][0][0]-m[1][0][0])
    assert gains==(F(1,4),F(1,2),F(1,2),F(3,4))
    assert not pure_nash(m)
    p,q=F(2,3),F(2,5)
    assert q*m[0][0][0]+(1-q)*m[0][1][0]==q*m[1][0][0]+(1-q)*m[1][1][0]
    assert p*m[0][0][1]+(1-p)*m[1][0][1]==p*m[0][1][1]+(1-p)*m[1][1][1]
    # Rational perturbations certify persistence for many nearby monotone instances.
    rng=Random(20261015)
    checked=0
    for _ in range(400):
        d=rates(eta)
        for k in 'ABC':
            for occ in (1,2):
                r,t=d[k][occ]
                d[k][occ]=(r+F(rng.randint(-2,2),100),
                           t+F(rng.randint(-2,2),100))
            assert d[k][1][0]>d[k][2][0]>0 and 0<d[k][1][1]<d[k][2][1]
        assert not pure_nash(payoffs(eta,d))
        checked+=1
    print('PASS: six exact regime and monotonicity cases, four improving-cycle inequalities, exact mixed indifference at eta=3/2,',checked,'small rational perturbations')

if __name__=='__main__': test()
