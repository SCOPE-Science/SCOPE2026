#!/usr/bin/env python3
"""Finite binary-matrix certificate for the incidence of smooth filling quartic pencils."""
from collections import Counter
I=(1<<0)|(1<<4)|(1<<8)

def mul(a,b):
    r=0
    for i in range(3):
        for j in range(3):
            z=0
            for k in range(3): z ^= ((a>>(3*i+k))&1)&((b>>(3*k+j))&1)
            r|=z<<(3*i+j)
    return r

def det(a):
    s=0
    for i,j,k in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)):
        s^=((a>>i)&1)&((a>>(3+j))&1)&((a>>(6+k))&1)
    return s

def rep(a):return min(a,a^I)

def good(a):return det(a)==1 and det(a^I)==1

def powm(a,n):
    v=I
    while n:
        if n&1:v=mul(v,a)
        a=mul(a,a);n>>=1
    return v

def fmt(a):return ''.join(str((a>>i)&1) for i in range(9))

def run():
    GL=[a for a in range(512) if det(a)]
    classes=sorted({rep(a) for a in range(512) if good(a)})
    assert len(GL)==168 and len(classes)==24
    H=set()
    for a in GL:
        if powm(a,7)==I and a!=I:
            h=frozenset(powm(a,k) for k in range(1,7))
            assert len(h)==6
            H.add(h)
    assert len(H)==8
    subgroup_to_forms={h:frozenset(rep(a) for a in h) for h in H}
    assert all(len(c)==3 for c in subgroup_to_forms.values())
    assert set().union(*map(set,subgroup_to_forms.values()))==set(classes)
    assert sum(len(c) for c in subgroup_to_forms.values())==24
    # This exhaustively checks the nontrivial, cross-subfield implication.
    pencils=set()
    for i,a in enumerate(classes):
        for b in classes[i+1:]:
            if good(a^b):
                pencils.add(frozenset((a,b,rep(a^b))))
    assert len(pencils)==8 and pencils==set(subgroup_to_forms.values())
    assert sum(len(p) for p in pencils)==24
    assert len(set().union(*map(set,pencils)))==24
    # Conjugation action, using an actual finite group.
    inv={}
    for b in GL:
        for c in GL:
            if mul(b,c)==mul(c,b)==I:
                inv[b]=c;break
    assert len(inv)==168
    def conjugate_form(b,a):return rep(mul(mul(b,a),inv[b]))
    orbit={frozenset(conjugate_form(b,a) for a in next(iter(pencils))) for b in GL}
    assert orbit==pencils
    assert sum(1 for b in GL if frozenset(conjugate_form(b,a) for a in next(iter(pencils)))==next(iter(pencils)))==21
    A=next(iter(classes))
    own=[p for p in pencils if A in p][0]
    stabilizer=[b for b in GL if conjugate_form(b,A)==A]
    assert len(stabilizer)==7
    # Centralizer orbit of the 21 outsider quartics has three seven-element orbits.
    others=set(classes)-set(own)
    rep_orbits=[]
    while others:
        v=min(others)
        o={conjugate_form(b,v) for b in stabilizer}
        assert len(o)==7 and all(not good(A^e) for e in o)
        rep_orbits.append((v,det(A^v),det((A^v)^I)))
        others-=o
    assert len(rep_orbits)==3
    print('group',len(GL),'smooth_filling_quartics',len(classes),'Singer_subgroups',len(H),'pencils',len(pencils))
    print('stabilizer_pencil',21,'stabilizer_curve',7,'other_curve_orbits',rep_orbits)
    print('representative_pencil_bits',*(fmt(a) for a in sorted(next(iter(pencils)))))
    print('all_pencils',*[tuple(sorted(p)) for p in sorted(pencils,key=lambda x:min(x))],sep='\n')
    print('PASS')
if __name__=='__main__':run()
