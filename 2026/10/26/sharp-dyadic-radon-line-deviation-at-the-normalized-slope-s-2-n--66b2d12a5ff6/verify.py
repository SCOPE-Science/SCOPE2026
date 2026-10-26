from fractions import Fraction


def offset(n,s,t):
    return sum(((t>>j)&1)*((s>>(n-j-1))-(s>>(n-j))) for j in range(n))


def slope_max(n,s):
    x=Fraction(0)
    p=Fraction(0)
    t=0
    for i in range(n):
        b=(s>>i)&1
        if b:
            p+=(1-x)/2
            t|=1<<(n-1-i)
        x=(x+b)/2
    return p,t


def exact(n):
    return Fraction(n,6)+Fraction(7,18)+Fraction(-1 if n%2 else 1,9*2**n)


def check():
    for n in range(1,12):
        N=1<<n
        mx=Fraction(-1); sl=[]
        for s in range(N):
            p,t=slope_max(n,s)
            assert p == Fraction(offset(n,s,t)*N-s*t,N), (n,s,t,p)
            if n<=7:
                brute=max(abs(Fraction(offset(n,s,u)*N-s*u,N)) for u in range(N))
                assert brute==p,(n,s,p,brute)
            if p>mx:
                mx=p;sl=[s]
            elif p==mx:sl.append(s)
        assert mx==exact(n),(n,mx,exact(n))
        print(f'n={n} N={N} max={mx} decimal={float(mx):.12f} slopes={sl[:12]} count={len(sl)}')
    print('VERIFIED_EXACT_N_1_TO_11_AND_ALL_COLUMNS_N_1_TO_7')

if __name__=='__main__':check()
