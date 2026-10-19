"""Independent finite-field tests of weighted convolution nullity on H_1(p)."""
from itertools import product

def rank_mod(A,mod):
    A=[list(map(lambda v:v%mod,row)) for row in A]
    r=0; cols=len(A[0]); rows=len(A)
    for col in range(cols):
        k=next((i for i in range(r,rows) if A[i][col]),None)
        if k is None:continue
        A[k],A[r]=A[r],A[k]
        inv=pow(A[r][col],-1,mod)
        A[r][col:]=[(x*inv)%mod for x in A[r][col:]]
        for i in range(r+1,rows):
            u=A[i][col]
            if u: A[i][col:]=[(v-u*w)%mod for v,w in zip(A[i][col:],A[r][col:])]
        r+=1
        if r==rows: break
    return r

def nextprime(x):
    x+=1
    while True:
        if all(x%k for k in range(2,int(x**.5)+1)):
            return x
        x+=1

def prime_1_mod(n):
    x=10003
    while True:
        x=int(nextprime(x));
        if (x-1)%n==0:return x

def primitive_root_of_order(n,l):
    # Find generator by screening primitive n-th order directly.
    def factors(n):
        result=[]; d=2
        while d*d<=n:
            if n%d==0:
                result.append(d)
                while n%d==0:n//=d
            d+=1
        if n>1:result.append(n)
        return result
    for b in range(2,l):
        g=pow(b,(l-1)//n,l)
        if g!=1 and all(pow(g,n//t,l)!=1 for t in factors(n)):
            return g
    raise AssertionError('no generator')

def hmul(x,y,p):
    u,v,t=x; U,V,s=y
    return ((u+U)%p,(v+V)%p,(t+s+(u*V-v*U)*pow(2,-1,p))%p)

def check_case(p,weights,ell):
    z=primitive_root_of_order(p,ell)
    abc=tuple(w%ell for w in weights)
    Z=sum((abc[0]+abc[1]*pow(z,r,ell)+abc[2]*pow(z,s,ell))%ell==0 for r,s in product(range(p),repeat=2))
    F=sum(pow(w,p,ell) for w in abc)%ell
    pred=Z+(p-1)*p*(F==0)
    H=list(product(range(p),repeat=3)); pos={v:i for i,v in enumerate(H)}
    M=[[0]*(p**3) for _ in H]
    e=(0,0,0);g=(1,0,0);h=(0,1,0)
    for j,x in enumerate(H):
        for coeff,gen in zip(abc,(e,g,h)):
            i=pos[hmul(gen,x,p)]
            M[i][j]=(M[i][j]+coeff)%ell
    actual=p**3-rank_mod(M,ell)
    assert pred==actual,(p,weights,ell,Z,F,pred,actual)
    return {'p':p,'weights':str(weights),'character_resonances':Z,'F_zero':F==0,'nullity':actual,'ell':ell}

if __name__=='__main__':
    out=[]
    for p in (3,5,7):
        ell=prime_1_mod(3*p)
        root3=primitive_root_of_order(3,ell)
        cases=[(4,1,1),(-2,1,1),(1,1,1),(1,-1,0),(1,0,0),(1,root3,pow(root3,2,ell))]
        if p==7:cases=cases[:3] # 343-square full matrix elimination costs more
        for w in cases:out.append(check_case(p,w,ell))
    print('VERIFY_OK',len(out),'full regular exact ranks')
    for t in out:print(t)
