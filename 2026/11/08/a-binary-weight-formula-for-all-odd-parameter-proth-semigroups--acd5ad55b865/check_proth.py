"""Exact integer checks for a binary-weight formula for Proth-semigroup Frobenius numbers."""
from heapq import heappop, heappush


def binary_weight(z):
    return z.bit_count()


def prediction(m, n):
    assert n >= 3 and 3 <= m < 2**n and m % 2
    h = binary_weight(m)
    t = 1
    while 2*t - binary_weight(t) < h:
        t += 1
    s = h - (2*(t-1) - binary_weight(t-1))
    a = m*2**n + 1
    return (a-1)**2 + a*(2*t-1) + s-1, (h,t,s,a)


def independent_apery(m, n):
    a = m*2**n + 1
    r = m.bit_length() - 1
    generators = [m*2**(n+i)+1 for i in range(1,n+r+1)]
    D = [-1]*a
    D[0] = 0
    heap = [(0,0)]
    while heap:
        d, u = heappop(heap)
        if d != D[u]:
            continue
        for g in generators:
            v = (u+g) % a
            nd = d+g
            if D[v] < 0 or nd < D[v]:
                D[v] = nd
                heappush(heap,(nd,v))
    assert all(d >= 0 for d in D)
    return max(D)-a


def greedy_digits(y, k):
    x = [0]*(k+1)
    for i in range(k, 0, -1):
        x[i], y = divmod(y, 2**i-1)
    assert y==0
    return x


def independent_digit_data(m, n):
    j = m*2**n
    k = n+m.bit_length()-1
    x = greedy_digits(j,k)
    return sum(x),next(i for i in range(1,k+1) if x[i])


def main():
    pairs, residue_count, perfect_cases, nontrivial = 0, 0, 0, 0
    for n in range(3,8):
        for m in range(3, 2**n, 2):
            predicted,(h,t,s,a)=prediction(m,n)
            actual = independent_apery(m,n)
            assert actual == predicted,(m,n,predicted,actual)
            c,sd=independent_digit_data(m,n)
            assert c==2*t and sd==s,(m,n,c,2*t,sd,s)
            residue_count+=a
            pairs+=1
            perfect_cases += s>1
            nontrivial += s>=3
    print(f"APERY_OK pairs={pairs} residue_classes={residue_count} s_gt_1={perfect_cases} s_ge_3={nontrivial}")

    large=0
    for n in range(8,17):
        for m in range(3,2**n,2):
            if m % 31 != 3:
                continue
            predicted,(h,t,s,a)=prediction(m,n)
            c,sd=independent_digit_data(m,n)
            assert c==2*t and sd==s,(m,n,c,2*t,sd,s)
            large+=1
    print(f"GREEDY_OK additional_parameter_pairs={large}")

    for m,n in [(3,6),(7,6),(31,6),(63,7),(127,8),(255,9),(511,10)]:
        answer,(h,t,s,a)=prediction(m,n)
        print(f"EXAMPLE m={m} n={n} h={h} t={t} s={s} F={answer}")

if __name__=='__main__':
    main()
