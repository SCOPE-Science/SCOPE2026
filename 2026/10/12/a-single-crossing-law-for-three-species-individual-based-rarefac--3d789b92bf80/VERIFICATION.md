---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The mathematical proof is infinite in scope (all finite census totals) and appears in the result document. This file reports only reproducible exact computational checks and their limitations.

Run `python3 verify_three_species_rarefaction_one_crossing.py` with Python 3 and no third-party libraries.

Expected leading output: `VERIFY_OK`.

The checker independently generates all positive unlabeled abundance triples through \(N=35\) using both an ordered-partition generator and a composition-and-sort generator. It calculates hypergeometric species-absence numerators at every interior integer sample depth, compares every unordered pair, and asserts that the nonzero signs never change more than once.

It also checks \(176194\) instances of the double summation-by-parts identity through \(N=26\) against direct binomial sums, and \(486980\) cross-product inequalities for the nonnegative kernel through \(N=27\). The unique first ten-individual crossing and its exact rational richness values are verified.

Numerical enumeration cannot certify an arbitrary unbounded census. The general proof rests on the explicit ordered sign pattern of the twice-integrated abundance-frequency difference and the kernel's cross-product inequality; the code only provides finite stress testing of these key steps.
