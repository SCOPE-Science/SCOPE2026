from itertools import combinations, product
from collections import Counter

# F4 = F2[w]/(w^2+w+1), encoded by two bits.
def fmul(a,b):
    a0,a1=a&1,(a>>1)&1
    b0,b1=b&1,(b>>1)&1
    return ((a0*b0)^(a1*b1)) | (((a0*b1)^(a1*b0)^(a1*b1))<<1)

def fpow(a,n):
    r=1
    while n:
        if n&1: r=fmul(r,a)
        a=fmul(a,a)
        n//=2
    return r

def finv(a):
    assert a
    return fpow(a,2)

alpha=2
assert fpow(alpha,3)==1 and alpha!=1

def vadd(x,y):
    return tuple(a^b for a,b in zip(x,y))

def vscale(a,x):
    return tuple(fmul(a,b) for b in x)

class G48:
    def __init__(self):
        self.V=list(product(range(4),repeat=2))
        self.zero=(0,0)
        self.elts=[(v,a) for v in self.V for a in range(3)]
        self.idx={g:i for i,g in enumerate(self.elts)}
        N=len(self.elts)
        self.tab=[[0]*N for _ in range(N)]
        for i,x in enumerate(self.elts):
            for j,y in enumerate(self.elts):
                self.tab[i][j]=self.idx[self.mul(x,y)]
        e=self.idx[(self.zero,0)]
        self.inv=[0]*N
        for i in range(N):
            for j in range(N):
                if self.tab[i][j]==e and self.tab[j][i]==e:
                    self.inv[i]=j
                    break

    def mul(self,x,y):
        v,a=x
        w,b=y
        return (vadd(v,vscale(fpow(alpha,a),w)),(a+b)%3)

    def closure_size(self,gens):
        N=len(self.elts)
        gs=list(gens)+[self.inv[g] for g in gens]
        e=self.idx[(self.zero,0)]
        seen=[False]*N
        seen[e]=True
        queue=[e]
        pos=0
        while pos<len(queue):
            x=queue[pos]
            pos+=1
            row=self.tab[x]
            for g in gs:
                y=row[g]
                if not seen[y]:
                    seen[y]=True
                    queue.append(y)
        return len(queue)

    def linearly_independent(self,v,w):
        if not any(v) or not any(w):
            return False
        return all(vscale(c,v)!=w for c in (1,2,3))

    def complement_label(self,x):
        v,a=x
        assert a
        c=fpow(alpha,a)^1
        return vscale(finv(c),v)

    def predicted_adj(self,x,y):
        vx,ax=x
        vy,ay=y
        if x==(self.zero,0) or y==(self.zero,0):
            return False
        if ax==0 and ay==0:
            return self.linearly_independent(vx,vy)
        if (ax==0)!=(ay==0):
            v=vx if ax==0 else vy
            return any(v)
        return self.complement_label(x)!=self.complement_label(y)

G=G48()
N=len(G.elts)
assert N==48

# Reconstruct adjacency from all minimum generating triples.
adj=set()
for tri in combinations(range(N),3):
    if G.closure_size(tri)==N:
        for i,j in combinations(tri,2):
            adj.add((i,j))

for i,j in combinations(range(N),2):
    assert ((i,j) in adj)==G.predicted_adj(G.elts[i],G.elts[j])

degrees=[]
for i in range(N):
    degrees.append(sum((min(i,j),max(i,j)) in adj for j in range(N) if j!=i))
assert Counter(degrees)==Counter({45:32,44:15,0:1})

# Kernel projective-line parts.
kernel=[x for x in G.elts if x[1]==0 and x[0]!=G.zero]
lines={}
for x in kernel:
    v=x[0]
    key=frozenset(vscale(c,v) for c in (1,2,3))
    lines.setdefault(key,[]).append(x)
assert len(lines)==5 and all(len(P)==3 for P in lines.values())

# Conjugate-complement parts.
outside=[x for x in G.elts if x[1]!=0]
parts={}
for x in outside:
    parts.setdefault(G.complement_label(x),[]).append(x)
assert len(parts)==16 and all(len(P)==2 for P in parts.values())

print("VERIFY_OK")
