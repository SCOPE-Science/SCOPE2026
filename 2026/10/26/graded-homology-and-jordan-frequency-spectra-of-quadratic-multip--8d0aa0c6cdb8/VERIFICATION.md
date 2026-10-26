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

The included `verify.py` implements field arithmetic over the binary field and over the four-element field using the polynomial `t^2+t+1`, explicitly enumerates homogeneous quadratics, constructs alternating coefficient matrices and all graded multiplication matrices, and computes their row-echelon ranks. It compares each reconstructed homology dimension and total Jordan rank against the theorem and compares complete rank-stratum histograms against the Gaussian-binomial formula.

Exhaustive configurations: `(q,n)=(2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(4,4)`. Additional deterministic tests: 48 coefficient vectors for each of `(2,6),(4,5),(4,6),(2,7)`. Total checked inputs: 5,454.

Reproduce by running `python3 verify.py` in a directory containing only this package's verifier. The expected final diagnostic is `VERIFY_OK_CHAR2_QUADRATIC_MULTIPLIERS 5454`. The formal tensor-complex argument, not numerical enumeration, proves the statement in every dimension and even finite field. The checker does not separately enumerate all larger dimensions.
