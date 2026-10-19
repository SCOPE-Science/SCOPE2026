from collections import Counter
from itertools import product

def check(q,m,kind):
    N=q**m
    def add(x,y):
        return (x+y)%N if kind=='integers' else x^y
    def mul(x,y):
        if kind=='integers':return x*y%N
        z=0
        for i in range(m):
            if (x>>i)&1:
                for j in range(m-i):
                    if (y>>j)&1:z^=1<<(i+j)
        return z
    def matmul(A,B):
        a,b,c,d=A;e,f,g,h=B
        return (add(mul(a,e),mul(b,g)),add(mul(a,f),mul(b,h)),add(mul(c,e),mul(d,g)),add(mul(c,f),mul(d,h)))
    def idx(A):
        cur=A
        for k in range(1,2*m+1):
            if cur==(0,0,0,0):return k
            cur=matmul(cur,A)
        return None
    hist=Counter();cyclic_max=Counter();witness={}
    for A in product(range(N),repeat=4):
        if kind=='integers':
            a,b,c,d=[z%q for z in A]
            tr=(a+d)%q;det=(a*d-b*c)%q
        else:
            a,b,c,d=[z&1 for z in A]
            tr=a^d;det=(a*d)^(b*c)
        if tr or det:continue
        k=idx(A);hist[k]+=1
        if k not in witness:witness[k]=A
    cls=(q*q-1)*q**(2*m-2);nmax=(q-1)*(q*q-1)*q**(4*m-5)
    assert sum(hist.values())==q**(4*m-2),(q,m,kind,sum(hist.values()))
    assert hist[2*m]==nmax,(q,m,kind,hist[2*m],nmax)
    assert not any(hist[k] for k in range(m+2,2*m)),hist
    if m==3:
        C=q**4*(q*q-1)
        expect={1:1,2:q**6-1+C,3:q**8-q**6+C*(q*q-1),4:C*(q**3-q*q),6:C*q**3*(q-1)}
        assert hist==expect,(hist,expect)
    print('PASS',q,m,kind,'N',sum(hist.values()),'class_size',cls,'hist',dict(sorted(hist.items())),'witness',witness,flush=True)

check(2,3,'integers')
check(2,3,'polynomials')
check(2,4,'integers')
check(3,3,'integers')

# Non-chain radical-cubed-zero boundary over F_p[x,y]/(x^2,y^2).
def check_nonchain(p):
    def plus(a,b):return tuple((u+v)%p for u,v in zip(a,b))
    def neg(a):return tuple(-u%p for u in a)
    def times(a,b):
        aa,ax,ay,axy=a; ba,bx,by,bxy=b
        return ((aa*ba)%p,(aa*bx+ax*ba)%p,(aa*by+ay*ba)%p,(aa*bxy+axy*ba+ax*by+ay*bx)%p)
    O=(0,0,0,0); I=(1,0,0,0); X=(0,1,0,0);Y=(0,0,1,0)
    def prod(A,B):
        a,b,c,d=A;e,f,g,h=B
        return (plus(times(a,e),times(b,g)),plus(times(a,f),times(b,h)),plus(times(c,e),times(d,g)),plus(times(c,f),times(d,h)))
    A=(O,neg(X),I,Y);V=A
    for k in range(1,7):
        if V==(O,)*4:
            assert k==(5 if p%2 else 4),(p,k)
            print('PASS nonchain p=',p,'nilpotency index',k)
            return
        V=prod(V,A)
    raise AssertionError('not nilpotent')
check_nonchain(3)
check_nonchain(5)
check_nonchain(2)
