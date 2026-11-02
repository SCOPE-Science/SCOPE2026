# Self-review

## Correctness — PASS

The claim is an exact identity for every integer \(b\ge1\) and deletion budget \(r\ge0\), plus its equivalent all-length extremal profile. The proof first derives a necessary-and-sufficient formula for the minimum number of deletions destroying the pattern \(0\,1^b\,0\). In its lower bound, a zero-count dichotomy and two disjoint intervals of consecutive zero gaps force the sharp number of ones; in its upper bound, every possible position of the outer surviving zeros is exhausted for the explicit word \(0^{s+1}1^b(01)^r0\). Boundaries \(r=0\), \(b=1\), and the regime transition at \(r=b-1\) are included. An independent dynamic-programming implementation agrees with the gap identity on 163,835 binary words and with the claimed extremal profile in 75 parameter cases; 960 explicit constructions and 1,201 actual deletion masks were also checked. Finite checks are supporting evidence, not an infinite proof.

## Originality — PASS, with residual priority risk

The closest directly relevant source, Xie–Sun–Ge, *New bounds for covering codes under insertions or deletions* (2026), Section III, Theorem III.2, proves that a deletion of \(r\) positions can eliminate the fixed subsequence \(0110\) from any binary word of length \(2r+4\). It does not give a matching shortest robust word, a variable interior run length \(b\), or the fixed-length resilience profile. The present statement closes that boundary and gives the nontrivial \(\min\{r,b-1\}\) transition. Searches for equivalent robust-supersequence, forbidden-scattered-subsequence, adversarial-erasure, and broader covering-code formulations found no covering published result. General deletion-descendant enumeration and subsequence universality concern different quantifiers, so neither directly implies the claim. Earlier unindexed or terminology-divergent literature cannot be excluded.

## Mathematical value — PASS

The motivating paper uses the survival or elimination of a single short forbidden subsequence to distinguish two coding-theoretic covering notions. Exactly how long a word must be to preserve that pattern against every choice of adversarial deletions is the natural threshold behind that example. The theorem supplies a complete, infinite, two-parameter solution, explicit optimal witnesses and an exact inverse extremal profile. The change from three symbols of length per extra protected deletion to two after \(r=b-1\) is explained structurally by disjoint zero-gap constraints. This is not a relabeling or a finite case computation; its proof settles arbitrarily large pattern lengths and deletion budgets.

## Closest literature and limitations

The directly comparable portion of Xie–Sun–Ge is Theorem III.2 and its proof; it entails only one direction of the special case \(b=2\). Liron–Langberg (2012) studies the number of distinct deletion descendants, rather than guaranteed survival of a designated subsequence. The theorem does not classify all extremizers or address arbitrary patterns with more than three runs. Unindexed prior results remain a priority uncertainty.

Self-review: passed. Independent audit: not yet performed.
