"""Standalone exact checks for the Grassmann-algebra derivation census.
Uses only the Python standard library; finite enumeration is supplementary to the proof.
"""
import itertools
import random


def mul_field(a,b,q):
    if q == 4:
        t = ((a if b & 1 else 0) ^ (a << 1 if b & 2 else 0))
        if t & 8: t ^= 12
        if t & 4: t ^= 7
        return t
    return (a*b) % q


def add(a,b,q):
    return a^b if q==4 else (a+b)%q


def sub(a,b,q):
    return a^b if q==4 else (a-b)%q


def det3(a,q):
    v=lambda x,y:mul_field(x,y,q)
    return add(sub(v(a[0],sub(v(a[4],a[8]),v(a[5],a[7]),q)),
                       v(a[1],sub(v(a[3],a[8]),v(a[5],a[6]),q)),q),
               v(a[2],sub(v(a[3],a[7]),v(a[4],a[6]),q)),q)


def enumerate_leading(q):
    good=0
    trace_fiber=0
    for A in itertools.product(range(q),repeat=9):
        t=add(add(A[0],A[4],q),A[8],q)
        if t!=1:continue
        trace_fiber+=1
        if det3(A,q)==0:continue
        IA=[sub(1 if i==j else 0,A[3*i+j],q) for i in range(3) for j in range(3)]
        if det3(IA,q):good+=1
    target=q**3*(q**5-2*q**4-q**3+q**2+3*q+(1 if q%2==0 else 2))
    assert good==target, (q,good,target)
    assert trace_fiber==q**8
    return good


def prod_monomials(i,j,p):
    if i & j:return (0,0)
    inversions=sum(1 for x in range(3) if (i>>x)&1 for y in range(3) if (j>>y)&1 and x>y)
    return (i|j, (-1 if inversions%2 else 1)%p)


def prod_vec(a,b,p):
    c=[0]*8
    for i,x in enumerate(a):
        if x==0:continue
        for j,y in enumerate(b):
            if y==0:continue
            k,z=prod_monomials(i,j,p)
            if z:c[k]=(c[k]+x*y*z)%p
    return c


def add_vec(a,b,p):return [(x+y)%p for x,y in zip(a,b)]

def basis(i):
    out=[0]*8
    out[i]=1
    return out


def generate_D(F,p):
    # D(x_1),D(x_2),D(x_3) give values of the k-linear map on monomials.
    out=[]
    for mask in range(8):
        acc=[0]*8
        vars=[i for i in range(3) if mask&(1<<i)]
        for pos,i in enumerate(vars):
            left=basis(sum(1<<j for j in vars[:pos]))
            right=basis(sum(1<<j for j in vars[pos+1:]))
            term=prod_vec(prod_vec(left,F[i],p),right,p)
            acc=add_vec(acc,term,p)
        out.append(acc)
    return out


def relation_matrix(p):
    # Linear equations for Leibniz in each of the 24 candidate generator coefficients.
    cols=[]
    for j in range(3):
        for m in range(8):
            F=[[0]*8 for _ in range(3)]
            F[j][m]=1
            D=generate_D(F,p)
            col=[]
            for i in range(8):
                for k in range(8):
                    jx,coeff=prod_monomials(i,k,p)
                    lhs=[(coeff*v)%p for v in D[jx]] if coeff else [0]*8
                    rhs=add_vec(prod_vec(D[i],basis(k),p),prod_vec(basis(i),D[k],p),p)
                    col.extend((a-b)%p for a,b in zip(lhs,rhs))
            cols.append(col)
    return [list(x) for x in zip(*cols)]


def rank(A,p):
    M=[row[:] for row in A]
    if not M:return 0
    r=0
    for c in range(len(M[0])):
        v=next((i for i in range(r,len(M)) if M[i][c]%p),None)
        if v is None:continue
        M[v],M[r]=M[r],M[v]
        z=pow(M[r][c],-1,p)
        M[r]=[(x*z)%p for x in M[r]]
        for i in range(r+1,len(M)):
            if M[i][c]:
                y=M[i][c]
                M[i]=[(a-y*b)%p for a,b in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r


def test_derivation_spaces():
    for p,dimension in [(2,24),(3,15),(5,15)]:
        constraints=relation_matrix(p)
        assert 24-rank(constraints,p)==dimension
        print('DERIVATION_DIMENSION',p,dimension)


def test_sample_rank_equivalence():
    rand=random.Random(1701)
    for p in (2,3,5):
        for _ in range(180):
            B=[[rand.randrange(p) for _ in range(3)] for _ in range(3)]
            F=[[0]*8 for _ in range(3)]
            for i in range(3):
                for j in range(3): F[i][1<<j]=B[j][i]
            if p==2:
                for i in range(3):
                    for mask in (3,5,6,7):F[i][mask]=rand.randrange(p)
            else:
                # Add an arbitrary odd inner derivation, and arbitrary cubic terms.
                a=[0]*8
                for i in range(3):a[1<<i]=rand.randrange(p)
                for i in range(3):
                    comm=add_vec(prod_vec(a,basis(1<<i),p),
                            [(-v)%p for v in prod_vec(basis(1<<i),a,p)],p)
                    F[i]=add_vec(F[i],comm,p)
                    F[i][7]=rand.randrange(p)
            D=generate_D(F,p)
            # Check every multiplication identity on the 8-element algebra basis.
            for i in range(8):
                for j in range(8):
                    k,c=prod_monomials(i,j,p)
                    lhs=[(c*v)%p for v in D[k]] if c else [0]*8
                    rhs=add_vec(prod_vec(D[i],basis(j),p),prod_vec(basis(i),D[j],p),p)
                    assert lhs==rhs,(p,i,j)
            assert all(D[j][0]==0 for j in range(1,8))
            lead=[B[j][i] for i in range(3) for j in range(3)]
            t=(B[0][0]+B[1][1]+B[2][2])%p
            K=[((t if i==j else 0)-B[j][i])%p for i in range(3) for j in range(3)]
            predicted=det3(lead,p)!=0 and det3(K,p)!=0 and t!=0
            actual=rank([[D[j][i] for j in range(1,8)] for i in range(1,8)],p)==7
            assert predicted==actual,(p,B,predicted,actual)
        print('RANK_AND_LEIBNIZ_CHECK',p,180)


if __name__=='__main__':
    for q in (2,3,4,5): print('LEADING_COUNT',q,enumerate_leading(q))
    test_derivation_spaces()
    test_sample_rank_equivalence()
    print('EXTERIOR_RANK_CENSUS_OK')
