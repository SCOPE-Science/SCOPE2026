#!/usr/bin/env python3
"""Reproducibility checks for majority attractors on cycle coronas.

State encoding: first n bits are the cycle; the next n*r bits are r
individual private leaves at each cycle vertex. Independent exhaustive
state checks and an integer transfer-matrix characteristic-polynomial check.
"""


def update(state, n, r):
    mask = (1 << n)-1
    a = state & mask
    out = 0  # private leaves are filled at their actual bundle positions
    for i in range(n):
        same = ((a >> ((i-1) % n)) & 1) + ((a >> ((i+1) % n)) & 1)
        for j in range(r):
            same += (state >> (n + r*i + j)) & 1
        count = r+2
        bit = int(same*2 > count or (same*2 == count and (a >> i) & 1))
        out |= bit << i
        if ((a >> i) & 1):
            out |= ((1 << r)-1) << (n+r*i)
    return out


def from_uniform(a,b,n,r):
    """Core=a; r identical leaves per site carrying b."""
    s=a
    for i in range(n):
        if b & (1 << i): s |= ((1 << r)-1) << (n+r*i)
    return s


def no_isolated(n):
    c=0
    for a in range(1 << n):
        if all(((a>>i)&1)==((a>>((i-1)%n))&1) or
               ((a>>i)&1)==((a>>((i+1)%n))&1) for i in range(n)):
            c+=1
    return c


def valid_triple(u,v,w):
    la,lc=u>>1,u&1
    ca,cc=v>>1,v&1
    ra,rc=w>>1,w&1
    return ca==cc or ((la==cc or ra==cc) and (lc==ca or rc==ca))


def multiply(A,B):
    m=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(m)] for i in range(m)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def matrix():
    M=[[0]*16 for _ in range(16)]
    for u in range(4):
        for v in range(4):
            for w in range(4):
                if valid_triple(u,v,w): M[4*u+v][4*v+w]=1
    return M


def characteristic_via_newton(M):
    # Coefficients a_k of det(zI-M) = z^16 + a_1 z^15 + ... + a_16.
    n=len(M)
    powers=[]
    P=[[int(i==j) for j in range(n)] for i in range(n)]
    for k in range(1,n+1):
        P=multiply(P,M)
        powers.append(trace(P))
    coeffs=[1]
    for k in range(1,n+1):
        value=-sum(coeffs[k-j]*powers[j-1] for j in range(1,k+1))
        assert value%k==0
        coeffs.append(value//k)
    return coeffs


def polynomial_product(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return C


def test_transfer():
    M=matrix()
    expect=polynomial_product([1,0,2],[1,1,1])
    expect=polynomial_product(expect,[1,-3,-1,0,2])
    expect=polynomial_product([1]+[0]*8,expect)
    got=characteristic_via_newton(M)
    assert got==expect,(got,expect)
    print('R2_CHARACTERISTIC_POLYNOMIAL_OK')
    P=[[int(i==j) for j in range(16)] for i in range(16)]
    for n in range(1,10):
        P=multiply(P,M)
        if n<3:continue
        recurrence_count=trace(P)
        a=0
        for core in range(1<<n):
            for prior in range(1<<n):
                s=from_uniform(core,prior,n,2)
                if update(update(s,n,2),n,2)==s:a+=1
        assert a==recurrence_count,(n,a,recurrence_count)
        assert sum(1 for core in range(1<<n) if update(from_uniform(core,core,n,2),n,2)==from_uniform(core,core,n,2))==1<<n
        print('r=2 n=%d periodic=%d fixed=%d' % (n,a,1<<n))


def test_regimes():
    Q={n:no_isolated(n) for n in range(3,11)}
    M=matrix()
    P=[[int(i==j) for j in range(16)] for i in range(16)]
    T={}
    for n in range(1,10):
        P=multiply(P,M)
        T[n]=trace(P)
    full=0
    for r,n_max in [(1,9),(2,6),(3,4),(4,3)]:
        for n in range(3,n_max+1):
            fixed=per=0
            for state in range(1<<(n*(r+1))):
                x=update(state,n,r)
                y=update(x,n,r)
                fixed+=x==state
                per+=y==state
                if r>=3:
                    # Every configuration is periodic no later than one step.
                    assert update(y,n,r)==x
            expected_fixed = Q[n] if r==1 else (1<<n)
            expected_per = ((no_isolated(2*n) if n%2 else Q[n]**2) if r==1
                            else T[n] if r==2 else 1<<(2*n))
            assert (fixed,per)==(expected_fixed,expected_per),(r,n,fixed,per,expected_fixed,expected_per)
            full+=1<<(n*(r+1))
            print('all states r=%d n=%d fixed=%d periodic=%d' % (r,n,fixed,per))
    print('EXHAUSTIVE_LABELLED_STATES=%d' % full)


if __name__=='__main__':
    test_transfer()
    test_regimes()
    print('SUNLET_LEAF_PHASES_VERIFY_OK')
