"""Exact checkerboard coupling tests for two-stage tail patching."""
from fractions import Fraction as F

def run(n,k,L,U):
    a=F(k,n); low=F(L,k); high=F(U,k)
    A=[[F(1,n*n) for j in range(n)] for i in range(n)]
    for i in range(k):
        for j in range(k):
            A[i][j]=(1-low)*A[i][j]
            if i==j:
                A[i][j]+=low*F(k,n*n)
    b=n-k
    rows=[sum(A[i][j] for j in range(b,n)) for i in range(b,n)]
    cols=[sum(A[i][j] for i in range(b,n)) for j in range(b,n)]
    assert sum(rows)==sum(cols)
    B=[[F(0) for j in range(n)] for i in range(n)]
    i=j=0; r=rows[0]; c=cols[0]
    while i<len(rows) and j<len(cols):
        v=min(r,c)
        B[b+i][b+j]+=v
        r-=v;c-=v
        if r==0:
            i+=1
            if i<len(rows):r=rows[i]
        if c==0:
            j+=1
            if j<len(cols):c=cols[j]
    for i in range(b,n):
        for j in range(b,n):
            A[i][j]=(1-high)*A[i][j]+high*B[i][j]
    checks=0
    for z in range(n):
        assert sum(A[z])==F(1,n)
        assert sum(A[i][z] for i in range(n))==F(1,n)
        checks+=2
    for t in range(n-k+1):
        val=sum(A[i][j] for i in range(k+t) for j in range(t))
        assert val==F(k+t,n)*F(t,n),(n,k,L,U,t,val)
        checks+=1
    assert n*A[0][0]==F(L,n)+F(1,n)*(1-low)
    assert n*A[-1][-1]==F(U,n)+F(1,n)*(1-high)
    checks+=2
    return checks

def main():
    total=0
    for n in (6,8,10,12,18):
        for k in range(1,n):
            for L_num in (0,1,2,3):
                for U_num in (0,1,2,3):
                    L=F(k*L_num,3)
                    U=F(k*U_num,3)
                    total+=run(n,k,L,U)
    print('PASS:',total,'exact marginal/section/tail checks')

if __name__=='__main__':main()
