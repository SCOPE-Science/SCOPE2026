# Review of palindromic three-subsequence covers

## Correctness

PASS. The all-constant targets \(aaa\) give a sharp \(3q\) lower bound. The three repeated permutation blocks realize all \(aba\). Each shortest candidate has exactly three occurrences of each letter, and the six excluded two-letter projections are precisely the arrangements failing at least one required nonconstant palindrome. The recurrence records exactly those letters between the first and third occurrence; induction on unfinished positions proves its count. Exact integer evaluation agrees with an independently structured exhaustive multiset enumeration for all sizes through the DNA-size alphabet of four letters (369600 length-12 words). The five-letter value is established by the proved recurrence and exact implementation, without claiming independent exhaustive brute enumeration.

## Originality

PASS on the inspected evidence; residual overlap risk remains. Adamson (2023, arXiv:2304.04583) counts words containing every pattern, while the present forbidden-projection class includes many words that fail full universality. Adamson et al. (2023, arXiv:2311.10658), especially its counting section, addresses full subsequence-universal words accepted by regular automata, not the palindromic-only 3-uniform class or these numeric counts. The binary shortest-cover census establishes the two-letter case, which is not claimed as new. OEIS A330022 counts contiguous-palindrome superstrings and is a different observation. The exact DNA-size value and general projection criterion were not found as a reported theorem in the checked material. Possible hidden overlap with enumeration of three-occurrence pairwise-interleaving words is expressly unresolved.

## Mathematical value

PASS. The four-symbol alphabet is the canonical DNA motif alphabet, and length 12 is forced by covering four constant trigrams. The exact count of admissible shortest indexed hosts is a natural finite design-space invariant: \(80016\), not merely a computer-sampled estimate. The theorem provides a complete local forbidden-projection characterization, a general exact recurrence, and a substantive comparison with all-pattern shortest coverage (\(80016\) versus \(13824\)). These facts are reusable for checking enumeration methods and constraining palindrome-only sequence-cover designs. No unproved coding-rate or experimental biotechnology implication is claimed.

## Closest literature and limits

The 2023 universal-language and ranking works provide the nearest algorithms, but address a stronger coverage requirement, while a binary finite census is a lower-alphabet specialization. The numerical result is not a general closed form and is vulnerable to previously unlocated combinatorial enumeration under different terminology. Values above alphabet size five are not computed or claimed.

Self-review: passed. Independent audit: not yet performed.
