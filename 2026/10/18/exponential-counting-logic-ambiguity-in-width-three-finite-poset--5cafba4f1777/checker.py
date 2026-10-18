"""Finite checks for cyclic three-chain posets.

Usage: python checker.py
"""
from itertools import product, permutations
from collections import Counter


def poset(signs):
    t=len(signs)
    h=2*t+1
    n=3*h
    E=[[False]*n for _ in range(n)]
    for i in range(h-1):
        for x in range(3):
            E[3*i+x][3*(i+1)+x]=True
    for j,s in enumerate(signs):
        for x in range(3):
            E[3*(2*j)+x][3*(2*j+2)+(x+s)%3]=True
    for k in range(n):
        for i in range(n):
            if E[i][k]:
                for j in range(n):
                    if E[k][j]: E[i][j]=True
    return E


def profiles(E):
    n=len(E)
    color=[0]*n
    series=[]
    for it in range(n+2):
        sig=[]
        for a in range(n):
            down=Counter(color[b] for b in range(n) if E[b][a])
            up=Counter(color[b] for b in range(n) if E[a][b])
            sig.append((color[a],tuple(sorted(down.items())),tuple(sorted(up.items()))))
        order={s:i for i,s in enumerate(sorted(set(sig)))}
        nxt=[order[x] for x in sig]
        series.append(tuple(nxt))
        if nxt==color: break
        color=nxt
    return tuple(color),series


def two_var_inv(E):
    n=len(E); h=n//3
    mat=[]
    for a in range(h):
        row=[]
        for b in range(h):
            row.append(sum(E[3*a][3*b+k] for k in range(3)))
        mat.append(tuple(row))
    return tuple(mat)


def isomorphic(E,F):
    # Each level is fixed by the strictly increasing number of predecessors.
    n=len(E); h=n//3
    for sigma in permutations(range(3)):
        f=[3*i+sigma[x] for i in range(h) for x in range(3)]
        if all(E[a][b]==F[f[a]][f[b]] for a in range(n) for b in range(n)):
            return True
    return False


def check():
    cases=0
    for t in range(1,8):
        family={sgn:poset(sgn) for sgn in product((-1,1),repeat=t)}
        reference=next(iter(family.values()))
        inv=two_var_inv(reference)
        expected_classes=2**(t-1)
        for sgn,E in family.items():
            n=len(E)
            assert all(not E[a][a] for a in range(n))
            assert all(not (E[a][b] and E[b][a]) for a in range(n) for b in range(n))
            assert two_var_inv(E)==inv
            pre=[sum(E[a][b] for a in range(n)) for b in range(n)]
            assert all(pre[3*i]==pre[3*i+j] for i in range(2*t+1) for j in range(3))
            assert all(pre[3*i]<pre[3*(i+1)] for i in range(2*t))
            colors,sequence=profiles(E)
            assert len(set(colors))==2*t+1
            assert all(colors[3*i+j]==colors[3*i] for i in range(2*t+1) for j in range(3))
            # All points lie in the three chains z=0,1,2, so width <=3.
            assert all(E[3*i+x][3*j+x] for x in range(3) for i in range(2*t+1) for j in range(i+1,2*t+1))
            for a in range(2*t+1):
                for b in range(a+1,2*t+1):
                    blocks=sum(1 for j in range(t) if a<=2*j and 2*j+2<=b)
                    assert inv[a][b]==(1 if blocks==0 else 2 if blocks==1 else 3), (sgn,a,b)
            cases+=1
        orbit_reps={min(sgn,tuple(-x for x in sgn)) for sgn in family}
        assert len(orbit_reps)==expected_classes
        if t<=4:
            ss=list(family)
            for i,p in enumerate(ss):
                for q in ss[i+1:]:
                    assert isomorphic(family[p],family[q])==(q==p or q==tuple(-x for x in p)), (t,p,q)
        print(f't={t}: vertices={3*(2*t+1)}, sign choices={2**t}, nonisomorphic classes={len(orbit_reps)}, common stable colour classes={2*t+1}, checked')
    print(f'PASS: {cases} finite constructions; exhaustive layer-preserving pairwise isomorphism for t<=4')

if __name__=='__main__':
    check()
