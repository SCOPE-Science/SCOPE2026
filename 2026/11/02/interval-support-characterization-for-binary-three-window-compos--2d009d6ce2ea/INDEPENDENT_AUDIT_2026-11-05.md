# Independent mathematical audit

## correctness

PASS

The sliding width-three weights satisfy s_(i+1)−s_i=w_(i+3)−w_i∈{−1,0,1}, hence interval support is necessary. The submitted explicit base words for every singleton/pair/triple/full contiguous support, with left 100 and right 011 three-cycle prepending/appending gadgets, increment prescribed counts while preserving required terminal states. This proves sufficiency for every positive composition of a consecutive support; counting intervals of r indices yields Σ_(r=1..4)(5−r) binom(m−1,r−1)=(m³+11m+12)/6. Exactly one witness per profile attains the noiseless zero-error size. At every width h≥4 a profile with one extra count at index 2 would force disjoint 0^h and 1^h factors in 2h+1 symbols; one remaining bit permits repeats only at 0,1,h−1,h, contradiction. Independently enumerated all binary words with m≤9 triple windows and verified profile counts and consecutive supports; all 512 words for h=4 also exclude (1,1,2,1,1).

## originality

PASS

OEIS A188554 already contains the same cubic numerical formula for another combinatorial model, so sequence novelty is explicitly excluded. Marcovich–Yaakobi handles literal k-substring multispectra, Gupta–Mahdavifar studies composition multisets over all substring lengths, and Sporring–Darkner preserves ordering of local histograms. The claim here is a complete iff description of UNORDERED multiplicity counts for overlapping width-three binary reads, with a constructive codebook and sharp width-four counterexample; none of the inspected statements directly establishes that channel output space. Historical equivalent hidden in sliding-histogram literature remains possible.

## value

PASS

A complete realizability theorem for a natural fixed-width unordered read-composition channel gives a one-line admission test and an explicit maximal zero-error codebook for every word length, as well as a sharp boundary h=3 versus h≥4 where support sufficiency breaks. That statement has independent coding-theoretic use even though the numerical polynomial is recorded elsewhere.

The dated certificate retains the supplied scientific assessment, sources and limitations.
