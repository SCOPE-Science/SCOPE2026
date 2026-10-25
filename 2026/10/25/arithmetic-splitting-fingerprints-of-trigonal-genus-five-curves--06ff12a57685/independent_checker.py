"""Independent exact check of rational Hurwitz profiles over F2.

All arithmetic uses explicit GF(2)-bit vectors and field multiplication;
reducibility is removed by a separately generated *set* of all degree-(1,4)
and degree-(2,3) products, without polynomial long division.
"""
from collections import Counter
from itertools import combinations_with_replacement

def mons(deg):
    return [(i,j,deg-i-j) for i in range(deg+1) for j in range(deg-i+1)]
M={i:mons(i) for i in range(1,6)}
where={x:i for i,x in enumerate(M[5])}
allowed=[x for x in M[5] if x not in ((0,0,5),(1,0,4),(0,1,4))]
assert len(allowed)==18

def gf_multiply(a,b,n):
    q=1<<n; mod={1:3,2:7,3:11,4:19,5:37}[n]
    s=0
    while b:
        if b&1:s^=a
        a<<=1
        if a&q:a^=mod
        b>>=1
    return s

def field(n):
    q=1<<n
    return [[gf_multiply(a,b,n) for b in range(q)] for a in range(q)]

def derive_point_rows(n,pt, mult):
    x,y,z=pt
    powers={w:[1] for w in pt}
    for w in pt:
        for j in range(5):powers[w].append(mult[powers[w][-1]][w])
    rows=[0]*(3*n)
    for pos,(i,j,k) in enumerate(allowed):
        for grad,exps in enumerate(((i-1,j,k),(i,j-1,k),(i,j,k-1))):
            if (i,j,k)[grad]%2==0:continue
            dx,dy,dz=exps
            value=mult[mult[powers[x][dx]][powers[y][dy]]][powers[z][dz]]
            for digit in range(n):
                if (value>>digit)&1:rows[grad*n+digit] |= 1<<pos
    return tuple(r for r in rows if r)

# Independent combinatorial test: all 7 linear factors and 63 conic factors.
# Build the complete set of products, using Gray codes.
reducibles=set()
for degree_a in (1,2):
    degree_b=5-degree_a
    for a in range(1,1<<len(M[degree_a])):
        base=[]
        for ex in M[degree_b]:
            b=0
            for idx,xx in enumerate(M[degree_a]):
                if (a>>idx)&1:
                    b ^= 1<<where[tuple(xx[t]+ex[t] for t in range(3))]
            base.append(b)
        x=0
        reducibles.add(x)
        old=0
        for i in range(1,1<<len(base)):
            gray=i^(i>>1)
            diff=gray^old
            x ^= base[diff.bit_length()-1]
            reducibles.add(x)
            old=gray
print('reducible-quintic-set-cardinality',len(reducibles))

# Retain one rational-coordinate representative of each Frobenius orbit.
classes=[]
for n in range(1,6):
    q=1<<n
    tab=field(n)
    points=[(1,a,b) for a in range(q) for b in range(q)]+[(0,1,b) for b in range(q)]+[(0,0,1)]
    new=[]
    for x,y,z in points:
        if (x,y,z)==(0,0,1):continue
        start=(x,y,z)
        orbit=[start]
        now=start
        while True:
            now=tuple(tab[t][t] for t in now)
            if now==start:break
            orbit.append(now)
        if len(orbit)!=n or start!=min(orbit):continue
        new.append(derive_point_rows(n,start,tab))
    classes+=new
    print('closed points degree',n,len(new))

pidx={v:i for i,v in enumerate(allowed)}

def coeff(mask,i,j,k):
    at=pidx.get((i,j,k))
    return at is not None and bool(mask&(1<<at))

def local_type(mask):
    a,b,c=[coeff(mask,*x) for x in ((2,0,3),(1,1,3),(0,2,3))]
    if b:return 2 if a and c else 1
    if not a and not c:return 0
    if a and c:
        cubic=sum(coeff(mask,i,3-i,2) for i in range(4))%2
    elif a:cubic=coeff(mask,0,3,2)
    else:cubic=coeff(mask,3,0,2)
    return 3 if cubic else 0

def polynomial(mask):
    return sum(((mask>>i)&1)<<where[x] for i,x in enumerate(allowed))

def res(mask,ux,uy):
    return sum(1 << (i+j-2) for idx,(i,j,k) in enumerate(allowed) if (mask>>idx)&1 and (ux or i==0) and (uy or j==0))  # no duplicate degree when parity? fix XOR below

def residual(mask,ux,uy):
    v=0
    for idx,(i,j,k) in enumerate(allowed):
        if (mask>>idx)&1 and (ux or i==0) and (uy or j==0):v^=1<<(i+j-2)
    return v

def splitting(v):
    r=(v&1==0)+(v&8==0)+(v.bit_count()%2==0)
    if r==0:return 0
    if r==3:return 4
    if r==2:return 3
    if v in (1,8,15):return 2
    return 1

counts=Counter();point_counts=Counter();bytype=Counter(); rejected=Counter();witness={}
for mask in range(1<<18):
    t=local_type(mask)
    if not t:continue
    fail=0
    for rows in classes:
        if all((mask&r).bit_count()%2==0 for r in rows):
            fail=1;break
    if fail:rejected['geometric']+=1;continue
    if polynomial(mask) in reducibles:
        rejected['reducible']+=1;continue
    types=sorted(splitting(residual(mask,*direction)) for direction in ((1,0),(0,1),(1,1)))
    profile=tuple(types)
    counts[(t,profile)]+=1
    witness.setdefault(profile,(t,mask))
    point_counts[(t,sum((0,1,1,2,3)[r] for r in types))]+=1
    bytype[(t,sum(r in (2,3) for r in types))]+=1
print('rejections',dict(rejected))
print('accepted',sum(counts.values()))
print('ramification hist by type:')
for t in (1,2,3):print(t,[bytype[(t,r)] for r in range(4)])
print('point counts by type:')
for t in (1,2,3):print(t,[point_counts[(t,n)] for n in range(10)])
print('number_nonzero_profiles',len(counts))
print('digest_summary',sum((t*101+i*17+j*7+k)*c for (t,(i,j,k)),c in counts.items()))

from collections import defaultdict
agg=defaultdict(int)
for (_,key),v in counts.items():agg[key]+=v
print('ALL 34 HURWITZ PROFILES, fixed-center counts, first witnesses:')
for profile in sorted(agg):
    t,mask=witness[profile]
    print(*profile,agg[profile],t,hex(mask))

print('ALL 75 PROFILE-BY-SINGULARITY COUNTS:')
for (t,(i,j,k)),c in sorted(counts.items()):print('PROFILE_CHECK',t,i,j,k,c)
