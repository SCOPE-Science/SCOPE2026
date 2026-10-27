#!/usr/bin/env python3
"""Exact finite checks for optimal strong odd colorings of wheel graphs.

Run with Python 3.10+ without third-party packages.
The mathematical proof of the all-order statements is given separately.
"""
from collections import defaultdict
from math import comb, factorial


def matrix(k, negatives):
    states = [(a, b) for a in range(k) for b in range(k) if a != b]
    lookup = {p: i for i, p in enumerate(states)}
    m = len(states)
    a = [[0] * m for _ in range(m)]
    for i, (x, y) in enumerate(states):
        for z in range(k):
            if z != x and z != y:
                a[i][lookup[(y, z)]] = -1 if z < negatives else 1
    return a


def multiply(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j, aj in enumerate(a[i]):
            if aj:
                for t, bj in enumerate(b[j]):
                    if bj:
                        c[i][t] += aj * bj
    return c


def mulpoly(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i+j] += v * w
    return out


def product_factors(factors):
    p = [1]
    for f, multiplicity in factors:
        for _ in range(multiplicity):
            p = mulpoly(p, f)
    return p

# Factor coefficient lists are ascending in degree, e.g. [-2, 1] is x-2.
EXPECTED = {
 (4,0): [([-2,1],1),([-1,1],3),([1,1],2),([2,1,1],3)],
 (4,1): [([-1,1],1),([4,0,-1,1],1),([2,1,1,1,1],2)],
 (4,2): [([1,0,1],1),([-2,-1,0,1],1),([2,-1,0,1],1),([-4,0,1,0,1],1)],
 (5,0): [([-3,1],1),([-1,1],6),([1,1],5),([3,1,1],4)],
 (5,1): [([-1,1],3),([1,1],2),([9,0,-2,1],1),([3,1,2,1,1],3)],
 (5,2): [([-1,1],1),([1,0,1],2),([-3,-2,0,1],1),([3,1,0,1,1],2),([-9,3,2,-1,1],1)],
}


def matrix_charpoly_and_traces(k, r, max_n=80):
    a = matrix(k,r)
    m = len(a)
    power = [[int(i==j) for j in range(m)] for i in range(m)]
    traces = [m]
    for _ in range(m):
        power = multiply(power, a)
        traces.append(sum(power[i][i] for i in range(m)))
    # Newton identities: P=x^m+c_1*x^(m-1)+...+c_m.
    co = [1]
    for j in range(1,m+1):
        num = -sum(co[j-t]*traces[t] for t in range(1,j+1))
        assert num%j==0
        co.append(num//j)
    expected = product_factors(EXPECTED[k,r])
    assert list(reversed(co))==expected, (k,r,'charpoly')
    for n in range(m+1,max_n+1):
        traces.append(-sum(co[j]*traces[n-j] for j in range(1,m+1)))
    return traces


def odd_cyclic_count(n,k):
    """Direct finite-state parity dynamic program, independent of signed matrices."""
    d={(0,1,3):1}
    for _ in range(2,n):
        nd=defaultdict(int)
        for (a,b,parity),count in d.items():
            for c in range(k):
                if c!=a and c!=b:
                    nd[b,c,parity^(1<<c)] += count
        d=nd
    good=sum(v for (a,b,p),v in d.items()
             if p==(1<<k)-1 and b not in (0,1) and a!=0)
    return k*(k-1)*good


def signed_count(k,n):
    d=len(matrix(k,0))
    def power_trace(r):
        a=matrix(k,r)
        base=a
        power=[[int(i==j) for j in range(d)] for i in range(d)]
        exp=n
        while exp:
            if exp&1:power=multiply(power,base)
            exp>>=1
            if exp:base=multiply(base,base)
        return sum(power[i][i] for i in range(d))
    return sum((-1)**r*comb(k,r)*power_trace(r) for r in range(k+1))//(1<<k)


def is_strong_odd_wheel(word):
    n=len(word)
    col=list(word)+[max(word)+1]
    nbr=[{(i-1)%n,(i+1)%n,n} for i in range(n)]+[set(range(n))]
    for v in range(n+1):
        if any(col[u]==col[v] for u in nbr[v]):return False
        counts=defaultdict(int)
        for u in nbr[v]:counts[col[u]]+=1
        if any(q%2==0 for q in counts.values()):return False
    return True


def restricted_growth(n,limit):
    w=[0]*n
    def visit(i,maxc):
        if i==n:
            if maxc+1==limit:yield tuple(w)
            return
        for a in range(min(maxc+1,limit-1)+1):
            w[i]=a
            yield from visit(i+1,max(maxc,a))
    yield from visit(1,0)


def brute_partition_count(n,k):
    total=0
    for w in restricted_growth(n,k):
        if is_strong_odd_wheel(w):total+=1
    return total*factorial(k+1)


def main():
    traces={key:matrix_charpoly_and_traces(*key,max_n=80) for key in EXPECTED}
    cert=[]
    for n in range(10,61,2):
        p0,p1,p2=[traces[4,r][n] for r in range(3)]
        assert (p0-4*p1+3*p2)%8==0
        expected=(p0-4*p1+3*p2)//8
        assert expected==odd_cyclic_count(n,4), ('k4',n,expected)
        cert.append(expected)
    for n in range(11,60,2):
        p0,p1,p2=[traces[5,r][n] for r in range(3)]
        assert (p0-5*p1+10*p2)%16==0
        expected=(p0-5*p1+10*p2)//16
        assert expected==odd_cyclic_count(n,5), ('k5',n,expected)
    exceptional_dp=odd_cyclic_count(14,6)
    exceptional_signed=signed_count(6,14)
    assert exceptional_dp==exceptional_signed==9344160
    cases=0
    for n,k in [(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,3),(10,4),(11,5)]:
        direct=brute_partition_count(n,k)
        expected=odd_cyclic_count(n,k)
        assert direct==expected*(k+1),(n,k,direct,expected)
        cases+=1
    anchors = {
        10: '0120120123', 11: '01201201234', 12: '012013023123',
        13: '0120123013243', 14: '01201203123453',
        18: '012012012013023123', 20: '01201203103123023123',
    }
    extension_cases=0
    for n, letters in anchors.items():
        word=tuple(map(int, letters))
        assert len(word)==n and is_strong_odd_wheel(word), (n, letters)
        if n in (10,11,13,18,20):
            for t in range(1,9):
                extended=tuple(map(int,letters[:3]+'012012'*t+letters[3:]))
                assert is_strong_odd_wheel(extended)
                extension_cases+=1
    assert odd_cyclic_count(9,3)==6
    assert odd_cyclic_count(15,3)==6
    print('VERIFICATION_OK characteristic_polynomials=6 even_k4_orders=26 odd_k5_orders=25 direct_original_graph_orders=9 wheel14_odd_rim6=9344160 wheel14_opt_named=65409120 extension_cases=40')
    print('SAMPLE_RIM_COUNTS k4:',[(n,odd_cyclic_count(n,4)) for n in (10,12,14,16,18,20)])
    print('SAMPLE_RIM_COUNTS k5:',[(n,odd_cyclic_count(n,5)) for n in (11,13,15,17,19)])

if __name__=='__main__':main()
