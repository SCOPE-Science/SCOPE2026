# Scientific review

## Correctness — PASS

The claim is an exact all-weight polynomial for the two-color outer-independent rainbow labelings of \(T_n=L(K_n)\) for every integer \(n\ge5\). Independence of empty vertices forces an underlying matching; for each matching edge exactly \(2(n-2)\) selected neighbors are eligible. The common-neighborhood union for \(k\) missing edges is exactly \(2k(n-k-1)\), since pairwise overlap counts four interpair edges. Incompatible opposite-color absence events do not meet, permitting the two-family inclusion-exclusion formula. The minimum-value construction checks both colors explicitly, and the minimum coefficient counts precisely the maximum-matching singleton assignments. No unproved general lemma is used. The complete definition-level coefficients match for \(n=3,4,5\); optimum counts match through \(n=6\). The finite checks are supporting, not the infinite proof.

## Originality — PASS (best-knowledge, with remaining priority risk)

The 2019–2023 literature on outer-independent two-rainbow domination primarily supplies bounds, characterizations of small or extremal minimum values, and formulas for graph products. The exact all-weight polynomial on the triangular graphs with \(n\ge5\) was not located. The closest record for all two-rainbow labelings of complete multipartite graphs concerns a different graph domain (the triangular graph ceases to be complete multipartite for \(n\ge5\)) and does not directly impose outer-independence. Other mathematical studies of power domination and paired domination on triangular graphs address different predicates, so their enumerators cannot imply the rainbow polynomial. Generic vertex-cover lower bounds give the minimum weight lower bound, not the new all-weight enumeration. The 2019 foundational publisher full text and any unindexed equivalent all-weight enumeration remain bibliographic risks; a negative search alone is not priority proof.

## Value — PASS

A complete exact weight distribution is a natural strengthening of a graph domination parameter, and the triangular graph family is a canonical line-graph/Johnson-graph family. The formula counts nontrivially coupled color-deficiency events around an omitted matching, giving an explicit finite polynomial, sharp minimum multiplicities and an exponential-density statement for feasible minimum colorings. This is not merely renaming a known vertex-cover bound or recounting a small graph table; it gives all coefficients uniformly for infinitely many graph orders.

## Scope and reproducibility

The proof is combinatorial inclusion-exclusion and applies to every integer \(n\ge5\). The accompanying verifier computes all four-label assignments for \(n=3,4,5\) and all minimum-weight singleton labelings for \(n=3,4,5,6\), and its saved output is reproducible using standard Python. Neither finite enumeration nor search establishes an unrestricted theorem or priority by itself.

Self-review: passed. Independent audit: not yet performed.
