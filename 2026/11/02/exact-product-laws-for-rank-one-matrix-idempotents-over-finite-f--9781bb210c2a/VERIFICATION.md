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

The theorem follows from a symbolic finite-field argument based on rank-one idempotent parameterization, a two-eigenvalue projective transfer matrix, multiplicative-character orthogonality, and conjugacy orbits. In particular, the cyclic trace character moment equals \(N^{1-k}\) for every nontrivial character; the consequent exceptional trace-one bias and exact conditional total-variation formula are established without numerical extrapolation.

`CHECK.py` independently enumerates all rank-one idempotents and all resulting matrices for products through lengths seven at \((n,q)=(2,2)\), six at \((2,3)\), and five at \((3,2)\). It compares exact rational pointwise masses (including outcomes absent from the enumerated support), nilpotency indices, trace probabilities, projective-cycle weights, and total-variation distances.

`CHECK_GF4.py` independently implements the four-element field and checks every resulting matrix-product distribution at \((n,q)=(2,4)\) through length five, including separate probabilities for all three nonzero traces.

Execution: `python3 CHECK.py` and `python3 CHECK_GF4.py` in an ordinary Python 3 environment. The exact stdout records are `CHECK_OUTPUT.txt` and `CHECK_GF4_OUTPUT.txt`. Both finish with `VERIFY_OK`.

**Limits:** The computations cover finitely many field sizes and lengths; the proof, not the computation, establishes the theorem for arbitrary prime powers and all word lengths. The checkers do not assess historical priority or provide independent mathematical audit.
