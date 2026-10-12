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
Run `python3 verify.py` using the standard library. The code reconstructs the original family with exact rational entries, checks its two marginal distributions and ground-ground probability, verifies the denominator and rational unnormalized signals for \(p=3/4\), \(r=3/20\), and separately checks the Kraus completeness relation at a valid \(p=1/4\) and an invalid \(p=3/4\). It also checks the exact polynomial inequality underlying PPT for the boundaries and an interior value of \(\alpha\).

The proof in `RESULT.md`, not a finite numeric sweep, establishes the full continuum claim. The computed raw \(\|R^{T_B}\|_1-1\) is not an entanglement measure outside unit-trace states; the correctly normalized output has zero negativity. The numerical curves from the motivating article are not reconstructed and no independent review or audit is claimed.
