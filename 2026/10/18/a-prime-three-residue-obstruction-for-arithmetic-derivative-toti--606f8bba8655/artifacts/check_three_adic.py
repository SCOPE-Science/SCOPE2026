"""Independent finite checks for the prime-three support obstruction."""
from math import isqrt

def factor(n):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:n//=d;a+=1
            out.append((d,a))
        d=3 if d==2 else d+2
    if n>1:out.append((n,1))
    return out

def Dphi(n):
    ff=factor(n)
    d=sum((n//p)*e for p,e in ff)
    ph=n
    for p,_ in ff:ph=ph//p*(p-1)
    return d,ph,ff

def run():
    hits=[]
    for n in range(3,100001,3):
        d,ph,f=Dphi(n)
        if d!=ph:continue
        hits.append(n)
        if n==9:continue
        assert f[0]==(3,1)
        assert len(f)>=2 and (len(f)-1)%2==1
        assert all(p%3==2 for p,e in f[1:])
        if len(f)==2:
            p,e=f[1]
            assert 3*e==p-2
    assert 9 in hits and 15 in hits and 3993 in hits
    for p in (5,11,17,23,29,41,47):
        n=3*p**((p-2)//3)
        d,ph,_=Dphi(n)
        assert d==ph,(p,n,d,ph)
    print('PASS: checked all multiples of 3 to 100000; prime-three restrictions hold')
    print('PASS: seven independently evaluated exact two-support examples')
    print('NOTICE: the infinite result uses the modular proof, not the scan')
if __name__=='__main__':run()
