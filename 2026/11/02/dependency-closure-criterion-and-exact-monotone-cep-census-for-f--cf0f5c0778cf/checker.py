"""Exact monotone Boolean-frame CEP census and two independent decision procedures.
Python 3.10+; no third-party dependencies. Prints ALL_CHECKS_OK on success.
"""
from itertools import product, permutations
from collections import Counter

N=3
M=1<<N
FULL=M-1
UNIVERSE=range(M)

# Every monotone {0,1}^3 -> {0,1} truth table, evaluated at bitmask arguments.
SCALAR_TABLES=[tuple((mask>>s)&1 for s in UNIVERSE)
    for mask in range(1<<M)
    if all(not ((x & ~y)==0 and ((mask>>x)&1)) or ((mask>>y)&1)
       for x in UNIVERSE for y in UNIVERSE)]
assert len(SCALAR_TABLES)==20

# A direct congruence calculation independent of dependency graphs.
def respects_kernel(values, support, domain):
    return all((x^y)&~support or not ((values[x]^values[y])&~support)
               for x in domain for y in domain)

def direct_cep(values):
    global_kernels=[k for k in UNIVERSE if respects_kernel(values,k,UNIVERSE)]
    for singleton in [1,2,4]:
        pair=FULL^singleton
        sub=(0,singleton,pair,FULL)
        if any(values[x] not in sub for x in sub):
            continue
        for block in (singleton,pair):
            if not respects_kernel(values,block,sub):
                continue
            other=FULL^block
            if not any((k&block)==block and (k&other)!=other for k in global_kernels):
                return False
    return True

# Independent graph/partition test, generalized for any finite number of atoms.
def essential_graph(values, atoms):
    out=[0]*atoms
    for i in range(atoms):
        b=1<<i
        for x in range(1<<atoms):
            if x&b: continue
            delta=values[x]^values[x|b]
            for j in range(atoms):
                if delta>>j&1: out[i]|=1<<j
    return out

def closure(start,graph):
    seen=start
    while True:
        nxt=seen
        for i,edges in enumerate(graph):
            if seen>>i&1:nxt|=edges
        if nxt==seen:return seen
        seen=nxt

def graph_cep(values,atoms):
    allbits=(1<<atoms)-1
    g=essential_graph(values,atoms)
    # list of partitions using restricted-growth strings
    partitions=[]
    def rec(labels,maximum):
        if len(labels)==atoms:
            blocks=[0]*(maximum+1)
            for v,j in enumerate(labels):blocks[j]|=1<<v
            partitions.append(blocks)
            return
        for j in range(maximum+2):rec(labels+[j],max(maximum,j))
    rec([0],0)
    for blocks in partitions:
        k=len(blocks)
        if k==atoms or k==1:continue
        sets=[0]*(1<<k)
        for subset in range(1<<k):
            sets[subset]=sum(b for j,b in enumerate(blocks) if subset>>j&1)
        projection={bits:j for j,bits in enumerate(sets)}
        if any(values[bits] not in projection for bits in sets):continue
        fpi=[projection[values[bits]] for bits in sets]
        induced=essential_graph(fpi,k)
        for J in range(1<<k):
            if closure(J,induced)!=J:continue
            T=closure(sets[J],g)
            if any((J>>i&1)==0 and (T&block)==block for i,block in enumerate(blocks)):
                return False
    return True

def is_additive(v):
    return all(v[x|y]==(v[x]|v[y]) for x in UNIVERSE for y in UNIVERSE)

def is_closure(v):
    return v[0]==0 and all((x & v[x])==x and v[v[x]]==v[x] for x in UNIVERSE)
    # We separately know monotonicity of all enumerated maps.

perms=list(permutations(range(N)))
bit_perms=[]
for p in perms:
    bit_perms.append(tuple(sum((1<<p[j]) for j in range(N) if x>>j&1) for x in UNIVERSE))

def fixed_under(v,P):return all(P[v[x]]==v[P[x]] for x in UNIVERSE)

def orbits(v):
    forms=[]
    for P in bit_perms:
        inv={P[x]:x for x in UNIVERSE}
        forms.append(tuple(P[v[inv[x]]] for x in UNIVERSE))
    return min(forms)

COUNTS=Counter()
ORBITS=set()
fixed_all=Counter(); fixed_fail=Counter()
for hs in product(SCALAR_TABLES,repeat=N):
    v=tuple(sum((1<<j) for j,h in enumerate(hs) if h[x]) for x in UNIVERSE)
    c=direct_cep(v)
    assert c==graph_cep(v,N), (v,c)
    additive=is_additive(v)
    normal=v[0]==0
    close=is_closure(v)
    COUNTS['all']+=1
    COUNTS['cep' if c else 'fail']+=1
    COUNTS[('normal',normal,'cep',c)]+=1
    COUNTS[('additive',additive,'cep',c)]+=1
    COUNTS[('closure',close,'cep',c)]+=1
    if not additive and c:COUNTS['nonadditive_cep']+=1
    ORBITS.add((orbits(v),c))
    for idx,P in enumerate(bit_perms):
        if fixed_under(v,P):
            fixed_all[idx]+=1
            if not c:fixed_fail[idx]+=1

assert COUNTS['all']==8000,COUNTS
assert (COUNTS['cep'],COUNTS['fail'])==(5249,2751),COUNTS
assert (COUNTS[('normal',True,'cep',True)],COUNTS[('normal',True,'cep',False)])==(4273,2586)
assert (COUNTS[('additive',True,'cep',True)],COUNTS[('additive',True,'cep',False)])==(729,0)
assert (COUNTS[('closure',True,'cep',True)],COUNTS[('closure',True,'cep',False)])==(32,13)
assert COUNTS['nonadditive_cep']==4520
assert (len(ORBITS),sum(not status for _,status in ORBITS))==(1440,492)
assert (sum(fixed_all.values())//6,sum(fixed_fail.values())//6)==(1440,492)
print('MONOTONE_TOTAL', COUNTS['all'])
print('CEP_PASS', COUNTS['cep'])
print('CEP_FAIL', COUNTS['fail'])
print('NORMAL_PASS_FAIL', COUNTS[('normal',True,'cep',True)], COUNTS[('normal',True,'cep',False)])
print('NONADDITIVE_CEP',COUNTS['nonadditive_cep'])
print('ORBIT_TOTAL_FAIL',len(ORBITS),sum(not s for _,s in ORBITS))
print('FIXED_ALL',tuple(fixed_all[i] for i in range(6)))
print('FIXED_FAIL',tuple(fixed_fail[i] for i in range(6)))
# Sanity: graph and direct tests also agree outside the monotone subclass.
import random
rng=random.Random(41753)
for trial in range(500):
    vals=tuple(rng.randrange(8) for _ in range(8))
    assert direct_cep(vals)==graph_cep(vals,3), vals
print('ALL_CHECKS_OK')
