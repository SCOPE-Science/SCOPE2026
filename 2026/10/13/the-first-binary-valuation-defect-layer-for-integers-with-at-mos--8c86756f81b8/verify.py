"""Finite regression for valuation-defect theorem; not a proof of completeness."""
N=200000
sigma=[0]*(N+1)
omega=[0]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d): sigma[n]+=d
for p in range(2,N+1):
    if omega[p]: continue
    for n in range(p,N+1,p):
        m=n
        while m%p==0:
            omega[n]+=1
            m//=p
found=[]
for n in range(2,N+1):
    if omega[n]>2: continue
    s=sigma[n]
    v2=(s&-s).bit_length()-1
    if (n-1).bit_length()-v2==1: found.append(n)
expected=[2,15]
for p in range(3,N//2+1,2):
    if (p+1)&p: continue
    if omega[p]!=1: continue
    expected.append(2*p)
assert sorted(expected)==found,(expected,found)
print(f'VERIFY_OK n_max={N} first_defect={found} exact_integer_sieve=PASS')
