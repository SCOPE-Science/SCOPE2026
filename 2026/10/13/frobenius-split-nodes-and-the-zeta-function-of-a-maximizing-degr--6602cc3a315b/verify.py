"""Independent exact finite-field checks for the arithmetic point-count identities.
The universal statements follow from the geometric proof, not this sample test.
No external packages or auxiliary files are needed.
"""

def chi(a, p):
    v = pow(a % p, (p - 1) // 2, p)
    return 0 if v == 0 else 1 if v == 1 else -1


def count_prime(p):
    def h(x,y,z):
        return ((x*x+y*y+z*z)**3 - 27*x*x*y*y*z*z)%p
    def on_d(x,y,z):
        return (x*y*z*h(x,y,z))%p == 0
    hs=ds=0
    for x in range(p):
        for y in range(p):
            hs += h(x,y,1)==0
            ds += on_d(x,y,1)
    for x in range(p):
        hs += h(x,1,0)==0
        ds += on_d(x,1,0)
    hs += h(1,0,0)==0
    ds += on_d(1,0,0)
    return hs,ds


def count_quadratic_extension(p):
    # Enumerate F_{p^2}=F_p[t]/(t*t-d) with d nonsquare.
    d=next(a for a in range(2,p) if chi(a,p)==-1)
    q=p*p
    elems=list(range(q))
    def add(a,b):
        return (a%p+b%p)%p+p*((a//p+b//p)%p)
    def mul(a,b):
        aa,ab=a%p,a//p
        ba,bb=b%p,b//p
        return ((aa*ba+d*ab*bb)%p)+p*((aa*bb+ab*ba)%p)
    def powe(a,n):
        r=1
        while n:
            if n&1:r=mul(r,a)
            a=mul(a,a);n//=2
        return r
    def h(x,y,z):
        squares=[mul(t,t) for t in (x,y,z)]
        s=add(add(squares[0],squares[1]),squares[2])
        c=mul(mul(squares[0],squares[1]),squares[2])
        negative27=(p-27%p)%p
        return add(powe(s,3),mul(negative27,c))
    def on_d(x,y,z):
        return mul(mul(mul(x,y),z),h(x,y,z))==0
    hs=ds=0
    for x in elems:
        for y in elems:
            hs+=h(x,y,1)==0
            ds+=on_d(x,y,1)
    for x in elems:
        hs+=h(x,1,0)==0
        ds+=on_d(x,1,0)
    hs+=h(1,0,0)==0
    ds+=on_d(1,0,0)
    return hs,ds


def run():
    prime_tests=[5,7,11,13,17,19,23,29,31,37,41]
    for p in prime_tests:
        a,b=chi(-3,p),chi(-1,p)
        h,d=count_prime(p)
        assert h==p+1-4*a,(p,h,p+1-4*a)
        assert d==4*p-2-4*a-3*b,(p,d,4*p-2-4*a-3*b)
    for p in [5,7,11]:
        q=p*p
        h,d=count_quadratic_extension(p)
        assert h==q+1-4,(p,h,q-3)
        assert d==4*q-9,(p,d,4*q-9)
    print('VERIFY_OK: 11 prime-field and 3 quadratic-extension sextic/divisor censuses')

if __name__=='__main__':
    run()
