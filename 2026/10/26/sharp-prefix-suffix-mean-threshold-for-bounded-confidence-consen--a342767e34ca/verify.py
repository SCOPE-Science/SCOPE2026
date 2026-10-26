"""Exact finite-path bounded-confidence checks; no random simulation is used as proof."""
from fractions import Fraction as F
from itertools import product
from random import Random


def threshold(x):
    n = len(x)
    return max(sum(x[k:], F(0)) / (n-k) - sum(x[:k], F(0)) / k
               for k in range(1, n))


def means(x):
    n = len(x)
    return [sum(x[k:], F(0)) / (n-k) - sum(x[:k], F(0)) / k
            for k in range(1, n)]


def update(x, i, mu):
    y=list(x)
    d=y[i+1]-y[i]
    y[i]+=mu*d
    y[i+1]-=mu*d
    return tuple(y)


def gaps(x):
    return tuple(x[i+1]-x[i] for i in range(len(x)-1))


def can_freeze(x, eps):
    return any(d >= eps for d in gaps(x))


def witness_below(x, eps, mu, rounds=1000):
    """Construct finite positive-probability edge-word causing a permanent cut."""
    n=len(x)
    cut=max(range(1,n), key=lambda k: means(x)[k-1])
    schedule=[i for i in range(n-1) if i != cut-1]
    y=tuple(x)
    if can_freeze(y, eps): return (), y
    for t in range(rounds):
        i=schedule[t%len(schedule)]
        assert gaps(y)[i] < eps
        y=update(y,i,mu)
        if can_freeze(y,eps):
            return tuple(schedule[j%len(schedule)] for j in range(t+1)), y
    raise AssertionError('Did not construct a freezing word in bounded rounds')


def main():
    checks=0
    rng=Random(16023)
    for n in range(3,8):
        for trial in range(35):
            x=[F(0)]
            for j in range(1,n): x.append(x[-1]+F(rng.randint(1,9),rng.randint(1,8)))
            x=tuple(x)
            theta=threshold(x)
            ds=gaps(x)
            assert theta > max(ds)
            checks+=1
            for mu in [F(1,2),F(1,3),F(2,5)]:
                for _ in range(30):
                    state=x
                    dd=means(state)
                    for step in range(25):
                        i=rng.randrange(n-1)
                        nex=update(state,i,mu)
                        assert all(t>=0 for t in gaps(nex))
                        newdd=means(nex)
                        assert all(b<=a for a,b in zip(dd,newdd))
                        assert max(gaps(nex))<=theta
                        state,dd=nex,newdd
                        checks+=3
                if n<=6:
                    # With confidence below theta, a finite edge-word must freeze.
                    eps=(theta+max(ds))/2
                    word,state=witness_below(x,eps,mu)
                    assert can_freeze(state,eps)
                    checks+=1

    # Equality is a strict-confidence distinction for midpoint gossip.
    examples=[(3,[0,1,2],F(3,2),[1]),
              (4,[0,1,2,3],F(2),[0,2])]
    for n,a,eps,word in examples:
        x=tuple(map(F,a))
        assert threshold(x)==eps
        assert not can_freeze(x,eps)
        for i in word:
            assert gaps(x)[i] < eps
            x=update(x,i,F(1,2))
        assert can_freeze(x,eps)
        checks+=4

    # Borderline nonfreezing for five or more agents, and sub-midpoint compromises:
    for n in range(3,7):
        x=tuple(F(i) for i in range(n))
        theta=threshold(x)
        for mu in [F(1,2),F(1,3)]:
            states={x}
            for depth in range(5):
                nxt=set()
                for st in states:
                    assert not can_freeze(st,theta) if (n>=5 or mu<F(1,2)) else True
                    checks+=1
                    for i in range(n-1):
                        if gaps(st)[i]<theta: nxt.add(update(st,i,mu))
                states=nxt
                if len(states)>25000: break
    print('PASS',checks,'exact-rational assertions')

if __name__ == '__main__': main()
