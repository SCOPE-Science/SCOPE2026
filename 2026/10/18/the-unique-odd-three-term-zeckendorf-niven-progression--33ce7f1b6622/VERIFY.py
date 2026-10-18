"""Exact elementary checks for a Zeckendorf step-two parity lemma."""

def fibonacci_up_to(n):
    a, b, ans = 1, 2, []
    while a <= n:
        ans.append(a)
        a, b = b, a+b
    return ans

def zeck_sum(n):
    assert n >= 0
    count = 0
    for f in reversed(fibonacci_up_to(n)):
        if f <= n:
            n -= f
            count += 1
    assert n == 0
    return count

def check():
    for n in range(34):
        a = [zeck_sum(n+2*j) for j in range(3)]
        assert len({v % 2 for v in a}) > 1 or a[0] == a[1] or a[1] == a[2], (n,a)
    # Base formulas for F_9=34 and F_10=55, offsets -4,-3,-2,-1.
    assert [zeck_sum(34-j) for j in range(4,0,-1)] == [3,3,3,4]
    assert [zeck_sum(55-j) for j in range(4,0,-1)] == [4,3,4,4]
    # All infinite boundary cases: k=2r or 2r+1, depending only on r mod 2.
    for r in range(5,11):
        for odd in (False,True):
            neg = {-4:r-1, -3:r-1 if odd else r-2, -2:r-1, -1:r if odd else r-1}
            pos = {0:1,1:2,2:2,3:2,4:3}
            vals = {**neg,**pos}
            for d in range(1,5):
                a = [vals[-d+2*j] for j in range(3)]
                assert len({v%2 for v in a})>1 or a[0]==a[1] or a[1]==a[2], (r,odd,d,a)
    for n in range(0,100000):
        a=[zeck_sum(n+2*j) for j in range(3)]
        assert len({v%2 for v in a})>1 or a[0]==a[1] or a[1]==a[2]
    triples=[n for n in range(1,100000,2) if all((n+2*j)%zeck_sum(n+2*j)==0 for j in range(3))]
    assert triples == [1],triples
    print('VERIFY_OK',len(triples),'odd-triple starts, 100000 parity windows')

if __name__ == '__main__':
    check()
