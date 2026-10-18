"""Exact induced-forest filtration and persistence check (standard library only).

Vertices of K_2 x K_3 x K_3 are ordered lexicographically. The complex
contains all vertex sets inducing a forest of maximum degree at most d.
Integer chain computations use deterministic acyclic matching and signed
Morse boundaries; persistence ranks are proved by nonzero modular minors.
"""
import json
from itertools import product
from collections import Counter, defaultdict, deque
from functools import lru_cache

VERTICES=list(product(range(2),range(3),range(3)))
N=len(VERTICES)
ADJ=[sum(1<<j for j,y in enumerate(VERTICES)
         if all(x[t]!=y[t] for t in range(3))) for x in VERTICES]

def forest(s):
    p=list(range(N))
    def root(i):
        while i!=p[i]:i=p[i]
        return i
    for i in range(N):
        if not (s>>i)&1:continue
        t=ADJ[i]&s&~((1<<(i+1))-1)
        while t:
            b=t&-t;t-=b;j=b.bit_length()-1
            a,c=root(i),root(j)
            if a==c:return False
            p[c]=a
    return True

def enumerated(d):
    return [s for s in range(1<<N) if all((ADJ[i]&s).bit_count()<=d
                for i in range(N) if (s>>i)&1) and forest(s)]

def boundary(s):
    i=0
    while s:
        b=s&-s;s-=b
        yield b,1 if i%2==0 else -1
        i+=1

def rank_mod(vectors,p):
    basis={}
    for vector in vectors:
        x={k:v%p for k,v in vector.items() if v%p}
        while x:
            z=min(x)
            if z not in basis:
                a=pow(x[z],-1,p)
                basis[z]={u:(q*a)%p for u,q in x.items()}
                break
            a=x[z]
            for u,q in basis[z].items():
                y=(x.get(u,0)-a*q)%p
                if y:x[u]=y
                else:x.pop(u,None)
    return len(basis)

class Reduction:
    def __init__(self,d):
        self.d=d;self.faces=enumerated(d);unpaired=set(self.faces)
        self.lower={};self.upper={}
        for i in range(N):
            for s in self.faces:
                t=s|(1<<i)
                if s in unpaired and t!=s and t in unpaired:
                    unpaired.remove(s);unpaired.remove(t)
                    self.lower[s]=t;self.upper[t]=s
        self.critical=unpaired
        self.crit={k:sorted(s for s in unpaired if s.bit_count()-1==k)
                   for k in range(-1,12)}
        self.ord={}
        for k in range(0,12):self.matched_dag(k)
    def matched_dag(self,k):
        if k in self.ord:return self.ord[k]
        lowers={s:t for s,t in self.lower.items() if s.bit_count()==k}
        degree={s:0 for s in lowers};nextfaces={}
        for s,u in lowers.items():
            aa=[]
            for bit,sgn in boundary(u):
                t=u^bit
                if t in lowers and t!=s:
                    aa.append((t,sgn));degree[t]+=1
            nextfaces[s]=aa
        q=deque(s for s in sorted(degree) if degree[s]==0)
        topo=[]
        while q:
            s=q.popleft();topo.append(s)
            for t,_ in nextfaces[s]:
                degree[t]-=1
                if degree[t]==0:q.append(t)
        assert len(topo)==len(lowers),(self.d,k,'closed V-path')
        self.ord[k]=(lowers,nextfaces,topo)
        return self.ord[k]
    @lru_cache(None)
    def project(self,s):
        if s in self.critical:return {s:1}
        if s in self.upper:return {}
        u=self.lower[s]
        bit=u^s
        inc=(-1 if (u&(bit-1)).bit_count()%2 else 1)
        out=defaultdict(int)
        for b,sgn in boundary(u):
            t=u^b
            if t==s:continue
            for z,a in self.project(t).items():out[z]-=inc*sgn*a
        return {z:a for z,a in out.items() if a}
    def morse_boundary(self,k):
        out=[]
        for s in self.crit[k]:
            col=defaultdict(int)
            for bit,sgn in boundary(s):
                for z,a in self.project(s^bit).items():col[z]+=sgn*a
            out.append({z:a for z,a in col.items() if a})
        return out
    def lift_cycle(self,k,s):
        low,arrows,order=self.matched_dag(k)
        row=defaultdict(int)
        for b,a in boundary(s):
            if (s^b) in low:row[s^b]+=a
        chain={s:1}
        for t in order:
            if row[t]==0:continue
            u=low[t]
            pivot_bit=u^t
            piv=-1 if (u&(pivot_bit-1)).bit_count()%2 else 1
            delta=-row[t]*piv
            chain[u]=chain.get(u,0)+delta
            if chain[u]==0:del chain[u]
            row[t]=0
            for z,a in arrows[t]:row[z]+=delta*a
        # Complete signed cycle check, not merely matched lower rows.
        bd=defaultdict(int)
        for q,a in chain.items():
            for bit,c in boundary(q):bd[q^bit]+=a*c
        assert all(a==0 for a in bd.values()),(self.d,k,s)
        return chain

def smith_unit_elimination(columns):
    # Use unit elementary row/column operations, with no division.
    # Suffices when all nonzero Smith factors are units as below.
    cols=[dict(c) for c in columns]
    count=0
    while True:
        pivot=None
        for j,c in enumerate(cols):
            for i,a in sorted(c.items()):
                if abs(a)==1:
                    pivot=(i,j,a);break
            if pivot:break
        if pivot is None:break
        i,j,a=pivot
        col=cols.pop(j)
        for c in cols:
            val=c.pop(i,0)
            if val:
                for r,x in col.items():
                    if r==i:continue
                    y=c.get(r,0)-val*a*x
                    if y:c[r]=y
                    else:c.pop(r,None)
        count+=1
    assert not any(cols),('nonunit residual',len(cols))
    return count

def homology(R):
    D={k:R.morse_boundary(k) for k in range(12)}
    # ∂² = 0 over the integers.
    for k in range(1,12):
        prev={s:c for s,c in zip(R.crit[k-1],D[k-1])}
        for col in D[k]:
            sums=defaultdict(int)
            for s,a in col.items():
                for t,b in prev[s].items():sums[t]+=a*b
            assert not any(sums.values()),('boundary-squared',R.d,k)
    rr={k:smith_unit_elimination(D[k]) for k in D}
    bet={k:len(R.crit[k])-rr[k]-rr.get(k+1,0) for k in range(11)}
    return D,{str(k):v for k,v in bet.items() if v},{str(k):v for k,v in rr.items() if v}

def persistence(A,B,k,Db):
    vectors=[];cycle_lengths=[]
    for s in A.crit[k]:
        chain=A.lift_cycle(k,s)
        cycle_lengths.append(len(chain))
        image=defaultdict(int)
        for t,a in chain.items():
            for q,b in B.project(t).items():image[q]+=a*b
        vectors.append({q:a for q,a in image.items() if a})
    p=1000000007
    r=rank_mod(vectors+Db[k+1],p)-rank_mod(Db[k+1],p)
    r2=rank_mod(vectors+Db[k+1],1000003)-rank_mod(Db[k+1],1000003)
    assert r==r2
    assert r==len(A.crit[k]),('noninjective',A.d,B.d,k,r)
    return {'source':A.d,'target':B.d,'degree':k,'rank':r,
            'cycle_chain_min':min(cycle_lengths),'cycle_chain_max':max(cycle_lengths)}

def run():
    reductions={d:Reduction(d) for d in range(5)}
    results={};Ds={}
    for d,R in reductions.items():
        D,bet,rank=homology(R);Ds[d]=D
        results[str(d)]={'faces':len(R.faces),
          'f_vector':{str(k):v for k,v in sorted(Counter(s.bit_count()-1 for s in R.faces).items())},
          'critical':{str(k):len(x) for k,x in R.crit.items() if x},
          'smith_unit_ranks':rank,'reduced_betti':bet}
    expect=[{'3':14},{'5':17},{'7':17,'8':36,'9':6},
            {'8':199,'9':6},{'8':217,'9':6}]
    assert [results[str(d)]['reduced_betti'] for d in range(5)]==expect
    inc=[persistence(reductions[a],reductions[b],k,Ds[b])
         for a,b,k in ((2,3,8),(2,3,9),(3,4,8),(3,4,9))]
    assert [x['rank'] for x in inc]==[36,6,199,6]
    result={'vertex_count':N,'edge_count':sum(a.bit_count() for a in ADJ)//2,
            'complexes':results,'inclusions':inc,
            'rational_barcodes':[
             {'degree':3,'birth':0,'death':1,'multiplicity':14},
             {'degree':5,'birth':1,'death':2,'multiplicity':17},
             {'degree':7,'birth':2,'death':3,'multiplicity':17},
             {'degree':8,'birth':2,'death':None,'multiplicity':36},
             {'degree':8,'birth':3,'death':None,'multiplicity':163},
             {'degree':8,'birth':4,'death':None,'multiplicity':18},
             {'degree':9,'birth':2,'death':None,'multiplicity':6}]}
    print(json.dumps(result,indent=2,sort_keys=True))
    return result
if __name__=='__main__':run()
