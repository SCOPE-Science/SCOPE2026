import math
def closed(b1,b2,r,n,G=1.0):
    m=G*((1+r)*(b2**(n-1))-r)
    c=G*(b1*(1+r)*(b2**(n-1))-r)
    return m,c
def replay(b1,b2,r,N,G=1.0):
    m=G; out=[]
    for n in range(1,N+1):
        g=-r*G
        c=b1*m+(1-b1)*g
        out.append((n,m,c))
        m=b2*m+(1-b2)*g
    return out
def nstale(b1,b2,r):
    A=r/(b1*(1+r))
    if A>=1: return 0
    return math.ceil(math.log(A)/math.log(b2)-1e-12)
def nmom(b2,r):
    A=r/(1+r)
    return math.ceil(math.log(A)/math.log(b2)-1e-12)
for b1,b2 in ((.9,.99),(.7,.8),(.4,.95),(.95,.999)):
    for r in (.05,.2,.7,1,2,5,20):
        N=max(nstale(b1,b2,r),nmom(b2,r))+5
        rows=replay(b1,b2,r,N)
        for n,m,c in rows:
            mm,cc=closed(b1,b2,r,n)
            assert abs(m-mm)<2e-11*max(1,abs(mm))
            assert abs(c-cc)<2e-11*max(1,abs(cc))
        assert sum(c>1e-11 for _,_,c in rows)==nstale(b1,b2,r)
        assert sum(m>1e-11 for _,m,_ in rows)==nmom(b2,r)
        assert nstale(b1,b2,r)<=nmom(b2,r)
assert nstale(.9,.99,1)==59
assert nmom(.99,1)==69
b1=.9
thr=b1/(1-b1)
assert abs(thr-9)<1e-14
assert closed(b1,.99,8.999,1)[1]>0
assert abs(closed(b1,.99,9,1)[1])<1e-14
assert closed(b1,.99,9.001,1)[1]<0
b1=.8; b2=.5; A=b2**3
r=A*b1/(1-A*b1)
rows=replay(b1,b2,r,5)
assert nstale(b1,b2,r)==3
assert rows[2][2]>0 and abs(rows[3][2])<1e-13 and rows[4][2]<0
print("verification passed")
