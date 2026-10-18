#!/usr/bin/env python3
"""Standalone exact enumerator for the ring-population dynamical theorem.

No external packages or external files are required. All tests use integers and
fractions. The dynamical model is defined afresh, independently of closed forms.
"""
from itertools import product
from fractions import Fraction


def evolve(state, alpha_numer, alpha_denom):
    """Simultaneous discrete population update, carrying capacity 2."""
    n = len(state)
    answer = []
    for i, x in enumerate(state):
        balance = 2 * alpha_denom * (2 - x) - alpha_numer * (state[(i-1)%n] + state[(i+1)%n])
        sign = (balance > 0) - (balance < 0)
        answer.append(x + (sign if x else 0))
    return tuple(answer)


def masks(bits):
    n = len(bits)
    medium = tuple(int(bits[i] and not(bits[(i-1)%n] and bits[(i+1)%n])) for i in range(n))
    strong = tuple(int(bits[i] and not bits[(i-1)%n] and not bits[(i+1)%n]) for i in range(n))
    pair = tuple(int(not bits[(i-1)%n] and bits[i] and bits[(i+1)%n] and not bits[(i+2)%n]) for i in range(n))
    return medium, strong, pair


def check_dynamics():
    cases = 0
    for n in range(5,12):
        moment = {key:[0,0] for key in ('medium','strong')}
        oscillators = 0
        for bits in product((0,1),repeat=n):
            initial=tuple(x+1 for x in bits)
            med,strong,pair=masks(bits)
            oscillators+=sum(pair)
            for label,an,ad in [('medium',3,2),('critical',2,1),('strong',5,2)]:
                t1=evolve(initial,an,ad)
                t2=evolve(t1,an,ad)
                t3=evolve(t2,an,ad)
                t4=evolve(t3,an,ad)
                t5=evolve(t4,an,ad)
                assert t1==bits, (n,label,bits,'t1')
                expected=strong if label=='strong' else med
                assert tuple(int(z>0) for z in t2)==expected, (n,label,bits,'mask')
                if label=='medium':
                    assert t2==t4 and t3==t5 and all(t2[i]==2*med[i] for i in range(n))
                    assert sum(t2)-sum(t3)==2*sum(pair)
                    moment['medium'][0]+=sum(med)
                    moment['medium'][1]+=sum(med)**2
                elif label=='critical':
                    assert t3==t4==t5, (n,label,bits,'critical stationarity')
                    assert tuple(int(z>0) for z in t3)==med
                else:
                    assert t2==t3==t4==t5, (n,label,bits,'strong stationarity')
                    assert all(t2[i]==2*strong[i] for i in range(n))
                    moment['strong'][0]+=sum(strong)
                    moment['strong'][1]+=sum(strong)**2
                cases+=1
        size=2**n
        for label,mean,var in [('medium',Fraction(3*n,8),Fraction(7*n,64)),('strong',Fraction(n,8),Fraction(7*n,64))]:
            s1,s2=moment[label]
            assert Fraction(s1,size)==mean,(label,n,s1)
            assert Fraction(s2,size)-mean**2==var,(label,n,s2)
        assert Fraction(oscillators,size)==Fraction(n,16),(n,oscillators)
    return cases


def check_local_covariance():
    # All 32 five-bit patterns are enumerated; indices 1,2,3 respectively
    # identify centers at distance 0,1,2 after periodic-shift-free extension.
    exp = [('medium',Fraction(3,8),Fraction(-5,64),Fraction(1,64)),
           ('strong',Fraction(1,8),Fraction(-1,64),Fraction(1,64))]
    for regime,mu,c1,c2 in exp:
        def y(bits,idx):
            a,b,c=bits[idx-1:idx+2]
            return b*(1-a*c) if regime=='medium' else b*(1-a)*(1-c)
        # Three and four and five bit windows for means and pair products.
        mean=sum(y(bits,1) for bits in product((0,1),repeat=3))
        j1=sum(y(bits,1)*y(bits,2) for bits in product((0,1),repeat=4))
        j2=sum(y(bits,1)*y(bits,3) for bits in product((0,1),repeat=5))
        assert Fraction(mean,8)==mu
        assert Fraction(j1,16)-mu**2==c1
        assert Fraction(j2,32)-mu**2==c2
        assert mu*(1-mu)+2*c1+2*c2==Fraction(7,64)
    return len(exp)


if __name__=='__main__':
    c=check_dynamics()
    a=check_local_covariance()
    print('PASS: %d exact complete ring update/reconstruction tests; %d exact local-covariance regimes.'%(c,a))
    print('PASS: ring sizes 5..11, equilibrium/period-two patterns, means, variances, and oscillator counts.')
