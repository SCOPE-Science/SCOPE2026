# Scientific review: exact weight-three palindromic periodicity count

## Correctness — PASS

The theorem is stated for every length \(n\ge3\) and indexed binary words with exactly three ones. The word-period characterization uses two possibly empty palindrome factors and includes the full word as a period; this handles the boundaries. For distinct cyclic gaps, every proper period has a root with one, two, or three marked positions. The one-marker case forces equal consecutive gaps and so cannot arise, while the other cases produce exactly the two interval families in `RESULT.md`. Their unions are analyzed without double counting. Equal gaps are counted separately. The disjoint generating-function decomposition and formal rational simplification prove the all-length formula. Direct root-and-palindrome-split enumeration of all \(7{,}315\) weight-three words through length 21, plus recurrence comparisons through length 160, returned `VERIFY_OK`. The all-length assertion depends on the proved combinatorial identities, not finite testing.

## Originality — PASS, qualified

The closest matching primary full-text works are Simpson (arXiv:2402.05381) and Fici–Shallit–Simpson (arXiv:2407.10564, plus the 2025 open-access CPM version). They develop the invariant and prove its occurrence in special word classes, but their conclusions concern unrestricted length counts and pose an unrestricted asymptotic problem; no fixed three-one rational generating function appears in the inspected sections. Guo–Shallit–Shur (arXiv:1503.09112) studies products of palindromes, a strict subclass: `01100100` is a palindromic periodicity that is not a product of two palindromes. OEIS A374495 tabulates the unrestricted count and gives a decision program, neither of which implies an exact all-length three-one expression. Literature searches for equivalent formulations, stronger implication coverage and exact fixed-weight tables did not find a covering result. **Risk:** unindexed equivalent enumerations remain possible, and novelty is not certified by negative searches.

## Mathematical value — PASS

Weight three is the earliest nontrivial binary fixed-content layer: zero-, one- and two-marker circular words always have a reflection and hence are symmetric. A complete fixed-weight theorem therefore answers the natural first unsolved slice of the broader counting problem. The exact quasipolynomial, period-12 behavior and sharp limiting fraction \(1/3\) are substantive structural information, not a finite table or relabeling. The scope does not include higher weights or unrestricted exponential-scale asymptotics.

## Limits and closest literature

Primary comparisons: arXiv:2402.05381; arXiv:2407.10564 and its CPM 2025 publication, doi:10.4230/LIPIcs.CPM.2025.11; arXiv:1503.09112; OEIS A374495. Definition-level computations are finite supporting checks. Independently performed scientific audit and complete literature priority verification remain outside this review.

Self-review: passed. Independent audit: not yet performed.
