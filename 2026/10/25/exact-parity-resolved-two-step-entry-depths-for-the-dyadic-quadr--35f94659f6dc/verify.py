from collections import Counter

def cv(k,t,par):
    if t==0:return 1
    m=k-3*(t-1)
    z=1<<(k-1)
    if par==0:
        if m<=3:return z
        if m<=6:return z//2
        return z//(1<<(m-5))
    if m<=5:return z
    return z//(1<<(m-5))

def check():
    for k in range(1,18):
        m=1<<k
        g=lambda x: ((x*x+1)**2+1)%m
        roots={}
        for par in (0,1):
            r=[x for x in range(par,m,2) if g(x)==x]
            assert len(r)==1,(k,par,r)
            roots[par]=r[0]
        # Make sure f maps 2-cycle
        f=lambda x:(x*x+1)%m
        assert f(roots[0])==roots[1] and f(roots[1])==roots[0]
        cumul={0:Counter(),1:Counter()}
        for x in range(m):
            n=x
            for t in range(k+2):
                if n==roots[x&1]:break
                n=g(n)
            else:raise AssertionError(('not converged',k,x))
            cumul[x&1][t]+=1
        for par in (0,1):
            for t in range(k+2):
                got=sum(v for s,v in cumul[par].items() if s<=t)
                expected=cv(k,t,par)
                assert got==expected,(k,par,t,got,expected,dict(cumul[par]))
        if k in (4,8,12,17):print(k,roots,dict(cumul[0]),dict(cumul[1]))
    print('VERIFY_OK: exhaustive k=1..17, 262142 residues, every parity cumulative and exact two-cycle')
if __name__=='__main__':check()
