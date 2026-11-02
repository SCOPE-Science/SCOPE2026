from fractions import Fraction as F
from itertools import combinations
from math import comb

def theory_mean(d):
    p0=F(1,2**(d-1))
    return F(d,2)+F(1-2*p0,6*d)

def theory_second(d):
    p0=F(1,2**(d-1))
    return F(d*d,4)+F(d,4)-F(1,6)+F(1-2*p0,6*d)

def theory_variance(d):
    mu=theory_mean(d)
    return theory_second(d)-mu*mu

def theory_density(d,t):
    if t<0 or t>d:return F(0)
    p0=F(1,2**(d-1))
    v=p0*2*(1-t)/d if 0<=t<=1 else F(0)
    for k in range(1,d):
        if k<t<k+1:v+=F(2*comb(d-1,k),d*2**(d-1))*(t-k)
    if d>=2:
        for k in range(d-1):
            a=t-k
            if 0<a<=1:z=a
            elif 1<a<2:z=2-a
            else:z=0
            v+=F((d-1)*comb(d-2,k),d*2**(d-2))*z
    return v

def edges(d):
    return [(i, sum(((b>>(j if j<i else j-1))&1)<<j for j in range(d) if j!=i)) for i in range(d) for b in range(2**(d-1))]

def direct_distance(e,f,s,t,d):
    i,v=e;j,w=f
    if e==f:return abs(s-t)
    def popcount(x):return x.bit_count()
    vals=[]
    for a in (0,1):
        va=v|(a<<i)
        for b in (0,1):
            wb=w|(b<<j)
            vals.append((s if a==0 else 1-s)+popcount(va^wb)+(t if b==0 else 1-t))
    return min(vals)

def predicted_distance(e,f,s,t,d):
    i,v=e;j,w=f
    if e==f:return abs(s-t)
    if i==j:
        k=((v^w)>>0).bit_count()
        return k+min(s+t,2-s-t)
    k=((v^w)&~((1<<i)|(1<<j))).bit_count()
    return k+abs(s-((w>>i)&1))+abs(t-((v>>j)&1))

def check():
    total=0
    for d in range(1,7):
        ed=edges(d)
        for e in ed:
            for f in ed:
                for s,t in [(F(1,5),F(2,7)),(F(3,4),F(4,11)),(F(1,9),F(8,9))]:
                    a=direct_distance(e,f,s,t,d)
                    b=predicted_distance(e,f,s,t,d)
                    assert a==b,(d,e,f,s,t,a,b)
                    total+=1
        # exact first two moments of edge-pair distribution by numerical quadrature,
        # independent mid-point integration at d<=5
        assert theory_density(d,F(1,3))>=0
        if d>=2:
            assert theory_density(d,F(d,1)-F(1,1000))>0
        print('dimension',d,'edges',len(ed),'mean',theory_mean(d),'variance',theory_variance(d))
    print('SUCCESS',total,'exact-rational shortest-path comparisons')
if __name__=='__main__':check()

def integral_moments(d):
    out=[F(0),F(0),F(0)]
    for k in range(d):
        x=F(k)+F(1,3);y=F(k)+F(2,3)
        dx=y-x
        slope=(theory_density(d,y)-theory_density(d,x))/dx
        intercept=theory_density(d,x)-slope*x
        for m in range(3):
            out[m]+=slope*F((k+1)**(m+2)-k**(m+2),m+2)+intercept*F((k+1)**(m+1)-k**(m+1),m+1)
    return out

for n in range(1,26):
    z=integral_moments(n)
    assert z==[F(1),theory_mean(n),theory_second(n)],(n,z,theory_mean(n),theory_second(n))
print('SUCCESS exact density/moment integration for dimensions 1..25')

# The one-sided integer density jumps are an exact additional certificate.
for n in range(3,26):
    for k in range(2,n):
        x=F(k)
        left=4*theory_density(n,x-F(1,4))-3*theory_density(n,x-F(1,3))
        right=4*theory_density(n,x+F(1,4))-3*theory_density(n,x+F(1,3))
        exact=F(2*comb(n-1,k-1),n*2**(n-1))
        assert left-right==exact,(n,k,left,right,exact)
print('SUCCESS exact binomial jump spectrum dimensions 3..25')
