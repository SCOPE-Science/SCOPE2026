"""Exact verification of the two-pinned-leader classification on a one-edge-defective biclique.

Requires Python 3.10+ and SymPy 1.10+. Execute `python verify.py`.
"""
import itertools
import sympy as s

n = s.symbols('n', integer=True, positive=True)
base = {'a':s.Integer(1), 'A':n-1, 'b':s.Integer(1), 'B':n-1}
deg = {'a':n-1,'A':n,'b':n-1,'B':n}
TYPES = ('ab','aA','aB','Ab','bB','AB','AA','BB')
FORMULAS = {
'ab': 2*(n-1)*(3*n-2)/(n*(2*n-1)),
'aA': (6*n**3-16*n**2+19*n-10)/(n*(2*n**2-3*n+2)),
'aB': (6*n**3-18*n**2+23*n-10)/(2*n*(n-1)**2),
'Ab': (6*n**3-18*n**2+23*n-10)/(2*n*(n-1)**2),
'bB': (6*n**3-16*n**2+19*n-10)/(n*(2*n**2-3*n+2)),
'AB': 2*(3*n**3-11*n**2+17*n-10)/(n*(2*n**2-5*n+4)),
'AA': (3*n**3-10*n**2+13*n-5)/(n*(n-1)**2),
'BB': (3*n**3-10*n**2+13*n-5)/(n*(n-1)**2),
}

def adjacent(g,h):
    return (g in 'aA') != (h in 'aA') and {g,h}!={'a','b'}


def symbolic_orbit(t):
    """Block-constant reduction; valid directly whenever nonempty group counts positive."""
    cnt={g:base[g]-t.count(g) for g in 'aAbB'}
    groups=[g for g in 'aAbB' if cnt[g]!=0]
    M=s.Matrix([[deg[g]*int(g==h)-int(adjacent(g,h))*cnt[h] for h in groups] for g in groups])
    return s.factor(s.trace(M.inv())+sum((cnt[g]-1)/deg[g] for g in groups))

for typ in TYPES:
    f=symbolic_orbit(typ)
    assert s.cancel(f-FORMULAS[typ])==0, (typ,f,FORMULAS[typ])

q=4*n**2-7*n+2
checks={
'aA':q/(n*(2*n-1)*(2*n**2-3*n+2)),
'aB':(2*n**3+4*n**2-7*n+2)/(2*n*(n-1)**2*(2*n-1)),
'AB':2*q/(n*(2*n-1)*(2*n**2-5*n+4)),
}
for key,expr in checks.items():
    assert s.cancel(FORMULAS[key]-FORMULAS['ab']-expr)==0
assert s.cancel(FORMULAS['ab']-FORMULAS['AA']-(n**3-6*n**2+5*n-1)/(n*(n-1)**2*(2*n-1)))==0
assert FORMULAS['AA']==FORMULAS['BB']
assert FORMULAS['aA']==FORMULAS['bB']
assert FORMULAS['aB']==FORMULAS['Ab']
f=n**3-6*n**2+5*n-1
assert [f.subs(n,i) for i in (3,4,5,6)]==[-13,-13,-1,29]
assert s.factor(f.subs(n,n+1)-f)==3*n*(n-3)
# Positivity proof: q = 4(n-3)^2+17(n-3)+17; P=2n^3+4n^2-7n+2 is positive at n>=3 and increasing.
x=s.symbols('x',integer=True,nonnegative=True)
assert s.expand(q.subs(n,x+3))==4*x*x+17*x+17
assert all(co>0 for co in s.Poly((2*n**3+4*n**2-7*n+2).subs(n,x+3),x).all_coeffs())


def direct_cost(N, pair):
    L=s.zeros(2*N)
    for i in range(N):
        for j in range(N,2*N):
            if (i,j)==(0,N):continue
            L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    followers=[i for i in range(2*N) if i not in pair]
    F=L.extract(followers,followers)
    return s.trace(F.inv())

def orbit(i,N):
    if i==0:return 'a'
    if i<N:return 'A'
    if i==N:return 'b'
    return 'B'

cnt=0
for N in range(3,8):
    for u,v in itertools.combinations(range(2*N),2):
        t=''.join(sorted((orbit(u,N),orbit(v,N)), key='aAbB'.index))
        assert t in TYPES
        value=direct_cost(N,(u,v))
        assert value==FORMULAS[t].subs(n,N),(N,u,v,t,value,FORMULAS[t].subs(n,N))
        cnt+=1
    # All tie cases and minimizing orbits, including N=3 empty healthy-class edge case.
    values={t:FORMULAS[t].subs(n,N) for t in TYPES}
    winner=[t for t in TYPES if values[t]==min(values.values())]
    assert winner==(['ab'] if N<=5 else ['AA','BB']),(N,winner)
print('VERIFY_OK 8 symbolic orbit identities, 4 exact comparison identities,',cnt,'direct rational grounded inverses, all minimum classes n=3..7')
