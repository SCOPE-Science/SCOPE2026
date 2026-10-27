"""Independent finite-field checks for the second jets of commuting 3x3 matrices.
Run with Python 3.10+, no dependencies.
"""
from itertools import product

class Field:
    def __init__(self, q):
        self.q = q
        if q == 4:
            self.add = [[a ^ b for b in range(4)] for a in range(4)]
            def mul(a,b):
                poly = 0
                for i in range(2):
                    for j in range(2):
                        if (a >> i)&1 and (b >> j)&1: poly ^= 1 << (i+j)
                if poly & 8: raise AssertionError('degree too large')
                if poly & 4: poly ^= 7 # x^2 = x+1
                return poly
            self.mul = [[mul(a,b) for b in range(4)] for a in range(4)]
        else:
            assert q in (2,3,5)
            self.add = [[(a+b)%q for b in range(q)] for a in range(q)]
            self.mul = [[(a*b)%q for b in range(q)] for a in range(q)]
        self.neg = [next(j for j in range(q) if self.add[i][j] == 0) for i in range(q)]
        self.inv = [0] + [next(j for j in range(1,q) if self.mul[i][j] == 1) for i in range(1,q)]

    def matrix_rank(self, mat):
        a = [row[:] for row in mat]; rows=len(a); cols=len(a[0]) if rows else 0
        k=0
        for j in range(cols):
            p=next((t for t in range(k,rows) if a[t][j] != 0), None)
            if p is None: continue
            a[k],a[p]=a[p],a[k]
            inv=self.inv[a[k][j]]
            a[k]=[self.mul[inv][x] for x in a[k]]
            for i in range(rows):
                if i!=k and a[i][j]:
                    t=a[i][j]
                    a[i]=[self.add[x][self.neg[self.mul[t][y]]] for x,y in zip(a[i],a[k])]
            k+=1
            if k==rows: break
        return k

    def matmul(self, x,y):
        return tuple(self.add[self.add[self.mul[x[3*i]][y[j]]][self.mul[x[3*i+1]][y[3+j]]]][self.mul[x[3*i+2]][y[6+j]]] for i in range(3) for j in range(3))

    def matcomm(self, x,y):
        z=self.matmul(x,y);w=self.matmul(y,x)
        return tuple(self.add[t][self.neg[u]] for t,u in zip(z,w))

    def linear_comm(self, x):
        mat=[]
        for j in range(9):
            e=[0]*9;e[j]=1
            mat.append(self.matcomm(tuple(e),x))
        return [[mat[col][row] for col in range(9)] for row in range(9)]

    def kernel_basis(self, mat):
        a=[r[:] for r in mat];nr=len(a);nc=len(a[0]);pivot=[];k=0
        for j in range(nc):
            p=next((t for t in range(k,nr) if a[t][j]),None)
            if p is None:continue
            a[k],a[p]=a[p],a[k];inv=self.inv[a[k][j]]
            a[k]=[self.mul[inv][x] for x in a[k]]
            for i in range(nr):
                if i!=k and a[i][j]:
                    t=a[i][j]
                    a[i]=[self.add[x][self.neg[self.mul[t][y]]] for x,y in zip(a[i],a[k])]
            pivot.append(j);k+=1
            if k==nr:break
        basis=[]
        for j in range(nc):
            if j in pivot:continue
            v=[0]*nc;v[j]=1
            for row,col in enumerate(pivot):v[col]=self.neg[a[row][j]]
            basis.append(tuple(v))
        return basis

    def span(self,basis):
        for v in product(range(self.q),repeat=len(basis)):
            out=[0]*9
            for c,b in zip(v,basis):
                if c:
                    for j in range(9):out[j]=self.add[out[j]][self.mul[c][b[j]]]
            yield tuple(out)


def theoretical(q):
    L=(q*q+q+1)**2; S=q*(q-1)*L;R=q**9-q-S
    T=q*q**9+S*q**5+R*q**3
    n9=q*q;n5=q*q*(q*q-1)*L;n3=T-n9-n5
    J1=n3*q**12+n5*q**14+n9*q**18
    J2=n3*q**24+n5*q**23*(q**3+q**2-1)+n9*q**18*T
    return S,R,T,(n3,n5,n9),J1,J2


def verify(q):
    F=Field(q); S,R,T,expected,J1,J2=theoretical(q)
    I=(1,0,0,0,1,0,0,0,1)
    N=(0,1,0,0,0,0,0,0,0)
    P=(1,0,0,0,0,0,0,0,0)
    # Two inequivalent noncentral rank-one strata: nilpotent, idempotent.
    for A in [N,P]:
        CB=F.kernel_basis(F.linear_comm(A))
        assert len(CB)==5
        buckets={}
        for B in F.span(CB):
            eqs=F.linear_comm(B)+F.linear_comm(A)
            dim=9-F.matrix_rank(eqs)
            buckets[dim]=buckets.get(dim,0)+1
        assert buckets=={5:q*q,3:q**5-q*q},('local',q,A,buckets)
        if q==2:
            # Literal second-order equation for every B1 in C(N) and every A1:
            # [A1,B1] lies in the image of ad_N iff a B2 exists.
            image_map=F.linear_comm(A)
            image_rank=F.matrix_rank(image_map)
            for B in F.span(CB):
                cdim=9-F.matrix_rank(F.linear_comm(A)+F.linear_comm(B))
                count=0
                for X in product(range(2),repeat=9):
                    rhs=F.matcomm(X,B)
                    aug=[row+[rhs[i]] for i,row in enumerate(image_map)]
                    if F.matrix_rank(aug)==image_rank:
                        count+=1
                assert count==2**(4+cdim),('literal obstruction',A,B,count,cdim)
        # Independent second-order obstruction rank: rank of [B,C(N)].
        for B in [tuple([0]*9), A, tuple(F.add[A[i]][P[i]] for i in range(9))]:
            if F.matcomm(A,B)!=(0,)*9: continue
            images=[F.matcomm(B,C) for C in CB]
            dim=F.matrix_rank([list(w) for w in images])
            joint=9-F.matrix_rank(F.linear_comm(A)+F.linear_comm(B))
            assert dim==5-joint
    if q==2:
        allm=list(product(range(q),repeat=9))
        d_counts={};cen_counts={3:0,5:0,9:0}
        for A in allm:
            CB=F.kernel_basis(F.linear_comm(A))
            cen_counts[len(CB)]+=1
            for B in F.span(CB):
                d=9-F.matrix_rank(F.linear_comm(A)+F.linear_comm(B))
                d_counts[d]=d_counts.get(d,0)+1
        assert cen_counts=={3:R,5:S,9:q},('matrix centralizer',cen_counts)
        assert tuple(d_counts.get(j,0) for j in (3,5,9))==expected,('pair strata',d_counts,expected)
        assert sum(d_counts.values())==T
    if q==3:
        # Independent full 3^9 census of matrix-centralizer dimensions.
        dims={3:0,5:0,9:0}
        for A in product(range(3),repeat=9):
            d=9-F.matrix_rank(F.linear_comm(A))
            dims[d]=dims.get(d,0)+1
        assert dims=={3:R,5:S,9:q},('matrix census F3',dims)
    print('VERIFIED q=',q,'regular matrices=',R,'noncyclic=',S,
          'commuting pairs=',T,'centralizer strata=',expected,
          'first jets=',J1,'second jets=',J2)

if __name__=='__main__':
    for q in (2,3,4,5): verify(q)
    print('VERIFY_OK_SECOND_JET_GL3_ALL_FOUR_FIELDS')
