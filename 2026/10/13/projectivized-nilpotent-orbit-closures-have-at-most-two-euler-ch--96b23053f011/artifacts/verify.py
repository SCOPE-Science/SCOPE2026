from itertools import product

def uniq(xs):
    return list(dict.fromkeys(xs))

def A(l):
    roots=[]
    n=l+1
    for i in range(n):
        for j in range(n):
            if i!=j:
                v=[0]*n; v[i]=1; v[j]=-1
                roots.append(tuple(v))
    return roots, roots, []

def B(l):
    long=[]; short=[]
    for i in range(l):
        for s in (-1,1):
            v=[0]*l; v[i]=s; short.append(tuple(v))
    for i in range(l):
        for j in range(i+1,l):
            for a,b in product((-1,1), repeat=2):
                v=[0]*l; v[i]=a; v[j]=b; long.append(tuple(v))
    return long+short, long, short

def C(l):
    long=[]; short=[]
    for i in range(l):
        for s in (-2,2):
            v=[0]*l; v[i]=s; long.append(tuple(v))
    for i in range(l):
        for j in range(i+1,l):
            for a,b in product((-1,1), repeat=2):
                v=[0]*l; v[i]=a; v[j]=b; short.append(tuple(v))
    return long+short, long, short

def D(l):
    roots=[]
    for i in range(l):
        for j in range(i+1,l):
            for a,b in product((-1,1), repeat=2):
                v=[0]*l; v[i]=a; v[j]=b; roots.append(tuple(v))
    return roots, roots, []

def F4():
    long=[]; short=[]
    for i in range(4):
        for j in range(i+1,4):
            for a,b in product((-2,2), repeat=2):
                v=[0]*4; v[i]=a; v[j]=b; long.append(tuple(v))
    for i in range(4):
        for a in (-2,2):
            v=[0]*4; v[i]=a; short.append(tuple(v))
    for signs in product((-1,1), repeat=4):
        short.append(tuple(signs))
    return uniq(long+short), uniq(long), uniq(short)

def G2():
    # simple-root coordinates: alpha short, beta long
    positives=[
        ((1,0),'s'), ((0,1),'l'), ((1,1),'s'),
        ((2,1),'s'), ((3,1),'l'), ((3,2),'l')
    ]
    long=[]; short=[]
    for v,t in positives:
        for sgn in (-1,1):
            w=(sgn*v[0], sgn*v[1])
            (short if t=='s' else long).append(w)
    return short+long, long, short

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def separating_cocharacter(roots):
    n=len(roots[0])
    for base in range(3,60):
        lam=tuple(base**i for i in range(n))
        vals=[dot(r,lam) for r in roots]
        if all(v!=0 for v in vals) and len(vals)==len(set(vals)):
            return lam
    raise AssertionError("no separating cocharacter in deterministic search")

systems=0
root_weight_checks=0

for l in range(1,13):
    roots,long,short=A(l)
    assert len(roots)==l*(l+1)
    assert len(short)==0
    separating_cocharacter(roots)
    root_weight_checks += len(roots)
    systems += 1

for l in range(2,13):
    roots,long,short=B(l)
    assert len(long)==2*l*(l-1)
    assert len(short)==2*l
    assert len(roots)==2*l*l
    assert (len(long),len(roots))==(2*l*(l-1),2*l*l)
    separating_cocharacter(roots)
    root_weight_checks += len(roots)
    systems += 1

for l in range(2,13):
    roots,long,short=C(l)
    assert len(long)==2*l
    assert len(short)==2*l*(l-1)
    assert len(roots)==2*l*l
    assert (len(long),len(roots))==(2*l,2*l*l)
    separating_cocharacter(roots)
    root_weight_checks += len(roots)
    systems += 1

for l in range(3,13):
    roots,long,short=D(l)
    assert len(roots)==2*l*(l-1)
    assert len(short)==0
    separating_cocharacter(roots)
    root_weight_checks += len(roots)
    systems += 1

roots,long,short=F4()
assert (len(long),len(short),len(roots))==(24,24,48)
separating_cocharacter(roots)
root_weight_checks += len(roots)
systems += 1

roots,long,short=G2()
assert (len(long),len(short),len(roots))==(6,6,12)
separating_cocharacter(roots)
root_weight_checks += len(roots)
systems += 1

exceptional={"E6":(78,6,72),"E7":(133,7,126),"E8":(248,8,240)}
for name,(dim,rank,roots) in exceptional.items():
    assert dim-rank==roots

print("VERIFY_OK", systems, root_weight_checks, len(exceptional))
