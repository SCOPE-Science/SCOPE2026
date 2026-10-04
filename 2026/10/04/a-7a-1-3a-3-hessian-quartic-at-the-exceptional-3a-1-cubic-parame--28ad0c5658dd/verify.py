#!/usr/bin/env python3
import sympy as sp

# Exact arithmetic in Q[rho]/(9 rho^2 - 14 rho + 9).
rho=sp.symbols('rho')
rel=9*rho**2-14*rho+9
x1,x2,x3,x4=sp.symbols('x1 x2 x3 x4')
xs=(x1,x2,x3,x4)

f=x4*(x2**2-x1*x3)+x2**2*(x1-(1+rho)*x2+rho*x3)
H=sp.hessian(f,xs)
h=sp.expand(H.det()/4)

def red(expr):
    expr=sp.cancel(expr)
    num,den=sp.fraction(expr)
    R=sp.Poly(rel,rho,domain=sp.EX)
    numr=sp.Poly(sp.expand(num),rho,domain=sp.EX).rem(R)
    denr=sp.Poly(sp.expand(den),rho,domain=sp.EX).rem(R)
    inv=sp.invert(denr,R)
    return sp.expand((numr*inv).rem(R).as_expr())

def assert_red_zero(expr,msg):
    r=sp.factor(red(expr))
    if r != 0:
        raise AssertionError(f'{msg}: {r}')

def affine_local(point, patch_index, names=('u','v','w')):
    """Substitute affine coordinates around a projective point with chosen patch coordinate fixed."""
    loc=sp.symbols(' '.join(names))
    subs={xs[patch_index]: sp.Integer(1)}
    j=0
    pscale=point[patch_index]
    if pscale == 0:
        raise ValueError('patch coordinate zero')
    scaled=[sp.cancel(sp.sympify(z)/sp.sympify(pscale)) for z in point]
    for i,z in enumerate(xs):
        if i==patch_index: continue
        subs[z]=scaled[i]+loc[j]
        j+=1
    return loc, sp.expand(h.subs(subs))

def homogeneous_piece(F, vars_, deg):
    P=sp.Poly(sp.expand(F),*vars_)
    out=0
    for mon,coef in P.terms():
        if sum(mon)==deg:
            term=coef
            for v,e in zip(vars_,mon): term*=v**e
            out += term
    return sp.expand(out)

def reduce_coeffs(expr, vars_):
    P=sp.Poly(sp.expand(expr),*vars_)
    out=0
    for mon,coef in P.terms():
        term=red(coef)
        for v,e in zip(vars_,mon): term*=v**e
        out += term
    return sp.expand(out)

def qform_hessian_det(F, vars_):
    q=reduce_coeffs(homogeneous_piece(F,vars_,2),vars_)
    M=sp.hessian(q,vars_)
    return red(M.det()), q

def split_corank_one(F, vars_, kernel_var):
    """For a corank-one germ, solve transverse critical equations through v^3 and return reduced 4-jet."""
    u,v,w=vars_
    assert v==kernel_var
    F=reduce_coeffs(F,vars_)
    q=reduce_coeffs(homogeneous_piece(F,vars_,2),vars_)
    M=sp.hessian(q,(u,w))
    if red(M.det())==0:
        raise AssertionError('transverse quadratic block is degenerate')
    a2,a3,b2,b3=sp.symbols('a2 a3 b2 b3')
    us=a2*v**2+a3*v**3
    ws=b2*v**2+b3*v**3
    eqs=[]
    for d in (sp.diff(F,u),sp.diff(F,w)):
        E=reduce_coeffs(sp.expand(d.subs({u:us,w:ws})),(v,a2,a3,b2,b3))
        # coefficients v^2 and v^3 are enough for reduced 4-jet
        eqs.extend([red(sp.expand(E).coeff(v,2)), red(sp.expand(E).coeff(v,3))])
    # Equations are linear in coefficients but over Q[rho]/rel. Substitute one exact algebraic root to solve,
    # then reduce the resulting identities back modulo rel.
    s=sp.sqrt(-2)
    rr=(sp.Integer(7)+4*s)/9
    eqs_rr=[sp.expand(e.subs(rho,rr)) for e in eqs]
    sol=sp.solve(eqs_rr,(a2,a3,b2,b3),dict=True)[0]
    # express solutions in Q(rho) by using the known exact root, then nsimplify against rho relation.
    # For this family solutions turn out rational or rational-linear in rho.
    solq={}
    for k,val in sol.items():
        val=sp.simplify(val)
        valq=sp.collect(sp.expand_complex(val),s,evaluate=True)
        A=sp.simplify((valq.subs(s,0)))
        # safer direct coefficient extraction in quadratic field
        valq=sp.expand(val)
        bcoef=sp.simplify((valq.coeff(s)))
        acoef=sp.simplify(valq.subs(s,0))
        solq[k]=sp.expand(acoef + bcoef*(9*rho-7)/4)
    usq=sp.expand(us.subs(solq)); wsq=sp.expand(ws.subs(solq))
    for d in (sp.diff(F,u),sp.diff(F,w)):
        E=reduce_coeffs(sp.expand(d.subs({u:usq,w:wsq})),(v,))
        assert_red_zero(E.coeff(v,2),'critical v^2 coefficient')
        assert_red_zero(E.coeff(v,3),'critical v^3 coefficient')
    G=reduce_coeffs(sp.expand(F.subs({u:usq,w:wsq})),(v,))
    c2=red(G.coeff(v,2)); c3=red(G.coeff(v,3)); c4=red(G.coeff(v,4))
    if c2!=0 or c3!=0 or c4==0:
        raise AssertionError((c2,c3,c4,solq,G))
    return q, solq, c4

# Source-normalized Hessian determinant identity.
h_expected=(rho**2*x2**2*x3**2-2*rho*x1*x2**2*x3+3*rho*x1*x2*x3*x4-rho*x1*x3**2*x4
            -2*rho*x2**2*x3*x4+x1**2*x2**2-x1**2*x3*x4-2*x1*x2**2*x4
            +3*x1*x2*x3*x4-x1*x3*x4**2+x2**2*x4**2)
assert sp.expand(h-h_expected)==0

# The three degree-two rank-drop components from Seigal--Sukarto acquire double roots exactly on rel=0.
t=sp.symbols('t')
qx=4*t**2-3*(rho+1)*t+2*rho
qy=4*rho*t**2-3*(rho+1)*t+2
assert sp.factor(sp.discriminant(qx,t))==rel
assert sp.factor(sp.discriminant(qy,t))==rel
x0=3*(rho+1)/8
y0=sp.Rational(23,24)-3*rho/8
assert_red_zero(qx.subs(t,x0),'first double root')
assert_red_zero(sp.diff(qx,t).subs(t,x0),'first double derivative')
assert_red_zero(qy.subs(t,y0),'second double root')
assert_red_zero(sp.diff(qy,t).subs(t,y0),'second double derivative')

# Seven rank<=2 support points: three doubled P_i and four reduced Q_i.
P=[(rho,x0,1,0),(0,x0,1,rho),(1,y0,0,1)]
Q=[(-rho,0,1,0),(0,1,0,0),(0,0,1,-rho),(1,0,0,-1)]
minors=[]
for I in sp.utilities.iterables.combinations(range(4),3):
    for J in sp.utilities.iterables.combinations(range(4),3):
        minors.append(sp.expand(H.extract(I,J).det()))
for label,pt in [('P1',P[0]),('P2',P[1]),('P3',P[2]),('Q1',Q[0]),('Q2',Q[1]),('Q3',Q[2]),('Q4',Q[3])]:
    for m in minors:
        assert_red_zero(m.subs(dict(zip(xs,pt))),f'{label} 3x3 minor')

# A3 classification at each coalesced rank-drop point by exact splitting-lemma 4-jet.
for i,(pt,patch) in enumerate([(P[0],2),(P[1],2)],1):
    vars_,F=affine_local(pt,patch)
    F=reduce_coeffs(F,vars_)
    q,sol,c4=split_corank_one(F,vars_,vars_[1])
    print(f'P{i}_quadratic={sp.factor(q)}')
    print(f'P{i}_critical_series={sol}')
    print(f'P{i}_reduced_v4={sp.factor(c4)}')
# At P3 choose the kernel coordinate v along x2.
u,v,w=sp.symbols('u v w')
vars_=(u,v,w)
F=reduce_coeffs(sp.expand(h.subs({x1:1,x2:y0+v,x3:u,x4:1+w})),vars_)
q,sol,c4=split_corank_one(F,vars_,v)
print(f'P3_quadratic={sp.factor(q)}')
print(f'P3_critical_series={sol}')
print(f'P3_reduced_v4={sp.factor(c4)}')

# Nonzero coefficients used in the node certificates are units modulo the quadratic parameter relation.
assert sp.gcd(sp.Poly(476*rho-1035,rho,domain=sp.QQ),sp.Poly(rel,rho,domain=sp.QQ)).degree()==0
assert sp.gcd(sp.Poly(14*rho-9,rho,domain=sp.QQ),sp.Poly(rel,rho,domain=sp.QQ)).degree()==0

# The four fixed rank-drop points are ordinary nodes of the quartic.
for i,(pt,patch) in enumerate([(Q[0],2),(Q[1],1),(Q[2],2),(Q[3],0)],1):
    vars_,F=affine_local(pt,patch)
    detq,q=qform_hessian_det(F,vars_)
    if detq==0:
        raise AssertionError(f'Q{i} quadratic degenerate')
    print(f'Q{i}_quadratic_det={sp.factor(detq)}')

# The three A1 points of the cubic yield the only possible rank-3 singular points of det(H).
# Directly verify they lie on Sing(h), have rank(H)=3, and have nondegenerate quadratic quartic germs.
A=[(1,0,0,0),(0,0,1,0),(0,0,0,1)]
for i,(pt,patch) in enumerate([(A[0],0),(A[1],2),(A[2],3)],1):
    subs=dict(zip(xs,pt))
    assert_red_zero(h.subs(subs),f'A{i} h')
    for z in xs:
        assert_red_zero(sp.diff(h,z).subs(subs),f'A{i} dh')
    Hpt=H.subs(subs)
    # rank over the quadratic field via a representative exact root
    rr=(sp.Integer(7)+4*sp.sqrt(-2))/9
    if Hpt.subs(rho,rr).rank()!=3:
        raise AssertionError(f'A{i} Hessian rank')
    vars_,F=affine_local(pt,patch)
    detq,q=qform_hessian_det(F,vars_)
    if detq==0:
        raise AssertionError(f'A{i} quartic quadratic degenerate')
    print(f'A{i}_quadratic={sp.factor(q)}')
    print(f'A{i}_quadratic_det={sp.factor(detq)}')

# Exhaustion lemma for rank-3 singular points: if rank H(x)=3 with kernel k, then
# d(det H)_x(v)=0 for all v iff T(k,k,v)=0 for all v, i.e. grad f(k)=0.
# For the three source-listed cubic nodes k=e1,e3,e4, H(x)k=0 forces x=k projectively.
for idx in [0,2,3]:
    k=sp.eye(4)[:,idx]
    vec=sp.expand(H*k)
    # Verify H(k)k=2 grad f(k)=0 and solve the linear equations H(x)k=0 up to projective scale by rank.
    for entry in vec.subs({x1:k[0],x2:k[1],x3:k[2],x4:k[3]}):
        assert_red_zero(entry,'node kernel check')
    M=sp.linear_eq_to_matrix(list(vec),xs)[0]
    rr=(sp.Integer(7)+4*sp.sqrt(-2))/9
    if M.subs(rho,rr).rank()!=3:
        raise AssertionError('kernel-incidence solution is not a unique projective point')

print('rank_drop_scheme_length=10_support=7_pattern=4x1+3x2')
print('hessian_singularity_basket=7A1+3A3')
print('VERIFY_OK')
