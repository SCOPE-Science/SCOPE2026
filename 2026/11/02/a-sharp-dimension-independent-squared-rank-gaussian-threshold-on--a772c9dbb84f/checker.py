"""Exact, standalone checks of rank-shell Fourier formulas on binary 3-column matrices.
Uses only Python's standard library; finite checks supplement the written all-m proof.
"""
from fractions import Fraction


def binary_rank(bits,m):
    basis={}
    rank=0
    for i in range(m):
        a=(bits>>(3*i))&7
        while a:
            j=a.bit_length()-1
            if j in basis:
                a^=basis[j]
            else:
                basis[j]=a
                rank+=1
                break
    return rank


def shell_spectrum(m,rankshell):
    N=1<<(3*m)
    arr=[int(r==rankshell) for r in (binary_rank(x,m) for x in range(N))]
    step=1
    while step<N:
        for block in range(0,N,2*step):
            for j in range(block,block+step):
                x,y=arr[j],arr[j+step]
                arr[j],arr[j+step]=x+y,x-y
        step*=2
    return arr


def exact_eigvals(m,s):
    T=1<<m
    g1=[7,3,1,0][s]
    g2=[7,1,0,0][s]
    return (1, T*g1-7, T*T*g2-3*T*g1+14,
            ((T**3) if s==0 else 0) -T*T*g2+2*T*g1-8)


def poly_val(coeff,u):
    return sum(Fraction(c)*u**(i*i) for i,c in enumerate(coeff))


def qpoly(u):
    return 4*u**5+4*u**4+4*u**3+6*u**2+6*u-1


def main():
    assert qpoly(Fraction(1,8))<0<qpoly(Fraction(1,6))
    for m in (3,4,5):
        N=1<<(3*m)
        ranks=[binary_rank(u,m) for u in range(N)]
        T=1<<m
        # Rank-two count: choose 2D row space (seven choices), then onto F_2^2 maps from F_2^m: (T-1)(T-2).
        expected_mult=(1,7*(T-1),7*(T-1)*(T-2), (T-1)*(T-2)*(T-4))
        assert tuple(ranks.count(s) for s in range(4))==expected_mult,(m,[ranks.count(s) for s in range(4)],expected_mult)
        for k in range(4):
            spectrum=shell_spectrum(m,k)
            assert all(spectrum[u]==exact_eigvals(m,ranks[u])[k] for u in range(N)),(m,k)
        assert sum(expected_mult)==N
        for u in (Fraction(0), Fraction(1,8), Fraction(1,6), Fraction(3,4), Fraction(4,5), Fraction(1)):
            signs=[poly_val(exact_eigvals(m,s),u) for s in range(4)]
            assert signs[0]>0
            if u==0 or u==Fraction(1,8):assert all(v>0 for v in signs)
            elif u==1:assert signs[0]==N and all(v==0 for v in signs[1:])
            elif u==Fraction(1,6) or u==Fraction(3,4):assert signs[3]<0
            elif u==Fraction(4,5):assert signs[2]<0
        print(f'PASS m={m}, N={N}, multiplicities={expected_mult}, all integer Fourier-shell values exact')
    print('PASS rational evaluations and exact endpoint bracketing')

if __name__=='__main__': main()
