#!/usr/bin/env python3
"""Finite-window certificate for palindromes in Kimberling's binary word.

Uses B = 0 pi(T), pi(0)=100, pi(1)=101, pi(2)=10,
T = phi^infinity(0), phi(0)=01, phi(1)=02, phi(2)=0.
"""
import json

PHI = {'0':'01','1':'02','2':'0'}
PI = {'0':'100','1':'101','2':'10'}
S = ('00','01','02','10','20')
EXPECTED = {
  1:['0','1'], 2:['00','11'], 3:['010','101'],
  4:['0110','1001'], 5:['00100','01010'],
  6:['010010'], 7:['0010100','1001001'],
  8:['10100101'], 9:['100101001'], 10:[], 11:[]
}

def morph(word, mapping):
    return ''.join(mapping[letter] for letter in word)

def iterate(word, mapping, repetitions):
    for _ in range(repetitions):
        word = morph(word, mapping)
    return word

def factors(w, n):
    return set(w[i:i+n] for i in range(len(w)-n+1))

def palindromes(w, n):
    return {v for v in factors(w,n) if v == v[::-1]}

def main():
    tribonacci_level4 = iterate('0', PHI, 4)
    pair_set = tuple(sorted(factors(tribonacci_level4, 2)))
    assert pair_set == S, (pair_set,S)
    block = {a:morph(iterate(a,PHI,3), PI) for a in '012'}
    assert block == {'0':'10010110010100101100',
                     '1':'10010110010100101',
                     '2':'10010110010'}
    assert min(map(len, block.values())) == 11
    cover = {'initial': '0'+block['0']}
    for x,y in S:
        cover[x+y] = block[x]+block[y]
    result = {}
    total = set()
    for n in range(1,12):
        pals = sorted(set().union(*(palindromes(word,n) for word in cover.values())))
        assert pals == EXPECTED[n], (n,pals,EXPECTED[n])
        total.update(pals)
        result[str(n)] = pals
    assert len(total) == 15
    assert max(map(len,total)) == 9
    # The same six finite windows yield factor complexity 2n for n <= 11.
    factor_counts = [len(set().union(*(factors(w,n) for w in cover.values())))
                     for n in range(1,12)]
    assert factor_counts == [2*n for n in range(1,12)]
    # Compare 24 and 25 positions of the independently given 0*pi(T) prefix.
    T = iterate('0', PHI, 8)
    B = '0'+morph(T, PI)
    distinct = lambda prefix: set().union(*(
        palindromes(prefix, n) for n in range(1,len(prefix)+1)))
    assert len(distinct(B[:24])) == 14
    assert len(distinct(B[:25])) == 15
    assert distinct(B[:25]) == total
    output = {
      'tribonacci_pair_set':pair_set,
      'blocks_phi3_pi':block,
      'six_finite_cover_words':cover,
      'factor_counts_at_lengths_1_through_11':factor_counts,
      'palindromic_factors_by_length':result,
      'distinct_nonempty_palindrome_count':len(total),
      'unique_longest_palindrome':'100101001',
      'prefix_length_24_palindrome_count':14,
      'prefix_length_25_palindrome_count':15,
      'minimal_palindrome_saturation_prefix_length':25,
    }
    print(json.dumps(output, sort_keys=True, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
