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

# Verification record

Run `python3 verify_klein.py` from any directory. It uses only the Python standard library and no network access, external data files, machine-specific paths, numerical approximations, or random search.

The verifier checks every one of the \(1330\) three-line determinants in the rank-two ring with relation \(\alpha^2+\alpha+2=0\), computes their complete integer norm histogram, enumerates the \(49\) generic incidence supports, checks both special-fiber line multiplicity distributions and the reduced intersection lattices, and determines all \(49\) two-prime marked-point specializations via exact division by the relevant local uniformizer. It checks pair-of-line independence of each point's reduction.

Actual command result:

`KLEIN_21_INTEGRAL_ARITHMETIC_REDUCTION_AND_49_SPECIALIZATIONS_PASS`

Exact output norm histogram: `{0: 112, 1: 169, 2: 228, 4: 271, 8: 320, 16: 156, 32: 70, 64: 4}`.

The conclusion for infinitely many non-dyadic primes follows from the field norm of every nonzero determinant being a power of \(2\), not from finite testing. The verifier does not establish model-independent reductions, intrinsic singular-scheme lengths, or a historical novelty certificate. No independent external mathematical validation has been performed.
