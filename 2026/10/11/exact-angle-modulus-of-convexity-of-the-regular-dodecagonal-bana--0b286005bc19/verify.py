import sympy as s

q=s.sqrt(3)
e=s.symbols("e", real=True)

facets=[
    s.Matrix([1,0]),
    s.Matrix([q/2,s.Rational(1,2)]),
    s.Matrix([s.Rational(1,2),q/2]),
    s.Matrix([0,1]),
    s.Matrix([-s.Rational(1,2),q/2]),
    s.Matrix([-q/2,s.Rational(1,2)]),
]
facets += [-v for v in facets]

verts=[]
for i in range(12):
    A=s.Matrix([
        [facets[i][0],facets[i][1]],
        [facets[(i+1)%12][0],facets[(i+1)%12][1]],
    ])
    verts.append(s.simplify(A.LUsolve(s.Matrix([1,1]))))

def dual_norm(w):
    vals=[s.simplify(w.dot(v)) for v in verts]
    # Every comparison is algebraic in Q(sqrt(3)); numerical ordering only
    # selects which exact expression is largest, then all values are checked.
    j=max(range(len(vals)), key=lambda k: float(vals[k].evalf()))
    m=vals[j]
    for z in vals:
        assert s.simplify(m-z)>=0
    return s.simplify(m)

# Exact weighted dual-facet certificates used in the upper bound.
table=[]
for k in range(7):
    p=facets[0]
    r=facets[k]
    S1=s.simplify(dual_norm(p+q*r)+dual_norm(p-q*r))
    S2=s.simplify(dual_norm(q*p+r)+dual_norm(q*p-r))
    table.append((S1,S2))
    assert s.simplify(4-S1)>=0
    assert s.simplify(4-S2)>=0
expected=[2*q,2+q,4,4,4,2+q,2*q]
assert [a for a,b in table]==expected
assert [b for a,b in table]==expected

r0=2-q
a=4-2*q
b=2*(q-1)
c=q
assert s.simplify(a-2*r0)==0
for left,right in [(0,a),(a,1),(1,b),(b,c),(c,2)]:
    assert float((right-left).evalf())>=-1e-12

def primal_norm_expr(v):
    vals=[s.expand(f.dot(v)) for f in facets]
    return vals

def prove_norm_on_interval(v,target,left,right):
    vals=primal_norm_expr(v)
    # The target-minus-facet values are affine in e. Nonnegativity at both
    # interval endpoints proves nonnegativity throughout the interval.
    for z in vals:
        d=s.expand(target-z)
        dl=s.simplify(d.subs(e,left))
        dr=s.simplify(d.subs(e,right))
        assert float(dl.evalf())>=-1e-10,(v,target,left,right,z,dl)
        assert float(dr.evalf())>=-1e-10,(v,target,left,right,z,dr)
    # At least one signed facet is identically the target.
    assert any(s.simplify(target-z)==0 for z in vals)

def certify_pair(x,y,target,left,right):
    prove_norm_on_interval(x,s.Integer(1),left,right)
    prove_norm_on_interval(y,s.Integer(1),left,right)
    prove_norm_on_interval(x-y,e,left,right)
    prove_norm_on_interval(x+y,target,left,right)

# Five explicit unit-pair families cover the three value branches.
x0=s.Matrix([1,-r0])

y1=s.Matrix([1,-r0+e])
certify_pair(x0,y1,s.Integer(2),0,a)

y2=s.Matrix([(4-e)/q-1,e-r0])
certify_pair(x0,y2,(4-e)/q,a,1)

y3=s.Matrix([q-e,(e+r0)/q])
certify_pair(x0,y3,(4-e)/q,1,b)

y4=s.Matrix([-2+3*q-2*e,1])
certify_pair(x0,y4,4-q*e,b,c)

x5=s.Matrix([1,2+q-2*e])
y5=s.Matrix([1-q,q-1])
certify_pair(x5,y5,4-q*e,c,2)

# The three candidate upper envelopes switch at exactly a and b.
assert s.simplify(((4-e)/q-2).subs(e,a))==0
assert s.simplify(((4-e)/q-(4-q*e)).subs(e,b))==0

print("VERIFY_OK dual_separations=7 witness_intervals=5 profile_branches=3 thresholds=4-2sqrt3,2(sqrt3-1)")
