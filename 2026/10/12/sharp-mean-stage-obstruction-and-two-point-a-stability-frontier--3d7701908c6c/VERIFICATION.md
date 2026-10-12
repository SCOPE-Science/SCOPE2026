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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 and its standard library. The program uses rational polynomial arithmetic to verify two fully expanded identities after clearing denominators: the quadratic supporting bound for the stiff-limit function, and the cancellation identity at the two-point A-stability threshold. It also performs 309 exact-rational evaluations spanning stable two-point laws, stiff witnesses beyond the threshold, and a sequence approaching the optimal variance coefficient. No numerical approximation enters those checks.

The mathematical proof in `RESULT.md` supplies the arguments not established by finite evaluation: strict positivity of the boundary polynomial for every left-half-plane argument, the limit/interchange arguments for arbitrary probability laws including an atom at zero, and the optimality sequence for the universal coefficient. These checks are internal and do not constitute independent validation. Analytic extension to nonlinear systems, correlated stages, full A- or B-stability of a multidimensional update, and general order assertions are not verified.
