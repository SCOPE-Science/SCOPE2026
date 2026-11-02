"""Exact finite residue checks for the critical fifteenth Stirling column.

Uses only Python standard library. These are checks, not a substitute for the
unrestricted 2-adic proof. All modular exponentiations are exact.
"""
from math import comb, factorial

K = 15
FAC = factorial(K)
FAC_TWO = 1 << 11
assert FAC % FAC_TWO == 0 and (FAC // FAC_TWO) % 2 == 1


def s_mod(n, width):
    """S(n,15) modulo 2**width, using the exact inclusion-exclusion formula."""
    base = 1 << width
    lifted = base * FAC_TWO
    numerator = sum(((-1) ** (K-j)) * comb(K,j) * pow(j,n,lifted)
                    for j in range(1,K+1)) % lifted
    assert numerator % FAC_TWO == 0
    return ((numerator // FAC_TWO) * pow(FAC // FAC_TWO,-1,base)) % base


def difference_mod(N,b,u,width):
    H = b*(1 << N) - 5
    e = H-N-1
    a = b+(1 << e)*u
    return (s_mod(a*(1 << N),width)-s_mod(b*(1 << N),width)) % (1 << width)


def check_instance(N,b,levels=8):
    H = b*(1 << N)-5
    e = H-N-1
    assert e > 0
    r = 1
    witnesses=[]
    for t in range(1,levels+1):
        width = H+t+1
        d = difference_mod(N,b,r,width)
        assert d % (1 << (H+t)) == 0
        if d:
            assert d == 1 << (H+t)
            witness = r
            r += 1 << t
        else:
            witness = r+(1 << t)
        witness += 1 << (t+1)
        x = difference_mod(N,b,witness,width)
        assert x == 1 << (H+t), (N,b,t,x)
        assert witness % 2 == 1
        witnesses.append((t,witness))
    return witnesses


def check_congruences():
    r=10
    mod = 1 << (r+13)
    Q = [(j, ((pow(j,1 << r,mod)-1)//(1 << (r+2)))%2048)
         for j in range(3,16,2)]
    assert Q == [(3,573),(5,415),(7,374),(9,1146),
                 (11,1355),(13,1137),(15,988)]
    assert sum(comb(15,j)*q for j,q in Q)%2048==1024
    for n in [16,32,48,64,128,1024,2048]:
        T=(105+5005*pow(3,n,128)+3003*pow(5,n,128)+15*pow(7,n,128))%128
        assert T==64
    return Q


if __name__=='__main__':
    Q=check_congruences()
    all_cases=[]
    for N,b,T in [(10,1,9),(10,2,7),(11,1,7),(11,2,5)]:
        w=check_instance(N,b,T)
        all_cases.append((N,b,T,w[:3]))
        print('CASE_OK',N,b,'levels',T,'initial_witnesses',w[:3])
    print('CERTIFICATE_Q',Q)
    print('VERIFY_OK cases',len(all_cases),'total_levels',sum(z[2] for z in all_cases))
