"""Exact sparse linear-syzygy checks for multi-leg spider Hilbert tangent characters.

For each monomial-ideal generator, an unknown image in its finite quotient
basis is assigned. Pair-lcm syzygies generate all monomial-ideal relations.
The script computes weight-by-weight nullity over a prime field; it does not
assume the proposed character when constructing or reducing the system.
"""
from collections import Counter, defaultdict
from itertools import combinations

P = 1000003

def add(u,v): return tuple(a+b for a,b in zip(u,v))
def sub(u,v): return tuple(a-b for a,b in zip(u,v))

def setup(exponents):
    r=len(exponents)
    zero=(0,)*r
    basis=[zero]
    for i,a in enumerate(exponents):
        for k in range(1,a):
            e=[0]*r;e[i]=k;basis.append(tuple(e))
    gens=[]
    for i,a in enumerate(exponents):
        e=[0]*r;e[i]=a;gens.append(tuple(e))
    for i,j in combinations(range(r),2):
        e=[0]*r;e[i]=e[j]=1;gens.append(tuple(e))
    return basis,gens

def rank_rows(rows):
    pivots={}
    for row0 in rows:
        row={k:v%P for k,v in row0.items() if v%P}
        while row:
            p=min(row)
            if p not in pivots:
                inv=pow(row[p],-1,P)
                pivots[p]={k:(v*inv)%P for k,v in row.items()}
                break
            fac=row[p]
            for k,v in pivots[p].items():
                new=(row.get(k,0)-fac*v)%P
                if new: row[k]=new
                else: row.pop(k,None)
    return len(pivots)

def compute_character(exponents):
    basis,gens=setup(exponents)
    n=len(basis)
    weight_vars=defaultdict(list)
    for gi,g in enumerate(gens):
        for mi,m in enumerate(basis):
            weight_vars[sub(m,g)].append(gi*n+mi)
    weight_rows=defaultdict(list)
    for gi,gj in combinations(range(len(gens)),2):
        g,h=gens[gi],gens[gj]
        lcm=tuple(max(a,b) for a,b in zip(g,h))
        left=sub(lcm,g);right=sub(lcm,h)
        for target in basis:
            row={}
            for sign,gen_id,mult in ((1,gi,left),(-1,gj,right)):
                for mi,m in enumerate(basis):
                    if add(m,mult)==target:
                        pos=gen_id*n+mi
                        row[pos]=row.get(pos,0)+sign
            row={k:v for k,v in row.items() if v}
            if row:
                weights={sub(basis[pos%n],gens[pos//n]) for pos in row}
                assert len(weights)==1,('weight mismatch',row,weights)
                weight_rows[next(iter(weights))].append(row)
    result=Counter()
    for w,vars_at_w in weight_vars.items():
        rank=rank_rows(weight_rows[w])
        nullity=len(vars_at_w)-rank
        assert nullity>=0
        if nullity:result[w]=nullity
    return result

def derivation_image_character(exponents):
    """Compute rank of Der(S,A) -> Hom_S(I,A), not by dimension subtraction."""
    basis, gens=setup(exponents)
    r=len(exponents); n=len(basis)
    index={m:k for k,m in enumerate(basis)}
    matrices=defaultdict(list)
    for i in range(r):
        ei=[0]*r;ei[i]=1;ei=tuple(ei)
        for monom in basis:
            weight=sub(monom,ei)
            vector={}
            for gid,g in enumerate(gens):
                if g[i]==0:continue
                exp=list(g);exp[i]-=1
                product=add(tuple(exp),monom)
                if product in index:
                    coord=gid*n+index[product]
                    vector[coord]=g[i]
            matrices[weight].append(vector)
    return Counter({w:rank_rows(cols) for w,cols in matrices.items()})

def closed_character(exponents):
    r=len(exponents)
    char=Counter()
    gens=[]
    for i,a in enumerate(exponents):
        x=[0]*r;x[i]=a;g=tuple(x)
        for j,b in enumerate(exponents):
            if i==j:
                monoms=range(1,b)
            else:
                monoms=[b-1]
            for t in monoms:
                v=[0]*r;v[j]=t
                char[sub(v,g)]+=1
    for i,j in combinations(range(r),2):
        g=[0]*r;g[i]=g[j]=1
        for k,b in enumerate(exponents):
            ts=range(1,b) if k in (i,j) else [b-1]
            for t in ts:
                v=[0]*r;v[k]=t
                char[sub(v,tuple(g))]+=1
    return char

def check(exponents):
    observed=compute_character(exponents)
    predicted=closed_character(exponents)
    assert observed==predicted,(exponents,observed-predicted,predicted-observed)
    n=1+sum(a-1 for a in exponents)
    r=len(exponents)
    dim=sum(observed.values())
    excess=r*(r-2)*(r+1)//2
    assert dim==r*n+excess,(dim,r*n+excess)
    deriv_rank=derivation_image_character(exponents)
    der_span=sum(deriv_rank.values())
    t1_char=observed.copy()
    for w,val in deriv_rank.items():
        t1_char[w]-=val
        assert t1_char[w]>=0
    t1_dim=sum(t1_char.values())
    predicted_t1=n-1+r*(r*r+r-4)//2
    assert t1_dim==predicted_t1,(exponents,t1_dim,predicted_t1)
    print('CHECK',{'legs':exponents,'length':n,'tangent_dim':dim,'excess':excess,'weight_types':len(observed),'T1_dim':t1_dim})
    return observed

if __name__=='__main__':
    for legs in ((2,2,2),(8,8,8),(2,2,2,2),(2,3,4,5),(3,3,3,3),(2,2,2,2,2),(2,3,2,4,2)):
        check(legs)
    print('VERIFY_OK')
