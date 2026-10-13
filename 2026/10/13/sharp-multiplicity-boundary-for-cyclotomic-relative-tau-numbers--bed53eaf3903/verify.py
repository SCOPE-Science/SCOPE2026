from math import isqrt

PRIMES=[2,3,5,7,11,13]
KMAX=3
NMAX=100000

def factor(n):
    fs=[]; x=n; p=2
    while p*p<=x:
        if x%p==0:
            e=0
            while x%p==0: x//=p; e+=1
            fs.append((p,e))
        p=3 if p==2 else p+2
    if x>1: fs.append((x,1))
    return fs

def tau_omega(n):
    fs=factor(n)
    t=1; om=0
    for _,e in fs: t*=e+1; om+=e
    return t,om,fs

def phi_prime_power_mod(n,p,k,mod):
    # 1+n^(p^(k-1))+...+n^((p-1)p^(k-1)) mod mod
    step=pow(n,p**(k-1),mod)
    s=0; cur=1
    for _ in range(p):
        s=(s+cur)%mod
        cur=(cur*step)%mod
    return s

checks=0; boundary_hits=[]; violations=[]
for p in PRIMES:
  for k in range(1,KMAX+1):
    for n in range(2,NMAX+1):
      t,om,fs=tau_omega(n)
      rel=(phi_prime_power_mod(n,p,k,t)==0)
      if rel:
        checks += 1
        if om < p-1:
          violations.append((p,k,n,t,om,fs,'below'))
        if om == p-1:
          ok=(len(fs)==1 and fs[0][1]==p-1 and fs[0][0]!=p)
          if not ok: violations.append((p,k,n,t,om,fs,'boundary-shape'))
          boundary_hits.append((p,k,n,fs))
      # converse at boundary in finite box
      if om==p-1 and len(fs)==1 and fs[0][1]==p-1 and fs[0][0]!=p:
        if not rel: violations.append((p,k,n,t,om,fs,'converse'))
assert not violations, violations[:10]
# explicit exceptional q=p boundary non-solutions where in range
for p in PRIMES:
  n=p**(p-1)
  if n<=NMAX:
    for k in range(1,KMAX+1):
      t,om,fs=tau_omega(n)
      assert phi_prime_power_mod(n,p,k,t)!=0
print('VERIFY_OK')
print(f'p_values={PRIMES}')
print(f'k_max={KMAX}')
print(f'n_max={NMAX}')
print(f'relative_hits={checks}')
print(f'boundary_hits={len(boundary_hits)}')
print('violations=0')
print('boundary_samples='+';'.join(f'p={p},k={k},n={n}' for p,k,n,_ in boundary_hits[:16]))
