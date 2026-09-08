import itertools, json
# GL2(F2): 2x2 bits row-major [a,b,c,d], det=1
G2=[(a,b,c,d) for a,b,c,d in itertools.product([0,1],repeat=4) if (a*d^b*c)==1]
print('G2',len(G2))
# GL3(F2): 9 bits
def det3(m):
    a,b,c,d,e,f,g,h,i=m
    return (a*(e*i^f*h)^b*(d*i^f*g)^c*(d*h^e*g))&1
G3=[m for m in itertools.product([0,1],repeat=9) if det3(m)==1]
print('G3',len(G3))
# precompute combined 6-bit action tables: matrix 3x2 bits: rows r0=r0c0+2*r0c1, index = r0+4*r1+16*r2
def left_apply(h, x):
    r=[x&3,(x>>2)&3,(x>>4)&3]
    o=[]
    for i in range(3):
        v=0
        for j in range(3):
            if h[i*3+j]:
                v^=r[j]
        o.append(v)
    return o[0]+4*o[1]+16*o[2]
def right_apply(g, x):
    # g = gi (2x2), each row w (2 bits: w0+w1*2 as row vector) -> w*g
    a,b,c,d=g
    o=0
    for i in range(3):
        w=(x>>(2*i))&3
        w0=w&1; w1=(w>>1)&1
        n0=w0*a^w1*c; n1=w0*b^w1*d
        o|=(n0+2*n1)<<(2*i)
    return o
def matinv2(g):
    a,b,c,d=g; return (d,b,c,a)
G2i=[matinv2(g) for g in G2]
# combined tables P[(hi,giidx)][64]
P=[]
for h in G3:
    Lh=[left_apply(h,x) for x in range(64)]
    for gi in G2i:
        P.append([right_apply(gi,Lh[x]) for x in range(64)])
print('pairs',len(P))
N=1<<18
seen=bytearray(N)
def enc3(k0,k1,k2): return k0+64*k1+4096*k2
ncl=0; reps=[]
for x in range(N):
    if seen[x]: continue
    k0=x&63; k1=(x>>6)&63; k2=(x>>12)&63
    orb=set()
    for T in P:
        orb.add(enc3(T[k0],T[k1],T[k2]))
    for o in orb: seen[o]=1
    reps.append((x,len(orb),k0,k1,k2))
    ncl+=1
print('classes',ncl)
import collections
print(collections.Counter(s for _,s,_1,_2,_3 in reps))
json.dump({'n_classes':ncl,'reps':[[x,s,k0,k1,k2] for x,s,k0,k1,k2 in reps]},open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts/s7_enum23.json','w'))
