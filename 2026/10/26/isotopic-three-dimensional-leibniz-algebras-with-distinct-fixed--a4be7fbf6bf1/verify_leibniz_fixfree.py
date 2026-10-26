"""Direct matrix enumeration of fixed-point-free automorphisms of 3D symmetric central Leibniz algebras."""
from itertools import product

def mm(A,B,q):
    return [[sum(A[i][k]*B[k][j] for k in range(2))%q for j in range(2)] for i in range(2)]

def trans(A):return [list(r) for r in zip(*A)]

def test(q,sgn):
    if sgn=='+':G=[[0,1],[1,0]]
    else:
        # take a with -a nonsquare
        a=next(x for x in range(1,q) if (-x)%q not in {(i*i)%q for i in range(q)})
        G=[[1,0],[0,a]]
    allsim=[]; fixfree=[]
    for flat in product(range(q),repeat=4):
        A=[list(flat[:2]),list(flat[2:])]
        det=(A[0][0]*A[1][1]-A[0][1]*A[1][0])%q
        if not det:continue
        b=mm(mm(trans(A),G,q),A,q)
        c=next((x for x in range(1,q) if b==[[(x*y)%q for y in row] for row in G]),None)
        if c is None:continue
        allsim.append((A,c))
        if c!=1 and ((A[0][0]-1)*(A[1][1]-1)-A[0][1]*A[1][0])%q:
            fixfree.append((A,c))
    expected_go=2*(q-1)**2 if sgn=='+' else 2*(q*q-1)
    expected_f=(2*(q-2)**2 if sgn=='+' else 2*(q+1)*(q-2))
    assert len(allsim)==expected_go,(q,sgn,len(allsim),expected_go)
    assert len(fixfree)==expected_f,(q,sgn,len(fixfree),expected_f)
    print('PASS',q,sgn,'GO',len(allsim),'fixfree linear',len(fixfree),'Leibniz automorphisms',len(allsim)*q*q,'fixfree',len(fixfree)*q*q)
for q in (3,5,7):
    for sign in '+-':test(q,sign)
print('ALL_EXACT_CHECKS_PASSED')
