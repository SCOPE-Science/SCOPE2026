"""Check identities for a countably branched affine interval map."""
import mpmath as mp
mp.mp.dps = 60

def check(q_input,lam_input):
    q=mp.mpf(str(q_input)); lam=mp.mpf(str(lam_input)); Z=mp.zeta(q); c=lam/Z
    def pressure(s): return c**s*mp.zeta(q*s)-1
    s=mp.findroot(pressure,(1/q+mp.mpf('0.05'),mp.mpf('0.95')))
    assert 1/q<s<1 and abs(pressure(s))<mp.mpf('1e-50')
    theta=q*s; d=(theta-1)/(q-1); H=1/((q-1)*Z);K=c**s/(theta-1)*H**(-d)
    def tail(p,n):return mp.zeta(p,n+1)
    def mass(x,depth=0):
        if x<=0:return mp.mpf('0')
        if x>=1:return mp.mpf('1')
        n=max(1,int((H/x)**(1/(q-1))))
        while tail(q,n)/Z>x:n+=1
        while n>1 and tail(q,n-1)/Z<=x:n-=1
        b=tail(q,n)/Z; r=c*n**(-q)
        base=c**s*tail(theta,n)
        if x>=b+r: return base+c**s*n**(-theta)
        if depth>80:raise AssertionError('excessive recursion')
        return base+c**s*n**(-theta)*mass((x-b)/r,depth+1)
    def F(a):return mass(a/lam) if a<lam else mp.mpf('1')
    for a0 in [0,mp.mpf('.07'),lam/2,lam, (lam+1)/2,1]:
        a=mp.mpf(a0); target=c**s*(F(a)-a)
        e=[]
        for n in [20,60,180,540]:
            x=tail(q,n)/Z + a*n**(-q)/Z
            v=n**theta*(mass(x)-K*x**d)
            e.append(abs(v-target))
        assert e[-1]<e[0] and e[-1]<mp.mpf('.003'),(a,e)
        if a==lam:assert target>0
    for m in [1000,10000,100000]:
        x=m**(-1/d)
        prob=mass(x)
        assert abs(float(m*prob-K))<0.02,(q,lam,m,m*prob,K)
    print('PASSED q=',q,'lambda=',lam,'s=',mp.nstr(s,16),'d=',mp.nstr(d,16),'K=',mp.nstr(K,14), 'sharp_profile_at_lambda=',mp.nstr(c**s*(1-lam),14))
for q,lam in [('2','.4'),('3','.7')]:check(q,lam)
print('PASS: 2 parameter pairs, 12 scaled-cell tests with 4 index scales, 6 tail-mass checks')
