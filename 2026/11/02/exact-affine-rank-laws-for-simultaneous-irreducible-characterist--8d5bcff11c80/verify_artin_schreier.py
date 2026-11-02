"""Independent finite-field checks for simultaneous irreducibility of Artin--Schreier cubics."""
from itertools import combinations

MODULI={1:(0,1),2:(1,0,1),3:(1,2,0,1)}

def digits(a,s):
    return [(a//(3**i))%3 for i in range(s)]

def enc(v):
    return sum((x%3)*3**i for i,x in enumerate(v))

class Field:
    def __init__(self,s):
        self.s=s; self.q=3**s; self.pol=MODULI[s]
        self.vec=[digits(i,s) for i in range(self.q)]
        self.add=[[enc([(self.vec[i][k]+self.vec[j][k])%3 for k in range(s)]) for j in range(self.q)] for i in range(self.q)]
        self.mul=[[0]*self.q for _ in range(self.q)]
        for i in range(self.q):
          for j in range(self.q):
            a=[0]*(2*s-1)
            for k,u in enumerate(self.vec[i]):
              for l,v in enumerate(self.vec[j]):a[k+l]=(a[k+l]+u*v)%3
            for k in range(2*s-2,s-1,-1):
              z=a[k]
              if z:
                for l in range(s):a[k-s+l]=(a[k-s+l]-z*self.pol[l])%3
            self.mul[i][j]=enc(a[:s])
        self.cube=[self.mul[self.mul[i][i]][i] for i in range(self.q)]
        # Check field inverses and polynomial irreducibility, independently.
        for i in range(1,self.q):
            assert any(self.mul[i][j]==1 for j in range(1,self.q))

    def rank(self,vectors):
        arr=[list(v) for v in vectors if any(v)]
        rank=0
        for c in range(self.s):
            pivot=next((r for r in range(rank,len(arr)) if arr[r][c]),None)
            if pivot is None:continue
            arr[rank],arr[pivot]=arr[pivot],arr[rank]
            z=arr[rank][c]
            arr[rank]=[(x*z)%3 for x in arr[rank]]
            for r in range(len(arr)):
                if r!=rank and arr[r][c]:
                    zz=arr[r][c]
                    arr[r]=[(x-zz*y)%3 for x,y in zip(arr[r],arr[rank])]
            rank+=1
        return rank

    def rank_formula(self,H):
        q=self.q; ssum=0
        for k in range(1,len(H)+1):
            for J in combinations(H,k):
                anchor=self.vec[J[0]]
                d=self.rank([[(self.vec[v][i]-anchor[i])%3 for i in range(self.s)] for v in J[1:]])
                ssum+=((-1)**(k+1))*(q//3**d)
        numerator=q*(3*q-2-ssum)
        assert numerator%6==0,(self.s,H,numerator)
        return numerator//6

    def brute(self,H):
        q=self.q; count=0
        for b in range(q):
            vals={self.add[self.cube[x]][self.mul[b][x]] for x in range(q)}
            for c in range(q):
                if all(self.add[c][h] not in vals for h in H):count+=1
        return count

    def spectral(self,H):
        q=self.q; out=0
        for linear_coefs in range(1,q):
            ell=self.vec[linear_coefs]
            image={sum(ell[i]*self.vec[h][i] for i in range(self.s))%3 for h in H}
            out+=3-len(image)
        assert q*out%6==0
        return q*out//6

checks=0; triples=0
for s in (1,2,3):
    F=Field(s); q=F.q
    if s<=2:
      hs=[t for k in range(1,q+1) for t in combinations(range(q),k)]
    else:
      hs=[(0,),(0,1),(0,1,2),(0,1,3),(0,1,2,3),(0,1,3,9),(0,1,2,3,9),(0,3,9,12),(0,1,4),(0,1,9),(0,1,2,9),(0,1,2,3,4,9)]
      Hmax=tuple(i for i in range(q) if F.vec[i][0]!=2)
      Hbad=tuple(sorted(set(Hmax)-{Hmax[1]}|{next(i for i in range(q) if F.vec[i][0]==2)}))
      hs.extend([Hmax,Hbad])
    for H in hs:
        a=F.rank_formula(H)
        b=F.brute(H)
        c=F.spectral(H)
        assert a==b==c,(q,H,a,b,c)
        if len(H)>2*q//3: assert a==0, (q,H,a)
        if len(H)==2*q//3 and a>0: assert a==q//3,(q,H,a)
        checks+=1
        if len(H)==3:
            r=F.rank([[(F.vec[h][i]-F.vec[H[0]][i])%3 for i in range(s)] for h in H[1:]])
            expect=q*(q-3)//9 if r==1 else q*(4*q-9)//27
            assert a==expect,(q,H,a,expect)
            triples+=1
    print(f'FIELD_OK q={q} checked_offset_sets={len(hs)}')
print(f'VERIFY_OK checked_offset_sets={checks} triple_classifications={triples} independent_direct_polynomial_root_tests=True')
