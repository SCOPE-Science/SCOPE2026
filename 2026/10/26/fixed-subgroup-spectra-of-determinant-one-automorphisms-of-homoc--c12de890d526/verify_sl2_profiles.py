"""Independent finite tests of a determinant-one fixed-subgroup profile formula."""
from collections import Counter

def vp(value, p, cap):
    if value == 0:
        return cap
    k = 0
    while k < cap and value % p == 0:
        value //= p
        k += 1
    return k

def predicted(p, a):
    result = {(0, 0): p*(p*p-p-1)*p**(3*(a-1))}
    for i in range(a):
        if i:
            result[i, i] = p*p*(p-1)*p**(3*(a-i-1))
        for j in range(i+1, a):
            result[i, j] = (p*p-1)*(p-1)*p**(3*(a-i-1)-(j-i))
        result[i, a] = (p*p-1)*p**(2*(a-i-1))
    result[a, a] = 1
    return result

def checked_exponents(p, a, B):
    m = p**a
    i = min(vp(t, p, a) for t in B)
    j = a if i == a else min(a, vp(B[0]*B[3]-B[1]*B[2], p, 2*a)-i)
    assert 0 <= i <= j <= a
    return i, j

def direct_fixed_subgroup(p, a, B):
    m = p**a
    fixed = []
    for u in range(m):
        for v in range(m):
            if (B[0]*u+B[1]*v)%m == (B[2]*u+B[3]*v)%m == 0:
                fixed.append((u, v))
    counts = []
    for k in range(1, a+1):
        pk = p**k
        counts.append(sum((pk*u)%m == (pk*v)%m == 0 for u,v in fixed))
    observed = sorted((i, j) for i in range(a+1) for j in range(i,a+1)
                      if all(counts[k-1] == p**(min(k,i)+min(k,j)) for k in range(1,a+1)))
    assert len(observed)==1
    return observed[0]

total = 0
checked_direct = 0
for p,a in ((2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(5,1)):
    modulus=p**a
    got=Counter()
    for x in range(modulus):
        for y in range(modulus):
            for z in range(modulus):
                for w in range(modulus):
                    if (x*w-y*z)%modulus != 1:
                        continue
                    B=((x-1)%modulus,y,z,(w-1)%modulus)
                    key=checked_exponents(p,a,B)
                    if (p,a) in ((2,1),(2,2),(2,3),(3,1),(3,2)):
                        assert key == direct_fixed_subgroup(p,a,B)
                        checked_direct += 1
                    got[key]+=1
    assert dict(got)==predicted(p,a), (p,a,got,predicted(p,a))
    assert sum(got.values()) == p*(p*p-1)*p**(3*(a-1))
    print(f"PASS prime={p} exponent={a} matrices={sum(got.values())} profile_types={len(got)}")
    total += sum(got.values())
print(f"ALL_SPECIAL_LINEAR_FIXED_SUBGROUP_CHECKS_PASSED matrices={total} direct_subgroups={checked_direct}")
