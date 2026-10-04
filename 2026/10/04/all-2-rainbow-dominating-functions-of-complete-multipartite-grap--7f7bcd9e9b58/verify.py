from itertools import product
from math import factorial

MAX_N=8

def parts(n, lo=1):
    if n==0:
        yield ()
        return
    for a in range(lo,n+1):
        for rest in parts(n-a,a):
            yield (a,)+rest

def weight(label):
    return (label&1>0)+(label&2>0)

def literal(ps, assn):
    idx=[]
    for i,n in enumerate(ps): idx += [i]*n
    for v,l in enumerate(assn):
        if l==0:
            i=idx[v]; u=0
            for w,x in enumerate(assn):
                if idx[w]!=i: u |= x
            if u!=3: return False
    return True

def structural(ps, assn):
    idx=[]
    for i,n in enumerate(ps): idx += [i]*n
    E=set(); I1=set(); I2=set()
    for i,l in zip(idx,assn):
        if l==0:E.add(i)
        if l&1:I1.add(i)
        if l&2:I2.add(i)
    return all((I1-{i}) and (I2-{i}) for i in E)

def gamma_formula(ps):
    m=min(ps)
    return min(4,max(2,m))

def comps4(n):
    for e in range(n+1):
      for a in range(n-e+1):
       for b in range(n-e-a+1):
        d=n-e-a-b
        yield e,a,b,d

def multinom(q):
    n=sum(q); z=factorial(n)
    for x in q:z//=factorial(x)
    return z

def profile_poly(ps):
    out=[0]*(2*sum(ps)+1)
    cps=[list(comps4(n)) for n in ps]
    for prof in product(*cps):
        E={i for i,(e,a,b,d) in enumerate(prof) if e>0}
        I1={i for i,(e,a,b,d) in enumerate(prof) if a+d>0}
        I2={i for i,(e,a,b,d) in enumerate(prof) if b+d>0}
        if not all((I1-{i}) and (I2-{i}) for i in E):
            continue
        w=sum(a+b+2*d for e,a,b,d in prof)
        c=1
        for q in prof:c*=multinom(q)
        out[w]+=c
    return out

profiles=assignments=coeffchecks=0
for n in range(2,MAX_N+1):
    for ps in parts(n):
        if len(ps)<2: continue
        profiles+=1
        coeff=[0]*(2*n+1)
        mn=None
        for assn in product(range(4), repeat=n):
            assignments+=1
            a=literal(ps,assn); b=structural(ps,assn)
            if a!=b:
                raise SystemExit(f'CLASS_FAIL ps={ps} assn={assn} literal={a} structural={b}')
            if a:
                w=sum(weight(x) for x in assn)
                coeff[w]+=1
                mn=w if mn is None else min(mn,w)
        gf=gamma_formula(ps)
        if mn!=gf:
            raise SystemExit(f'GAMMA_FAIL ps={ps} brute={mn} formula={gf}')
        p=profile_poly(ps)
        coeffchecks+=len(coeff)
        if p!=coeff:
            raise SystemExit(f'POLY_FAIL ps={ps} brute={coeff} profile={p}')
print(f'VERIFY_OK profiles={profiles} assignments={assignments} coefficient_checks={coeffchecks} max_order={MAX_N}')
