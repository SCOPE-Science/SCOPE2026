# Scientific review: parity-alternating Turán inequalities

**Correctness — PASS.** The published exact generating function [1] is the stated input, not a theorem being reproved. The analyticity bound on the Catalan composition and the expansions at both \(1/2\) and \(-1/2\) are explicit. The negative-square-root term has nonzero coefficient, and coefficient transfer produces a positive signed leading constant for the Turán determinant. Finite checks compare exact Catalan-series coefficients to an independent permutation enumeration and are used only as corroboration. The proof specifies the sign for sufficiently large indices, not for every index.

**Originality — PASS, with bibliographic limitations.** The closest primary manuscript, Archer–Graves [1], determines \(A(z)\) and first-order asymptotics but does not address the adjacent Turán determinant, its parity, or the weak negative singularity. Bóna–Smith [2] and OEIS A322779 [3] provide earlier context and finite data. Searches against equivalent names and nearby stronger coefficient-curvature results, including mathematical research records, found no covering result. Older original articles were available at abstract level only, and unindexed equivalent work is a residual risk. The result is not claimed as a new generating function.

**Value — PASS.** Alternation between eventual strict log-concavity (even indices) and strict log-convexity (odd indices) is a qualitative shape classification with an exact asymptotic defect. It is motivated by the previously unresolved shape of the newly enumerated strong-pattern-avoidance sequence: the leading \(2^n/\sqrt n\) growth does not predict this effect. The nontrivial feature is that the weaker singularity at the negative radius dominates the adjacent Turán difference.

**Limitations.** No optimal starting index is established; the checked finite range does not promote a conjectural cutoff to a theorem. The derivation relies on [1] for exact enumeration; independent external audit has not taken place.

Self-review: passed. Independent audit: not yet performed.

References: [1] Archer–Graves, arXiv:2604.25912v1; [2] Bóna–Smith, arXiv:1901.00026; [3] OEIS A322779; [4] Flajolet–Sedgewick, *Analytic Combinatorics* (2009).
