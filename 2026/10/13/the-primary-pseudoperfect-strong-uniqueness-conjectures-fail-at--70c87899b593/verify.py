N = 47058
PRIMES = [2, 3, 11, 23, 31]
S = [1,47058,2,23529,3,15686,22,2139,23,2046,31,1518,33,1426,93,506]

def is_prime_trial(p):
    if p < 2:
        return False
    d = 2
    while d*d <= p:
        if p % d == 0:
            return False
        d = 3 if d == 2 else d + 2
    return True

def main():
    assert all(is_prime_trial(p) for p in PRIMES)
    prod = 1
    for p in PRIMES:
        prod *= p
    assert prod == N
    assert 1 + sum(N//p for p in PRIMES) == N
    assert len(S) == len(set(S)) == 16
    assert all(N % d == 0 for d in S)
    assert all(N//d in S for d in S)
    assert sum(S) == 2*N == 94116
    pairs = sorted((min(d,N//d), max(d,N//d)) for d in S if d <= N//d)
    expected = sorted([(1,47058),(2,23529),(3,15686),(22,2139),(23,2046),(31,1518),(33,1426),(93,506)])
    assert pairs == expected
    print('VERIFY_OK n=47058 primary=1 strongly_pseudoperfect=1 pairs=8 sum=94116')

if __name__ == '__main__':
    main()
