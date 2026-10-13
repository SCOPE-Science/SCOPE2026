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
The universal theorem is proved symbolically in `RESULT.md`. The finite checker `verify.py` replays only exact algebra used in the displayed \(\kappa=4\), \(\varepsilon=1/10\) witness: the exact-line warm-start step, the long and short BB steps, the two endpoint second iterates, and the negative sign of the short-endpoint threshold polynomial.

The checker does not establish the all-dimensional statement by enumeration. The universal part rests on the analytic inequalities \(\alpha_1^{\mathrm S}\le\alpha_1\le\alpha_1^{\mathrm L}=\alpha_0\), \(\theta\ge2\mu\), and the Stieltjes sign pattern. The sharp family for arbitrary \(\kappa>2\) is proved by the exact quadratic inequality displayed in `RESULT.md`.
