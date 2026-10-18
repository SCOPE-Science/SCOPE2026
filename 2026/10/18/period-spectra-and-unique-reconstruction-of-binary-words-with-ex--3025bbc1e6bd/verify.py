"""Independent exhaustive and spot checks of fixed-weight-two period profiles."""
from collections import Counter
from random import Random


def direct(n, i, j):
    w = (1 << i) | (1 << j)
    return tuple(p for p in range(1, n)
                 if (w & ((1 << (n-p))-1)) == ((w >> p) & ((1 << (n-p))-1)))


def predicted(n, i, j):
    p = j-i
    m = max(n-i, j+1)
    tail = tuple(range(m,n))
    return ((p,) + tail) if i < p and i+2*p >= n else tail


def closed(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    return n//2 - 1 + sum((min(n-p,3*p-n)+1)//2 for p in range(n//3+1,n))


def quasi(n):
    # Integer numerator over 12; 12*(n^2/12 + 2n/3 - c_r).
    correction12 = (12,21,8,21,12,17)[n%6]
    v=n*n+8*n-correction12
    assert v%12==0
    return v//12


def independent(n):
    return len({direct(n,i,j) for i in range(n) for j in range(i+1,n)})


def main():
    cases=0
    for n in range(2,101):
        seen=set()
        profiles=Counter()
        for i in range(n):
            for j in range(i+1,n):
                a=direct(n,i,j)
                b=predicted(n,i,j)
                assert a==b, (n,i,j,a,b)
                cases+=1
                seen.add(a)
                profiles[a] += 1
        if n>=4:
            singles=sum(v == 1 for v in profiles.values())
            predicted_singles=sum((p-n)%2 for p in range(n//3+1,n-1)) + int(n%2==0 and n>=6)
            assert singles==predicted_singles,(n,singles,predicted_singles)
        assert len(seen)==closed(n), (n,len(seen),closed(n))
        if n>=4:
            assert len(seen)==quasi(n), (n,len(seen),quasi(n))
    random=Random(493128)
    for n in (101,128,177,256,512,1000):
        for _ in range(1000):
            i,j=sorted(random.sample(range(n),2))
            assert direct(n,i,j)==predicted(n,i,j),(n,i,j)
            cases+=1
        assert closed(n)==quasi(n),n
    print('PERIOD_TWO_MARKER_CHECKS_PASSED', 'checked_pairs', cases,
          'complete_lengths','2..100', 'large_spot_lengths', '101,128,177,256,512,1000')

if __name__=='__main__': main()
