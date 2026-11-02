"""Finite independent checks of exact critical-partition M-map formulas.

Requires sympy and mpmath. The analytical proof of the infinite statements
is given in RESULT.md; these finite tests are not an independent proof.
"""
import sympy as sp
import mpmath as mp

z, ell = sp.symbols('z ell')
mats = {
    'low': sp.Matrix([[1,1,1,1],[0,1,1,1],[0,1,1,1],[1,1,1,1]]),
    'middle': sp.Matrix([[1,1,1,1],[0,0,1,1],[0,0,1,1],[1,1,1,1]]),
    'high': sp.Matrix([[1,1,1,1],[0,0,0,1],[0,0,0,1],[1,1,1,1]]),
}
polys = {
    'low': ell**2*(ell**2-4*ell+2),
    'middle': ell**3*(ell-3),
    'high': ell**2*(ell**2-2*ell-2),
}
generating = {
    'low': (4*z-2*z*z)/(1-4*z+2*z*z),
    'middle': 4*z/(1-3*z),
    'high': (4*z+2*z*z)/(1-2*z-2*z*z),
}
u=sp.ones(4,1)
for name,A in mats.items():
    assert sp.expand(A.charpoly(ell).as_expr()-polys[name]) == 0
    resolved = sp.factor(z*(u.T*(sp.eye(4)-z*A).inv()*u)[0])
    assert sp.cancel(resolved-generating[name]) == 0

p=sp.symbols('p')
v=(4*p-1)/(4*p*p)
assert sp.factor((v-p)*4*p*p) == -(4*p**3-4*p+1)
assert sp.factor((v-sp.Rational(1,2))*4*p*p) == -(2*p*p-4*p+1)
assert sp.factor((v-(1-p))*4*p*p) == (4*p**3-4*p*p+4*p-1)

mp.mp.dps=70
roots = {
    'low': mp.findroot(lambda t:4*t**3-4*t+1, (mp.mpf('.26'),mp.mpf('.28'))),
    'middle': 1-1/mp.sqrt(2),
    'high': mp.findroot(lambda t:4*t**3-4*t*t+4*t-1,(mp.mpf('.31'),mp.mpf('.33'))),
}
def uniq(seq):
    out=[]
    for value in sorted(seq):
        if not out or value-out[-1]>mp.mpf('1e-35'):
            out.append(value)
    return out

def image(x, a):
    t=x if x<=mp.mpf('.5') else 1-x
    return t/a*(2-t/a)

independent_checks=0
for name,a in roots.items():
    assert mp.mpf('.25')<a<mp.mpf('.5')
    verts=[mp.mpf(0),a,mp.mpf('.5'),1-a,mp.mpf(1)]
    actual=mp.matrix(4)
    for i in range(4):
        bottom=min(image(verts[i],a),image(verts[i+1],a))
        top=max(image(verts[i],a),image(verts[i+1],a))
        for j in range(4):
            actual[i,j]=int(bottom<=verts[j]+mp.mpf('1e-50') and top>=verts[j+1]-mp.mpf('1e-50'))
    expected=mats[name]
    for i in range(4):
        for j in range(4):
            assert int(actual[i,j]) == int(expected[i,j])
            independent_checks+=1
    level=[a,mp.mpf('.5'),1-a]
    all_turns=[]
    for n in range(1,8):
        all_turns=uniq(all_turns+level)
        predicted=int(sum(mats[name]**(n-1)))
        assert len(all_turns)+1 == predicted, (name,n,len(all_turns)+1,predicted)
        independent_checks+=1
        next_level=[]
        for y in level:
            d=mp.sqrt(max(mp.mpf(0),1-y))
            for left in [a*(1-d),a*(1+d)]:
                if 0<=left<=mp.mpf('.5')+mp.mpf('1e-40'):
                    next_level.extend((left,1-left))
        level=uniq(next_level)

# The two endpoint cases are full-branch: four arms at p=1/4,
# and the standard two-arm quadratic map at p=1/2.
assert mp.almosteq(image(mp.mpf('.5'),mp.mpf('.25')),mp.mpf(0))
assert mp.almosteq(image(mp.mpf('.5'),mp.mpf('.5')),mp.mpf(1))
print('PASS: 3 characteristic polynomials, 3 rational generating functions, 3 algebraic branch identities,')
print(f'       {independent_checks} Markov-cell and independent inverse-image lap checks; endpoint branch values.')
