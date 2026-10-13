from math import comb, factorial

def tables(N):
    S=[[0]*(N+1) for _ in range(N+1)]
    B=[[0]*(N+1) for _ in range(N+1)]
    S[0][0]=B[0][0]=1
    for r in range(1,N+1):
        for m in range(N+1):
            S[r][m]=sum(comb(m,j)*S[r-1][m-j] for j in range(1,m+1))
            B[r][m]=sum(comb(m,j)*B[r-1][m-j] for j in range(2,m+1))
    return S,B
S,B=tables(15)
def U(m,r,s):
    t=S[r][m]
    if s>=2: return t
    t-=B[r][m]
    if s==1: return t
    if r>0 and m>0:t-=r*m*B[r-1][m-1]
    if m==2*r:t+=factorial(m)//(2**r)
    return t

def cnt(n,q):
    t=0
    for s in range(min(n,q)+1):
        m=n-s
        sh=comb(n,s)*factorial(q)//factorial(q-s)
        for r in range(min(m,q-s)+1):
            a=U(m,r,s)
            if a==0:continue
            for z in range(min(m,q-s-r)+1):
                b=U(m,z,s)
                if b==0:continue
                t+=sh*comb(q-s,r)*comb(q-s-r,z)*a*b
    return t
if __name__=='__main__':
    # Independent exhaustive C++ counts with direct neighbor checks.
    expected={(3,4):96,(4,4):384,(5,4):240,(6,4):360,(4,3):0,(5,3):0}
    for k,v in expected.items():
        r=cnt(*k);assert r==v,(k,r,v)
    for n in range(4,13):
        predicted=384 if n==4 else 24*comb(n,2)
        assert cnt(n,4)==predicted,(n,cnt(n,4),predicted)
    for n in range(3,11):
        print('n',n,'counts_q2_to_q7',[cnt(n,q) for q in range(2,8)])
    print('ALL_CHECKS_PASSED')
