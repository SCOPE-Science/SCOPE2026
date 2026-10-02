# Independent mathematical audit — Sumset growth from the first Kunz layer at prime multiplicity

Audit date: 2026-10-01 (UTC) UTC
Disposition: passed

## Correctness
the Apéry/Kunz carry calculation shows that an h-fold sum of first-layer residues lands in cumulative layer at most 2h-1. Repeated Cauchy–Davenport at prime multiplicity gives the stated linear lower bound, and summing cumulative layers yields the conductor-depth Wilf inequality with the claimed monotonicity in the depth parameter. The worked semigroup was independently recomputed as multiplicity 29, conductor 218, q=8, rho=14, first-layer size 5, cumulative layers 5,7,13,16,21,24, left-elements count 107, and Wilf number 424.

## Originality
the inspected 2026 Yang–Zhang first-Kunz-layer preprint develops first-layer and cumulative-layer Wilf bounds but its multilayer section does not contain the h-fold sumset/Cauchy–Davenport mechanism. Resultary searches for prime-multiplicity Kunz sumset growth returned this record and no earlier dominating theorem.

### equivalent_formulations
No prior source located states this sumset-to-layer propagation.

Searches: Resultary: Kunz first layer sumset Cauchy Davenport prime multiplicity Wilf numerical semigroup; Preprints.org 202604.0551; arXiv:1710.03623

Evidence: Equivalent formulation: h-fold sums of first-layer residues force occupancy of cumulative odd Kunz layers.

### broader_coverage
No stronger theorem inspected dominates the propagation inequality and its prime-multiplicity consequence.

Searches: Yang–Zhang, Wilf's Conjecture from the First Kunz Layer; Eliahou 2018; Eliahou–Fromentin arXiv:1710.03623

Evidence: Yang–Zhang develops first/multi-layer bounds but the inspected text contains no Cauchy–Davenport/sumset propagation; older additive work uses different constructions.

### exact_database_or_table
Exact-database coverage is inapplicable to the theorem; no table was used as novelty evidence.

Searches: Resultary prime multiplicity Kunz layer growth

Evidence: The multiplicity-29 example is illustrative; the main result is a uniform theorem and was not extracted from a table.

### claim_vs_prior_implication
The final theorem needs the record's semigroup-specific bridge and is not a direct prior corollary.

Searches: Preprints.org 202604.0551; Cauchy–Davenport theorem

Evidence: Cauchy–Davenport plus the new semigroup containment yields the prime bound; the containment itself is not supplied by the classical additive theorem or Yang–Zhang.

### Source inspections
- **Yang and Zhang, Wilf's Conjecture from the First Kunz Layer** — Primary full text inspected, including its multilayer cumulative-layer section; no sumset or Cauchy–Davenport argument was found. Assessment: Compared against the final statement and implication scope.
- **Cauchy–Davenport theorem** — Classical additive-combinatorics input used for the prime cyclic group. Assessment: Compared against the final statement and implication scope.
- **Resultary search** — Searched Kunz first-layer, sumset, Cauchy–Davenport, prime multiplicity, and Wilf combinations. Assessment: Compared against the final statement and implication scope.

## Scientific value
the claim links a motivated invariant from current Wilf-conjecture work to additive-combinatorial growth and yields a reusable sufficient criterion, rather than merely recomputing one semigroup.

## Reproducibility
Independent exact arithmetic reproduced the record's worked example and the lower bound |L| >= 68 at H=3.

## Limitations and residual risks
The explicit Cauchy–Davenport lower bound requires prime multiplicity; the sumset containment itself does not. The Wilf criterion is sufficient, not necessary, and does not resolve Wilf's conjecture in full. Very recent follow-up work may be incompletely indexed.
- Recent numerical-semigroup preprints may not yet be fully indexed.
- The prime-multiplicity hypothesis is essential for the stated Cauchy–Davenport step and should not be generalized silently.
