"""Independent finite-case checks for split-eigenspace Lie subalgebra permutability."""
from itertools import combinations,product
from math import prod

def ga(n,k,q):
    if k<0 or k>n:return 0
    return prod(q**(n-j)-1 for j in range(k))//prod(q**(k-j)-1 for j in range(k))

def H(x,z,q):return sum(ga(x,t,q)*q**(z*(x-t)) for t in range(x+1))

def exact_counts(blocks,q):
    n=sum(blocks)
    choices=list(product(*(range(a+1) for a in blocks)))
    n0=sum(ga(n,k,q) for k in range(n+1))
    n1=q**n*prod(sum(ga(a,i,q)*q**(-i) for i in range(a+1)) for a in blocks) if False else sum(prod(ga(a,i,q) for a,i in zip(blocks,idx))*q**(n-sum(idx)) for idx in choices)
    p01=p11=0
    for idx in choices:
        m=prod(ga(a,i,q) for a,i in zip(blocks,idx));x=sum(idx)
        p01+=m*q**(n-x)*sum(prod(ga(a-i,z,q) for a,i,z in zip(blocks,idx,jdx))*H(x,sum(jdx),q)
                               for jdx in product(*(range(a-i+1) for a,i in zip(blocks,idx))))
    for ix in choices:
        for iy in choices:
            possibilities=[]
            for a,i,j in zip(blocks,ix,iy):
                possibilities.append([(s,ga(a,i,q)*ga(i,s,q)*ga(a-i,j-s,q)*q**((i-s)*(j-s)))
                                      for s in range(max(0,i+j-a),min(i,j)+1)])
            for choices_s in product(*possibilities):
                inter=sum(s for s,m in choices_s)
                multiplicity=prod(m for s,m in choices_s)
                zs=[a-i-j+s for a,i,j,(s,m) in zip(blocks,ix,iy,choices_s)]
                p11+=multiplicity*q**(n-inter)*(1+sum(q**v-1 for v in zs))
    return (n0,n1,p01,p11)

def rref(rows,q):
    if not rows:return ()
    A=[list(x) for x in rows];d=len(A[0]);pivot=0
    for k in range(d):
        j=next((j for j in range(pivot,len(A)) if A[j][k]%q),None)
        if j is None:continue
        A[pivot],A[j]=A[j],A[pivot]
        mul=pow(A[pivot][k],-1,q)
        A[pivot]=[(mul*x)%q for x in A[pivot]]
        for v in range(len(A)):
            if v!=pivot:
                c=A[v][k]
                if c:A[v]=[(x-c*y)%q for x,y in zip(A[v],A[pivot])]
        pivot+=1
        if pivot==len(A):break
    return tuple(tuple(x) for x in A[:pivot])

def all_spaces(d,q):
    for k in range(d+1):
        for piv in combinations(range(d),k):
            places=[(i,j) for i in range(k) for j in range(piv[i]+1,d) if j not in piv]
            for data in product(range(q),repeat=len(places)):
                M=[[int(j==piv[i]) for j in range(d)] for i in range(k)]
                for (i,j),x in zip(places,data):M[i][j]=x
                yield tuple(map(tuple,M))

def brute(blocks,q,lams):
    assert q in (2,3) and len(lams)==len(blocks) and len(set(lams))==len(lams)
    n=sum(blocks);d=n+1;lam=[l for x,l in zip(blocks,lams) for _ in range(x)]
    def br(x,y):return (0,)+tuple(((x[0]*y[k+1]-x[k+1]*y[0])*lam[k])%q for k in range(n))
    subspaces=[A for A in all_spaces(d,q) if all(len(rref(A+(br(x,y),),q))==len(A) for x in A for y in A)]
    n0=sum(not any(v[0] for v in A) for A in subspaces);n1=len(subspaces)-n0
    p01=p11=0
    sums={(i,j):rref(A+B,q) for i,A in enumerate(subspaces) for j,B in enumerate(subspaces)}
    for i,A in enumerate(subspaces):
        for j,B in enumerate(subspaces):
            S=sums[i,j];closed=all(len(rref(S+(br(x,y),),q))==len(S) for x in A for y in B)
            if closed:
                type_a=int(any(x[0] for x in A));type_b=int(any(y[0] for y in B))
                if type_a+type_b==1:p01+=1
                if type_a+type_b==2:p11+=1
    computed=(n0,n1,p01//2,p11); predicted=exact_counts(blocks,q)
    assert p01%2==0 and computed==predicted, (blocks,q,computed,predicted)
    print('EXHAUSTIVE_OK',blocks,q,'subalgebras',len(subspaces),'n0,n1,cross,same',computed)

if __name__=='__main__':
    for blocks,q,lams in [((1,1),2,(0,1)),((1,2),2,(0,1)),((2,2),2,(0,1)),
                           ((1,1),3,(0,1)),((1,2),3,(0,2)),((1,1,1),3,(0,1,2))]:
        brute(blocks,q,lams)
    for blocks,q in [((2,2),2),((2,3),2),((3,3),2),((4,4),2),((2,2,2),3),((2,3,2),3)]:
        n0,n1,cross,same=exact_counts(blocks,q)
        lost=(n0+n1)**2-(n0*n0+2*cross+same)
        assert lost>0
        print('SUM_OK',blocks,q,'total',n0+n1,'nonpermuting',lost,'prob',round(lost/(n0+n1)**2,7))
    print('VERIFY_OK')
