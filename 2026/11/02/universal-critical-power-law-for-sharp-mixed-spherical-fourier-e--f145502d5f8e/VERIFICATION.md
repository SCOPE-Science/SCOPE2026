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

The analytical proof in `RESULT.md` explicitly uses the finite-exponent best-constant formula and all-positive Bessel-zero cells from Xu's 2026 theorem as published premises. The new calculations concern the divergent common critical Bessel residue, the convergent critical adjacent-mode difference, its positive limit, and the sharp fractional and normalized asymptotics.

Run `python3 verify_critical_collapse.py` with NumPy and SciPy installed to reproduce the supplementary checks. Its execution passed for dimensions three and four, including residues, positive approximate critical modal differences and six distinct near-critical exponents. The approximate numerical coefficients are \(L_3\approx0.176150\), \(L_4\approx0.143480\), with corresponding leading absolute coefficients approximately \(48.5805\) and \(264.058\). These digits are observations, **not rigorously enclosed constants**.

Finite quadrature, including its leading-mean tail approximation, is not a proof of the convergence, positivity for every dimension, all-dimensional asymptotics, or global optimality. Those assertions rest on the Hankel/periodic-cancellation argument, Xu's zero-cell result, and his exact sharp constant. Independent audit has not been performed.
