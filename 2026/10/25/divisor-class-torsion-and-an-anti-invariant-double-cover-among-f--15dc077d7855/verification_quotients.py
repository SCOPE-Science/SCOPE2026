"""Reproduce finite matrix calculations for four dimension-four quotient varieties.

Matrices are the integral generators of cases 45, 105, 65, and 66 in
Burek--Cynk, arXiv:2610.16962v1, Appendix A. Requires Python >=3.9.
This program verifies finite group claims; geometric deductions use
standard class-group and quasi-etale quotient theorems separately.
"""
from collections import Counter, deque
from fractions import Fraction


def mat(*rows):
    return tuple(int(v) for row in rows for v in row)


def multiply(a, b):
    return tuple(sum(a[4*r+k]*b[4*k+c] for k in range(4))
                 for r in range(4) for c in range(4))


def inverse(a):
    rows = [[Fraction(a[4*r+c]) for c in range(4)] +
            [Fraction(int(r == c)) for c in range(4)] for r in range(4)]
    for j in range(4):
        pivot = next(i for i in range(j, 4) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        z = rows[j][j]
        rows[j] = [w / z for w in rows[j]]
        for k in range(4):
            if k != j:
                z = rows[k][j]
                rows[k] = [rows[k][c]-z*rows[j][c] for c in range(8)]
    out = [v for row in rows for v in row[4:]]
    assert all(v.denominator == 1 for v in out)
    return tuple(int(v) for v in out)


I = mat([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])
A=mat([0,0,0,-1],[0,1,0,2],[0,0,1,-1],[1,0,0,-1])
B=mat([-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1])
C=mat([-1,-1,0,-1],[1,0,-1,1],[-1,0,1,0],[-1,0,0,0])
D=mat([1,1,0,0],[0,-1,0,0],[0,1,1,0],[0,0,0,-1])
E=mat([-1,0,0,0],[0,-1,0,0],[0,1,1,0],[0,1,0,1])
F=mat([1,0,0,-1],[0,1,0,2],[0,0,1,-1],[0,-1,0,-1])
G=mat([0,-1,-1,-1],[0,1,2,0],[0,0,-1,0],[-1,-1,-1,0])
H=mat([0,1,1,1],[0,-1,0,-2],[-1,0,0,1],[0,1,0,1])
G45=[
 mat([1,0,0,0],[-1,-1,0,0],[0,0,-1,-1],[0,0,0,1]), B,
 mat([-1,-1,0,0],[1,0,0,0],[0,0,-1,-1],[0,0,1,0]),
 mat([1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,-1,-1])]
G105=[
 mat([1,-1,0,0],[0,-1,0,0],[0,0,0,1],[0,0,1,0]),
 mat([-1,0,0,0],[0,-1,0,0],[0,0,0,1],[0,0,-1,0]),
 mat([1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]),
 mat([0,-1,0,0],[1,-1,0,0],[0,0,1,0],[0,0,0,1])]
SETS={45:G45,105:G105,65:[A,B,C,D,E,G,H],66:[A,B,C,D,E,F,G,H]}


def closure(gens, cap=10000):
    discovered={I}; queue=deque([I])
    while queue:
        x=queue.popleft()
        for y in gens:
            z=multiply(x,y)
            if z not in discovered:
                discovered.add(z); queue.append(z)
                if len(discovered)>cap:
                    raise RuntimeError('group exceeds bound')
    return discovered


def derived_group(gens):
    invs={g:inverse(g) for g in gens}
    comms={multiply(multiply(multiply(a,b),invs[a]),invs[b])
           for a in gens for b in gens}
    normal=set(comms); queue=deque(comms)
    while queue:
        a=queue.popleft()
        for b in gens:
            z=multiply(multiply(b,a),invs[b])
            if z not in normal:
                normal.add(z); queue.append(z)
    return closure(normal)


def quotient_profile(group, derived):
    remaining=set(group); histogram=Counter()
    while remaining:
        representative=next(iter(remaining))
        coset={multiply(representative,h) for h in derived}
        assert coset <= remaining
        remaining-=coset
        x=representative; order=1
        while x not in derived:
            x=multiply(x,representative); order+=1
            assert order <= len(group)
        histogram[order]+=1
    return dict(sorted(histogram.items()))


def verify():
    results={}
    expected={45:(36,9,{1:1,2:3}),105:(24,6,{1:1,2:3}),
              65:(288,32,{1:1,3:8}),66:(576,288,{1:1,2:1})}
    for case,gens in SETS.items():
        for g in gens: assert multiply(g,inverse(g))==I
        group=closure(gens); comm=derived_group(gens)
        assert comm<=group
        assert all(multiply(a,multiply(b,inverse(a))) in comm
                   for a in gens for b in comm)
        hist=quotient_profile(group,comm)
        assert (len(group),len(comm),hist)==expected[case]
        results[case]=(group,comm,hist)
        print(f'CASE {case}: |G|={len(group)} |G_derived|={len(comm)} '
              f'abelian_quotient_orders={hist}')
    g65,comm65,_=results[65]; g66,comm66,_=results[66]
    assert g65<g66 and len(g66)==2*len(g65)
    assert F not in g65 and multiply(F,F) in g65
    fi=inverse(F)
    # Conjugation by the added generator is negation on G65^ab.
    for g in SETS[65]:
        f_g_fi=multiply(multiply(F,g),fi)
        assert f_g_fi in g65
        assert multiply(f_g_fi,g) in comm65
    print('COVER: G65 normal index 2 in G66; added generator acts as -1 on G65_ab')
    print('VERIFY_OK four_group_abelianizations_and_cover_involution')


if __name__=='__main__':
    verify()
