"""Exact modular checks for ordered Bell index-shift defects.
No numerical limits in the proof are inferred from these tests.
"""
from math import factorial


def ordered_bell_mod(q, N):
    f = [1]
    row = [1]
    for n in range(1, N + 1):
        row = [1] + [(row[j-1] + row[j]) % q for j in range(1, n)] + [1]
        f.append(sum(row[j] * f[n-j] for j in range(1,n+1)) % q)
    return f


def stirling_row(n):
    row=[1]
    for m in range(1,n+1):
        row=[0]+[row[j-1]+j*(row[j] if j<len(row) else 0) for j in range(1,m+1)]
    return row


def residue_R(p,n,q):
    d=2**p-1
    inv=pow(d,-1,q)
    S=stirling_row(n)
    return (pow(2,p-1,q)*sum(factorial(j)*S[j]*pow(inv,j+1,q) for j in range(n+1)))%q


def run():
    grids=[(3,k) for k in range(1,7)]+[(5,k) for k in range(1,5)]+[(7,k) for k in range(1,4)]+[(11,k) for k in range(1,3)]+[(13,k) for k in range(1,3)]
    checks=0; prime_checks=0; preperiods=[]; direct_values=0
    for p,k in grids:
        q=p**k; P=(p-1)*p**(k-1)
        nmax=max(20,k+8)
        F=ordered_bell_mod(q,P+nmax)
        R=[residue_R(p,n,q) for n in range(nmax+1)]
        for n in range(nmax+1):
            assert (F[n+P]-F[n]+pow(p,n,q)*R[n])%q==0,(p,k,n,F[n+P],F[n],R[n])
            checks+=1
            if n<k and F[n] % p:
                assert (F[n+P]-F[n]) %p**(n+1) !=0,(p,k,n)
                assert (F[n+P]-F[n]) %p**n==0,(p,k,n)
                prime_checks+=1
        s=next(i for i in range(k+1) if all(F[n]==F[n+P] for n in range(i,nmax+1)))
        preperiods.append((p,k,s))
        if p==3:
            expected=1 if k==1 else (k-1 if k%2 else k)
            assert s==expected, (p,k,s,expected)
        direct_values+=len(F)
    # Distinct exact/integer recurrence cross-check for small n.
    A=[1]
    for n in range(1,15):
        S=stirling_row(n)
        A.append(sum(factorial(j)*S[j] for j in range(n+1)))
    f=ordered_bell_mod(10**12,14)
    assert all(a%10**12==b for a,b in zip(A,f))
    print('VERIFY_OK', 'prime_power_grids=',len(grids), 'modular_shift_checks=', checks,'sharp_valuation_tests=', prime_checks,'direct_sequence_terms=',direct_values)
    print('TERNARY_PREPERIODS', [x for x in preperiods if x[0]==3])
    print('OTHER_PREPERIODS', [x for x in preperiods if x[0]!=3])

if __name__=='__main__':run()
