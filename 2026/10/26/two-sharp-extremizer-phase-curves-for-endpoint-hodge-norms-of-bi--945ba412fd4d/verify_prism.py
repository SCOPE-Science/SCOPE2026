"""Exact rational and polynomial verification for bipartite-prism Hodge norms.

Requires Python 3 and sympy. No floating-point decisions are used.
"""
import sympy as s

p, q, u, v = s.symbols('p q u v', integer=True, positive=True)
N = p + q
H0 = 3 - 2/p - 2/q + 2/(p*q) + (2*p+q)/((q+2)*(N+2)) + (p+2*q)/((p+2)*(N+2))
delta = 1/(q+2) - (N+4)/((p+2)*(q+2)*(N+2)) - (p-1)/(p*q)
H1 = H0 + (q-1)*delta
QA = 1 + 2*q*(2*p+q)/((q+2)*(N+2))
QB = 1 + 2*p*(p+2*q)/((p+2)*(N+2))
RH = ((N-1)/(p*q) + 1/(p+2) + 1/(q+2) - (N+4)/((p+2)*(q+2)*(N+2)))/2
RA = (2*p+3*q+4)/((q+2)*(N+2))
RB = (3*p+2*q+4)/((p+2)*(N+2))
CA = s.factor(1+QA-2*RA)
CB = s.factor(1+QB-2*RB)
CH0 = 1+H0-2*RH
CH1 = 1+H1-2*RH
assert s.simplify(CA-2*q*(3*p+2*q+1)/((q+2)*(N+2))) == 0
assert s.simplify(CB-2*p*(2*p+3*q+1)/((p+2)*(N+2))) == 0
assert s.simplify(QB-QA-2*(q-p)*(p*q-2*N)/((p+2)*(q+2)*(N+2))) == 0
assert s.simplify(CB-CA-2*(q-p)*(p*q-4*N-2)/((p+2)*(q+2)*(N+2))) == 0


def certify_nonnegative(expr, replacements, variables):
    """Prove a rational expression nonnegative on a nonnegative orthant.

    After cancellation, require numerator and denominator coefficientwise
    nonnegative, with strictly positive denominator constant term.
    """
    r = s.cancel(expr.subs(replacements, simultaneous=True))
    num, den = s.fraction(r)
    A, B = s.Poly(num, *variables), s.Poly(den, *variables)
    assert all(c >= 0 for c in A.coeffs()), (expr, replacements, A)
    assert all(c >= 0 for c in B.coeffs()), (expr, replacements, B)
    assert B.eval({x:0 for x in variables}) > 0
    return A.total_degree(), len(A.terms())

# For 2 <= p <= q: only one of four horizontal current types can
# exceed the first-layer cut flow. The others have directly positive
# differences after clearing positive denominators.
gA01=(q-1)/(p*q)
gB01=1/(p+2)-(N+4)/((p+2)*(q+2)*(N+2))
certify_nonnegative(gA01-gB01, {p:u+2, q:u+v+2}, (u,v))
gA11=(N-1)/(p*q)
gB11=1/(q+2)+1/(p+2)-(N+4)/((p+2)*(q+2)*(N+2))
certify_nonnegative(gA11-gB11, {p:u+2, q:u+v+2}, (u,v))
certify_nonnegative(1/(p*q)-(N+4)/((p+2)*(q+2)*(N+2)),
                        {p:u+2, q:u+v+2}, (u,v))

# Horizontal columns never strictly maximize the cut norm.
for pv in (2,3):
    for H in (H0,H1):
        certify_nonnegative(QA-H, {p:s.Integer(pv), q:pv+v}, (v,))
for H in (H0,H1):
    certify_nonnegative(QB-H, {p:u+4, q:u+v+4}, (u,v))

# Horizontal columns never maximize the cycle norm except at (3,3).
for pv, low in ((2,2),(3,4),(4,4)):
    for H in (CH0,CH1):
        certify_nonnegative(CA-H, {p:s.Integer(pv), q:low+v}, (v,))

# The finite branch where 5 <= p <= 8 and pq <= 4(p+q)+2.
finite_count = 0
for pv, last in ((5,22),(6,13),(7,10),(8,8)):
    for qv in range(pv,last+1):
        for H in (CH0, CH1):
            assert s.cancel((CA-H).subs({p:pv,q:qv})) >= 0
            finite_count += 1

# All remaining cycle cases have a positive-coefficient witness.
for pv, low in ((5,23),(6,14),(7,11),(8,9)):
    for H in (CH0,CH1):
        certify_nonnegative(CB-H, {p:s.Integer(pv), q:low+v}, (v,))
for H in (CH0,CH1):
    certify_nonnegative(CB-H, {p:u+9,q:u+v+9}, (u,v))

# The exceptional balanced small graph.
q33 = [s.cancel(x.subs({p:3,q:3})) for x in (QA,QB,CH0,CH1,CA,CB)]
assert q33 == [s.Rational(47,20),s.Rational(47,20),s.Rational(73,30),
               s.Rational(103,45),s.Rational(12,5),s.Rational(12,5)]

# Independent incidence-Laplacian reconstruction in small graphs.
def exact_columns(pv,qv):
    k=pv+qv; size=2*k
    edges=[]
    for layer in (0,1):
        for a in range(pv):
            for b in range(pv,k):
                edges.append((layer*k+a,layer*k+b,'H'))
    for a in range(k):
        edges.append((a,k+a,'A' if a<pv else 'B'))
    lap=s.zeros(size)
    for a,b,_ in edges:
        lap[a,a]+=1; lap[b,b]+=1; lap[a,b]-=1; lap[b,a]-=1
    j=s.ones(size,size)/size
    pinv=(lap+j).inv()-j
    norms={}
    for a,b,kind in edges:
        potentials=pinv[:,a]-pinv[:,b]
        curr=[potentials[x]-potentials[y] for x,y,_ in edges]
        qq=sum(abs(c) for c in curr)
        cc=1+qq-2*(potentials[a]-potentials[b])
        norms.setdefault(kind,set()).add((qq,cc))
    assert all(len(z)==1 for z in norms.values())
    test={k:next(iter(z)) for k,z in norms.items()}
    cuts={t:s.cancel(x.subs({p:pv,q:qv})) for t,x in [('A',QA),('B',QB)]}
    cycles={t:s.cancel(x.subs({p:pv,q:qv})) for t,x in [('A',CA),('B',CB)]}
    cuts['H']=max(s.cancel(x.subs({p:pv,q:qv})) for x in (H0,H1))
    cycles['H']=max(s.cancel(x.subs({p:pv,q:qv})) for x in (CH0,CH1))
    for kind,(x,y) in test.items():
        assert x==cuts[kind] and y==cycles[kind],(pv,qv,kind,x,y)
    return len(edges)

edge_columns=sum(exact_columns(pv,qv) for pv,qv in
                 ((2,2),(2,3),(2,6),(3,3),(3,4),(3,6),(3,7),(4,4),(4,5),(5,5)))
print('PASS exact symbolic phase inequalities,', finite_count,
      'finite comparison certificates,',edge_columns,'incidence edge columns')
