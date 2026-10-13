import math

LIMIT = 300000

def factorint(n):
    x=n
    f={}
    p=2
    while p*p<=x:
        while x%p==0:
            f[p]=f.get(p,0)+1
            x//=p
        p=3 if p==2 else p+2
    if x>1:
        f[x]=f.get(x,0)+1
    return f

def divisors_from_factorization(f):
    ds=[1]
    for p,e in f.items():
        base=list(ds)
        mul=1
        for _ in range(e):
            mul*=p
            ds += [d*mul for d in base]
    return ds

def small_sum(n,f):
    return sum(d for d in divisors_from_factorization(f) if d*d<=n)

def theorem(n,f):
    om=sum(f.values())
    if n<2 or om>3:
        return False
    if len(f)==1:
        (_,e),=f.items()
        return e==1
    if om==2:
        return n==6
    if om==3:
        if len(f)==3:
            return False
        if len(f)==1:
            return False
        p=q=None
        for r,e in f.items():
            if e==2:
                p=r
            elif e==1:
                q=r
        if p is None:
            return False
        return n in (12,18) or q==p*p+p+1 or q==p*p-p-1
    return False

checked=0
solutions=[]
mismatches=[]
for n in range(2,LIMIT+1):
    f=factorint(n)
    if sum(f.values())<=3:
        checked+=1
        actual=(n % small_sum(n,f)==0)
        predicted=theorem(n,f)
        if actual:
            solutions.append(n)
        if actual!=predicted:
            mismatches.append((n,f,small_sum(n,f),actual,predicted))
            break

if mismatches:
    raise SystemExit('VERIFY_FAIL '+repr(mismatches[0]))
composites=[n for n in solutions if len(factorint(n))>1]
head=','.join(map(str,composites[:10]))
print(f'VERIFY_OK limit={LIMIT} checked={checked} solutions={len(solutions)} composite_solutions={head},... mismatches=0')
