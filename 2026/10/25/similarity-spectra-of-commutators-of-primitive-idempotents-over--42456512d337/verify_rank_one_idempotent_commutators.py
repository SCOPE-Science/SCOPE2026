"""Independent exhaustive finite-field check of rank-one idempotent commutators.

Each tested matrix is scanned directly, not generated from a frame/coframe
parametrization. Finite checks corroborate but do not prove the general theorem.
"""
from collections import Counter
from itertools import product


def field(q):
    if q == 4:
        add = [[a ^ b for b in range(q)] for a in range(q)]
        mul = []
        for a in range(q):
            row = []
            for b in range(q):
                aa, bb, z = a, b, 0
                while bb:
                    if bb & 1:
                        z ^= aa
                    bb >>= 1
                    aa <<= 1
                    if aa & 4:
                        aa ^= 7  # irreducible quadratic modulus over the binary field
                row.append(z)
            mul.append(row)
        sub = add
    else:
        add = [[(a + b) % q for b in range(q)] for a in range(q)]
        sub = [[(a - b) % q for b in range(q)] for a in range(q)]
        mul = [[a * b % q for b in range(q)] for a in range(q)]
    return add, sub, mul


def mm(A, B, n, add, mul):
    C = [0] * (n * n)
    for i in range(n):
        for k in range(n):
            a = A[i * n + k]
            if a:
                for j in range(n):
                    C[i * n + j] = add[C[i * n + j]][mul[a][B[k * n + j]]]
    return tuple(C)


def rk(A, n, q, sub, mul):
    R = [list(A[i * n:(i+1) * n]) for i in range(n)]
    pivots = 0
    inv = {a: next(b for b in range(1,q) if mul[a][b] == 1) for a in range(1,q)}
    for j in range(n):
        k = next((i for i in range(pivots,n) if R[i][j]), None)
        if k is None:
            continue
        R[pivots],R[k]=R[k],R[pivots]
        factor=inv[R[pivots][j]]
        R[pivots]=[mul[factor][x] for x in R[pivots]]
        for i in range(pivots+1,n):
            t=R[i][j]
            if t:
                R[i]=[sub[R[i][v]][mul[t][R[pivots][v]]] for v in range(n)]
        pivots += 1
        if pivots == n:
            break
    return pivots


def predicted(q, n, sub, mul):
    d=n-1
    B=(q**d-1)*q**(d-1)
    counts=Counter({'Z':1+B//(q-1), 'J2':2*B+2*(q**d-1),
                    'J3':(q**d-1)*(q**(d-1)-1)})
    for c in range(q):
        t=mul[c][sub[c][1]]  # c(c-1)
        if t:
            counts['D'+str(t)]+=B
    return counts


def main():
    scenarios=[(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3),(5,2)]
    total_idempotents=0
    total_matrices=0
    for q,n in scenarios:
        add,sub,mul=field(q)
        E=(1,)+tuple(0 for _ in range(n*n-1))
        z=(0,)*(n*n)
        seen=Counter()
        for F in product(range(q),repeat=n*n):
            total_matrices+=1
            if sum(F[i*n+i] for i in range(n))%q!=1 and q!=4:
                continue
            if rk(F,n,q,sub,mul)!=1 or mm(F,F,n,add,mul)!=F:
                continue
            total_idempotents+=1
            EF=mm(E,F,n,add,mul)
            FE=mm(F,E,n,add,mul)
            C=tuple(sub[EF[i]][FE[i]] for i in range(n*n))
            rankC=rk(C,n,q,sub,mul)
            C2=mm(C,C,n,add,mul)
            C3=mm(C2,C,n,add,mul)
            c=EF[0]
            delta=mul[c][sub[c][1]]
            assert C3==tuple(mul[delta][v] for v in C),('cubic identity',q,n,F)
            if rankC==0:
                assert C==z
                key='Z'
            elif rankC==1:
                assert C2==z
                key='J2'
            elif rankC==2 and delta==0:
                assert C2!=z and C3==z
                key='J3'
            elif rankC==2 and delta!=0:
                assert C3!=z
                key='D'+str(delta)
            else:
                raise AssertionError(('bad type',q,n,F))
            seen[key]+=1
        expected=predicted(q,n,sub,mul)
        assert seen==expected,(q,n,seen,expected)
        assert sum(seen.values())==q**(n-1)*(q**n-1)//(q-1)
        print('q=%d n=%d idempotents=%d classes=%s PASS'%
              (q,n,sum(seen.values()),dict(sorted(seen.items()))))
    print('ALL_RANK_ONE_IDEMPOTENT_COMMUTATOR_CHECKS_PASSED cases=%d scanned_matrices=%d rank_one_idempotents=%d'%
          (len(scenarios),total_matrices,total_idempotents))

if __name__=='__main__':
    main()
