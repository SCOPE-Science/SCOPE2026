# Independent mathematical audit

## correctness

PASS

Digit splitting gives exactly one mixed-parity summand pair for a mixed integer. A same-parity representation of a mixed integer must carry and thus has two positive summands. Each even-start block has 2g−1 carry-or-no-carry values; the odd-start family loses the units digit and has only g choices for the last digit because overflow is forbidden. The intersection has units zero and 2k−1 free binary digits. Removing pure outputs before inclusion–exclusion gives (3g−1)(2g−1)^(k−1)−2g^k−2^(2k−1)+1. For a positive pure integer, the number of same-parity unordered positive pairs is (∏(d_j+1)−2+I)/2, where I is 1 exactly when every active digit is even. This is one only for a lone 2 or 3 or two 1s. An opposite-parity carry gives at least two unordered pairs whenever all present digits are 1 and units is zero, because each used preceding digit has to split g, with floor(g/2)≥2 choices even at one site. A lone unit 1 has neither type. The surviving unique pure count is 5k−1 and the only missing integers are 0 and 1. Adding the two ambiguity counts gives the formula; 2g−1>4 gives the stated leading asymptotic. Independent summand enumeration reproduced all 21 recorded configurations (3,550,513 admitted pairs).

## originality

PASS

The distinct finding is an exact uniform exceptional-set size and exponent on natural cutoffs for g≥4. The closest published theorem gives density-one uniqueness for the very same basis; a distinct same-date ternary record gives a materially related exact formula via the same parity decomposition, but at a disjoint base with a different pure-digit correction. Neither supplies this quantified count.

## value

PASS

Density leaves the rate of exceptional representations undetermined in a classical thin additive basis. Complete two-digit blocks are natural for its parity decomposition; counting all such blocks in all higher bases gives an exact rate, coefficient and finite correction with a genuine low-base carry distinction. This is useful beyond any one verified grid and need not extend to arbitrary partitions or cutoffs to be worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
