"""Finite exact combinatorial verification of graded S6 homology characters.

No external libraries or stored face lists are required. This script performs
finite-chain computations; the separate literature theorem supplies integral
homology torsion-freeness used in interpreting the modular invariant ranks.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict
from functools import lru_cache
from math import factorial

N=6
EDGES=list(combinations(range(N),2))
INDEX={e:i for i,e in enumerate(EDGES)}
TYPES=[(6,),(5,1),(4,2),(4,1,1),(3,3),(3,2,1),(3,1,1,1),
       (2,2,2),(2,2,1,1),(2,1,1,1,1),(1,1,1,1,1,1)]
EXPECTED4=[0,0,-1,-1,-2,0,-2,3,3,3,115]
EXPECTED5=[0,-1,0,0,0,-1,3,0,0,8,24]

# A graph belongs to the complex precisely when no pair of its vertices
# dominates all six: singleton dominating sets extend to such pairs.
def permitted(mask):
    for a,b in combinations(range(N),2):
        if all((mask&(1<<INDEX[tuple(sorted((a,v)))])) or
               (mask&(1<<INDEX[tuple(sorted((b,v)))]))
               for v in range(N) if v!=a and v!=b):
            return False
    return True

FACES=[m for m in range(1<<len(EDGES)) if permitted(m)]
BY_DIM={d:[m for m in FACES if m.bit_count()==d+1] for d in range(-1,7)}
assert [len(BY_DIM[d]) for d in range(-1,7)]==[1,15,105,455,1185,1647,915,180]
assert all(m^(1<<i) in FACES for m in FACES
           for i in range(len(EDGES)) if m&(1<<i))

def cycle_perm(parts):
    p=list(range(N));off=0
    for n in parts:
        for i in range(n):p[off+i]=off+(i+1)%n
        off+=n
    return p

def compose(p,q):return [p[q[i]] for i in range(N)]
def cycle_type(p):
    seen=set();parts=[]
    for i in range(N):
        if i in seen:continue
        v=i;l=0
        while v not in seen:
            seen.add(v);v=p[v];l+=1
        parts.append(l)
    return tuple(sorted(parts,reverse=True))

def edge_map(p):
    return [INDEX[tuple(sorted((p[i],p[j])))] for i,j in EDGES]

def action(mask,emap):
    seq=[emap[i] for i in range(len(EDGES)) if mask&(1<<i)]
    new=sum(1<<v for v in seq)
    inversions=sum(seq[i]>seq[j] for i in range(len(seq))
                   for j in range(i+1,len(seq)))
    return new,(-1 if inversions%2 else 1)

def cyclic_powers(parts):
    p=cycle_perm(parts);a=[list(range(N))]
    while True:
        q=compose(p,a[-1])
        if q==a[0]:return a
        a.append(q)

def invariant_complex(parts):
    actions=[edge_map(p) for p in cyclic_powers(parts)]
    rep_of={};orbit_sign={};reps=defaultdict(list);representatives=[]
    for d in range(-1,7):
        for f in BY_DIM[d]:
            if f in rep_of:continue
            orbit={};orientable=True
            for em in actions:
                g,s=action(f,em)
                if g in orbit and orbit[g]!=s:orientable=False
                orbit[g]=s
            oid=len(representatives);representatives.append(f)
            for g,s in orbit.items():rep_of[g]=oid;orbit_sign[g]=s
            if orientable:reps[d].append(oid)
    indexed={d:{k:i for i,k in enumerate(reps[d])} for d in range(-1,7)}
    boundary={}
    for d in range(7):
        columns=[]
        for oid in reps[d]:
            f=representatives[oid];col={}
            for position,edge in enumerate(i for i in range(15) if f&(1<<i)):
                g=f^(1<<edge);r=rep_of[g]
                if r not in indexed[d-1]:continue
                i=indexed[d-1][r]
                col[i]=col.get(i,0)+(-1 if position%2 else 1)*orbit_sign[g]
            columns.append({i:x for i,x in col.items() if x})
        boundary[d]=columns
    return reps,boundary

def rank_mod(columns,p):
    pivots={}
    for col in columns:
        v={i:x%p for i,x in col.items() if x%p}
        while v:
            pivot=min(v)
            if pivot not in pivots:
                z=pow(v[pivot],-1,p)
                pivots[pivot]={i:(x*z)%p for i,x in v.items()}
                break
            factor=v[pivot]
            for i,x in pivots[pivot].items():
                z=(v.get(i,0)-factor*x)%p
                if z:v[i]=z
                else:v.pop(i,None)
    return len(pivots)

def check_d_squared(boundary):
    for d in range(1,7):
        for col in boundary[d]:
            summed={}
            for mid,a in col.items():
                for target,b in boundary[d-1][mid].items():
                    summed[target]=summed.get(target,0)+a*b
            assert not any(summed.values()),('boundary_squared',d)

def bettis(reps,boundary,p):
    ranks={d:rank_mod(boundary[d],p) for d in range(7)}
    return [len(reps[d])-ranks.get(d,0)-ranks.get(d+1,0)
            for d in range(-1,7)],ranks

def character_from_invariants(invariants,degree):
    character={(1,)*6:invariants[(1,)*6][degree]}
    # The later items in TYPES are powers of earlier ones; reverse order
    # therefore determines each remaining class character recursively.
    for typ in reversed(TYPES[:-1]):
        powers=cyclic_powers(typ)
        mult=Counter(cycle_type(p) for p in powers)
        others=sum(c*character[t] for t,c in mult.items() if t!=typ)
        numerator=len(powers)*invariants[typ][degree]-others
        assert numerator%mult[typ]==0
        character[typ]=numerator//mult[typ]
    return character

def signed_fixed_chain_trace(parts):
    em=edge_map(cycle_perm(parts));s=0
    for f in FACES:
        g,sgn=action(f,em)
        if f==g:
            d=f.bit_count()-1
            s+=(-1 if d%2 else 1)*sgn
    return s

@lru_cache(None)
def irreducible_character(partition,mu):
    l=len(partition)
    target=tuple(partition[i]+l-i-1 for i in range(l))
    @lru_cache(None)
    def ways(index,remaining):
        if index==len(mu):return int(all(x==0 for x in remaining))
        j=mu[index]
        return sum(ways(index+1,remaining[:i]+(remaining[i]-j,)+remaining[i+1:])
                   for i in range(l) if remaining[i]>=j)
    ans=0
    for sigma in permutations(range(l)):
        rem=tuple(target[i]-(l-1-sigma[i]) for i in range(l))
        if min(rem)<0:continue
        inv=sum(sigma[i]>sigma[j] for i in range(l) for j in range(i+1,l))
        ans+=(-1 if inv%2 else 1)*ways(0,rem)
    return ans

def class_size(mu):
    z=1
    for k,n in Counter(mu).items():z*=k**n*factorial(n)
    return factorial(6)//z

def decompose(char):
    # Frobenius alternant characters form an orthonormal basis.
    for a in TYPES:
        for b in TYPES:
            dot=sum(class_size(mu)*irreducible_character(a,mu)*
                    irreducible_character(b,mu) for mu in TYPES)
            assert dot==(factorial(6) if a==b else 0)
    result={}
    for lam in TYPES:
        numerator=sum(class_size(mu)*char[mu]*irreducible_character(lam,mu)
                      for mu in TYPES)
        assert numerator%factorial(6)==0
        multiplicity=numerator//factorial(6)
        assert multiplicity>=0
        if multiplicity:result[str(lam)]=multiplicity
    return result

def run():
    by_prime={};examples={}
    for prime in (2147483647,1000000007):
        inv={}
        for typ in TYPES:
            reps,bd=invariant_complex(typ)
            check_d_squared(bd)
            reduced,ranks=bettis(reps,bd,prime)
            assert reduced[:-3]==[0,0,0,0,0] # dimensions -1 through 3
            assert reduced[-1]==0 # dimension 6
            inv[typ]={4:reduced[5],5:reduced[6]}
            if prime==2147483647:
                examples[str(typ)]={'cyclic_order':len(cyclic_powers(typ)),
                 'invariant_chain_dimensions':[len(reps[d]) for d in range(-1,7)],
                 'invariant_boundary_ranks':[ranks[d] for d in range(7)],
                 'invariant_betti_4_5':[reduced[5],reduced[6]]}
        by_prime[prime]=inv
    assert by_prime[2147483647]==by_prime[1000000007]
    inv=by_prime[2147483647]
    assert (inv[(1,)*6][4],inv[(1,)*6][5])==(115,24)
    c4=character_from_invariants(inv,4)
    c5=character_from_invariants(inv,5)
    assert [c4[typ] for typ in TYPES]==EXPECTED4
    assert [c5[typ] for typ in TYPES]==EXPECTED5
    assert all(signed_fixed_chain_trace(typ)==c4[typ]-c5[typ] for typ in TYPES)
    d4=decompose(c4);d5=decompose(c5)
    assert d4=={'(5, 1)':1,'(4, 2)':2,'(4, 1, 1)':1,
     '(3, 3)':1,'(3, 2, 1)':3,'(3, 1, 1, 1)':1,
     '(2, 2, 2)':1,'(2, 2, 1, 1)':1,'(2, 1, 1, 1, 1)':1}
    assert d5=={'(5, 1)':1,'(4, 2)':1,'(4, 1, 1)':1}
    import json
    print(json.dumps({'face_counts':[len(BY_DIM[d]) for d in range(-1,7)],
     'conjugacy_types':[list(x) for x in TYPES],
     'character_degree_4':[c4[x] for x in TYPES],
     'character_degree_5':[c5[x] for x in TYPES],
     'specht_degree_4':d4,'specht_degree_5':d5,
     'cyclic_invariant_checks':examples,
     'primes':[2147483647,1000000007],
     'status':'D63_SYMMETRY_VERIFY_OK'},sort_keys=True,indent=2))

if __name__=='__main__':run()
