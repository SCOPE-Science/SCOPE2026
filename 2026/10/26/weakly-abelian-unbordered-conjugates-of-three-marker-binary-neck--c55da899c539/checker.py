"""Direct reproducibility checks for weak-Abelian-unbordered rotations."""
from collections import defaultdict
from math import comb, gcd
from random import Random


def weakly_unbordered(word):
    n = len(word)
    if n < 2:
        return True
    prefix_slopes = set()
    count = 0
    for length, symbol in enumerate(word[:-1], start=1):
        count += (symbol == '1')
        factor = gcd(count, length)
        prefix_slopes.add((count // factor, length // factor))
    count = 0
    for length, symbol in enumerate(reversed(word[1:]), start=1):
        count += (symbol == '1')
        factor = gcd(count, length)
        if (count // factor, length // factor) in prefix_slopes:
            return False
    return True


def circle(a, b, c):
    return '1' + '0'*a + '1' + '0'*b + '1' + '0'*c


def brute_count(a, b, c):
    word = circle(a, b, c)
    rotations = {word[i:]+word[:i] for i in range(len(word))}
    return sum(weakly_unbordered(r) for r in rotations)


def predicted_count(a, b, c):
    m = a+b+c
    values = (a,b,c)
    return sum((3*values[i]-m)*(3*values[(i+1)%3]-m)<0 for i in range(3))


def necklace_representatives(m):
    for a in range(m+1):
        for b in range(m-a+1):
            c = m-a-b
            t=(a,b,c)
            if t == min(t,(b,c,a),(c,a,b)):
                yield t


def predicted_distribution(m):
    delta = int(m%3==0)
    c0 = delta
    c1 = 2*(m//3)*delta
    total = (comb(m+2,2)+2*delta)//3
    return {0:c0,1:c1,2:total-c0-c1}


def check_explicit_failed_chord_witnesses():
    """Reconstruct the three proof witnesses, using exact prefix/suffix counts."""
    checked = 0
    for a in range(31):
        for b in range(31):
            for c in range(1,31):
                m = a + b + c
                w = circle(a, b, c)
                if 3*a < m < 3*c:
                    assert weakly_unbordered(w), (a, b, c)
                else:
                    if a >= c:
                        p = c + 1
                        s = c + 1
                    elif 3*a >= m:
                        p = a + 1
                        s = 2*a + 2
                    else:
                        assert 3*c <= m
                        p = 2*c + 2
                        s = c + 1
                    assert 0 < p < len(w) and 0 < s < len(w)
                    assert w[:p].count('1') * s == w[-s:].count('1') * p, (a,b,c,p,s)
                    assert not weakly_unbordered(w), (a,b,c)
                checked += 1
    return checked


def run():
    n_triples = 0
    n_necklaces = 0
    for m in range(0,29):
        direct = defaultdict(int)
        for triple in necklace_representatives(m):
            got = brute_count(*triple)
            want = predicted_count(*triple)
            assert got == want, (m,triple,got,want)
            direct[got] += 1
            n_necklaces += 1
        want_dist = predicted_distribution(m)
        assert all(direct.get(j,0) == want_dist.get(j,0) for j in range(4)), (m,direct,want_dist)
        n_triples += comb(m+2,2)
    rng = Random(20261024)
    random_cases = 500
    for _ in range(random_cases):
        a,b,c=(rng.randrange(0,150) for j in range(3))
        assert brute_count(a,b,c) == predicted_count(a,b,c), (a,b,c)
    for m in range(0,150):
        dist=defaultdict(int)
        for triple in necklace_representatives(m):
            dist[predicted_count(*triple)] += 1
        want=predicted_distribution(m)
        assert all(dist.get(j,0) == want.get(j,0) for j in range(4)), (m,dist,want)
    example='1110000011000'
    assert weakly_unbordered(example)
    n=len(example); k=example.count('1'); ss=0
    heights=[]
    for i,bit in enumerate(example[:-1],start=1):
        ss += bit=='1'
        heights.append(n*ss-k*i)
    assert min(heights)<0<max(heights), heights
    witness_cases = check_explicit_failed_chord_witnesses()
    print('PASS: three-marker iff and exact reverse witnesses:', witness_cases)
    print('PASS: exhaustive necklaces m=0..28:',n_necklaces)
    print('PASS: parent labeled gap triples covered:',n_triples)
    print('PASS: random larger three-marker necklaces:',random_cases)
    print('PASS: analytic distributions for m=0..149')
    print('PASS: known five-marker failure of unrestricted strict-chord converse')


if __name__ == '__main__':
    run()
