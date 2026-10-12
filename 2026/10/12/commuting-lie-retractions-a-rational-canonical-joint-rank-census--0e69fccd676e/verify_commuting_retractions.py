"""Reproduce finite-field commuting Lie retraction counts; no external packages."""
from itertools import product
from collections import Counter
from math import prod


def matmul(A,B,p):
    return [[sum(x*y for x,y in zip(row,col))%p for col in zip(*B)] for row in A]

def rank(A,p):
    A=[row[:] for row in A]; R=len(A); C=len(A[0]); i=0
    for j in range(C):
        pivot=next((k for k in range(i,R) if A[k][j]%p),None)
        if pivot is None: continue
        A[i],A[pivot]=A[pivot],A[i]
        inv=pow(A[i][j],-1,p); A[i]=[a*inv%p for a in A[i]]
        for k in range(R):
            if k==i:continue
            fac=A[k][j]%p
            if fac: A[k]=[(x-fac*y)%p for x,y in zip(A[k],A[i])]
        i+=1
        if i==R:break
    return i

def bracket(A,B,N,p):
    # A,B are coefficient arrays (t,v1,...), N is dxd matrix
    av=A[1:]; bv=B[1:]
    vv=[(A[0]*b-B[0]*a)%p for a,b in zip(av,bv)]
    return [0]+[sum(row[j]*vv[j] for j in range(len(vv)))%p for row in N]

def sample(p,r,ell,N_override=None):
    d=r*ell; n=d+1
    N=[[0]*d for _ in range(d)]
    for b in range(r):
        for i in range(ell):
            N[b*ell+i][b*ell+i]=1
            if i+1<ell:N[b*ell+i][b*ell+i+1]=1
    if N_override is not None:N=N_override
    units=[[int(i==j) for j in range(n)] for i in range(n)]
    zero=[0]*n
    generators=[units[i] for i in range(n)]
    # F matrix column conventions to test all n*n arrays
    valid=[]
    for flat in product(range(p),repeat=n*n):
        M=[list(flat[i*n:(i+1)*n]) for i in range(n)]
        if matmul(M,M,p)!=M:continue
        cols=[list(col) for col in zip(*M)]
        ok=True
        for i in range(n):
            for j in range(i):
                Bij=bracket(generators[i],generators[j],N,p)
                lhs=[sum(M[x][k]*Bij[k] for k in range(n))%p for x in range(n)]
                rhs=bracket(cols[i],cols[j],N,p)
                if lhs!=rhs:ok=False;break
            if not ok: break
        if ok:valid.append((M,rank(M,p)))
    counts=Counter(); P=Counter()
    for M,ra in valid:
        P[ra]+=1
        for E,rb in valid:
            if matmul(M,E,p)==matmul(E,M,p): counts[(ra,rb)]+=1
    return P,counts

def gl(m,q,ell):
    if m==0:return 1
    return q**((ell-1)*m*m)*prod(q**m-q**j for j in range(m))

def qbinom(r,k,q):
    if k<0 or k>r:return 0
    return prod(q**(r-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def predicted(q,r,ell):
    I=Counter();P=Counter({0:1})
    for k in range(r+1):
        P[1+ell*k]+=qbinom(r,k,q)*q**((2*ell-1)*k*(r-k)+ell*(r-k))
    for a in range(r+1):
     for b in range(r-a+1):
      for c in range(r-a-b+1):
        d=r-a-b-c
        ns=(a,b,c,d) # 00,01,10,11
        size=gl(r,q,ell)//prod(gl(x,q,ell) for x in ns)
        I[(1+ell*(c+d),1+ell*(b+d))]+=size*q**(ell*(r-d))
    # with zero map
    for k,c in P.items():
        if k!=0:
            I[(k,0)]+=c;I[(0,k)]+=c
    I[(0,0)]+=1
    return P,I

def aut_module(q, block_map):
    # block_map keys are (monic-polynomial-label, degree, Jordan length)
    groups={}
    for (label,degree,j),m in block_map.items():
        if m:groups.setdefault((label,degree),{})[j]=m
    out=1
    for (_,degree),mult in groups.items():
        Q=q**degree
        E=sum(sum(m for length,m in mult.items() if length>=i)**2
              for i in range(1,max(mult)+1))
        out *= Q**(E-sum(v*v for v in mult.values()))
        out *= prod(gl(m,Q,1) for m in mult.values())
    return out


def predicted_general(q, block_map):
    types=list(block_map)
    mvals=[block_map[k] for k in types]
    dim=sum(k[1]*k[2]*block_map[k] for k in types)
    Aut=aut_module(q,block_map)
    P=Counter({0:1});C=Counter()
    for ks in product(*(range(m+1) for m in mvals)):
        A={typ:k for typ,k in zip(types,ks) if k}
        B={typ:m-k for typ,m,k in zip(types,mvals,ks) if m-k}
        ways=Aut//(aut_module(q,A)*aut_module(q,B))
        assert ways*(aut_module(q,A)*aut_module(q,B))==Aut
        a=sum(t[1]*t[2]*v for t,v in A.items())
        P[1+a]+=ways*q**(dim-a)
    for split in product(*(tuple((a,b,c,m-a-b-c) for a in range(m+1) for b in range(m-a+1) for c in range(m-a-b+1)) for m in mvals)):
        ms=[{k:quad[j] for k,quad in zip(types,split) if quad[j]} for j in range(4)]
        ways=Aut//prod(aut_module(q,xx) for xx in ms)
        assert ways*prod(aut_module(q,xx) for xx in ms)==Aut
        ds=[sum(t[1]*t[2]*m for t,m in xx.items()) for xx in ms]
        C[(1+ds[2]+ds[3],1+ds[1]+ds[3])]+=ways*q**(dim-ds[3])
    for rankF,c in P.items():
        if rankF:
            C[(0,rankF)]+=c
            C[(rankF,0)]+=c
    C[(0,0)]+=1
    return P,C

def main():
    for p,r,ell in [(2,1,1),(3,1,1),(2,2,1),(2,1,2),(2,1,3)]:
        v=sample(p,r,ell);pred=predicted(p,r,ell)
        assert v==pred, (p,r,ell,v,pred)
        print('EXHAUSTIVE_OK',p,r,ell,'total',sum(v[0].values()),'commuting',sum(v[1].values()))
    # Irreducible quadratic and split distinct-linear rational canonical cases.
    for p,N,expected_total,expected_comm in [(2,[[0,1],[1,1]],6,24),(3,[[1,0],[0,2]],17,133)]:
        P,I=sample(p,2,1,N);assert sum(P.values())==expected_total and sum(I.values())==expected_comm,(p,P,I)
        print("GENERIC_RC_OK",p,expected_total,expected_comm)
    # Test a mixed Jordan partition, which is not a free module over one chain ring.
    for p,N,blocks in [
        (2,[[1,1,0],[0,1,0],[0,0,1]],{("f1",1,2):1,("f1",1,1):1}),
        (2,[[0,1],[1,1]],{("f2",2,1):1}),
        (3,[[1,0],[0,2]],{("f1",1,1):1,("f2",1,1):1}),
        (2,[[1,0],[0,1]],{("f1",1,1):2})]:
        P,C=sample(p,len(N),1,N)
        Pg,Cg=predicted_general(p,blocks)
        assert (P,C)==(Pg,Cg),(p,N,P,Pg,C,Cg)
        print('GENERAL_MODULE_OK',p,blocks,'endomorphisms',sum(P.values()),'commuting',sum(C.values()))
    for q,r,ell in [(2,2,2),(3,2,2),(2,3,2),(2,2,3)]:
        P,I=predicted(q,r,ell)
        assert sum(I.values())<=sum(P.values())**2
        print('FORMULA',q,r,ell,'total',sum(P.values()),'commuting',sum(I.values()))
    print('VERIFY_OK')
if __name__=='__main__':main()
