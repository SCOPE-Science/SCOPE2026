"""Independent exact verification of upper-dominating sets on circular prisms."""
from itertools import combinations

def masks(n):
    v = 2*n
    closed = [1 << i for i in range(v)]
    for j in range(n):
        k=(j+1)%n
        for a,b in ((2*j, 2*j+1), (2*j, 2*k), (2*j+1, 2*k+1)):
            closed[a] |= 1 << b
            closed[b] |= 1 << a
    return closed

def is_minimal_dominating(s, clo):
    target=(1<<len(clo))-1
    d=0
    t=s
    while t:
        bit=t & -t; d |= clo[bit.bit_length()-1]; t-=bit
    if d != target:return False
    t=s
    while t:
        bit=t & -t
        d=0; rest=s-bit
        while rest:
            b=rest & -rest; d|=clo[b.bit_length()-1];rest-=b
        if d == target:return False
        t-=bit
    return True

def predicted(n):
    ans=set()
    for row in range(2):ans.add(sum(1 << (2*i+row) for i in range(n)))
    if n%2==0:
        for phase in range(2):ans.add(sum(1 << (2*i+((i+phase)%2)) for i in range(n)))
    if n%4==0:
        for shift in range(4):
            ans.add(sum(((3 if (i+shift)%4 in (0,1) else 0) << (2*i)) for i in range(n)))
    return ans

def run():
    for n in range(3,11):
        clo=masks(n); actual=set()
        for seq in combinations(range(2*n), n):
            mask=sum(1<<j for j in seq)
            if is_minimal_dominating(mask,clo):actual.add(mask)
        expected=predicted(n)
        assert actual==expected,(n,len(actual),len(expected), actual^expected)
        print('n=',n,'maximal-minimal cardinality=',n,'count=',len(actual))
    # Cross-check that n really is the maximum, not just the extremal level.
    for n in range(3,9):
        clo=masks(n)
        for k in range(n+1,2*n+1):
            for seq in combinations(range(2*n),k):
                assert not is_minimal_dominating(sum(1<<j for j in seq),clo),(n,k,seq)
    print('VERIFY_OK: all size-n sets n=3..10; all larger sets n=3..8')
if __name__=='__main__':run()
