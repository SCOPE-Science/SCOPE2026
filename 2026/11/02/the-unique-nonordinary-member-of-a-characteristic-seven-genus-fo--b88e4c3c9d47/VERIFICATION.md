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

# Exact reproducibility

Run `python3 verify.py` with standard Python 3 (no third-party packages). The script reconstructs coefficients of the seventh-power Cartier matrix from the multinomial expansion, validates the special-fiber nilpotence ranks, certifies the four finite extension rings are fields, and computes curve point counts by two distinct exact enumeration methods. It then derives the special numerator using Newton identities and the genus-four functional equation. Expected output is embedded in `verify_output.txt`, ending in `VERIFY_OK`.

The four field moduli are `t` for the prime field, `t^2+1`, `t^3+t+1`, and `t^4+t+1`. For each modulus, every nonzero residue class is checked to have a multiplicative inverse by a finite multiplicative-order test; no irreducibility assertion is left to a probabilistic oracle. Counts of \(C_0(\mathbb F_{7^m})\) for \(m=1,2,3,4\) are \(8,50,344,2094\), and an independent ordinary-fiber test uses \(a=2\).

The proof of the all-geometric-parameter classification is symbolic; finite enumeration is used only for the exact zeta numerator and its Newton slopes. The proof does not rely on numeric floating point or any historical verification files.
