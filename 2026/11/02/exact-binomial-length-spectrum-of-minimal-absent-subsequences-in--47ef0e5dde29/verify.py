"""Reproduce exact minimal-absent-subsequence spectrum for alternating binary words.
Run: python3 verify.py. Uses only the Python standard library.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def subseq(u, w):
    pos = 0
    for letter in u:
        while pos < len(w) and w[pos] != letter:
            pos += 1
        if pos == len(w):
            return False
        pos += 1
    return True


def minimal_absent(u, w):
    return (not subseq(u, w)) and all(subseq(u[:i] + u[i+1:], w) for i in range(len(u)))


def local_predicate(u, m):
    if len(u) < 2: return False
    cost = len(u) - sum(u[i:i+2] == '01' for i in range(len(u)-1))
    return (cost == m + 1 and u[:2] != '01' and u[-2:] != '01'
            and all(u[i:i+3] not in ('010', '101') for i in range(len(u)-2)))


def expected(m):
    return {m+1+j: comb(m+2-j, 2*j+1)
            for j in range((m+1)//3+1)}


def transfer(m_max):
    # Independently count accepted words by four two-letter suffix states.
    # An integer map has keys (weight, length) and counts words.
    states = ['00', '01', '10', '11']
    allowed = set(['00','10','11'])
    dp = {s: {(1,2): 1} for s in allowed}
    output = defaultdict(Counter)
    for s, d in dp.items():
        for (weight, length), v in d.items():
            if weight <= m_max:
                output[weight][length] += v
    for _ in range(2*m_max):
        ndp = {s: defaultdict(int) for s in states}
        for s, data in dp.items():
            for b in '01':
                triple = s+b
                if triple in ('010','101'): continue
                suffix = triple[1:]
                dw = 0 if suffix == '01' else 1
                for (weight,length), val in data.items():
                    if weight+dw<=m_max:
                        ndp[suffix][(weight+dw,length+1)] += val
        dp = ndp
        for s in allowed:
            for (weight,length),v in dp[s].items():
                output[weight][length] += v
    return output


def main():
    all_candidates = 0
    total_mas = 0
    for m in range(1, 9):
        w = '01'*m
        actual=Counter()
        for length in range(1, 2*m+2):
            for chars in product('01',repeat=length):
                u=''.join(chars)
                direct=minimal_absent(u,w)
                local=local_predicate(u,m)
                assert direct==local,(m,u,direct,local)
                if direct:actual[length]+=1
                all_candidates += 1
        assert dict(actual)==expected(m),(m,dict(actual),expected(m))
        total_mas += sum(actual.values())
        print(f'm={m}: length_histogram={dict(sorted(actual.items()))}, total={sum(actual.values())}')
    trans=transfer(50)
    for m in range(1, 51):
        assert dict(trans[m])==expected(m),(m,dict(trans[m]),expected(m))
    print(f'PASS: {all_candidates} distinct words checked by direct subsequence membership; '
          f'{total_mas} minimal absences counted; 50 transfer-distribution checks')

if __name__=='__main__':
    main()
