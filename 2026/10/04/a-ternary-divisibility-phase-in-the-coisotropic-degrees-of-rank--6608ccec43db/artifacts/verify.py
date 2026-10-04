from math import comb, gcd

def chern_I(n,j):
    s=0
    hdeg=n+2-j
    for a in range(4):
        b=j-a
        if b<0 or b>n+1: continue
        hx=2-a
        if 0<=hx<=hdeg:
            s += comb(3,a)*comb(n+1,b)*comb(hdeg,hx)
    return s

def polar_prefix(n, upto):
    d=n+2
    I=[chern_I(n,j) for j in range(upto+1)]
    out=[]
    for i in range(upto+1):
        out.append(sum((-1)**j*comb(d-j+1,i-j)*I[j] for j in range(i+1)))
    return out

for n in range(2,501):
    got=polar_prefix(n,4)
    exp=[comb(n+2,2),2*n*(n+1),3*n*n,2*(n*n-1),comb(n+1,2)]
    assert got==exp,(n,got,exp)
    g=0
    for v in exp: g=gcd(g,v)
    assert g==gcd(3,n+1)

for n in range(2,41):
    got=polar_prefix(n,n+2)
    assert all(v==0 for v in got[5:]),(n,got)

assert polar_prefix(4,6)==[15,40,48,30,10,0,0]
assert polar_prefix(5,7)==[21,60,75,48,15,0,0,0]
print("VERIFY_OK",499,39)
