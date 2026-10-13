#!/usr/bin/env python3
LIMIT = 300000

# Smallest-prime-factor sieve.
spf = list(range(LIMIT + 1))
for i in range(2, int(LIMIT**0.5) + 1):
    if spf[i] == i:
        step = i
        start = i*i
        for j in range(start, LIMIT + 1, step):
            if spf[j] == j:
                spf[j] = i

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        out.append((p,a))
    return out

def funcs(n, fac):
    ph = n
    ps = n
    sg = 1
    squarefree = True
    for p,a in fac:
        ph = ph // p * (p-1)
        ps = ps // p * (p+1)
        sg *= (p**(a+1)-1)//(p-1)
        if a > 1:
            squarefree = False
    return ph,ps,sg,squarefree

min_def = None
mins = []
comp_count = 0
sf_min = None
nsf_min = None
branch_violations = []
for n in range(2, LIMIT + 1):
    fac = factor(n)
    prime = (len(fac)==1 and fac[0][1]==1)
    ph,ps,sg,sf = funcs(n, fac)
    defect = ph**3 + ps**3 + sg**3 - (3*n**3 + 3*n*n + 9*n + 1)
    if prime:
        if defect != 0:
            raise AssertionError(("prime defect",n,defect))
        continue
    comp_count += 1
    x = ps-n
    y = sg-ps
    if ph + ps < 2*n:
        branch_violations.append((n,"phi+psi",ph,ps))
    if sf:
        if y != 0 or x < 6:
            branch_violations.append((n,"squarefree bounds",x,y,fac))
        sf_min = defect if sf_min is None else min(sf_min, defect)
    else:
        if x < 2 or y < 1:
            branch_violations.append((n,"nonsquarefree bounds",x,y,fac))
        nsf_min = defect if nsf_min is None else min(nsf_min, defect)
    if min_def is None or defect < min_def:
        min_def = defect
        mins = [n]
    elif defect == min_def:
        mins.append(n)
    if defect < 290:
        raise AssertionError(("defect below 290",n,defect,fac))

if branch_violations:
    raise AssertionError(branch_violations[:5])
if min_def != 290 or mins != [4]:
    raise AssertionError(("wrong minimum",min_def,mins[:20]))
print("VERIFY_OK")
print(f"limit={LIMIT}")
print(f"composite_cases={comp_count}")
print(f"minimum_defect={min_def}")
print(f"unique_minimizer={mins[0]}")
print(f"squarefree_composite_minimum={sf_min}")
print(f"nonsquarefree_composite_minimum={nsf_min}")
print("branch_bound_violations=0")
