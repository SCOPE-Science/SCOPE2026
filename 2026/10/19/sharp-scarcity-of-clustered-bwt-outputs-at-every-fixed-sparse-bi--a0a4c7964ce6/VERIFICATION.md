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

The convention is indexed words, duplicate rotations retained, no marker, and linear runs. For nonconstant input the first sorted row starts with a longest cyclic zero block, hence has predecessor 1. Likewise the last sorted row starts with a longest one block, with predecessor 0. Ties of equal rotations cannot change those letters. There are exactly k predecessor ones, so maximal run count is equivalent to isolation of all output ones. When all gaps are positive, output ones correspond to starting at the first zero of a gap. If the gap sizes are separated by at least two, a rotation starting one position later in the longer gap has an intermediate zero-prefix length and predecessor 0, so lexicographically separates the two output ones. When the largest gap is repeated (with n>k, so it is positive), the first rows are those gap starts and the output begins 11. For the upper count, a specified zero coordinate leaves k−1 nonnegative variables of fixed total, with O_k(n^(k−2)) solutions. A specified difference in {−1,0,1} leaves O(n) choices for one of the two coordinates and O_k(n^(k−3)) for the remaining k−2 at fixed sum; finitely many such relations suffice. For the lower count, prescribe g1=g2=m in [0.36n,0.38n]. At fixed k and all sufficiently large n the remaining n−k−2m is positive, comparable to n and less than m, so the first two coordinates are exactly the largest. There are Θ(n) values of m and Θ_k(n^(k−3)) ordered compositions for each. A marked tuple plus an absolute marked position fixes the indexed word, with each word admitting at most k of the allowed markings even for periodic words. Thus the lower family gives Ω_k(n^(k−1)) words; using the same marking relation for the upper count gives O_k(n^(k−1)). Division by binomial(n,k) gives the probability. The positive even deficit among exceptions is between 2 and 2k−2, so the expected-deficit comparison also holds.

## originality

PASS

Credit the sharp lower-order obstruction and the two-sided law uniformly as a statement for every fixed k≥4, not the upper exponent alone, the separated-gap criterion by itself, or the isolated weight-four result. The strongest all-weight comparison already has the same run upper bound and separated-gap sufficiency with an O_k(1/n) failure bound, but not a matching lower failure bound. A separate exact weight-four spectrum proves that instance with a leading constant. The distinct content is a construction and matching order of rarity for the general fixed-weight regime.

## value

PASS

In a fixed sparse alphabet ensemble, 2k is the structural maximum for the output. Knowing it is generic does not tell how rare clustering can be. A stable family of tied longest gaps gives precisely the missing lower order throughout the fixed-weight regime, and thereby fixes both the failure scale and the expected run deficit. This goes beyond the isolated known cases or counting unrestricted candidate output strings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
