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

# Verification of finite Hermite center-curvature identity

The proof in `RESULT.md` is the primary verification. It establishes the exact Wronskian identity for all integers \(0\le j<q\), the convergent generating function for the finite central-binomial sum, and the two parity-dependent increments in \(V_q''(0)\). The nonvanishing sign is exact, not inferred from numerical samples.

Run `python check_curvature.py` using Python 3.9 or later. The self-contained exact part uses `fractions.Fraction` and checks the all-order formula for \(1\le q\le100\) and both finite binomial identities for \(1\le m\le80\), reporting 260 exact rational assertions. With SciPy and NumPy installed, it additionally integrates 16 Hermite Gram matrices directly and compares their second derivatives. The observed output was `260 exact rational checks passed` and `16 independent numerical Hermite-integral comparisons passed`.

These finite computations do not prove the infinite family, global extremality, historical priority, or independence. They supplement the written induction only. All numerical evaluations use the normalized physicists' Hermite coordinate explicitly specified in `RESULT.md`.
