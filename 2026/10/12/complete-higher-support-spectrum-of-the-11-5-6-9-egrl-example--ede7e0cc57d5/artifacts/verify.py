from itertools import combinations, product
from collections import Counter

# GF(9)=GF(3)[w]/(w^2-w-1); elements a+3b represent a+bw.
def add(x,y): return ((x%3+y%3)%3)+3*(((x//3)+(y//3))%3)
def mul(x,y):
    a,b=x%3,x//3; c,d=y%3,y//3
    return ((a*c+b*d)%3)+3*((a*d+b*c+b*d)%3)
def fpow(x,n):
    r=1
    while n:
        if n&1: r=mul(r,x)
        x=mul(x,x); n//=2
    return r
# multiplication/addition lookup tables
ADD=[[add(a,b) for b in range(9)] for a in range(9)]
MUL=[[mul(a,b) for b in range(9)] for a in range(9)]

def generator(p):
    return [
        [1,1,1,1,1,1,1,1,0,0,2],
        [1,fpow(p,1),fpow(p,2),fpow(p,3),2,fpow(p,5),fpow(p,6),fpow(p,7),0,0,0],
        [1,fpow(p,2),2,fpow(p,6),1,fpow(p,2),2,fpow(p,6),0,0,0],
        [1,fpow(p,3),fpow(p,6),fpow(p,1),2,fpow(p,7),fpow(p,2),fpow(p,5),1,1,0],
        [1,2,1,2,1,2,1,2,2,1,0],
    ]

def msg_index(v):
    z=0; p=1
    for x in v:
        z += x*p; p*=9
    return z

def support_masks(G):
    out=[0]*(9**5)
    weight=Counter()
    idx=0
    for v in product(range(9),repeat=5):
        mask=0
        for j in range(11):
            s=0
            for i in range(5): s=ADD[s][MUL[v[i]][G[i][j]]]
            if s: mask |= 1<<j
        out[msg_index(v)]=mask
        weight[mask.bit_count()]+=1
        idx+=1
    assert idx==9**5
    return out,weight

def rref_row_indices(n,r,q=9):
    for piv in combinations(range(n),r):
        nonp=[j for j in range(n) if j not in piv]
        slots=[]
        for j in nonp:
            for i,pi in enumerate(piv):
                if pi<j: slots.append((i,j))
        for vals in product(range(q),repeat=len(slots)):
            rows=[[0]*n for _ in range(r)]
            for i,pi in enumerate(piv): rows[i][pi]=1
            for (i,j),v in zip(slots,vals): rows[i][j]=v
            yield tuple(msg_index(row) for row in rows)

def spectrum(masks,r):
    c=Counter()
    for rows in rref_row_indices(5,r):
        u=0
        for z in rows: u |= masks[z]
        c[u.bit_count()]+=1
    return c

def gaussian(n,r,q):
    num=den=1
    for i in range(r):
        num*=q**(n-i)-1; den*=q**(r-i)-1
    return num//den

expected_w=Counter({0:1,6:224,7:1520,8:4880,9:14040,10:22240,11:16144})
expected={
 1:Counter({6:28,7:190,8:610,9:1755,10:2780,11:2018}),
 2:Counter({8:165,9:4510,10:72567,11:528000}),
 3:Counter({9:55,10:8910,11:596277}),
 4:Counter({10:11,11:7370}),
 5:Counter({11:1}),
}
w=3
for e in (1,3,5,7):
    p=fpow(w,e)
    G=generator(p)
    masks,ow=support_masks(G)
    assert ow==expected_w,(e,ow)
    for r in range(1,6):
        sp=spectrum(masks,r)
        assert sp==expected[r],(e,r,sp)
        assert sum(sp.values())==gaussian(5,r,9)
print('ORDINARY_WEIGHT_ENUMERATOR',dict(sorted(expected_w.items())))
print('SUBCODE_SUPPORT_SPECTRA',{r:dict(sorted(expected[r].items())) for r in range(1,6)})
print('GENERALIZED_HAMMING_WEIGHTS',[min(expected[r]) for r in range(1,6)])
print('MIN_SUPPORT_SUBCODE_COUNTS',[expected[r][min(expected[r])] for r in range(1,6)])
print('PRIMITIVE_CHOICES_CHECKED',4)
print('VERIFY_OK')
