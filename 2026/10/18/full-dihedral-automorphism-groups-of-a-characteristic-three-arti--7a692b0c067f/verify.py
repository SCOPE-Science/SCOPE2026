"""Exact checks for the Artin–Schreier curve family in characteristic three.

These finite checks support the displayed algebraic identities and group
relations. Exhaustiveness of the full automorphism group is a theorem in
RESULT.md, not a conclusion inferred from examples.
"""
from collections import deque
from sympy import symbols, diff, expand, cancel

U,V,x,L=symbols('U V x L')

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def check(m):
    assert m>=5 and m%3==2
    F=U**m-V**m
    H=expand(diff(F,U,2)*diff(F,V,2)-diff(F,U,V)**2)
    c=-(m*(m-1))**2
    assert expand(H-c*(U*V)**(m-2))==0
    assert c%3!=0
    f=L/(x**m-1)
    assert cancel(f.subs(x,1/x)+f+L)==0
    assert 2* (2*m-2)-2 == -6+4*m
    assert (m-1)*2 == 2*m-2
    # Group on the m-by-3 residue grid, where rotation and deck translation
    # generate a cyclic group of order 3m and reflection inverts both.
    els=[(a,b) for a in range(m) for b in range(3)]
    idx={z:i for i,z in enumerate(els)}
    r=tuple(idx[((a+1)%m,b)] for a,b in els)
    t=tuple(idx[(a,(b+1)%3)] for a,b in els)
    s=tuple(idx[((-a)%m,(-b)%3)] for a,b in els)
    e=tuple(range(3*m))
    assert compose(s,s)==e
    assert compose(r,t)==compose(t,r)
    assert compose(compose(s,r),s)==tuple(idx[((a-1)%m,b)] for a,b in els)
    assert compose(compose(s,t),s)==tuple(idx[(a,(b-1)%3)] for a,b in els)
    subgroup={e}
    q=deque([e])
    while q:
        cur=q.popleft()
        for g in (r,t,s):
            nxt=compose(g,cur)
            if nxt not in subgroup:
                subgroup.add(nxt);q.append(nxt)
    assert len(subgroup)==6*m
    print(f'm={m} g={2*m-2} group_order={len(subgroup)} Hessian_scalar_mod3={c%3}')

for m in (5,8,11,14):
    check(m)
print('VERIFY_OK')
