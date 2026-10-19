"""Independent complete enumeration from BCH root parity-check equations.
The checks use GF(32)=GF(2)[t]/(t^5+t^2+1) and root exponents 1,3,5.
"""
from collections import Counter

N=31
GF_MOD=0b100101

def mul(a,b):
    c=0
    while b:
        if b&1: c^=a
        b>>=1; a<<=1
        if a&32: a^=GF_MOD
    return c

powers=[1]
for i in range(1,N):powers.append(mul(powers[-1],2))
assert len(set(powers))==N and mul(powers[-1],2)==1

cols=[]
for j in range(N):
    cols.append(powers[j] | (powers[(3*j)%N]<<5) | (powers[(5*j)%N]<<10))


# Independent polynomial-root verification of the defining BCH code.
def eval_polynomial(poly, at):
    val=0
    for i in range(poly.bit_length()-1,-1,-1):
        val=mul(val,at)^((poly>>i)&1)
    return val

def poly_multiply(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1; b>>=1
    return r

def poly_remainder(a,b):
    while a and a.bit_length()>=b.bit_length():
        a^=b<<(a.bit_length()-b.bit_length())
    return a

min_factors=[(0x25,1),(0x3d,3),(0x37,5)]
g=1
for f,e in min_factors:
    assert f.bit_length()==6 and eval_polynomial(f,powers[e])==0
    for k in range(1,5):
        assert eval_polynomial(f,powers[(e*(1<<k))%31])==0
    g=poly_multiply(g,f)
assert g==0x8faf and poly_remainder((1<<31)|1,g)==0
print('BCH_GENERATOR_OK g=0x8faf factors=(0x25,0x3d,0x37)',file=__import__('sys').stderr)

# Exhaustive finite rank lemma: no two disjoint nine-coordinate zero runs
# in a nonzero codeword. Translation takes the first run to 0..8.
def binary_rank(vectors):
    pivots={}
    for x in vectors:
        while x:
            i=x.bit_length()-1
            if i not in pivots:
                pivots[i]=x
                break
            x^=pivots[i]
    return len(pivots)

for start in range(9,23):
    forced_zero=set(range(9))|set(range(start,start+9))
    remaining=[j for j in range(N) if j not in forced_zero]
    assert len(remaining)==13 and binary_rank([cols[j] for j in remaining])==13
print('TWO_DISJOINT_NINE_ZERO_RUNS_IMPOSSIBLE 14_full_rank_cases',file=__import__('sys').stderr)

rows=[]
for i in range(15):
    rows.append(sum(((col>>i)&1)<<j for j,col in enumerate(cols)))

pivot=[]
rank=0
for j in range(N):
    pos=next((p for p in range(rank,15) if (rows[p]>>j)&1),None)
    if pos is None:continue
    rows[rank],rows[pos]=rows[pos],rows[rank]
    for i in range(15):
        if i!=rank and (rows[i]>>j)&1: rows[i]^=rows[rank]
    pivot.append(j)
    rank+=1
    if rank==15:break
assert rank==15
free=[j for j in range(N) if j not in pivot]
assert len(free)==16

hist=[Counter() for _ in range(N+1)]
seen=set()
for msg in range(1<<16):
    w=sum(((msg>>k)&1)<<j for k,j in enumerate(free))
    for j,row in zip(pivot,rows):
        w |= ((w&row).bit_count()&1)<<j
    assert w not in seen
    seen.add(w)
    syndrome=0
    for j in range(N):
        if (w>>j)&1:syndrome^=cols[j]
    assert syndrome==0
    if not w:
        for b in range(1,N+1):hist[b][0]+=1
        continue
    ones=[j for j in range(N) if (w>>j)&1]
    gaps=[(ones[(i+1)%len(ones)]-ones[i]-1)%N for i in range(len(ones))]
    zero_windows=[0]*(N+1)
    for gap in gaps:
        for b in range(1,gap+1):
            zero_windows[b]+=gap-b+1
    for b in range(1,N+1):
        hist[b][N-zero_windows[b]]+=1

assert len(seen)==65536
for b in range(1,N+1):
    assert sum(hist[b].values())==65536 and hist[b][0]==1
    print(f'{b}:'+''.join(f'{w}={hist[b][w]},' for w in sorted(hist[b])))
print('ROOT_SYNDROME_CENSUS_OK words=65536 rank=15 root_exponents=(1,3,5)',file=__import__('sys').stderr)
