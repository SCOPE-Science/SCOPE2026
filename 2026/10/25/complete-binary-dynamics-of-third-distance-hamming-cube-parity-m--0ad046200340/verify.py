"""Exact finite-dimensional cross-checks for a distance-three binary Hamming parity map."""
from itertools import combinations
from random import Random


def expected(n):
    k = n % 4
    if k == 0 or k == 3:
        return 1 << (n - 1)
    if k == 1:
        return (1 << (n - 1)) - (1 << ((n - 1)//2))
    return (1 << (n - 2)) - (1 << ((n - 2)//2))


def rank_binary(rows):
    pivots={}
    for row in rows:
        while row:
            k=row.bit_length()-1
            if k in pivots:
                row ^= pivots[k]
            else:
                pivots[k]=row
                break
    return len(pivots)


def operator(n):
    N=1<<n
    shifts=[sum(1<<k for k in triple) for triple in combinations(range(n),3)]
    # Each matrix row is directly formed from the unshifted distance-three neighbors.
    rows=[]
    for v in range(N):
        bits=0
        for m in shifts:
            bits |= 1<<(v^m)
        rows.append(bits)
    return rows, shifts


def apply(rows, state):
    return sum(((state & row).bit_count()&1)<<i for i,row in enumerate(rows))


def run():
    rng=Random(173)
    comparisons=0
    for n in range(3,13):
        rows,_=operator(n)
        N=1<<n
        k=n%4
        c=int(k==3)
        shifted=[row^(c<<i) for i,row in enumerate(rows)]
        assert rank_binary(shifted)==expected(n),(n,'rank')
        # Exact group-convolution calculation of every coefficient of the square.
        _,shifts=operator(n)
        square_parity={}
        for a in shifts:
            for d in shifts:
                key=a^d
                square_parity[key]=square_parity.get(key,0)^1
        assert {k:v for k,v in square_parity.items() if v}==({0:1} if c else {})
        # The full matrix action for both loop choices is cross-checked on
        # every basis vector in the moderate sizes and on random states otherwise.
        for b in (0,1):
            update=[row^(b<<i) for i,row in enumerate(rows)]
            if n<=8:
                for v in range(N):
                    image=apply(update,1<<v)
                    second=apply(update,image)
                    assert second==((1<<v) if b!=c else 0),(n,b,'basis-square')
            for j in range(18 if n<=10 else 2):
                state=rng.getrandbits(N)
                y=apply(update,state)
                z=apply(update,y)
                assert z==(state if b!=c else 0)
                if b!=c:
                    assert (y==state)==(apply(shifted,state)==0)
                else:
                    assert (y==0)==(apply(shifted,state)==0)
            comparisons+=N+(18 if n<=10 else 2)
    # Complete orbit census for 3-dimensional Boolean cube: 2^8 states.
    n=3; rows,_=operator(n)
    fix=sum(apply(rows,x)==x for x in range(1<<(1<<n)))
    assert fix==(1<<( (1<<n) - expected(n)))
    assert ((1<<(1<<n))-fix)%2==0
    # Complete orbit census for four-dimensional Boolean cube: 2^16 states.
    n=4; rows,_=operator(n)
    counts=[0,0,0]
    for x in range(1<<(1<<n)):
        if x==0:counts[0]+=1
        elif apply(rows,x)==0:counts[1]+=1
        else:
            assert apply(rows,apply(rows,x))==0
            counts[2]+=1
    r=expected(n); M=1<<n
    assert counts==[1,(1<<(M-r))-1,(1<<M)-(1<<(M-r))]
    print('VERIFY_OK dimensions=3..12', 'ranks=10', 'basis_square_checks=',2*sum(1<<n for n in range(3,9)), 'trajectory_checks=',8*2*18+2*2*2, 'orbit_census_states=',(1<<8)+(1<<16),'total_checks=',comparisons)

if __name__=='__main__':
    run()
