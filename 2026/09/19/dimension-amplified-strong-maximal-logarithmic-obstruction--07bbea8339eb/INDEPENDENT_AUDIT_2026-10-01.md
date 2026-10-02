# Independent audit — Dimension-amplified logarithmic endpoint failure for the strong maximal operator

Audit date: 2026-10-01 (UTC) UTC

## Final claim

For every dimension at least two and every exponent between one and infinity, rectangular A_p weights force the strong maximal norm to carry a logarithmic lower factor whose exponent is (dimension minus 1) divided by p, beyond the endpoint Buckley power.

## Correctness — PASS

The construction is internally complete. The cumulative-mass recurrence and the chosen side length bound every one-coordinate growth ratio uniformly, making the anchored rectangular A_p estimate a convergent product of geometric series. A two-cell rectangle gives the matching characteristic lower bound. On the hyperbolic index set the cumulative mass stays uniformly bounded, while the multiparameter divisor count supplies on the order of theta inverse times the (dimension minus 1)-st power of log theta inverse many disjoint cells. Testing from the source cell therefore yields the stated logarithmic norm exponent after taking the p-th root. The coordinatewise averaging and periodic reflection steps extend the estimate from anchored rectangles to the whole space.

## Originality — PASS

Two earlier published records were inspected in full. The 2026-09-18 all-p record proves only the planar logarithmic exponent one over p and carries that same rate to higher dimensions by ignoring extra coordinates. The 2026-09-17 tensor-amplification record proves the p equals 2 logarithmic exponent floor(dimension over 2) divided by 2, and notes that the product-factorization lemma itself works for general p. Combining those prior results gives at most floor(dimension over 2) divided by p, which is strictly smaller than the present exponent (dimension minus 1) divided by p in every dimension at least three. The two-dimensional slice is covered, but the final all-dimensional theorem is not.

### Equivalent formulations

Searches: Resultary semantic search for strong maximal logarithmic weighted lower bounds in all dimensions and all (p); inspection of earlier published SCOPE records on all-(p) obstruction and tensor amplification

Evidence: The closest all-(p) result has exponent (1/p); the closest dimension-amplified result is (p=2) with exponent (lfloor n/2rfloor/2).

Reasoning: Neither is equivalent to an exponent ((n-1)/p) for all (p,n).

### Broader coverage

Searches: Primary abstract inspection of Ombrosi–Rey arXiv:2609.17246; searches for Lerner arXiv:2609.14008 and subsequent strong-maximal lower bounds

Evidence: Ombrosi–Rey provide all-(p), all-dimensional upper bounds; Lerner supplies the planar (p=2) lower obstruction.

Reasoning: No inspected theorem dominates the new lower logarithmic exponent.

### Exact database or table

Searches: No finite database/table is natural for weighted-operator lower bounds.

Evidence: The parameter family is analytic and asymptotic rather than tabulated.

Reasoning: Database comparison is inapplicable.

### Claim versus prior implication

Searches: Compared exponents and constructions of the 2026-09-17, 2026-09-18, and audited 2026-09-19 records.

Evidence: Prior tensorization yields at most (lfloor n/2rfloor/p) after combining with the planar all-(p) theorem; the audited hyperbolic count yields ((n-1)/p).

Reasoning: The final claim is not a corollary of the prior records for (nge3); only its planar slice is covered.

## Value — PASS

The stronger logarithmic exponent identifies a genuinely multiparameter hyperbolic-count mechanism that pairwise tensoring misses. It materially sharpens the known endpoint obstruction as dimension grows while leaving the open optimal power exponent untouched. That is a meaningful boundary result in weighted multiparameter harmonic analysis.

## Source inspections

- **Published record All-p logarithmic obstruction to the Buckley endpoint power for the strong maximal operator (2026-09-18)** — Material read: complete RESULT.md from the frozen repository. Finding: Proves (A^{1/(p-1)}(log A)^{1/p}) in dimension two and carries the same rate to higher dimensions by ignoring extra coordinates.
- **Published record Tensor amplification of the strong maximal A2 obstruction (2026-09-17)** — Material read: complete RESULT.md from the frozen repository. Finding: Tensorizes planar (p=2) examples and gives exponent (lfloor n/2rfloor/2); the product lemma is general but does not reach ((n-1)/p).
- **Sheldy Ombrosi, Guillermo Rey, Improved weighted bounds for the strong maximal function, arXiv:2609.17246** — Material read: primary abstract. Finding: All-(p), all-dimensional upper-bound work; does not state the audited lower theorem.

## Residual risks

- The full Lerner and Ombrosi–Rey manuscripts were not retrievable through the available full-text route in this run. Their relevant lower/upper scopes were cross-checked against primary abstracts and the complete earlier published records. Very recent unindexed work remains a residual risk.

The assessment applies to the single final claim above. Computational artifacts are corroborative evidence only; they are not used as a substitute for the mathematical proof.
