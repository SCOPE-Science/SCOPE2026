"""Direct finite-field checks for square-zero elements in a two-cycle truncated path algebra."""
from itertools import product


def polynomial_mul(x,y,degree,q):
    ans=[0]*degree
    for i,v in enumerate(x):
        for j,w in enumerate(y):
            if i+j<degree:
                ans[i+j]=(ans[i+j]+v*w)%q
    return tuple(ans)


def square_zero_direct(a,d,b,c,q):
    # Matrices [[a(z),z*b(z)],[c(z),d(z)]] over truncated paths.
    m=len(b)
    aa=polynomial_mul(a,a,m+1,q)
    dd=polynomial_mul(d,d,m+1,q)
    bc=polynomial_mul(b,c,m,q)
    top=tuple((aa[i]+(bc[i-1] if i>=1 else 0))%q for i in range(m+1))
    bot=tuple((dd[i]+(bc[i-1] if i>=1 else 0))%q for i in range(m+1))
    s=tuple((a[i]+d[i])%q for i in range(m+1))
    return not any(top+bot+polynomial_mul(s,b,m,q)+polynomial_mul(s,c,m,q))


def components(a,d,b,c,q):
    a1,a2=a[1:3]
    d1,d2=d[1:3]
    b0,b1,b2=b
    c0,c1,c2=c
    base=(d1+a1)%q==0 and (d2+a2)%q==0
    one=base and c0==0 and (b0*c1+a1*a1)%q==0 and (b0*c2+b1*c1+2*a1*a2)%q==0
    two=base and b0==0 and (c0*b1+a1*a1)%q==0 and (c0*b2+c1*b1+2*a1*a2)%q==0
    three=a1==d1==b0==c0==b1==0
    four=a1==d1==b0==c0==c1==0
    return (one,two,three,four)


def enumerate_independently(q):
    # a3,d3 occur freely in the square-zero equations, so enumerate
    # the remaining ten coordinates and restore the q^2 multiplicity.
    good=0
    badcoverage=0
    singles=[0]*4
    for a1,a2,d1,d2,b0,b1,b2,c0,c1,c2 in product(range(q),repeat=10):
        a=(0,a1,a2,0)
        d=(0,d1,d2,0)
        b=(b0,b1,b2)
        c=(c0,c1,c2)
        ok=square_zero_direct(a,d,b,c,q)
        components_here=components(a,d,b,c,q)
        if ok:good+=1
        if ok!=any(components_here):badcoverage+=1
        for j,x in enumerate(components_here):
            if x:singles[j]+=1
    exact=good*q*q
    expected=q**6*(4*q-3)
    print('field_order',q,'square_zero_count',exact,'formula',expected,
          'component_raw_memberships',tuple(t*q*q for t in singles),
          'bad_component_coverage',badcoverage)
    assert badcoverage==0 and exact==expected


def group_algebra_change_of_variable(q=7):
    # k[C_7] = k[t]/(t^7), t=r-1, and inversion r -> r^-1.
    deg=7
    t=(0,1,0,0,0,0,0)
    r=(1,1,0,0,0,0,0)
    r_inv=tuple((-1)**i%q for i in range(deg))
    numerator=tuple((r[i]-r_inv[i])%q for i in range(deg))
    denominator=tuple((r[i]+r_inv[i])%q for i in range(deg))
    assert denominator[0]==2
    two_inv=pow(2,-1,q)
    h=tuple((two_inv*denominator[i])%q for i in range(deg))
    e=(1,0,0,0,0,0,0)
    w=tuple((e[i]-h[i])%q for i in range(deg))
    inverse=(0,)*deg
    power=e
    result=[0]*deg
    for _ in range(deg):
        for i in range(deg):result[i]=(result[i]+power[i])%q
        power=polynomial_mul(power,w,deg,q)
    inv=tuple((two_inv*x)%q for x in result)
    y=polynomial_mul(numerator,inv,deg,q)
    assert y[0]==0 and y[1]==1
    # r -> r^-1 sends t -> r^-1-1; verify y -> -y.
    tinv=tuple((r_inv[i]-e[i])%q for i in range(deg))
    def sub(poly,arg):
        ans=[0]*deg
        power=e
        for coefficient in poly:
            for j in range(deg):ans[j]=(ans[j]+coefficient*power[j])%q
            power=polynomial_mul(power,arg,deg,q)
        return tuple(ans)
    assert sub(y,tinv)==tuple((-x)%q for x in y)
    ypower=e
    for j in range(1,deg+1):
        ypower=polynomial_mul(ypower,y,deg,q)
        if j<deg: assert ypower[j]==1
        else: assert not any(ypower)
    print('modular_dihedral_change_of_variable', 'PASS')


if __name__=='__main__':
    enumerate_independently(3)
    group_algebra_change_of_variable()
    print('VERIFY_OK')
