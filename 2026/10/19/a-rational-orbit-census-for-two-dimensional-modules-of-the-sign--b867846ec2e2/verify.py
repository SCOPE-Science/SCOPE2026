#!/usr/bin/env python3
"""Independent finite-field enumeration for two-dimensional skew-plane modules.
Run with Python 3. Requires only the standard library.
"""
from itertools import product
from collections import Counter

def matmul(A,B,q):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)

def inv(A,q):
    a,b,c,d=A
    det=(a*d-b*c)%q
    assert det
    v=pow(det,-1,q)
    return ((d*v)%q,(-b*v)%q,(-c*v)%q,(a*v)%q)

def anticommutes(A,B,q):
    a,b,c,d=A;e,f,g,h=B
    return ((2*a*e+b*g+c*f)%q==0 and
            ((a+d)*f+b*(e+h))%q==0 and
            ((a+d)*g+c*(e+h))%q==0 and
            (2*d*h+c*f+b*g)%q==0)

def type_of_X(X,q):
    a,b,c,d=X
    if X==(0,0,0,0):
        return "zero"
    if b==c==0 and a==d:
        return "scalar"
    trace=(a+d)%q
    det=(a*d-b*c)%q
    if trace==0:
        if det==0:
            return "nilpotent"
        discriminant=(-4*det)%q
        return "split_trace0" if discriminant in {(j*j)%q for j in range(q)} else "nonsplit_trace0"
    return "singular_nonzero_trace" if det==0 else "regular_nonzero_trace"

def verify(q):
    mats=list(product(range(q),repeat=4))
    solutions={(A,B) for A in mats for B in mats if anticommutes(A,B,q)}
    predicted=q**5+3*q**4-2*q**3-2*q**2+q
    assert len(solutions)==predicted,(q,len(solutions),predicted)
    # Elementary unipotents, a diagonal primitive-root scaling and Weyl exchange
    # generate GL_2(F_q) for q=3,5.
    matrices=((1,1,0,1),(1,0,1,1),(2,0,0,1),(0,1,1,0))
    actions=[(g,inv(g,q)) for g in matrices]
    remaining=solutions.copy(); counts=[]; stratum_counts=Counter()
    while remaining:
        start=next(iter(remaining))
        stratum_counts[type_of_X(start[0],q)]+=1
        remaining.remove(start)
        queue=[start]
        k=0
        while k<len(queue):
            A,B=queue[k];k+=1
            for g,h in actions:
                nxt=(matmul(matmul(g,A,q),h,q),matmul(matmul(g,B,q),h,q))
                assert nxt in solutions
                if nxt in remaining:
                    remaining.remove(nxt)
                    queue.append(nxt)
        counts.append(len(queue))
    predicted_orbits=4*q*q+q-2
    assert len(counts)==predicted_orbits,(q,len(counts),predicted_orbits)
    assert sum(counts)==len(solutions)
    expected_strata={"zero":q*q+q,"scalar":q-1,"nilpotent":2*q-1,
                     "split_trace0":(q-1)*(q+2)//2,
                     "nonsplit_trace0":q*(q-1)//2,
                     "singular_nonzero_trace":q*(q-1),
                     "regular_nonzero_trace":(q-1)**2}
    assert dict(stratum_counts)==expected_strata,(q,dict(stratum_counts),expected_strata)
    print(f'q={q}: labeled={len(solutions)}, orbits={len(counts)}, distinct_orbit_sizes={sorted(set(counts))}')

if __name__=='__main__':
    for q in (3,5):
        verify(q)
    print('VERIFY_OK')
