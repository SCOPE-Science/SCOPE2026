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
# Exact verification

Run `python3 verify.py` with Python 3.9 or newer. The script imports only `fractions.Fraction` and verifies, by equality of integer-rational polynomial coefficients, the identity
\[
-yR(y)/C=y\left[(1-y)Q(y)-1\right].
\]
It also verifies positive infection coefficients, simple endemic roots, derivative signs and the sharp attractor count for each integer \(M=1,\ldots,18\). It separately reproduces the five exact rational rates and three attracting endemic prevalences for the six-body witness. The executed script returned `VERIFY_OK` and the exact prescribed fractions; no tolerance-based root fitting was used.

The unrestricted theorem relies on the symbolic elementary-symmetric-sum inequality and the sign-alternation argument in RESULT.md, not on asserting that finite cases imply all cases. The code checks the deterministic scalar field only; the finite-population stochastic process and a stochastic-to-ODE limit for arbitrary order are not verified here.
