---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At fixed n,k the only needed count is H=number of scattered 01 pairs; H=Σ_j j w_j−binom(k,2) in zero-based indexing. Advancing the rotation start by one changes H by n w_i−k, so equal values require equal starts modulo L=n/g. For any nonempty subset of one start group, the selected starts share a value exactly when each arc between successive selected starts contains d_jK ones. The arcs partition all labeled positions, and the probability is the product of binomial coefficients over the fixed-weight denominator. Inside an equality block of size a, summing (−1)^{r+1} binom(a,r) over nonempty subsets of the block gives one; this proves the expectation without any independence assumption across collisions or start groups. Equality at the global minimum forces every length-L window to contain K ones, so sliding one place gives w_{i+L}=w_i; the converse and g=1 follow. For g=3 the three pair events have equal probability p, all pair-event intersections are the same triple event of probability q, and the singleton, double and triple contributions yield the displayed multiplicities. Uniform Stirling for fixed g and interior density gives order L^{−(r−1)/2} for r specified starts in one group; hence only pairs affect the √L term. An unordered pair sum equals g/2 times the sum over its g−1 directed separations, giving the coefficient and the uniform O(1) remainder. An independent finite check computed all six signature counts at all rotations of every one of the 84 labeled length-nine weight-three words and compared them with the positional moment and window period test. It found counts of words 3,18,36,18,9 at diversity 3,4,5,6,7 respectively, and mean 36/7 (p=15/28, q=9/28); the finite check is not evidence for uniform asymptotics apart from the proof.

## originality

PASS

The distinct finding is the expectation and leading loss for general fixed gcd, beyond the exact overlapping g=2 result. Binary linear-word equivalence, the deterministic lower-bound characterization, and the g=2 moment and asymptotic are not counted as distinct from their inspected matches. No inspected stronger result implies the general gap-product formula or its square-root coefficient after specialization.

## value

PASS

The observable measures how many distinct observations remain when the start of a fixed-composition circular word is unknown. Neither deterministic bounds nor the g=2 exact result quantifies the typical loss at general gcd. The gap-product expression supplies such a mean for all fixed compositions, and its explicit square-root correction distinguishes pair collisions from higher-order coincidences; both are useful beyond the matching deterministic criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
