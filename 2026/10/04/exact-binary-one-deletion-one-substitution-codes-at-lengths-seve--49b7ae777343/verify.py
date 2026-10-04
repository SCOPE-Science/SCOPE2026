from itertools import combinations

def ball(w):
    n=len(w); out=set()
    for i in range(n):
        y=w[:i]+w[i+1:]
        out.add(y)
        for j in range(n-1):
            out.add(y[:j]+('1' if y[j]=='0' else '0')+y[j+1:])
    return frozenset(out)

def graph(n):
    W=[format(i,f'0{n}b') for i in range(1<<n)]
    B=[ball(w) for w in W]
    adj=[0]*len(W)
    for i in range(len(W)):
        for j in range(i+1,len(W)):
            if B[i].isdisjoint(B[j]):
                adj[i]|=1<<j; adj[j]|=1<<i
    return W,B,adj

def enumerate_cliques(adj,k):
    out=[]; N=len(adj)
    def rec(chosen,cand,need):
        if need==0:
            out.append(tuple(chosen)); return
        while cand.bit_count()>=need:
            l=cand & -cand; v=l.bit_length()-1; cand ^= l
            rec(chosen+[v], cand & adj[v], need-1)
    rec([], (1<<N)-1, k)
    return out

def transform(w,k):
    if k&2: w=w[::-1]
    if k&1: w=''.join('1' if c=='0' else '0' for c in w)
    return w

def canon(words):
    return min(tuple(sorted(transform(w,k) for w in words)) for k in range(4))

# n=7: exhibit size 3 and exclude 4.
W7,B7,A7=graph(7)
w7=('0010110','1110000','1111111')
idx7=[W7.index(w) for w in w7]
assert all(B7[i].isdisjoint(B7[j]) for i,j in combinations(idx7,2))
C4=enumerate_cliques(A7,4)
assert C4==[]

# n=8: enumerate every size-5 code and exclude size 6 by extension.
W8,B8,A8=graph(8)
C5=enumerate_cliques(A8,5)
assert len(C5)==12
for c in C5:
    common=(1<<len(W8))-1
    for v in c: common &= A8[v]
    assert common==0
    words=tuple(W8[v] for v in c)
    assert '00000000' in words and '11111111' in words
canons={canon(tuple(W8[v] for v in c)) for c in C5}
assert len(canons)==4
sizes={c:0 for c in canons}
for C in C5: sizes[canon(tuple(W8[v] for v in C))]+=1
assert sorted(sizes.values())==[2,2,4,4]
reps=sorted(canons)
expected=[
('00000000','00001111','01110001','11001100','11111111'),
('00000000','00010111','01110001','11001100','11111111'),
('00000000','00011011','01111000','11000110','11111111'),
('00000000','00011011','10111000','11000110','11111111')]
assert reps==expected

print('DS_1,2(7)=3')
print('DS_1,2(8)=5')
print('optimal_length8_codes=12')
print('reversal_complement_orbits=4')
print('orbit_sizes=2,2,4,4')
for r in reps: print('REP',','.join(r))
print('VERIFY_OK')
