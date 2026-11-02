"""Exact finite checks for the critical dyadic Lucas recurrence U[n+2]=U[n+1]+9*U[n]."""
from collections import Counter

def term(n, modulus):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (b + 9*a) % modulus
    return a

def g_mod(t, h):
    # 2-adic finite-difference approximation to f'(t)/32, accurate mod 2**h.
    n = h + 3
    mod = 1 << (5 + n + h + 2)
    delta = (term(6*(t+(1 << n))+3, mod) - term(6*t+3, mod)) % mod
    assert delta % (1 << (5+n)) == 0
    return (delta >> (5+n)) % (1 << h)

def check():
    # Matrix A=[[1,9],[1,0]], A**6=I+X, v3=A**3*(1,0).
    X = ((1260, 2520), (280, 980))
    v3 = (19, 10)
    assert all((X[i][j]//4) % 2 == int(i==j) for i in range(2) for j in range(2))
    xv = (X[1][0]*v3[0] + X[1][1]*v3[1])
    x2v = X[1][0]*(X[0][0]*v3[0] + X[0][1]*v3[1]) + X[1][1]*xv
    assert (xv-x2v//2) % 64 == 0
    # The prime 2 has exactly one critical index in Z_2 for the 6t+3 branch.
    for h in range(1, 8):
        roots = [t for t in range(1 << h) if g_mod(t, h)==0]
        assert len(roots)==1, (h, roots)
    for k in range(5, 16):
        m=1 << k
        h=(k-4+1)//2  # ceil((k-4)/2)
        critical_t = next(t for t in range(1 << h) if g_mod(t, h)==0)
        r = term(6*critical_t+3,m)
        assert r % 4 == 2
        period=3*(1 << (k-1))
        a,b=0,1
        count=Counter()
        positions=[]
        for n in range(period):
            count[a] += 1
            if a==r: positions.append(n)
            a,b = b, (b+9*a)%m
        assert (a,b)==(0,1)
        assert count[r] == (1 << (k//2)), (k,r,count[r],h,critical_t)
        assert all(n%6==3 for n in positions)
        print(f'LEVEL_OK k={k} period={period} residue={r} multiplicity={count[r]} critical_index_mod_2^{h}={critical_t}')
    print('VERIFY_OK derivative_hensel_levels=1..7 exact_frequency_levels=5..15')

if __name__=='__main__':
    check()
