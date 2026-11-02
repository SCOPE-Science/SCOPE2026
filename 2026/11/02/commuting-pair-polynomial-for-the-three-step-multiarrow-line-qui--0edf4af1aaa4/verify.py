from itertools import product

def ranks(q,d):
    out=[0,0,0]
    for pair in product(range(q),repeat=2*d):
        a=pair[:d];b=pair[d:]
        if not any(a+b):k=0
        elif all((a[i]*b[j]-a[j]*b[i])%q==0 for i in range(d) for j in range(d)):k=1
        else:k=2
        out[k]+=1
    return out

def formula(q,r,s,t):
    nr,nt,ns=ranks(q,r),ranks(q,t),ranks(q,s)
    # integer avoid negative exponents by full dimension
    D=2*r*s+2*s*t; W=2*r*s*t
    a=sum(nr[i]*nt[j]*q**(D-s*(i*t+r*j-i*j)) for i in range(3) for j in range(3) if nr[i]*nt[j])
    b=(q+1)*(q**s-1)*(q**D+(q**r-1)*q**(D-s*t)+(q**t-1)*q**(D-s*r)+(q**r-1)*(q**t-1)*q**(D-s*(r+t-1)))
    c=ns[2]*q**D
    return (a+b+c)*q**W

def direct(q,r,s,t):
    # generate words as concatenation over quiver 0->1->2->3, labels i for arrow
    paths=[]
    for i in range(4):
        for j in range(i+1,4):
            choices=[range(z) for z in [r,s,t][i:j]]
            for lab in product(*choices):paths.append((i,j,lab))
    dim=len(paths); pindex={p:i for i,p in enumerate(paths)}
    mult=[(i,j,pindex[(a[0],b[1],a[2]+b[2])]) for i,a in enumerate(paths) for j,b in enumerate(paths) if a[1]==b[0]]
    basis=list(product(range(q),repeat=dim))
    total=0
    for A in basis:
      for B in basis:
        comm=[0]*dim
        for i,j,k in mult:
          comm[k]+=(A[i]*B[j]-B[i]*A[j])
        if all(x%q==0 for x in comm):total+=1
    return total,dim
for q,r,s,t in [(2,1,1,1),(3,1,1,1),(2,2,1,1),(2,1,2,1)]:
 f=formula(q,r,s,t);d,n=direct(q,r,s,t)
 print('TEST',q,r,s,t,'dim',n,'formula',f,'direct',d,'OK',f==d,flush=True)
 assert f==d
