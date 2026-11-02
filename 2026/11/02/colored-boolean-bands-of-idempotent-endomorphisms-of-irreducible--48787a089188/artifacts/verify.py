"""Finite-field checks for commuting idempotent endomorphisms of affine Frobenius groups."""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, p, f, modulus):
        self.p, self.f, self.q, self.modulus = p, f, p**f, modulus
    def digits(self, a):
        out=[]
        for _ in range(self.f):
            out.append(a%self.p);a//=self.p
        return out
    def number(self, ds):
        return sum((v%self.p)*(self.p**i) for i,v in enumerate(ds[:self.f]))
    def add(self,a,b):
        return self.number([(x+y)%self.p for x,y in zip(self.digits(a),self.digits(b))])
    def neg(self,a):
        return self.number([-x for x in self.digits(a)])
    def mul(self,a,b):
        u=self.digits(a);v=self.digits(b)
        c=[0]*(2*self.f-1)
        for i in range(self.f):
            for j in range(self.f):c[i+j]=(c[i+j]+u[i]*v[j])%self.p
        for k in range(len(c)-1,self.f-1,-1):
            z=c[k]
            for j in range(self.f):c[k-self.f+j]=(c[k-self.f+j]-z*self.modulus[j])%self.p
        return self.number(c)
    def pow(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out

def run_case(p,f,modulus,a,m,full):
    F=Field(p,f,modulus);q=F.q
    assert (q-1)%m==0 and F.pow(a,m)==1 and all(F.pow(a,d)!=1 for d in range(1,m))
    # The action must generate the full field over its prime field.
    span={F.number([(x if i==0 else 0) for i in range(f)]) for x in range(p)}
    z=1
    for _ in range(f):
        span.update([F.add(x,F.mul(c,z)) for x in tuple(span) for c in range(p)])
        z=F.mul(z,a)
    assert len(span)==q
    def mulG(x,y):
        v,i=x;w,j=y
        return (F.add(v,F.mul(F.pow(a,i),w)),(i+j)%m)
    def powerG(x,k):
        ans=(0,0)
        for _ in range(k):ans=mulG(ans,x)
        return ans
    def sub(x,y):return F.add(x,F.neg(y))
    eidx=[j for j in range(m) if j*j%m==j]
    r=len({d for d in range(2,m+1) if m%d==0 and all(d%h for h in range(2,int(d**0.5)+1))})
    assert len(eidx)==2**r
    # Reproducibility: derive the idempotents from the generator relations,
    # not from the claimed multiplication table.
    def phi(A,v,j,x):
        w,i=x
        return mulG((A[w],0),powerG((v,j),i))
    vals=[]
    if full:
        for basis_img in product(range(q),repeat=f):
            A=[]
            for x in range(q):
                d=F.digits(x);z=0
                for b,y in zip(d,basis_img):
                    for _ in range(b):z=F.add(z,y)
                A.append(z)
            for j in range(m):
                for v in range(q):
                    if powerG((v,j),m)!=(0,0):continue
                    if any(A[F.mul(a,x)]!=F.mul(F.pow(a,j),A[x]) for x in range(q)):continue
                    vals.append((tuple(A),v,j))
        assert len(vals)==1+q*(m-1)+f*q*(q-1),(p,f,m,len(vals))
    else:
        A0=tuple([0]*q)
        Aid=tuple(range(q))
        vals=[(A0,0,0),(Aid,0,1)]
        vals.extend((A0,F.mul(sub(1,F.pow(a,j)),c),j) for j in eidx if j for c in range(q))
    basis=[p**i for i in range(f)]
    e=[]
    for A,v,j in vals:
        if all(phi(A,v,j,phi(A,v,j,(x,0)))==phi(A,v,j,(x,0)) for x in basis) and phi(A,v,j,phi(A,v,j,(0,1)))==phi(A,v,j,(0,1)):
            e.append((A,v,j))
    assert len(e)==2+q*(2**r-1),(p,f,m,len(e),r)
    def compose_key(P,Q):
        A,v,j=P;B,w,k=Q
        return tuple(phi(A,v,j,phi(B,w,k,(x,0))) for x in basis)+(phi(A,v,j,phi(B,w,k,(0,1))),)
    def id_key(P):
        A,v,j=P
        return tuple(phi(A,v,j,(x,0)) for x in basis)+(phi(A,v,j,(0,1)),)
    keys={id_key(P):P for P in e}
    assert len(keys)==len(e)
    for P in e:
        for Q in e:
            assert compose_key(P,Q) in keys
            assert compose_key(P,keys[compose_key(P,Q)])==compose_key(P,Q)
            assert compose_key(keys[compose_key(P,Q)],P)==compose_key(P,Q)
    # Independently reconstruct the predicted labelled band.
    labels={}
    zero=next(P for P in e if P[2]==0)
    one=next(P for P in e if P[0]==tuple(range(q)))
    labels[id_key(zero)]=('zero',)
    labels[id_key(one)]=('one',)
    for j in eidx:
        if j==0:continue
        for c in range(q):
            v=F.mul(sub(1,F.pow(a,j)),c)
            target=next(P for P in e if P[2]==j and P[1]==v and P[0]==tuple([0]*q))
            labels[id_key(target)]=(c,j)
    assert len(labels)==len(e)
    for P in e:
        for Q in e:
            labP,labQ=labels[id_key(P)],labels[id_key(Q)]
            if labP[0]=='one':wanted=labQ
            elif labQ[0]=='one':wanted=labP
            elif 'zero' in (labP[0],labQ[0]):wanted=('zero',)
            else:
                c,j=labP;d,k=labQ;jk=(j*k)%m
                wanted=('zero',) if jk==0 else (c,jk)
            assert labels[compose_key(P,Q)]==wanted
    # Direct commutation graph, with full maximal-clique enumeration on small cases.
    graph={i:set() for i in range(len(e))}
    edge_count=0
    for i in range(len(e)):
        for j in range(i+1,len(e)):
            if compose_key(e[i],e[j])==compose_key(e[j],e[i]):
                graph[i].add(j);graph[j].add(i);edge_count+=1
    sizes=[len([k for k in range(len(e)) if k==i or k in graph[i]]) for i in range(len(e))]
    expected=[]
    for P in e:
        L=labels[id_key(P)]
        if len(L)==1: expected.append(len(e));continue
        c,j=L
        # Count the nonzero prime-power residues in the CRT support.
        mm=m;s=0
        for z in range(2,mm+1):
            if mm%z==0 and all(z%h for h in range(2,int(z**0.5)+1)):
                pp=z
                while mm%(pp*z)==0:pp*=z
                s+=(j%pp!=0)
        expected.append(2**r+1+(q-1)*(2**(r-s)-1))
    assert sizes==expected
    if len(e)<=60:
        maximal=[]
        def bron_kerbosch(R,P,X):
            if not P and not X:
                maximal.append(R)
                return
            pivot=max(P|X,key=lambda u:len(P & graph[u])) if P|X else None
            for v in tuple(sorted(P-(graph[pivot] if pivot is not None else set()))):
                bron_kerbosch(R|{v},P & graph[v],X & graph[v])
                P.remove(v);X.add(v)
        bron_kerbosch(set(),set(graph),set())
        pred=0
        # Stirling recursion with falling factorial.
        S=[[0]*(r+1) for _ in range(r+1)];S[0][0]=1
        for n in range(1,r+1):
            for b in range(1,n+1):S[n][b]=S[n-1][b-1]+b*S[n-1][b]
        fall=1
        for b in range(1,r+1):
            fall*=q-b+1
            pred+=S[r][b]*fall
        assert len(maximal)==pred==q**r,(len(maximal),pred,q**r)
        assert max(map(len,maximal))==2**r+1
        assert sum(len(c)==2**r+1 for c in maximal)==q
        profile=Counter()
        for coloring in product(range(q),repeat=r):
            multiplicities=Counter(coloring)
            size=2+sum(2**k-1 for k in multiplicities.values())
            profile[size]+=1
        assert Counter(map(len,maximal))==profile,(Counter(map(len,maximal)),profile)
    print('CASE_OK',p,f,m,'|End|',len(vals) if full else 'not_enumerated', '|E|',len(e),'omega',r,'edges',edge_count,'maximal_families',len(maximal) if len(e)<=60 else 'not_enumerated','sizes',sorted(profile.items()) if len(e)<=60 else [])

if __name__=='__main__':
    run_case(7,1,[0],3,6,True)
    run_case(2,2,[1,1],2,3,True)
    run_case(2,4,[1,1,0,0],2,15,False)
    print('VERIFY_OK')
