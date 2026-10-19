"""Finite independent tests of a period-doubling 2-binomial complexity formula."""
from collections import defaultdict

def substitute(depth):
    w = '0'
    for _ in range(depth):
        w = ''.join('01' if c=='0' else '00' for c in w)
    return w

def digit_word(size):
    return ''.join(str(((i+1 & -(i+1)).bit_length()-1)%2) for i in range(size))

def signature(w):
    z = 0
    t = 0
    for c in w:
        if c == '0':
            z += 1
        else:
            t += z
    return (z,t)

def classes_direct(w,n):
    return {signature(w[j:j+n]) for j in range(len(w)-n+1)}

def classes_recursion(k):
    fs = {'000','001','010','100','101'}
    for _ in range(k):
        fs = {''.join('0'+('1' if c=='0' else '0') for c in v) for v in fs} | {''.join(('1' if c=='0' else '0')+'0' for c in v) for v in fs}
    return {signature(v) for v in fs}

def main():
    w=substitute(15)
    assert w == digit_word(len(w))
    for k in range(9):
        n=3*2**k
        s=classes_direct(w,n)
        assert s == classes_recursion(k),(k,len(s),len(classes_recursion(k)))
        groups=defaultdict(set)
        for z,t in s: groups[z].add(t)
        r=2**(k+1)
        assert set(groups)=={r-1,r,r+1}
        assert len(groups[r-1])==len(groups[r+1])==2**k
        central=sorted(groups[r]); assert len(central)==k+3
        assert all(central[i+1]-central[i]==2**k for i in range(len(central)-1))
        assert len(s)==2**(k+1)+k+3
    print('VERIFY_OK substitution_depth=15 direct_scales=9 recurrence_scales=9')
if __name__=='__main__': main()
