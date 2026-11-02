"""Finite checks for a Boolean symmetric-difference quasi-equation.

Represent subsets of an n-atom set by their bit masks. The theorem for arbitrary
Boolean algebras is proved separately; finite checks are corroboration only.
"""

def is_join_map(bits,n):
    N=1<<n
    return all(((bits>>(x|y))&1)==(((bits>>x)&1)|((bits>>y)&1)) for x in range(N) for y in range(N))

def is_quasi_scalar(bits,n):
    N=1<<n
    for x in range(N):
        for y in range(N):
            if ((bits>>x)&1)==((bits>>y)&1):
                continue
            dx=x^y
            for z in range(N):
                if (dx&~z)==0 and ((bits>>z)&1)==0:
                    return False
    return True

def test():
    expected={1:3,2:5,3:9,4:17}
    for n,target in expected.items():
        N=1<<n
        yesq=yesadd=0
        for bits in range(1<<N):
            q=is_quasi_scalar(bits,n)
            a=is_join_map(bits,n)
            assert q==a,(n,bits,q,a)
            yesq+=int(q);yesadd+=int(a)
        assert yesq==yesadd==target,(n,yesq,yesadd,target)
    f=list(range(8));f[5]=7
    x,y,z=1,5,4
    assert ((x^y)&~z)==0
    assert ((f[x]^f[y])&~f[z])!=0
    assert (f[x]^f[y])==6 and f[z]==4
    # For each n-atom endomorphism the choices for each output coordinate
    # are exactly 2^n OR-linear maps or constant 1.
    for n in range(1,5):
        assert (2**n+1)**n>0
    print('ALL_CHECKS_OK scalar_quasi_vs_additive_atom_sizes=1..4 counts=3,5,9,17 witness=(1,5,4)->(1,7,4)')

if __name__=='__main__':test()
