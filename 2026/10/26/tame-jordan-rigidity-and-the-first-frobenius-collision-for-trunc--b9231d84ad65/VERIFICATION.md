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

The proof is symbolic. For finite regression, run `python3 artifacts/verify.py`. This program constructs the truncated substitution endomorphism in a monomial basis, subtracts the identity, multiplies matrices and computes finite-field Gaussian-elimination ranks without invoking the theorem to calculate those ranks.

The executed program checked 3,487 natural-module matrices with complete power profiles. Exhaustive cases included all normalized substitutions for \((p,m)=(2,3),(3,3),(3,4),(5,3),(5,4),(5,5),(5,6)\), and analogous extension-field checks for \((q,m)=(4,3),(9,4)\). First-wild depth strata were exhaustively checked for several small configurations and deterministically sampled in larger cases. A separate ten-case comparison checked the if-and-only-if threshold for similarity collisions of consecutive depths.

Observed final line:
`VERIFY_OK 3487 matrix-power profiles; exhaustive runs, deterministic samples, and first-wild similarity collisions`

The observations support the exact formulas, but finite enumeration does not establish the unlimited parameter statements. The all-field proof is in `RESULT.md`. No external or independent audit was conducted.
