#!/usr/bin/env python3
"""Exact independent checks for dissociation sets of cycle prisms.

Run: python3 verify.py .  Uses Python 3.9+ standard library only.
"""
from collections import Counter

STATES = tuple(range(4))


def pop2(x):
    return (x & 1) + ((x >> 1) & 1)


def admissible(a,b,c):
    for layer in (0,1):
        if (b >> layer) & 1:
            neighbors = ((a >> layer)&1) + ((c >> layer)&1) + ((b >> (1-layer))&1)
            if neighbors > 1:
                return False
    return True


def transfer_numeric(z):
    T = [[0]*16 for _ in range(16)]
    for a in STATES:
        for b in STATES:
            for c in STATES:
                if admissible(a,b,c):
                    T[4*a+b][4*b+c] = z**pop2(b)
    return T


def trace_powers_numeric(T, count):
    # Sparse multiplication to compute successive powers, one row at a time.
    N=len(T)
    edges = [[(j,v) for j,v in enumerate(row) if v] for row in T]
    R=[[int(i==j) for j in range(N)] for i in range(N)]
    traces=[]
    for _ in range(count):
        Rn=[[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                v=R[i][j]
                if v:
                    for k,w in edges[j]:
                        Rn[i][k]+=v*w
        R=Rn
        traces.append(sum(R[i][i] for i in range(N)))
    return traces


def det_coeff_numeric(z):
    tr=trace_powers_numeric(transfer_numeric(z), 16)
    q=[1]
    # Newton identities for det(I-u*T), without floating-point arithmetic.
    for k in range(1,17):
        numerator=-sum(q[k-j]*tr[j-1] for j in range(1,k+1))
        assert numerator%k==0
        q.append(numerator//k)
    return q


def expected_q(z):
    return [1,-1,-2*z-2*z*z,-3*z*z-2*z**3,-2*z**3,-z**4+2*z**5,z**6]+[0]*10


def polynomial_add(a,b):
    n=max(len(a),len(b))
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]


def polynomial_scale(a,s):
    return [s*v for v in a]


def polynomial_multiply(a,b):
    result=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            result[i+j]+=x*y
    return result


QS=[[1],[-1],[0,-2,-2],[0,0,-3,-2],[0,0,0,-2],[0,0,0,0,-1,2],[0,0,0,0,0,0,1]]


def recurrence_polynomials(stop):
    # p_n = [u^n](-u Q_u/Q), the exact Newton power sums.
    p=[[]]
    for n in range(1,stop+1):
        expr=[0]
        if n<=6:
            for j in range(1,n):
                expr=polynomial_add(expr,polynomial_multiply(QS[j],p[n-j]))
            expr=polynomial_add(expr,polynomial_scale(QS[n],n))
        else:
            for j in range(1,7):
                expr=polynomial_add(expr,polynomial_multiply(QS[j],p[n-j]))
        p.append(polynomial_scale(expr,-1))
    return p


def brute(n):
    adj=[]
    for i in range(n):
        for r in range(2):
            nb=(1<<(2*i+1-r)) | (1<<(2*((i-1)%n)+r)) | (1<<(2*((i+1)%n)+r))
            adj.append(nb)
    result=Counter()
    for mask in range(1<<(2*n)):
        if all((mask & adj[v]).bit_count()<=1 for v in range(2*n) if mask & (1<<v)):
            result[mask.bit_count()]+=1
    return result


def lucas(n):
    a,b=2,1
    for _ in range(n):
        a,b=b,a+b
    return a


def main():
    # Characteristic polynomial certificate: every coefficient of det(I-uT) has
    # z-degree <= 32, so agreement at 33 distinct z-values proves equality.
    for z in range(33):
        actual=det_coeff_numeric(z)
        assert actual==expected_q(z), (z,actual)
    print('EXACT_DETERMINANT_IDENTITY_OK')

    p=recurrence_polynomials(35)
    for n in range(3,11):
        direct=brute(n)
        poly={degree:v for degree,v in enumerate(p[n]) if v}
        assert poly==direct,(n,poly,direct)
    print('EXHAUSTIVE_SUBSETS_n3_TO_n10_OK')

    for n in range(3,36):
        coeff=p[n]
        maximum=max(i for i,v in enumerate(coeff) if v)
        count=lucas(n)+(2 if n%3==0 else -1)+(2 if n%2==0 else 0)
        assert maximum==n and coeff[n]==count, (n,maximum,coeff[n],count)
    print('EXTREMAL_SEQUENCE_n3_TO_n35_OK')
    print('VERIFY_OK')


if __name__=='__main__':
    main()
