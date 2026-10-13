LIMIT = 1_000_000

def factor_data(n):
    x=n
    p=2
    omega=0
    exps=[]
    while p*p<=x:
        if x%p==0:
            e=0
            while x%p==0:
                x//=p; e+=1
            omega += e
            exps.append((p,e))
        p = 3 if p==2 else p+2
    if x>1:
        omega += 1
        exps.append((x,1))
    tau=1
    for _,e in exps:
        tau *= e+1
    return omega, tau, exps

def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

fibers={}
data={}
for n in range(2,LIMIT+1):
    om,tau,fac=factor_data(n)
    if om<=2:
        data[n]=(tau,fac)
        fibers.setdefault(n+tau,[]).append(n)

bad=[]
nontrivial=[]
for value, xs in fibers.items():
    if len(xs)>1:
        nontrivial.append((value,xs))
        if len(xs)!=2:
            bad.append((value,xs,'fiber-size'))
            continue
        m,n=xs
        ok=(m,n)==(4,5)
        if not ok:
            tau_m, fac_m=data[m]
            tau_n, fac_n=data[n]
            ok=(tau_m==4 and tau_n==2 and n==m+2 and is_prime(n)
                and len(fac_m)==2 and all(e==1 for _,e in fac_m)
                and all(p%2==1 for p,_ in fac_m))
        if not ok:
            bad.append((value,xs,'shape'))

for m,(tau_m,fac_m) in data.items():
    if tau_m==4 and len(fac_m)==2 and all(e==1 for _,e in fac_m) and all(p%2==1 for p,_ in fac_m):
        n=m+2
        if n<=LIMIT and is_prime(n):
            if fibers.get(m+4)!=[m,n]:
                bad.append((m,m+4,n,'converse'))

assert not bad, bad[:10]
assert fibers[7]==[4,5]
assert max(map(len,fibers.values()))==2
print(f"VERIFY_OK limit={LIMIT} low_omega_inputs={len(data)} nontrivial_fibers={len(nontrivial)} exceptional_4_5={fibers[7]==[4,5]} theorem_mismatches={len(bad)} max_fiber={max(map(len,fibers.values()))}")
