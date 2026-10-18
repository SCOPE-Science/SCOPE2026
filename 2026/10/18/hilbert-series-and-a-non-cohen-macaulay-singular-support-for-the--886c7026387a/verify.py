#!/usr/bin/env python3
"""Independent finite checks for the Birkhoff singular-support Hilbert function.

Only the degree-one to degree-four enumerations are computational checks;
all-degree validity requires the proof in RESULT.md.
"""
from math import comb


def rows_with_sum(d):
    return [(a, b, c, d-a-b-c) for a in range(d+1)
            for b in range(d-a+1) for c in range(d-a-b+1)]


def count(d):
    R = rows_with_sum(d)
    all_tables = disconnected = 0
    for a in R:
        for b in R:
            if any(a[j]+b[j]>d for j in range(4)):
                continue
            for c in R:
                last = tuple(d-a[j]-b[j]-c[j] for j in range(4))
                if min(last)<0 or sum(last)!=d:
                    continue
                M=(a,b,c,last)
                all_tables += 1
                found={0}
                todo=[0]
                while todo:
                    u=todo.pop()
                    nb=(4+j for j in range(4) if M[u][j]>0) if u<4 else (i for i in range(4) if M[i][u-4]>0)
                    for v in nb:
                        if v not in found:
                            found.add(v)
                            todo.append(v)
                if len(found)<8:
                    disconnected += 1
    return all_tables,disconnected


def p(d):
    return 2*d**4+12*d**3+48*d**2-72*d+34


def hilbert(d):
    return 0 if d<0 else (1 if d==0 else p(d))


def main():
    known_total=(24,282,2008,10147)
    for d in range(1,5):
        full, disc=count(d)
        assert full==known_total[d-1]
        assert disc==p(d),(d,disc,p(d))
        print('degree',d,'all',full,'disconnected',disc)
    numerator=[1,19,100,-84,-21,33]
    for k in range(11):
        coefficient=sum((-1)**j*comb(5,j)*hilbert(k-j) for j in range(min(k,5)+1))
        assert coefficient==(numerator[k] if k<len(numerator) else 0),(k,coefficient)
    assert sum(numerator)==48
    print('VERIFY_OK')

if __name__=='__main__':
    main()
