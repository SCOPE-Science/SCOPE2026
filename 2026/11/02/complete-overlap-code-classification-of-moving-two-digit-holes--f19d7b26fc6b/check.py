"""Independent finite checks for the moving-forbidden-bigram overlap formulas.

No random sampling is used. Finite checks support, but do not replace,
the all-length algebraic proof.
"""
from itertools import product
from math import sqrt, log

def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def pfx_count_matrix(alphabet, holes, n):
    q=alphabet
    if n==1: return q
    v=[1]*q
    for u,w in holes[:n-1]:
        v=[sum(v)-v[u]*(j==w) for j in range(q)]
    return sum(v)

def pfx_count_direct(alphabet,holes,n):
    return sum(all((s[k],s[k+1])!=holes[k] for k in range(n-1)) for s in product(range(alphabet), repeat=n))

def h(delta,q): return [[q,1],[-1,-int(delta)]]

def overlap_count(q,holes,n):
    if n==1:return q
    v=[[q,1]]
    for k in range(n-2):
        delta=holes[k][1]==holes[k+1][0]
        v=matmul(v,h(delta,q))
    return matmul(v,[[q],[-1]])[0][0]

def check_all():
    tests=0
    for q,n in [(3,3),(3,4),(4,3)]:
        pairs=list(product(range(q),repeat=2))
        for holes in product(pairs,repeat=n-1):
            a=pfx_count_direct(q,holes,n)
            b=pfx_count_matrix(q,holes,n)
            c=overlap_count(q,holes,n)
            assert a==b==c,(q,n,holes,a,b,c)
            tests+=1
    print('EXHAUSTIVE_MOVING_BIGRAM_PREFIX_COUNTS_PASS',tests)
    for q in (3,4,5,7):
        # Each binary overlap code of length 4 is realizable, and uniquely
        # determines the displayed prefix counts through length 6.
        signatures={}
        for seq in product((0,1),repeat=4):
            holes=tuple((0,0 if v else 1) for v in seq)+( (0,0),)
            counts=tuple(overlap_count(q,holes,n) for n in range(2,7))
            assert counts not in signatures, (q,seq,signatures.get(counts))
            signatures[counts]=seq
        assert len(signatures)==16
    print('BINARY_OVERLAP_CODE_SEPARATION_PASS',4*16)
    for q in (3,4,5,7):
        values=[]
        for sig in ((0,0),(0,1),(1,1)):
            c=matmul(h(sig[0],q),h(sig[1],q))
            tr=c[0][0]+c[1][1]
            det=c[0][0]*c[1][1]-c[0][1]*c[1][0]
            t=q*q-2+int(sig==(1,1))
            d=(1-q)**sum(sig)
            assert tr==t and det==d
            lam=(tr+sqrt(tr*tr-4*det))/2
            # Compare to the b-by-b product for a representative 2-periodic
            # hole, using a direct power-method Rayleigh quotient.
            hh=[(0,0 if s else 1) for s in sig]
            def a(pair):
                u,v=pair
                return [[0 if (i,j)==(u,v) else 1 for j in range(q)] for i in range(q)]
            prod=matmul(a(hh[0]),a(hh[1]))
            vec=[1.0]*q
            for _ in range(100):
                nxt=[sum(y*z for y,z in zip(row,vec)) for row in prod]
                norm=max(nxt)
                vec=[t/norm for t in nxt]
            estimate=max(sum(y*z for y,z in zip(row,vec)) for row in prod)
            assert abs(estimate-lam)<1e-11
            values.append(lam)
        assert values[0]<values[1]<values[2]
        print('TWO_PHASE_PERRON_ORDER_PASS',q, [round(t,9) for t in values])
    print('ASYMPTOTIC_DIMENSIONS_AND_INFINITE_LENGTH_USE_ANALYTIC_PROOF')

if __name__=='__main__': check_all()
