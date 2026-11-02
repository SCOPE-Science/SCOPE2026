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

# Reproducibility and verification

Run `python verify.py` with packages in `requirements.txt`. The checker was executed against these standalone files. It passes symbolic cancellation; exact rational Jacobian, determinant, trace, forcing vector, and first-harmonic coefficient; comparisons of the paper's original payoff quotients with their continuous extensions; and three independently solved period-map shooting problems with positive interior margins.

Numerical periodic-orbit tests at forcing amplitudes \(0.03\), \(0.08\), and \(0.16\) give temporal mean cooperator fractions approximately \(0.499989730646\), \(0.499926994862\), and \(0.499708277440\), respectively. In each case the residual of \(\overline{x^2}=\bar x/2\) is below \(2\cdot10^{-9}\), with a shooting residual below \(10^{-9}\). The observed scaled mean deficits tend to the exact coefficient \(625/54772\).

The analytical proof in RESULT.md, not these finite tests, establishes the exact identity for every admissible group size and existing strictly interior periodic orbit. Periodic existence and local stability use the implicit-function theorem at the specific rational base point. Independent audit is not performed.
