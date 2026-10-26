#!/usr/bin/env python3
"""Exact-rational verifier for the cubic ordinary divisor-range decomposition.

Uses Python's standard library only. This finite program certifies the
finite rational comparisons, not the infinite prime-interval theorem.
"""
from fractions import Fraction as Q
from itertools import product

HEAD = ((2, 2), (3, 1), (5, 1), (7, 1))


def cubic_factor(p, a):
    return sum((Q(1, p ** (3*j)) for j in range(a + 1)), Q(0))


def bounds_on_T(N=200):
    zpart = sum((Q(1, n**3) for n in range(1, N + 1)), Q(0))
    zlo = zpart + Q(1, 2*(N+1)**2)
    zhi = zpart + Q(1, 2*N**2)
    pref = Q(1)
    for p, _ in HEAD:
        pref *= 1-Q(1,p**3)
    return zlo*pref, zhi*pref


def options():
    data = []
    for p,A in HEAD:
        choices = []
        for a in range(A):
            u = cubic_factor(p,a)
            choices.append((str(a),u,u,Q(p-1,p**(a+1))))
        choices.append((str(A)+'+',cubic_factor(p,A),Q(p**3,p**3-1),Q(1,p**A)))
        data.append(choices)
    return data


def tabulate(Tlo,Thi):
    rows=[]
    for choices in product(*options()):
        lab=tuple(c[0] for c in choices)
        lo=hi=weight=Q(1)
        for _,l,h,w in choices:
            lo*=l;hi*=h;weight*=w
        rows.append((lab,lo,hi,weight))
    assert len(rows)==24
    rows.sort(key=lambda x:x[1])
    assert len(set(x[1] for x in rows))==24
    groups=[]; comparisons=[]
    for name,l,u,w in rows:
        if not groups:
            groups.append(dict(low=l,upper_mult=u,density=w,names=[name]))
            continue
        prev=groups[-1]
        # Exact rational disjoint-vs-overlap certificate, interval arithmetic.
        if l > prev['upper_mult']*Thi:
            comparisons.append(('gap',prev['upper_mult'],l))
            groups.append(dict(low=l,upper_mult=u,density=w,names=[name]))
        else:
            assert l < prev['upper_mult']*Tlo, (name,l,prev)
            comparisons.append(('overlap',prev['upper_mult'],l))
            prev['density']+=w
            prev['names'].append(name)
            prev['upper_mult']=max(prev['upper_mult'],u)
    assert len(groups)==14
    assert len([c for c in comparisons if c[0]=='gap'])==13
    assert len([c for c in comparisons if c[0]=='overlap'])==10
    assert sum(g['density'] for g in groups)==1
    assert groups[0]['low']==1 and groups[0]['upper_mult']==1
    full_head = Q(1)
    for p, _ in HEAD:
        full_head *= Q(p**3, p**3 - 1)
    assert groups[-1]['upper_mult'] == full_head
    return rows,groups,comparisons


def check_tail_small_primes():
    for p,qs in [(11,[13,17,19]), (13,[17,19,23,29]),
                 (17,[19,23,29]),(19,[23,29,31]),(23,[29,31,37])]:
        assert sum((Q(1,q**3) for q in qs),Q(0)) > Q(1,p**3)
    assert sum((Q(5,6)**(3*k) for k in (1,2,3)),Q(0))>1


def main():
    Tlo,Thi=bounds_on_T()
    assert Q(1)<Tlo<Thi<Q(1002,1000)
    for p,A in HEAD:
        ratio_after=cubic_factor(p,A+1)/cubic_factor(p,A)
        assert ratio_after<Tlo
        ratio_before=cubic_factor(p,A)/cubic_factor(p,A-1)
        assert ratio_before>Thi
    check_tail_small_primes()
    rows,gs,comparisons=tabulate(Tlo,Thi)
    print('CERTIFICATE_OK', 'prime_head_options',len(rows),
          'connected_components',len(gs),'gaps',13,'overlaps',10,
          'total_density',str(sum(g['density'] for g in gs)))
    print('T_bounds_float',format(float(Tlo),'.14f'),format(float(Thi),'.14f'))
    for i,g in enumerate(gs,1):
        print('COMPONENT',i,str(g['low']),str(g['upper_mult']),
              str(g['density']),';'.join(':'.join(x) for x in g['names']))

if __name__=='__main__':
    main()
