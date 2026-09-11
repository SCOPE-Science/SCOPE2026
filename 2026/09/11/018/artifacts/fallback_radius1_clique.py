"""Fallback F1: kill radius-1 local Borel 7-rules via explicit pattern-graph clique.
Window W=B_1(e) (9 pts), 512 patterns. For fixed s: O = W cap s^-1 W (constraint
positions on p-side), J = sO cap W (constraint positions on q-side). Patterns
vanishing on O union J are pairwise s-consistent -> clique of size 2^(9-|OuJ|).
If >= 8 for some s, no radius-1 local rule with 7 colors exists."""
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def madj(M):
    a,b,c,d,e,f,g,h,i = M[0][0],M[0][1],M[0][2],M[1][0],M[1][1],M[1][2],M[2][0],M[2][1],M[2][2]
    return ((e*i-f*h,c*h-b*i,b*f-c*e),(f*g-d*i,a*i-c*g,c*d-a*f),(d*h-e*g,b*g-a*h,a*e-b*d))
def EE(i,j,v=1):
    M=[[0]*3 for _ in range(3)]
    for k in range(3): M[k][k]=1
    M[i][j]=v
    return tuple(tuple(r) for r in M)
I=((1,0,0),(0,1,0),(0,0,1))
g1=EE(0,1); g2=EE(1,0); g3=EE(1,2); g4=EE(2,1)
S=[g1,madj(g1),g2,madj(g2),g3,madj(g3),g4,madj(g4)]
names=['a','A','b','B','c','C','d','D']
W=[I]+S; pos={w:i for i,w in enumerate(W)}; setW=set(W)
for si,s in enumerate(S):
    sm=madj(s)
    O=[w for w in W if mm(s,w) in setW]          # W cap s^-1 W
    sO=[mm(s,w) for w in O]
    J=[w for w in sO if w in setW]               # sO cap W
    fixed=set(pos[w] for w in O)|set(pos[w] for w in J)
    free=[i for i in range(9) if i not in fixed]
    # explicit clique: all patterns supported on 'free'
    import itertools
    fam=[]
    for bits in itertools.product([0,1], repeat=len(free)):
        p=0
        for b,i in zip(bits,free):
            if b: p|=(1<<i)
        fam.append(p)
    # verify pairwise s-consistency: p[w]==q[sw] for w in O
    constr=[(pos[w],pos[mm(s,w)]) for w in O]
    ok=True
    for a in fam:
        for b in fam:
            if any(((a>>i)&1)!=((b>>j)&1) for i,j in constr):
                ok=False; break
        if not ok: break
    print(f"s={names[si]}: |O|={len(O)} |OuJ|={len(fixed)} clique_size={len(fam)} verified={ok}", flush=True)
