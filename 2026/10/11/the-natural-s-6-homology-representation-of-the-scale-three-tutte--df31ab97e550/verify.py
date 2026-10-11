"""Exact S_6 character checks for scale-3 Rips homology of the doily incidence graph."""
from itertools import permutations, combinations
from collections import Counter
from math import factorial
from fractions import Fraction

S=range(6)
points=tuple(combinations(S,2))
def matches(v):
    if not v:yield ()
    else:
        x,*rest=v
        for y in rest:
            for m in matches([t for t in rest if t!=y]):
                yield tuple(sorted(((x,y),)+m))
lines=tuple(sorted(set(matches(list(S)))))
pidx={a:i for i,a in enumerate(points)}
lidx={a:i for i,a in enumerate(lines)}
flags={(i,j) for i,p in enumerate(points) for j,l in enumerate(lines) if p in l}
assert len(flags)==45

# Simplicial point-collinearity / line-concurrency face lists.
def side_faces(side):
    f={(i,) for i in range(15)}
    for center in (lines if side=='P' else points):
        incident=(tuple(i for i,p in enumerate(points) if p in center) if side=='P'
                  else tuple(j for j,l in enumerate(lines) if center in l))
        assert len(incident)==3
        for k in (2,3):f.update(combinations(incident,k))
    assert len(f)==75
    return tuple(sorted(f))
PA=side_faces('P');LA=side_faces('L')

def signperm(arr):
    return (-1)**sum(arr[i]>arr[j] for i in range(len(arr)) for j in range(i+1,len(arr)))

def partition(n,maxpart=None):
    if n==0:
        yield ()
    else:
        for k in range(min(n,maxpart if maxpart is not None else n),0,-1):
            for rem in partition(n-k,k):yield (k,)+rem

def cycle_type(g):
    seen=set();a=[]
    for i in range(6):
        if i in seen:continue
        j=i;k=0
        while j not in seen:seen.add(j);k+=1;j=g[j]
        a.append(k)
    return tuple(sorted(a,reverse=True))

def action(g):
    pm=[pidx[tuple(sorted((g[a],g[b])))] for a,b in points]
    lm=[lidx[tuple(sorted(tuple(sorted((g[a],g[b]))) for a,b in L))] for L in lines]
    return pm,lm

def trchain(faces,permutation):
    trace=0
    for f in faces:
        img=[permutation[i] for i in f]
        if tuple(sorted(img))==f:trace+=signperm(img)
    return trace

def char_comb(g):
    pm,lm=action(g)
    fflag=sum(pm[i]==i and lm[j]==j for i,j in flags)
    fp=sum(pm[i]==i for i in range(15))
    fl=sum(lm[j]==j for j in range(15))
    h1=fflag-fp-fl+1
    hp=1-trchain([x for x in PA if len(x)==1],pm)+trchain([x for x in PA if len(x)==2],pm)-trchain([x for x in PA if len(x)==3],pm)
    hl=1-trchain([x for x in LA if len(x)==1],lm)+trchain([x for x in LA if len(x)==2],lm)-trchain([x for x in LA if len(x)==3],lm)
    assert hp==hl==h1,(g,h1,hp,hl)
    return h1

allchars={}
for g in permutations(S):
    ty=cycle_type(g);v=char_comb(g)
    allchars.setdefault(ty,[]).append(v)
assert sum(map(len,allchars.values()))==factorial(6)
assert len(allchars)==11
chi={ty:vals[0] for ty,vals in allchars.items()}
assert all(len(set(vals))==1 for vals in allchars.values())
assert chi[(1,1,1,1,1,1)]==16
assert sum(len(vals)*chi[ty]**2 for ty,vals in allchars.items())==factorial(6) # irreducible

# Frobenius alternant coefficient: p_mu=symmetric power sum product, then
# coefficient [x^(lambda+delta)] det(x_i^(ell-j)) p_mu(x) = chi^lambda(mu).
def specht_character(lam,mu):
    ell=len(lam)
    tgt=[lam[i]+ell-i-1 for i in range(ell)]
    total=0
    for sigma in permutations(range(ell)):
        sg=signperm(sigma)
        needs=tuple(tgt[i]-(ell-sigma[i]-1) for i in range(ell))
        if min(needs)<0 or sum(needs)!=sum(mu):continue
        dp={tuple([0]*ell):1}
        for c in mu:
            nd={}
            for v,n in dp.items():
                for j in range(ell):
                    z=list(v);z[j]+=c;z=tuple(z)
                    if z[j] <= needs[j]:nd[z]=nd.get(z,0)+n
            dp=nd
        total+=sg*dp.get(needs,0)
    return total

irreps={}
for lam in partition(6):
    t={ty:specht_character(lam,ty) for ty in allchars}
    irreps[lam]=t
    assert sum(len(allchars[ty])*x*x for ty,x in t.items())==720, (lam,t)
assert len(irreps)==11
lam=(3,2,1)
assert irreps[lam]==chi,('not Specht (3,2,1)',irreps[lam],chi)
mult={lam:sum(len(allchars[ty])*chi[ty]**2*t[ty] for ty in allchars)//720 for lam,t in irreps.items()}
assert all(sum(len(allchars[ty])*chi[ty]**2*t[ty] for ty in allchars)%720==0 for t in irreps.values())
assert all(v>=0 for v in mult.values())
assert sum(mult[l]*irreps[l][(1,)*6] for l in mult)==256
assert mult[(6,)]==1
assert sum(len(allchars[ty])*chi[ty]**2 for ty in allchars)==720 # H3 has 1 invariant
assert sum(len(allchars[ty])*chi[ty] for ty in allchars)==0 # H1 no invariant
print('S6_CHAR_BY_CYCLE_TYPE')
for ty in sorted(allchars,key=lambda x:(len(x),x)):
    print(' ',ty,'class_size',len(allchars[ty]),'H1',chi[ty],'H3',chi[ty]**2)
print('H1_IRREDUCIBLE_SPECHT',(3,2,1))
print('H3_SPECHT_MULTIPLICITIES',[(str(k),v) for k,v in mult.items() if v>0])
print('H3_S6_INVARIANT_DIMENSION',mult[(6,)])
print('VERIFY_EQUIV_OK')
