"""Exact-integer checks for commuting toral endomorphism transfer calculations.

This program verifies matrix identities, Fourier image-lattice membership,
and the resulting finite collections of singular-value labels. It does
not replace the infinite-dimensional proof.
"""


def mul(a,b):
    return ((a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]),
            (a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]))


def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def transpose(a):
    return ((a[0][0],a[1][0]),(a[0][1],a[1][1]))


def power(a,n):
    if n<0:
        d=det(a)
        assert abs(d)==1
        a=((a[1][1]//d,-a[0][1]//d),(-a[1][0]//d,a[0][0]//d))
        n=-n
    res=((1,0),(0,1))
    while n:
        if n&1:res=mul(res,a)
        a=mul(a,a)
        n//=2
    return res


def in_image(b,k):
    d=det(b)
    x=b[1][1]*k[0]-b[0][1]*k[1]
    y=-b[1][0]*k[0]+b[0][0]*k[1]
    return x%d==0 and y%d==0


def predicted(n,k):
    q=2**(n//2)
    return k[0]%q==0 and k[1]%(q*(2 if n%2 else 1))==0


def main():
    u=((1,2),(1,1)); r=((0,2),(1,0)); ident=((1,0),(0,1))
    assert u==((ident[0][0]+r[0][0],ident[0][1]+r[0][1]),
               (ident[1][0]+r[1][0],ident[1][1]+r[1][1]))
    assert det(u)==-1 and det(r)==-2
    assert mul(u,r)==mul(r,u) and mul(r,r)==((2,0),(0,2))
    count=0
    for m in range(-5,6):
        a=mul(power(u,m),r)
        assert abs(det(a))==2
        for n in range(0,13):
            b=power(transpose(a),n)
            for x in range(-9,10):
                for y in range(-9,10):
                    k=(x,y)
                    assert in_image(b,k)==predicted(n,k),(m,n,k,b)
                    count+=1
            # For all output frequencies, Fourier singular weights are
            # indexed by B*l in the input space, with pairwise distinct labels.
            found=set()
            for x in range(-3,4):
                for y in range(-3,4):
                    if (x,y)==(0,0):continue
                    k=(b[0][0]*x+b[0][1]*y,b[1][0]*x+b[1][1]*y)
                    found.add(k)
                    assert predicted(n,k)
            assert len(found)==48
    assert count==11*13*19*19
    print('PASS',count,'exact lattice-membership checks; all matrix and Fourier-label checks passed')


if __name__=='__main__':
    main()
