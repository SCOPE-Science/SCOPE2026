"""Exact reproducible checks for a two-leader weighted depth-two spider theorem.

Requires Python 3 and SymPy. No network access.
"""
from itertools import combinations
from sympy import symbols, Rational, Matrix, factor, simplify, zeros

t = symbols('t', positive=True)
k = symbols('k', integer=True, positive=True)

COSTS = {
    'center_inner': k * (t+2) - 2,
    'center_leaf': k * (t+2) - (t+1) - 1/(t+1),
    'inner_leaf_same': k * (t+4) - t-3,
    'inner_inner_different': k * (t+3) - Rational(11, 2),
    'inner_leaf_different': (k*(t*t+6*t+6) - (t*t+7*t+11))/(t+2),
    'leaf_leaf_different': (k*(4*t*t+10*t+6) - (5*t*t+14*t+11))/(2*(t+1)),
}

def graph(m, resistance):
    vertices = ['c'] + [('u',i) for i in range(m)] + [('v',i) for i in range(m)]
    idx={v:i for i,v in enumerate(vertices)}
    lap=zeros(len(vertices))
    for i in range(m):
        for x,y,conductance in [('c',('u',i),1),(('u',i),('v',i),1/resistance)]:
            a,b=idx[x],idx[y]
            lap[a,a]+=conductance; lap[b,b]+=conductance
            lap[a,b]-=conductance; lap[b,a]-=conductance
    return vertices,lap

def orbit(a,b):
    if a=='c' or b=='c': return 'center_inner' if (a if b=='c' else b)[0]=='u' else 'center_leaf'
    a,b=sorted([a,b], key=lambda v: 0 if v[0]=='u' else 1)
    if a[0]=='u' and b[0]=='u': return 'inner_inner_different'
    if a[0]=='v' and b[0]=='v': return 'leaf_leaf_different'
    return 'inner_leaf_same' if a[1]==b[1] else 'inner_leaf_different'

def inverse_trace(lap,leaders):
    remaining=[i for i in range(lap.rows) if i not in leaders]
    return lap.extract(remaining,remaining).inv().trace()

count=0
for m in [3,4,5,6]:
    for r in [Rational(1,7),Rational(1,2),Rational(1),Rational(3,2),Rational(7,2)]:
        vs,lap=graph(m,r)
        groups={}
        for ia,ib in combinations(range(len(vs)),2):
            label=orbit(vs[ia],vs[ib]); value=inverse_trace(lap,[ia,ib]); expected=COSTS[label].subs({k:m,t:r})
            assert simplify(value-expected)==0, (m,r,label,value,expected)
            groups.setdefault(label,value)
            count+=1
        assert len(groups)==6
        best=min(groups.values())
        winners={z for z,val in groups.items() if val==best}
        if m>=4: wanted={'center_leaf'}
        elif r<1: wanted={'inner_inner_different'}
        elif r==1: wanted={'center_leaf','inner_inner_different'}
        else: wanted={'center_leaf'}
        assert winners==wanted,(m,r,winners,wanted)

# Symbolic comparisons: for all positive t and k>=4, the k=4 difference
# from center_leaf has a strictly positive numerator and nonnegative slope in k.
cv=COSTS['center_leaf']
checks={
'center_inner': t**2/(t+1),
'inner_leaf_same': (6*t+7)/(t+1),
'inner_inner_different': (2*t*t+t+1)/(2*(t+1)),
'inner_leaf_different': (4*t*t+4*t+1)/((t+1)*(t+2)),
'leaf_leaf_different': (5*t+1)/2,
}
for label,p in checks.items():
    assert simplify((COSTS[label]-cv).subs(k,4)-p)==0
    slope=simplify((COSTS[label]-cv).subs(k,5)-(COSTS[label]-cv).subs(k,4))
    assert slope.subs(t,Rational(1,3))>=0
    numerator,denominator=slope.as_numer_denom()
    # all slopes are nonnegative rational expressions on the positive ray.
    assert slope in [0,2,1,2*(t+1)/(t+2),t+1] or simplify(slope-2*(t+1)/(t+2))==0,(label,slope)

uu=COSTS['inner_inner_different']
assert simplify((uu-cv).subs(k,3) - (t-1)*(2*t+1)/(2*(t+1)))==0
assert simplify((COSTS['inner_leaf_different']-uu).subs(k,3) - t*(3-2*t)/(2*(t+2)))==0
assert simplify((COSTS['leaf_leaf_different']-uu).subs(k,3) - t*(t+3)/(2*(t+1)))==0
assert simplify((COSTS['inner_leaf_same']-uu).subs(k,3) - (11-2*t)/2)==0
print(f'VERIFY_OK: {count} exact grounded-Laplacian inversions; complete orbit formulas; two exact parameter regimes; symbolic difference certificates.')
