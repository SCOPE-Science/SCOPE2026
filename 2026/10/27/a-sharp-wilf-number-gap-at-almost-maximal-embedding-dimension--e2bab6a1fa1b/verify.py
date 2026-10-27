from itertools import product

def probe():
    tested=0; near=0; equal=0
    for m, bound in ((4,7),(5,6),(6,5),(7,5),(8,4),(9,4)):
        family=0
        for vec in product(range(1,bound+1),repeat=m-1):
            x=(0,)+vec
            if any(x[i]+x[j]+(i+j>=m)<x[(i+j)%m] for i in range(1,m) for j in range(1,m) if (i+j)%m):
                continue
            tested+=1
            w=tuple(m*x[r]+r for r in range(m))
            composite=set()
            for i in range(1,m):
                for j in range(i,m):
                    k=(i+j)%m
                    if k and w[i]+w[j]==w[k]:composite.add(k)
            e=m-len(composite)
            if e!=m-1:continue
            near+=1;family+=1
            c=max(w)-m+1
            N=sum(1 for u in w if u<c for _ in range((c-1-u)//m+1))
            W=e*N-c
            assert W>=m-3,(m,vec,e,c,N,W)
            if W==m-3:
                equal+=1
                left={v for v in range(c) if v%m==0 or (w[v%m]<=v)}
                fam1= c==2*m and N==3 and any(left=={0,m,m+r} for r in range(1,(m+1)//2))
                fam2= c==3*m-1 and left=={0,m,2*m-1,2*m}
                assert fam1 or fam2,(m,vec,c,N,W,left)
        print('m',m,'near-max',family)
    return tested,near,equal
if __name__=='__main__':
 print('VERIFY_OK:',probe())
