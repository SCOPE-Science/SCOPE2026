import itertools, json, pathlib
HERE=pathlib.Path(__file__).resolve().parent
cert=json.loads((HERE/'beat_sequence.json').read_text())
R_names=['c1','c2','c3','b1','b2','b3','a1','a2','a3']
R_covers=[('c1','b1'),('c2','b1'),('c1','b2'),('c2','b2'),('c3','b2'),('c2','b3'),('c3','b3'),
          ('b1','a1'),('b1','a2'),('b2','a1'),('b2','a3'),('b3','a2'),('b3','a3')]
def closure(names,covers):
    n=len(names); ix={x:i for i,x in enumerate(names)}
    le=[[False]*n for _ in range(n)]
    for i in range(n): le[i][i]=True
    for x,y in covers: le[ix[x]][ix[y]]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if le[i][k] and le[k][j]: le[i][j]=True
    return le
R_le=closure(R_names,R_covers)
C_le=[[i==j for j in range(4)] for i in range(4)]
for i in (0,1):
    for j in (2,3): C_le[i][j]=True
rels=[(i,j) for i in range(9) for j in range(9) if R_le[i][j]]
def mono(f): return all(C_le[f[i]][f[j]] for i,j in rels)
# Enumeration A: all functions, then exact order constraints.
maps_a=[f for f in itertools.product(range(4),repeat=9) if mono(f)]
# Enumeration B: recursive pruning by relations to already assigned vertices.
def enumerate_b():
    out=[]; f=[None]*9
    def rec(k):
        if k==9: out.append(tuple(f)); return
        for y in range(4):
            if all((not R_le[i][k] or C_le[f[i]][y]) for i in range(k)):
                f[k]=y; rec(k+1); f[k]=None
    rec(0); return out
maps_b=enumerate_b()
assert maps_a==maps_b
assert len(maps_a)==cert['map_count']==172
M=set(maps_a)
def lemap(f,g): return all(C_le[a][b] for a,b in zip(f,g))
up=down=0
for step in cert['deletions']:
    f=tuple(step['map']); w=tuple(step['witness'])
    assert f in M and w in M and f!=w
    if step['kind']=='up':
        U=[g for g in M if g!=f and lemap(f,g)]
        assert w in U and all(lemap(w,g) for g in U)
        up+=1
    elif step['kind']=='down':
        L=[g for g in M if g!=f and lemap(g,f)]
        assert w in L and all(lemap(g,w) for g in L)
        down+=1
    else: raise AssertionError(step['kind'])
    M.remove(f)
final={tuple(x) for x in cert['final_maps']}
assert M==final
assert M=={(k,)*9 for k in range(4)}
# The induced order on constants is exactly the four-point circle order.
fm=sorted(M)
for i in range(4):
    for j in range(4):
        assert lemap((i,)*9,(j,)*9)==C_le[i][j]
# Dual source has the same map count, and its mapping poset is order-dual via target order reversal.
Rop=[[R_le[j][i] for j in range(9)] for i in range(9)]
rels_op=[(i,j) for i in range(9) for j in range(9) if Rop[i][j]]
def mono_op(f): return all(C_le[f[i]][f[j]] for i,j in rels_op)
maps_op=[f for f in itertools.product(range(4),repeat=9) if mono_op(f)]
assert len(maps_op)==172
# order-reversing involution theta on C: minima 0,1 < maxima 2,3; choose 0<->2, 1<->3.
theta={0:2,1:3,2:0,3:1}
transformed={tuple(theta[x] for x in f) for f in maps_op}
assert transformed==set(maps_a)
print(f"VERIFY_OK maps=172 deletions={len(cert['deletions'])} up={up} down={down} core=4 constants dual_maps={len(maps_op)}")
