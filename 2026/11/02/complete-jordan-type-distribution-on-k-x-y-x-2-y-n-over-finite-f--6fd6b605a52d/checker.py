"""Direct finite-field verification for Jordan ranks of multiplications in k[x,y]/(x^2,y^n).
The predictions come from truncated valuations; the direct check multiplies basis vectors
and computes ranks by independent Gaussian elimination over the original field.
"""
import itertools
from collections import Counter

class Field:
    def __init__(self,p,modulus=None):
        self.p=p; self.modulus=modulus; self.d=1 if modulus is None else len(modulus)-1
        self.q=p**self.d
        def coeffs(a):
            z=[]
            for _ in range(self.d):z.append(a%p);a//=p
            return z
        def encode(z):return sum((v%p)*p**i for i,v in enumerate(z))
        def add(a,b):return encode([(u+v)%p for u,v in zip(coeffs(a),coeffs(b))])
        def mul(a,b):
            u,v=coeffs(a),coeffs(b);w=[0]*(2*self.d-1)
            for i in range(self.d):
                for j in range(self.d):w[i+j]=(w[i+j]+u[i]*v[j])%p
            if self.modulus is not None:
                for h in range(len(w)-1,self.d-1,-1):
                    c=w[h]
                    for j in range(self.d):w[h-self.d+j]=(w[h-self.d+j]-c*modulus[j])%p
            return encode(w[:self.d])
        self.A=[[add(i,j) for j in range(self.q)] for i in range(self.q)]
        self.M=[[mul(i,j) for j in range(self.q)] for i in range(self.q)]
        self.N=[next(j for j in range(self.q) if self.A[i][j]==0) for i in range(self.q)]
        self.I=[0]+[next(j for j in range(1,self.q) if self.M[i][j]==1) for i in range(1,self.q)]
    def rank(self,mat):
        a=[row[:] for row in mat];rows=len(a);cols=len(a[0]) if a else 0;r=0
        for j in range(cols):
            pivot=next((k for k in range(r,rows) if a[k][j]),None)
            if pivot is None:continue
            a[r],a[pivot]=a[pivot],a[r];inv=self.I[a[r][j]]
            a[r]=[self.M[inv][v] for v in a[r]]
            for k in range(rows):
                if k==r or not a[k][j]:continue
                fac=self.N[a[k][j]]
                a[k]=[self.A[u][self.M[fac][v]] for u,v in zip(a[k],a[r])]
            r+=1
            if r==rows:break
        return r
    def mm(self,a,b):
        l=len(a);o=[[0]*l for _ in range(l)]
        for i in range(l):
            for k,x in enumerate(a[i]):
                if x:
                    for j,y in enumerate(b[k]):
                        if y:o[i][j]=self.A[o[i][j]][self.M[x][y]]
        return o

def valuation(v,n):
    return next((i for i,c in enumerate(v) if c),n)

def prediction(n,p,alpha,beta):
    out=[2*n]
    for t in range(1,2*n+1):
        a=min(t*alpha,n)
        b=n if t%p==0 else min((t-1)*alpha+beta,n)
        d=min(a,b);e=2*a-d
        out.append(2*n-min(d,n)-min(e,n))
    assert out[-1]==0
    counts=[out[t-1]-2*out[t]+out[t+1] for t in range(1,2*n)] + [out[2*n-1]]
    assert min(counts)>=0 and sum((i+1)*v for i,v in enumerate(counts))==2*n
    return tuple(out),tuple(reversed([i+1 for i,c in enumerate(counts) for _ in range(c)]))

def direct_matrix(n,field,a,b):
    size=2*n;mat=[[0]*size for _ in range(size)]
    for j in range(n):
        for i in range(n-j):
            mat[i+j][j]=a[i]
            mat[n+i+j][j]=b[i]
            mat[n+i+j][n+j]=a[i]
    return mat

def calculate(n,p,modulus=None):
    f=Field(p,modulus);q=f.q;hist=Counter();direct=Counter();hits=0
    zero=[[0]*(2*n) for _ in range(2*n)]
    for a_tail in itertools.product(range(q),repeat=n-1):
        a=(0,)+a_tail
        for b in itertools.product(range(q),repeat=n):
            alpha,beta=valuation(a,n),valuation(b,n)
            ranks,typ=prediction(n,p,alpha,beta)
            hist[typ]+=q # optional scalar constant has q choices
            m=direct_matrix(n,f,a,b);cur=[[int(i==j) for j in range(2*n)] for i in range(2*n)]
            rr=[2*n]
            for _ in range(2*n):
                cur=f.mm(cur,m)
                rr.append(f.rank(cur))
                if rr[-1]==0:break
            rr += [0]*(2*n+1-len(rr))
            assert tuple(rr)==ranks,(p,q,n,a,b,rr,ranks)
            direct[typ]+=q
            hits+=1
    assert hist==direct and sum(hist.values())==q**(2*n)
    return (q,n,hits,len(hist),','.join(f'{k}:{v}' for k,v in sorted(hist.items(),reverse=True)))

def main():
    configs=[(2,2,None),(2,3,None),(2,4,None),(2,5,None),(3,2,None),(3,3,None),(3,4,None),(5,2,None),(5,3,None),(2,3,[1,1,1]),(3,2,[1,0,1])]
    for p,n,poly in configs:
        q,nn,hits,types,hist=calculate(n,p,poly)
        print(f'PASS GF({q}) n={nn} direct_nilpotent_elements={hits} jordan_types={types} histogram={hist}')
    print('JORDAN_MULTIPLICATION_VALUATIONS_OK 11_EXHAUSTIVE_CONFIGURATIONS')
if __name__=='__main__':main()
