#!/usr/bin/env python3
"""Independent brute-force small-level checks for prime-power images."""
from math import isqrt

def squares(p,m):
    if m == 0:
        return 1
    return 1+sum((p-1)*p**(m-2*j-1)//2 for j in range((m+1)//2))

def predicted(p,k):
    if p == 3:
        if k in (1,2):
            return 3
        if k == 3:
            return 5
        return 13*3**(k-4)
    if k <= 2:
        return p
    return p**(k-2)+(p-1)*squares(p,k-3)

T={0,2,9,18,27,29,36,45,52,54,63,72,79}
systems=0
inputs=0
for p,maxk in ((3,9),(5,7),(7,6),(11,5),(13,4)):
    for k in range(1,maxk+1):
        m=p**k
        values={(pow(x,p,m)-p*x)%m for x in range(m)}
        assert len(values)==predicted(p,k),(p,k,len(values),predicted(p,k))
        if p==3 and k>=4:
            assert values=={n for n in range(m) if n%81 in T}
        systems+=1;inputs+=m
full_structural_checks=0
for p,k in ((5,3),(5,4),(5,5),(7,3),(7,4),(11,3),(11,4)):
    m=p**k
    modulus=p**(k-3)
    predicted_values={p*p*j for j in range(p**(k-2))}
    squares={(t*t)%modulus for t in range(modulus)}
    for a in range(1,p):
        z=pow(a,p**(k+3),m)
        assert (pow(z,p-1,m)==1 and z%p==a)
        u=((p-1)//2)*pow(z,p-2,m)
        center=((1-p)*z)%m
        predicted_values.update((center+p**3*u*t)%m for t in squares)
    actual={(pow(x,p,m)-p*x)%m for x in range(m)}
    assert predicted_values==actual,(p,k,len(predicted_values),len(actual))
    full_structural_checks+=1
print(f"VERIFY_OK systems={systems} enumerated_inputs={inputs} ternary_classes={len(T)} structural_sets={full_structural_checks}")
