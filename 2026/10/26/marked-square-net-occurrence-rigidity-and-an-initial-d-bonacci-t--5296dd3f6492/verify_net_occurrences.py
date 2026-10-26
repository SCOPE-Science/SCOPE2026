"""Independent exact occurrence enumerator for a marked-square word family."""
from collections import Counter
from itertools import product


def observed_nets(t):
    """Enumerate all proper nonempty factors and their net occurrences."""
    n = len(t)
    nets = []
    for width in range(1, n):
        counts = Counter(t[i:i+width] for i in range(n-width+1))
        if all(v == 1 for v in counts.values()):
            continue
        extended = Counter(t[i:i+width+1] for i in range(n-width))
        for i in range(n-width+1):
            if counts[t[i:i+width]] < 2:
                continue
            if i and extended[t[i-1:i+width]] != 1:
                continue
            if i+width < n and extended[t[i:i+width+1]] != 1:
                continue
            nets.append((i, width))
    return sorted(nets)


def zimin(r):
    w = '0'
    for k in range(1,r):
        w = w + str(k) + w
    return w


def db(d,k):
    w='0'
    for _ in range(k):
        w=''.join('0'+str(int(a)+1) if int(a)<d-1 else '0' for a in w)
    return w


def expected(x):
    m=len(x)
    return sorted([(0,2*m),(m+1,m),(2*m+1,2*m)])


def main():
    totals=0
    for q in (2,3):
        for m in range(1,10 if q==2 else 8):
            for interior in product('012'[:q], repeat=max(0,m-2)):
                x='0'+''.join(interior)+'0' if m>1 else '0'
                if '00' in x: continue
                z='z'
                t=x+z+x+x+z+x[:-1]
                got=observed_nets(t)
                assert got==expected(x),(q,m,x,got,expected(x))
                totals+=1
    print('MARKED_WORD_TESTS',totals,'PASS')
    for d in range(2,9):
        for k in range(d+2):
            t=db(d,k)
            count=0 if k<2 else 2 if k<=d else 3
            got=observed_nets(t)
            assert len(got)==count,(d,k,got,count)
            if k==d+1:
                x=zimin(d-1)
                assert t==x+str(d-1)+x+x+str(d-1)+x[:-1]
                assert got==expected(x),(d,got,expected(x))
            if k==d:
                assert t==zimin(d)
        print('D_BONACCI',d,'ITERATES',d+2,'PASS')
    print('TOTAL_STATUS PASS')

if __name__ == '__main__':main()
