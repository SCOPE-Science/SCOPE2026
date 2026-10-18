"""Exact checks for commuting square-zero pairs over finite dual numbers.

Uses only the Python standard library.  Finite-field base pairs are enumerated
for q=2,3 and every corresponding 18-variable lift space is ranked exactly.
The field and lifting classification for arbitrary q is proved in RESULT.md;
finite checks alone are not used as a proof for arbitrary fields.
"""
from itertools import product

N = 3
ZERO = (0,) * 9
E12 = (0,1,0, 0,0,0, 0,0,0)
E13 = (0,0,1, 0,0,0, 0,0,0)


def mul(a,b,q):
    return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))%q
                 for i in range(3) for j in range(3))


def add(a,b,q):
    return tuple((x+y)%q for x,y in zip(a,b))


def sub(a,b,q):
    return tuple((x-y)%q for x,y in zip(a,b))


def basis(k):
    return tuple(1 if i==k else 0 for i in range(9))


def linrank(cols,q):
    # Gaussian elimination of a matrix supplied in column form.
    A = [list(row) for row in zip(*cols)]
    width = len(cols)
    piv = 0
    for j in range(width):
        spot = next((i for i in range(piv,len(A)) if A[i][j]%q),None)
        if spot is None: continue
        A[piv],A[spot]=A[spot],A[piv]
        v=pow(A[piv][j],-1,q)
        A[piv][j:]=[(x*v)%q for x in A[piv][j:]]
        for i in range(piv+1,len(A)):
            if A[i][j]:
                scale=A[i][j]
                A[i][j:]=[(x-scale*y)%q for x,y in zip(A[i][j:],A[piv][j:])]
        piv+=1
        if piv==len(A):break
    return piv


def lift_nullity(a,b,q):
    # Constraints on A1,B1: aA1+A1a=0, bB1+B1b=0,
    # and aB1-B1a+A1b-bA1=0.
    z = ZERO
    cols=[]
    for k in range(9):
        x=basis(k)
        d1=add(mul(a,x,q),mul(x,a,q),q)
        d3=sub(mul(x,b,q),mul(b,x,q),q)
        cols.append(d1+z+d3)
    for k in range(9):
        y=basis(k)
        d2=add(mul(b,y,q),mul(y,b,q),q)
        d3=sub(mul(a,y,q),mul(y,a,q),q)
        cols.append(z+d2+d3)
    return 18-linrank(cols,q)


def base_kind(a,b,q):
    if a==ZERO and b==ZERO:return 'zero_zero'
    if a==ZERO or b==ZERO:return 'one_zero'
    if any(b==tuple(t*x%q for x in a) for t in range(1,q)):
        return 'dependent'
    return 'independent'


def theoretical(q):
    S=(q*q+q+1)*(q*q-1)
    contributions={
        'zero_zero':q**18,
        'one_zero':2*S*q**10,
        'dependent':S*(q-1)*q**(10 if q==2 else 9),
        'independent':2*S*q*(q-1)*q**8,
    }
    return contributions, sum(contributions.values())


def verify(q):
    sq=[a for a in product(range(q),repeat=9) if mul(a,a,q)==ZERO]
    S=(q*q+q+1)*(q*q-1)
    assert len(sq)==S+1,(q,len(sq),S+1)
    actual={k:0 for k in ('zero_zero','one_zero','dependent','independent')}
    tally={k:{} for k in actual}
    for a in sq:
        for b in sq:
            if mul(a,b,q)!=mul(b,a,q):continue
            # In dimension 3, commuting square-zero reductions annihilate.
            assert mul(a,b,q)==ZERO
            kind=base_kind(a,b,q)
            actual[kind]+=1
            d=lift_nullity(a,b,q)
            tally[kind][d]=tally[kind].get(d,0)+1
    expected={
        'zero_zero':1,
        'one_zero':2*S,
        'dependent':S*(q-1),
        'independent':2*S*q*(q-1),
    }
    dims={
        'zero_zero':18,
        'one_zero':10,
        'dependent':10 if q==2 else 9,
        'independent':8,
    }
    assert actual==expected,(q,actual,expected)
    assert all(tally[k]=={dims[k]:expected[k]} for k in actual),(q,tally)
    total=sum(actual[k]*q**dims[k] for k in actual)
    contributions,predicted=theoretical(q)
    assert total==predicted
    print('q=',q,'field_square_zero=',len(sq),'base_types=',actual,
          'lift_dimensions=',dims,'dual_pair_count=',total)


def verify_representatives(q):
    # Rank matrices computed from the actual defining equations, all primes.
    reps={
       'zero_zero':(ZERO,ZERO,18),
       'one_zero':(E12,ZERO,10),
       'dependent':(E12,E12,10 if q==2 else 9),
       'independent':(E12,E13,8),
    }
    for name,(a,b,expect) in reps.items():
        got=lift_nullity(a,b,q)
        assert got==expect,(q,name,got,expect)
    print('q=',q,'representative_lift_ranks=OK')


if __name__=='__main__':
    for q in (2,3):verify(q)
    for q in (2,3,5,7):verify_representatives(q)
    print('VERIFY_OK')
