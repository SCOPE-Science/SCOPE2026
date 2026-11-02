"""Standalone exact-arithmetic checks for digit-sum spectrum and length theorem."""
from itertools import product

def digit_sum(n, base):
    total = 0
    while n:
        total += n % base
        n //= base
    return total

def witness(base, length_parameter, residue, copies=0):
    b, t, r = base, length_parameter, residue
    M = b**t - 1
    head = M if r == 0 else M * (b**t + b**r + 1)
    return head + sum(M*b**(3*t*j) for j in range(1, copies+1))

def main():
    count=0
    for b in range(2, 14):
        for t in range(1, 9):
            M=b**t - 1
            for r in range(t):
                for q in range(4):
                    val=witness(b,t,r,q)
                    assert val % M == 0
                    assert digit_sum(val,b) == (b-1)*(t+r+q*t)
                    if 0<r<t and q==0:
                        assert b**(2*t) <= val < b**(2*t+1)
                    count += 1
    assert count == 1728
    checked=0
    for b in range(2, 8):
        for t in range(1, 7):
            M=b**t - 1
            for k in range(1, 701):
                x=k*M
                assert digit_sum(x,b)>=t*(b-1)
                checked+=1
    length_cases=0
    for b,t in [(2,2),(2,3),(2,4),(2,5),(2,6),
                (3,2),(3,3),(3,4),(3,5),
                (4,2),(4,3),(4,4),
                (5,2),(5,3),(6,2),(7,2)]:
        M=b**t-1
        seen=set()
        for n in range(M,b**(2*t),M):
            seen.add(digit_sum(n,b))
        assert seen=={t*(b-1),2*t*(b-1)},(b,t,seen)
        for r in range(1,t):
            val=witness(b,t,r)
            assert val>=b**(2*t) and digit_sum(val,b)==(t+r)*(b-1)
        length_cases+=1
    print('VERIFY_OK constructive_cases=%d lower_bound_instances=%d exact_short_length_cases=%d arithmetic=exact' % (count,checked,length_cases))

if __name__=='__main__': main()
