"""Supplementary finite checks for additive cubes in the base-four digit-sum fixed point.
This finite check supplements, and does not replace, the supplied infinite proof.
"""

def digit_sum4(n):
    s=0
    while n:
        n,r=divmod(n,4)
        s+=r
    return s

def t(n):
    return digit_sum4(n)%4

def prefix_heights(N):
    s=0; h=[0]
    for i in range(N):
        s+=2*t(i)-3
        h.append(s)
    return h

def witness(n):
    if n%2: return None
    if n%4==0:return 0
    m=n//2
    h=1
    while 4**h<=m+(n-2)//4 or (3*h-digit_sum4(m-1))%2==0:
        h+=1
    k=4**h-m
    a=4*(k-(n-2)//4)
    assert a>=0
    return a

def verify():
    N=100000
    H=prefix_heights(N)
    for j in range(N+1):
        m,r=divmod(j,4)
        s=t(m)
        formula=2*sum((s+i)%4 for i in range(r))-3*r
        assert H[j]==formula, ('height', j,H[j],formula)
    # Full-exhaustive finite-index test of the odd-order obstruction.
    for n in range(1,240,2):
        assert all(not (H[a+2*n]-2*H[a+n]+H[a]==0 and
                        H[a+3*n]-2*H[a+2*n]+H[a+n]==0)
                   for a in range(N-3*n)),('odd',n)
    # Explicit witnesses beyond the finite prefix can be huge; direct small orders.
    for n in range(2,121,2):
        a=witness(n)
        hs=[H[a+j*n] for j in range(4)]
        assert hs==[0]*4,('even',n,a,hs)
    # Arbitrarily large witness formula validated at its digit endpoints without constructing prefixes.
    for n in range(2,20001,2):
        a=witness(n)
        if n%4==0: assert a==0
        else:
            u=(a+n)//4
            v=(a+3*n)//4
            assert (a+n)%4==2 and (a+3*n)%4==2
            assert t(u)%2==1 and t(v)%2==1 and v-u==n//2
    # Additional direct-modular checks of the even-alphabet obstruction.
    for q in range(2,18,2):
        def tq(i):
            x=i; z=0
            while x:
                x,r=divmod(x,q); z+=r
            return z%q
        M=2500
        h=[0]
        for i in range(M):h.append(h[-1]+2*tq(i)-(q-1))
        for i,v in enumerate(h):
            assert (v%4==0 if i%2==0 else v%2==1), ('modular',q,i)
        for n in range(1,79,2):
            for a in range(M-3*n):
                assert (h[a+2*n]-2*h[a+n]+h[a]!=0 or
                        h[a+3*n]-2*h[a+2*n]+h[a+n]!=0),('generic',q,n,a)
    print('VERIFY_OK universal_even_bases=2..16 height_modular_N=2500 odd_order_no_cube_n<79 height_formula_N=100000 all_odd_orders_n<240 explicit_even_witness_n<=120 digit_witness_all_even_n<=20000')
if __name__=='__main__':verify()
