"""Check finite instances of the parity-profile theorem (standard library only).

The general upper bound uses a published structural theorem on large
sum-free sets, and is therefore not certified by this finite program.
"""
from itertools import combinations

def population(x):
    return x.bit_count()

def allowed_columns(r):
    return [x for x in range(1 << r) if population(x) >= 3]

def sumfree(S):
    A = set(S)
    return len(S) == len(A) and all((u ^ v) not in A for u, v in combinations(S, 2))

def examples(r):
    by_parity = [v for v in range(1 << r) if population(v) >= 3 and population(v) % 2 == 1]
    coordinate = [[v for v in range(1 << r) if population(v) >= 3 and ((v >> i) & 1)] for i in range(r)]
    return by_parity, coordinate

def brute_optima(r):
    A=allowed_columns(r)
    mx=-1
    opts=[]
    for bits in range(1 << len(A)):
        if bits.bit_count() < mx:
            continue
        S=tuple(A[i] for i in range(len(A)) if bits & (1 << i))
        if not sumfree(S):
            continue
        if len(S) > mx:
            mx=len(S);opts=[]
        opts.append(S)
    return mx, set(opts)

def distance_checks(S):
    k=len(S)
    # All codeword differences for k <= 11; every nonzero message difference.
    for bits in range(1, 1 << k):
        syn=0
        for i in range(k):
            if (bits >> i) & 1:
                syn ^= S[i]
        weight=population(bits) + population(syn)
        assert weight >= 3, (S,bits,weight)
        if population(bits) % 2:
            assert weight >= 4, (S,bits,weight)

def main():
    target={3:(1,1),4:(5,1),5:(11,6)}
    for r,(v,c) in target.items():
        mx,sets=brute_optima(r)
        assert (mx,len(sets)) == (v,c),(r,mx,len(sets))
        print(f'r={r}: exhaustive max={mx}; labeled optimum sets={len(sets)}')
        parity,coordinate=examples(r)
        if r>=5:
            expected={tuple(sorted(S)) for S in [parity]+coordinate}
            assert sets==expected, (r, sets^expected)
        if r==4:
            assert sets=={tuple(allowed_columns(r))}
    for r in range(5,10):
        parity,coordinate=examples(r)
        goal=(1 << (r-1))-r
        assert len(parity)==goal
        assert sumfree(parity)
        for S in coordinate:
            assert len(S)==goal
            assert sumfree(S)
        assert len({tuple(parity),*(tuple(S) for S in coordinate)})==r+1
        print(f'r={r}: {r+1} explicit candidate maximizers of size {goal} checked')
    for r in (3,4,5):
        if r==3:
            S=allowed_columns(r)
        elif r==4:
            S=allowed_columns(r)
        else:
            S=examples(r)[0]
        distance_checks(S)
        print(f'r={r}: all {2**len(S)-1} nonzero message differences checked')
    print('VERIFY_OK')
if __name__=='__main__':
    main()
