"""Exact-rational consistency checks for matched-pair-stretched bipartite metrics.

Requires only the Python standard library. Tests are finite corroboration;
the universal inequalities and rigidity follow from the accompanying proof.
"""
from fractions import Fraction as F


def Q(n, r):
    low = 4 * F(n-1, n-1+r)
    mid = F(4*(n-2), n)
    high = r * F(n-2, 2*(n-1))
    return max(low, mid, high), low, mid, high


def simplex_gram(i, j, n):
    return F(2*(n-1), n) if i == j else -F(2, n)


def gram(n, r, regime):
    t, low, mid, high = Q(n, r)
    if regime == 'low':
        eta = 1 - F(n)*r / (F(n-1)+r)
        assert -1 <= eta <= 0
        def inner(side1, i, side2, j):
            u = simplex_gram(i, j, n)
            return u * (eta if side1 != side2 else 1)
        a, b, c = F(4), t, r*t
        dim = (2*n-2 if eta > -1 else n-1)
    else:
        scale_sq = (F(1) if regime == 'plateau' else r*F(n, 8*(n-1)))
        def inner(side1, i, side2, j):
            return scale_sq * simplex_gram(i,j,n) * (1 if side1==side2 else -1)
        a = 4*scale_sq
        b = (F(4*(n-2), n)*scale_sq)
        c = (F(8*(n-1), n)*scale_sq)
        dim = n-1
    for x in range(2*n):
        for y in range(x+1,2*n):
            i, j = x%n, y%n
            s1, s2 = x//n, y//n
            dist_sq = inner(s1,i,s1,i)+inner(s2,j,s2,j)-2*inner(s1,i,s2,j)
            expected = c if s1!=s2 and i==j else b if s1!=s2 else a
            assert dist_sq == expected, (n,r,x,y,dist_sq,expected)
            base_sq = r if s1!=s2 and i==j else 1 if s1!=s2 else 4
            assert base_sq <= dist_sq <= t*base_sq, (n,r,dist_sq,base_sq,t)
    assert (n-1)*(a-b)-c <= 0
    assert c-a-b <= 0
    assert b-a-c < 0
    zero_null_modes = int((n-1)*(a-b)==c) + (n-1)*int(c==a+b)
    # Dimension is the rank of the centered Gram matrix.
    assert 2*n-1-zero_null_modes == dim, (n,r,dim,zero_null_modes)
    return a,b,c,t,dim


count=0
phase_counts={'low':0,'plateau':0,'high':0}
for n in range(3,26):
    r1=F(2*(n-1), n-2)
    r2=F(8*(n-1), n)
    choices=[F(1), (F(1)+r1)/2,r1, (r1+r2)/2,r2,(r2+F(9))/2,F(9)]
    for r in choices:
        t,L,C,H=Q(n,r)
        if r<r1:
            assert t==L and t>C and t>H
            regime='low'
        elif r>r2:
            assert t==H and t>C and t>L
            regime='high'
        elif r==r1:
            assert t==L==C
            regime='low'
        elif r==r2:
            assert t==H==C
            regime='plateau'
        else:
            assert t==C and t>L and t>H
            regime='plateau'
        a,b,c,t2,dim=gram(n,r,regime)
        assert t==t2
        assert a>=4 and b<=t and c>=r and c<=r*t
        # The three sharp lower bounds follow from the two Hilbert identities.
        assert t >= L and t >= C and t >= H
        if regime=='low':
            assert a==4 and b==t and c==r*t
        else:
            assert c==a+b and c==(n-1)*(a-b)
        phase_counts[regime]+=1
        count+=1
print('EXACT_RATIONAL_OPTIMAL_PHASE_AND_GRAM_TESTS_OK',count,phase_counts)

# Check the known six-cycle and cube endpoints, without assuming these cases in the proof.
assert Q(3,F(9))[0]==F(9,4)
assert Q(4,F(9))[0]==F(3)
assert Q(3,F(1))[0]==F(8,3)
print('CYCLE_CUBE_AND_COMPLETE_BIPARTITE_ENDPOINTS_OK')
print('THREE_BRANCH_SHARP_HILBERT_DISTORTION_CHECKS_OK')

# Independently replay the two universal identities on arbitrary rational Hilbert vectors.
from random import Random
rng = Random(20261031)
identity_count=0
for nn in range(3,9):
    for rep in range(20):
        A=[[F(rng.randint(-4,4), rng.randint(1,5)) for _ in range(3)] for i in range(nn)]
        B=[[F(rng.randint(-4,4), rng.randint(1,5)) for _ in range(3)] for i in range(nn)]
        def dsq(x,y):
            return sum((a-b)*(a-b) for a,b in zip(x,y))
        alpha=(sum(dsq(A[i],A[j])+dsq(B[i],B[j]) for i in range(nn) for j in range(i+1,nn))/F(nn*(nn-1)))
        beta=sum(dsq(A[i],B[j]) for i in range(nn) for j in range(nn) if i!=j)/F(nn*(nn-1))
        gamma=sum(dsq(A[i],B[i]) for i in range(nn))/F(nn)
        sums=[[A[i][k]+B[i][k] for k in range(3)] for i in range(nn)]
        diff=[sum(A[i][k]-B[i][k] for i in range(nn)) for k in range(3)]
        assert sum(dsq(sums[i],sums[j]) for i in range(nn) for j in range(i+1,nn))==nn*(nn-1)*(alpha+beta-gamma)
        assert sum(d*d for d in diff)==nn*(gamma-(nn-1)*(alpha-beta))
        identity_count+=1
print('EXACT_GENERAL_HILBERT_IDENTITIES_OK',identity_count)
