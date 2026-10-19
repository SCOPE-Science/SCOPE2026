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
# Verification

Run `python3 order15_fullspark_checker.py` using the included standalone Python 3 script. It requires no external modules. It executes an exact non-probabilistic orbit census and checks all relevant maximal Fourier minors using integer arithmetic modulo the primes 31 and 61; both selected residues have multiplicative order 15.

Every one of the five excluded affine classes is witnessed by an exact signed-permutation determinant expansion with fifteen zero integer coefficients. Every remaining balanced representative has its complete family of maximal minors checked: 53,803 are nonzero modulo 31 and 1,125 additional minors are nonzero modulo 61, for 54,928 in total. Any characteristic-zero vanishing at a primitive fifteenth root would imply vanishing in both finite fields. Counting all balanced row sets and invoking affine and complement invariance proves the asserted classification for every subset.

Observed checker result: `PASS: finite exhaustive certificate without floating point.` The output also gives the complete cardinality census and 2,310 proper full-spark row sets. The independent status field above concerns independent mathematical audit, which has not been performed; the computational evidence is not represented as independent certification.

Limits: no floating-point conditioning bounds, no other Fourier orders, and no claim of an infinite classification.
