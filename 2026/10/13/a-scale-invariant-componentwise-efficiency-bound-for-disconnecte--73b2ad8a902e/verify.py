from fractions import Fraction

def component_bound(q, edges):
    M=max(q)
    m=min(q[i]*q[j]/(q[i]+q[j]) for i,j in edges)
    return M/m, M, m

def global_bound(components, scales):
    nums=[]; dens=[]
    for (q,edges),c in zip(components,scales):
        p=[c*x for x in q]
        nums.extend(p)
        dens.extend(p[i]*p[j]/(p[i]+p[j]) for i,j in edges)
    return max(nums)/min(dens)

# Two identical disconnected symmetric pairs: intrinsic bound 2, global gauge bound 2C.
comps=[([Fraction(1),Fraction(1)],[(0,1)]),([Fraction(1),Fraction(1)],[(0,1)])]
for C in [Fraction(1),Fraction(3),Fraction(17)]:
    assert global_bound(comps,[C,Fraction(1)]) == 2*C
assert max(component_bound(*x)[0] for x in comps)==2

# Scale invariance and optimal normalization on heterogeneous examples.
comps=[([Fraction(1),Fraction(2),Fraction(4)],[(0,1),(1,2)]),([Fraction(3),Fraction(5)],[(0,1)])]
Bs=[]; scales=[]
for q,e in comps:
    B,M,m=component_bound(q,e)
    Bs.append(B); scales.append(1/M)
    for c in [Fraction(2),Fraction(7,3)]:
        B2,_,_=component_bound([c*x for x in q],e)
        assert B2==B
B=max(Bs)
assert global_bound(comps,scales)==B
for trial in [[Fraction(1),Fraction(1)],[Fraction(2),Fraction(3)],[Fraction(5),Fraction(1,4)]]:
    assert global_bound(comps,trial)>=B
print('VERIFY_OK')
