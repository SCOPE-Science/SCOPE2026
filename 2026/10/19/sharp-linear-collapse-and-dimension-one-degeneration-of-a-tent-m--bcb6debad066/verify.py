from fractions import Fraction as F
from itertools import product
from math import floor,log2,sqrt

def tau(x): return 2*min(x,1-x)
def tent_periodic(m):
    # affine tent iterate exactly on each dyadic m-cylinder; obtain its fixed point
    out=[]
    for k in range(2**m):
        lo=F(k,2**m); hi=F(k+1,2**m)
        a=lo; b=hi
        for _ in range(m):
            a=tau(a); b=tau(b)
        assert {a,b}=={F(0),F(1)}
        if a==0: # increasing branch
            x=lo/(1-(hi-lo)) # 2**m*(x-lo)=x -> x=2**m*lo/(2**m-1)
            x=lo/(1-F(1,2**m))
        else: # decreasing branch 2**m*(hi-x)=x
            x=hi/(1+F(1,2**m))
        assert lo<=x<=hi
        y=x
        for j in range(m): y=tau(y)
        assert y==x
        out.append(x)
    return out

def solve_period(x,delta,m):
    z=[x]
    for _ in range(m-1): z.append(tau(z[-1]))
    branches=[1 if u<F(1,2) else -1 for u in z]
    assert not any(u==F(1,2) for u in z)
    # z_(j+1)=cj+2sj*((1-d)*zj+d*z_(j-1))
    import sympy as sp
    A=sp.zeros(m,m); rhs=sp.zeros(m,1)
    for j in range(m):
        sj=branches[j]
        A[j,(j+1)%m]+=1
        A[j,j]-=2*sj*(1-delta)
        A[j,(j-1)%m]-=2*sj*delta
        rhs[j,0]=0 if sj==1 else 2
    zz=A.inv()*rhs
    vz=[F(int(v.p),int(v.q)) for v in zz]
    for j in range(m):
        inp=(1-delta)*vz[j]+delta*vz[(j-1)%m]
        assert 0<=inp<=1,(m,delta,j,inp)
        assert (inp<F(1,2)) == (branches[j]==1),(m,delta,j,inp,branches)
        assert vz[(j+1)%m]==tau(inp)
        assert abs(vz[j]-z[j])<=2*delta/(1-4*delta)
    return vz

def test():
    count=0
    for delta in [F(1,64), F(1,128),F(1,256),F(1,512),F(1,1024),F(1,2048)]:
        m=floor(log2(1/float(16*delta)))
        assert 1<=m<=7
        for x in tent_periodic(m):
            if x==0: continue
            solve_period(x,delta,m)
            count+=1
        a=2*(1-2*delta)/(5-8*delta)
        b=4*(1-delta)/(5-8*delta)
        G=lambda x,y:(y,tau((1-delta)*y+delta*x))
        assert G(a,b)==(b,a) and G(b,a)==(a,b)
        assert b-2*a==4*delta/(5-8*delta)
    # Cone expansion and determinant product (singular value upper proof)
    for d in [F(1,8),F(1,16),F(1,64)]:
        for ss in product([-1,1],repeat=7):
            u,v=F(0),F(1)
            for s in ss:
                u,v=v,2*s*(d*u+(1-d)*v)
                assert abs(v)>=2*(1-2*d)*abs(u)
            assert abs(v)>1
    print('VERIFY_OK',count)
if __name__=='__main__':test()
