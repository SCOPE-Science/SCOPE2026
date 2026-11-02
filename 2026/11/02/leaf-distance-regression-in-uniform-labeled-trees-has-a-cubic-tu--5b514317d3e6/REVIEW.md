# Scientific review: leaf–distance regression in uniform labeled trees

## Correctness — PASS

The proof reduces conditioning on a fixed path to the classical root-forest determinant \(hN^{N-h-1}\); deleting specified off-path leaves and chosen path endpoints gives the exact joint inclusion probabilities. Inclusion–exclusion recovers the conditional leaf polynomial, and a direct subtraction yields the signed cubic first difference. The boundaries \(n=3\), \(s=n\), \(q=s\) and the possible equality plateau are included. Independently decoded Prüfer trees through eight vertices verify exact finite instances; computation is corroboration rather than a replacement for the infinite proof.

## Originality — PASS (qualified)

Remmel–Williamson (2010, arXiv:1009.2060, fully inspected at the leaf-count statements) enumerates trees by their leaf sets, without marked-distance conditioning. Bousquet-Mélou–Chapuy (2012, especially their rooted Cayley height/offspring-degree enumeration) permits broad joint combinatorial reconstruction; however, their inspected statements do not give this explicit marked-pair conditional law or its exact cubic change of monotonicity. The published endpoint-degree/distance result overlaps with, and has priority over, the endpoint-only subcase; that known subcase is not a claimed contribution. Targeted literature and semantic-record searches did not identify an explicit equal or stronger sign-transition result. Historical equivalence remains possible, especially through more general enumerators and inaccessible complete sources; failed searches are not a novelty proof.

## Value — PASS

The entire conditional distribution connects a global branching statistic (total leaves) to a pairwise geometric statistic (marked distance) in the canonical uniform spanning-tree model of a complete graph. The exact positive-to-negative regression change is structural, not a tiny numerical improvement: a short marked path initially raises the global expected leaf count, yet sufficiently long paths suppress it. The new explicit integer cubic boundary and \(n^{1/3}\) peak scale isolate this nonmonotonicity without asymptotic approximations.

## Scope and limitations

Only uniform Cayley trees and degree-one leaves are covered; no claim is made for generic simply generated trees, random recursive trees or arbitrary edge weights. The older forest enumeration and the known single-endpoint distance regression are acknowledged inputs/overlaps, not original. The closest modern published record was readable as a title and summary but not as an entire source; some older texts were only readable as abstracts. This leaves historical-priority risk. The finite enumeration does not prove the all-size theorem.

Self-review: passed. Independent audit: not yet performed.
