"""Check local-degree counts in the acyclic-orientation flip graph of K_{a,b}."""
from collections import Counter
from itertools import product
from math import factorial


def positive_compositions(n, k):
    if k == 0:
        if n == 0:
            yield ()
        return
    if k == 1:
        if n >= 1:
            yield (n,)
        return
    for v in range(1, n-k+2):
        for rest in positive_compositions(n-v, k-1):
            yield (v,) + rest


def predicted(a, b):
    hist = Counter()
    for length in range(2, a+b+1):
        for first in (0, 1):
            colors = [(first+i)%2 for i in range(length)]
            ca, cb = colors.count(0), colors.count(1)
            if ca > a or cb > b:
                continue
            for sizes_a in positive_compositions(a, ca):
                for sizes_b in positive_compositions(b, cb):
                    ia = ib = 0
                    blocks = []
                    den = 1
                    for color in colors:
                        if color == 0:
                            size = sizes_a[ia]
                            ia += 1
                        else:
                            size = sizes_b[ib]
                            ib += 1
                        blocks.append(size)
                        den *= factorial(size)
                    degree = sum(x*y for x, y in zip(blocks, blocks[1:]))
                    hist[degree] += factorial(a)*factorial(b)//den
    return hist


def falling(n, j):
    return factorial(n)//factorial(n-j)


def simple_count(a, b):
    if min(a,b) == 1:
        return 2**max(a,b)
    t = 2*sum(falling(a,j)*falling(b,j) for j in range(1,min(a,b)))
    if a>b:
        t += falling(a,b-1)*factorial(b)*(2**(a-b+1)-2)
    if b>a:
        t += falling(b,a-1)*factorial(a)*(2**(b-a+1)-2)
    return t


def acyclic(bits, a, b):
    n=a+b
    successors=[[] for _ in range(n)]
    for i in range(a):
        for j in range(b):
            if bits & (1 << (i*b+j)):
                successors[i].append(a+j)
            else:
                successors[a+j].append(i)
    state=[0]*n
    def visit(v):
        if state[v] == 1:
            return False
        if state[v] == 2:
            return True
        state[v]=1
        for w in successors[v]:
            if not visit(w):
                return False
        state[v]=2
        return True
    return all(visit(i) for i in range(n) if state[i]==0)


def observed(a, b):
    good={x for x in range(1<<(a*b)) if acyclic(x,a,b)}
    histogram=Counter()
    for x in good:
        degree=sum((x^(1<<k)) in good for k in range(a*b))
        histogram[degree] += 1
    if min(a,b) >= 2:
        simple={x for x in good if sum((x^(1<<k)) in good for k in range(a*b))==a+b-1}
        assert all((x^(1<<k)) not in simple for x in simple for k in range(a*b))
    return histogram


def main():
    tests=0
    for a in range(1,5):
        for b in range(a,5):
            theo=predicted(a,b)
            brute=observed(a,b)
            assert theo == brute, (a,b,theo,brute)
            assert min(theo)==a+b-1
            assert max(theo)==a*b
            assert theo[a+b-1]==simple_count(a,b)
            assert theo[a*b]==2**a+2**b-2
            assert sum(d*c for d,c in theo.items())%2==0
            tests+=1
    for a,b,total,simple,maxim in ((3,3,230,90,14), (4,4,6902,1472,30), (4,5,41506,6280,46), (5,5,329462,36850,62)):
        h=predicted(a,b)
        assert sum(h.values())==total
        assert h[a+b-1]==simple
        assert h[a*b]==maxim
        tests+=1
    print('PRIMARY_DIRECT_DAG_AND_COMPOSITION_PASS',tests)

if __name__=='__main__':
    main()
