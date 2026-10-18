"""Exact-rational verification of complete-clique prism projection formulas.
Run: python3 verify_prism.py (Python standard library only).
Theorem for all m>=3 is analytic; finite assertions corroborate it.
"""
from fractions import Fraction as F

def model(m):
    es=[(h*m+i,h*m+j) for h in (0,1) for i in range(m) for j in range(i+1,m)]
    es.extend((i,m+i) for i in range(m))
    r=m*(m-1)//2; N=len(es)
    ei={tuple(sorted(e)):k for k,e in enumerate(es)}
    def zvec():return [F(0) for _ in range(N)]
    def R(x):return [xi-sum(x)/m for xi in x]
    def div(a):
        y=[F(0) for _ in range(m)]
        for k,(i,j) in enumerate(es[:r]):y[i]-=a[k];y[j]+=a[k]
        return y
    def grad(u):return [u[j]-u[i] for i,j in es[:r]]
    def split(x):return x[:r],x[r:2*r],x[2*r:]
    def join(a,b,c):return a+b+c
    def add(*arr):return [sum(z) for z in zip(*arr)]
    def scale(x,q):return [q*z for z in x]
    def cycle(u):
        g=scale(grad(u),F(1,m));return join(g,scale(g,-1),u)
    def source(x):
        a,b,c=split(x)
        return scale(add(div([aa-bb for aa,bb in zip(a,b)]),scale(R(c),-2)),F(1,2*(m+2)))
    def P0(x):
        a,b,c=split(x)
        u=scale(add(div([aa-bb for aa,bb in zip(a,b)]),scale(R(c),m)),F(1,m+2))
        ga=grad(div(a));gb=grad(div(b)); g=grad(u)
        return join([aa-xx/F(m)+gg/F(m) for aa,xx,gg in zip(a,ga,g)],
                    [bb-xx/F(m)-gg/F(m) for bb,xx,gg in zip(b,gb,g)],u)
    def H(x):return cycle(source(x))
    def HT(x):
        a,b,c=split(x)
        u=add(scale(div([aa-bb for aa,bb in zip(a,b)]),F(1,m)),R(c))
        g=scale(grad(u),F(1,2*(m+2)))
        return join(g,scale(g,-1),scale(u,F(-1,m+2)))
    def P(x,t):return add(P0(x),scale(H(x),t))
    def Q(x,s):return add(x,scale(P0(x),-1),scale(HT(x),s))
    def col(j):
        x=zvec();x[j]=F(1);return x
    def mat(op):return [op(col(j)) for j in range(N)]
    def action(p,flip,x):
        y=zvec()
        for j,(a,b) in enumerate(es):
            u=(1-(a//m) if flip else a//m)*m+p[a%m]
            v=(1-(b//m) if flip else b//m)*m+p[b%m]
            k=ei[tuple(sorted((u,v)))]; sign=1 if (u,v)==es[k] else -1
            y[k]+=sign*x[j]
        return y
    def abs_sum(v):return sum(map(abs,v))
    return locals()

def run():
    count=0
    for m in [3,4,5,6,7,8]:
        M=model(m);N=M['N'];r=M['r'];c=M['col'];P=M['P'];Q=M['Q'];P0=M['P0'];H=M['H'];HT=M['HT'];act=M['action'];div=M['div'];split=M['split'];grad=M['grad'];R=M['R'];a=M['add'];sc=M['scale'];ab=M['abs_sum']
        t=F((m-2)*(m-4),5*m-2)
        s=F((m-2)**2,m*(m-1)+2)
        zval=F(16*(m-1)**2,m*(5*m-2))
        bval=F(2*(m*m-m+1),m*m-m+2)
        pcols=[P(c(j),t) for j in range(N)]
        qcols=[Q(c(j),s) for j in range(N)]
        assert max(map(ab,pcols))==zval,(m,'cycle norm')
        assert max(map(ab,qcols))==bval,(m,'cut norm')
        count+=2
        assert len(set(ab(col) for col in pcols[:2*r]))==1
        assert len(set(ab(col) for col in pcols[2*r:]))==1
        assert len(set(ab(col) for col in qcols[:2*r]))==1
        assert len(set(ab(col) for col in qcols[2*r:]))==1
        count+=4
        if m<=5:
            for j in range(N):
                x=c(j);p=pcols[j];q=qcols[j]
                # Idempotence and complementary-space identities.
                assert P(p,t)==p
                assert Q(q,s)==q
                assert P0(P0(x))==P0(x)
                assert H(H(x))==[F(0)]*N
                assert P0(H(x))==H(x)
                assert H(P0(x))==[F(0)]*N
                aa,bb,cc=split(p)
                assert div(aa)==cc and div(bb)==sc(cc,-1)
                # Cut space is the orthogonal complement of the cycle space:
                # Q(x) must be a discrete gradient on the prism.
                # Check orthogonality to full cycle basis via P0.
                assert P0(q)==[F(0)]*N
                count+=8
            gen=[]
            for i in range(m-1):
                p=list(range(m));p[i],p[i+1]=p[i+1],p[i];gen.append((p,False))
            gen.append((list(range(m)),True))
            for p,flip in gen:
                for j in range(N):
                    x=c(j)
                    assert P(act(p,flip,x),t)==act(p,flip,pcols[j])
                    assert Q(act(p,flip,x),s)==act(p,flip,qcols[j])
                    count+=2
    print('PASS',count,'exact rational structural/projection assertions')
    print('Verified m = 3,...,8; automorphism/idempotence checks through m=5.')
    print('Analytic proof required for all m>=3; finite tests are not exhaustive.')
if __name__=='__main__':run()
