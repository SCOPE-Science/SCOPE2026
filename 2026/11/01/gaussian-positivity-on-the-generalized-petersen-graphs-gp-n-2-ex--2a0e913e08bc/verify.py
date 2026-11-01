"""Exact certificates for Gaussian positivity on GP(n,2). Python 3, standard library only."""
from collections import deque


def graph(n):
    if n < 5:
        raise ValueError("Require n >= 5")
    adjacency = [set() for _ in range(2*n)]
    for i in range(n):
        for a, b in ((i, (i+1)%n), (i, n+i), (n+i, n+(i+2)%n)):
            adjacency[a].add(b)
            adjacency[b].add(a)
    assert all(len(row)==3 for row in adjacency)
    return adjacency


def distances_from(adjacency, start):
    d = [-1]*len(adjacency)
    d[start]=0
    q=deque([start])
    while q:
        a=q.popleft()
        for b in adjacency[a]:
            if d[b]<0:
                d[b]=d[a]+1
                q.append(b)
    assert all(x>=0 for x in d)
    return d


def distances(n):
    a=graph(n)
    return [distances_from(a,i) for i in range(2*n)]


def lifted_distance(layer_a,layer_b,shift):
    s=abs(shift)
    h=(s+1)//2
    if layer_a==0 and layer_b==0:
        return min(s,2+h)
    if layer_a != layer_b:
        return 1+h
    return s//2 if s%2==0 else 2+h


def quotient_distance(n,layer_a,layer_b,shift):
    return min(lifted_distance(layer_a,layer_b,shift+k*n) for k in range(-2,3))


def quadratic(D, weights):
    return sum(weights[i]*D[i][j]*weights[j] for i in weights for j in weights)


def paired(n,idx,signs):
    w={}
    for i,s in zip(idx,signs):
        assert i<n and s!=0
        w[i]=-s
        w[n+i]=s
    return w


def polynomial_multiply(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            r[i+j]+=a*b
    return r


def expected_polynomial(n):
    # Each tuple is coefficients of one monic factor, descending by degree,
    # with a nonnegative integer multiplicity. Zero roots are listed explicitly.
    FACTORS = {
      5: [([1,0],4),([1,-18],1),([1,-3],4)],
      6: [([1,0],4),([1,-6,4],1),([1,-36,314,-780,688,-192],1)],
      9: [([1,0],8),([1,-1],1),([1,-18,87,-73],1),([1,-63,669,-2380,3309,-1548],1)],
      10: [([1,0],9),([1,-2],3),([1,-14,4],2),([1,-66,252,-88],1)]
    }
    parts=FACTORS[n]
    poly=[1]
    for factor,mult in parts:
        assert factor[0]==1
        if factor != [1,0]:
            assert all((-1)**i*c>0 for i,c in enumerate(factor))
        for _ in range(mult):
            poly=polynomial_multiply(poly,factor)
    return poly


def mul(A,B):
    n=len(A)
    out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    out[i][j]+=a*b
    return out


def charpoly(A):
    # Newton power sums: c_k = -(1/k) sum_{i=1}^k c_{k-i} trace(A^i).
    n=len(A)
    powers=[[int(i==j) for j in range(n)] for i in range(n)]
    traces=[0]
    for k in range(1,n+1):
        powers=mul(powers,A)
        traces.append(sum(powers[i][i] for i in range(n)))
    coefficients=[1]
    for k in range(1,n+1):
        top=-sum(coefficients[k-i]*traces[i] for i in range(1,k+1))
        assert top%k==0
        coefficients.append(top//k)
    return coefficients


def check_finite():
    ranks={5:5,6:7,9:9,10:10}
    for n,rank in ranks.items():
        D=distances(n)
        B=[[D[0][i]+D[0][j]-D[i][j] for j in range(1,2*n)] for i in range(1,2*n)]
        calculated=charpoly(B)
        assert calculated==expected_polynomial(n), n
        # Every real negative root is ruled out by the alternating signs in
        # each nonzero factor; B is real symmetric and hence has real roots.
        assert calculated[0]==1
        nullity=0
        while calculated[-1-nullity]==0:
            nullity+=1
        assert (2*n-1-nullity)==rank
        print(f"FINITE_PSD n={n} anchored_rank={rank} nullity={nullity} characteristic_polynomial=OK")


def check_witnesses():
    for n in [7,8,11,12,13,14,15,16,17,18,19,20,21,30,60,100]:
        D=distances(n)
        if n==7:
            w={0:1,n+2:1,n+3:1,2:-1,n+0:-1,n+6:-1};target=2
        elif n==8:
            w={i:3*(-1)**i for i in range(n)}
            w.update({n+i:-(-1)**i for i in range(n)});target=16
        elif n==11:
            w=paired(n,[0,1,2,3,5,9],[1,-1,-1,1,-1,-1]);target=2
        elif n==13:
            w=paired(n,[0,1,3,4,8,9],[1,-1,1,-1,1,-1]);target=2
        elif n==15:
            w=paired(n,[0,5,10],[1,1,1]);target=6
        elif n==17:
            w=paired(n,[0,5,10],[1,1,1]);target=4
        else:
            w=paired(n,[0,2,5,7],[1,1,1,1]);target=2
        assert sum(w.values())==0
        got=quadratic(D,w)
        assert got==target,(n,got,target)
        print(f"NEGATIVE_TYPE_OBSTRUCTION n={n} quadratic_form={got} OK")


def check_lift_formula():
    cases=0
    for n in range(5,51):
        D=distances(n)
        for i in range(2*n):
            for j in range(2*n):
                formula=quotient_distance(n,int(i>=n),int(j>=n),(j%n)-(i%n))
                assert D[i][j]==formula,(n,i,j,D[i][j],formula)
                cases+=1
    print(f"UNIVERSAL_COVER_FORMULA finite_cross_checks={cases} OK")


def check_infinite_pattern():
    S=[0,2,5,7]
    labels=[(0,i) for i in S]+[(1,i) for i in S]
    block=[[lifted_distance(a,b,j-i) for b,j in labels] for a,i in labels]
    # Explicit universal-cover matrix from the path formulas, independent of n.
    expected=[
      [0,2,5,6,1,2,4,5],
      [2,0,3,5,2,1,3,4],
      [5,3,0,2,4,3,1,2],
      [6,5,2,0,5,4,2,1],
      [1,2,4,5,0,1,5,6],
      [2,1,3,4,1,0,4,5],
      [4,3,1,2,5,4,0,1],
      [5,4,2,1,6,5,1,0]
    ]
    assert block==expected
    vec=[-1]*4+[1]*4
    q=sum(vec[i]*block[i][j]*vec[j] for i in range(8) for j in range(8))
    assert q==2
    # Distinct lift displacement magnitudes for the nontrivial winding classes
    # satisfy |delta+kn|>=11 if |delta|<=7 and n>=18.
    # Under this bound, UU and UV paths cost at least 8 and 7;
    # VV paths cost at least 6. They cannot improve these eight local distances.
    assert max(expected[i][j] for i in range(4) for j in range(4))<=6
    assert max(expected[i][j] for i in range(4) for j in range(4,8))<=5
    assert max(expected[i][j] for i in range(4,8) for j in range(4,8))<=6
    for n in range(18,51):
        for a,i in labels:
            for b,j in labels:
                assert quotient_distance(n,a,b,j-i)==lifted_distance(a,b,j-i)
    print('ALL_n_GE_18_UNIVERSAL_WITNESS quadratic_form=2 analytical_wrap_bound=OK')


if __name__=='__main__':
    check_finite()
    check_witnesses()
    check_lift_formula()
    check_infinite_pattern()
    print('GP_GAUSSIAN_POSITIVITY_EXACT_CHECK_OK')
