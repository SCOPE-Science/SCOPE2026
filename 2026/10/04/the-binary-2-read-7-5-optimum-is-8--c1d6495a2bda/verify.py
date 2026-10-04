from itertools import product, combinations
N=7
WORDS=[''.join(p) for p in product('01', repeat=N)]

def r2_sum(w):
    a=[0]+[int(c) for c in w]+[0]
    return tuple(a[i]+a[i+1] for i in range(N+1))

def r2_multi(w):
    a=[0]+[int(c) for c in w]+[0]
    return tuple(tuple(sorted((a[i],a[i+1]))) for i in range(N+1))

SUM=[r2_sum(w) for w in WORDS]
MUL=[r2_multi(w) for w in WORDS]
assert all(tuple(sum(t) for t in MUL[i])==SUM[i] for i in range(128))
def dist(i,j): return sum(a!=b for a,b in zip(SUM[i],SUM[j]))
def dist2(i,j): return sum(a!=b for a,b in zip(MUL[i],MUL[j]))
for i in range(128):
    for j in range(i): assert dist(i,j)==dist2(i,j)
ADJ=[0]*128
for i in range(128):
    for j in range(i):
        if dist(i,j)>=5:
            ADJ[i]|=1<<j; ADJ[j]|=1<<i

def color_sort(P):
    order=[]; bounds=[]; uncolored=P; color=0
    while uncolored:
        color+=1; avail=uncolored
        while avail:
            bit=avail & -avail; v=bit.bit_length()-1
            order.append(v); bounds.append(color)
            uncolored ^= bit
            avail &= ~bit
            avail &= ~ADJ[v]
    return order,bounds
best=[]
def expand(P,R):
    global best
    if not P:
        if len(R)>len(best): best=R[:]
        return
    order,bounds=color_sort(P)
    for k in range(len(order)-1,-1,-1):
        if len(R)+bounds[k] <= len(best): return
        v=order[k]; bit=1<<v
        if P & bit:
            expand(P & ADJ[v], R+[v])
            P ^= bit
expand((1<<128)-1,[])
max1=len(best)
# Independent Bron-Kerbosch maximal-clique enumeration, with a size upper bound.
max2=0; count2=0
def bk(rsize,P,X):
    global max2,count2
    if rsize+P.bit_count()<max2: return
    if not P and not X:
        if rsize>max2: max2=rsize; count2=1
        elif rsize==max2: count2+=1
        return
    U=P|X
    if U:
        u=max((i for i in range(128) if (U>>i)&1), key=lambda i:(P & ADJ[i]).bit_count())
        C=P & ~ADJ[u]
    else: C=P
    while C:
        bit=C & -C; v=bit.bit_length()-1
        bk(rsize+1,P & ADJ[v],X & ADJ[v])
        P ^= bit; X |= bit; C ^= bit
        if rsize+P.bit_count()<max2: return
bk(0,(1<<128)-1,0)
assert max1==max2==8
W=[WORDS[i] for i in best]
assert len(W)==8
for i,j in combinations(best,2): assert dist2(i,j)>=5
# Classical binary (7,3) comparison: Hamming bound <=16 and standard Hamming code achieves 16.
def syn(w):
    s=0
    for pos,c in enumerate(w,1):
        if c=='1': s ^= pos
    return s
H=[w for w in WORDS if syn(w)==0]
assert len(H)==16
for a,b in combinations(H,2): assert sum(x!=y for x,y in zip(a,b))>=3
assert 16*(1+N)==2**N
print('READ_GRAPH_VERTICES 128')
print('MAX_2READ_7_5 8')
print('SECOND_EXACT_MAX 8')
print('MAXIMAL_CLIQUES_OF_MAX_SIZE',count2)
print('WITNESS',' '.join(W))
print('CLASSICAL_7_3_MAX 16')
print('VERIFY_OK')
