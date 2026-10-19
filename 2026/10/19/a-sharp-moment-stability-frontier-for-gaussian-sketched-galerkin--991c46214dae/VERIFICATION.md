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

The exact reduced-rate identity is \(\mu+\beta Z/\sqrt V\) with independent \(Z\sim N(0,1)\) and \(V\sim\chi^2_\ell\). Critical analytic checks are (i) Gaussian independence from orthogonal input directions; (ii) inverse chi-square moments exist only for orders strictly smaller than half the degrees of freedom; (iii) the positive exponential moment of \(1/\sqrt V\) diverges at the origin for every positive multiplier; and (iv) fresh-sketch Euler conditional moments multiply independently. These steps constitute the proof of the infinite and finite claims; sampling does not.

`check.py` has been executed with Python, NumPy and SciPy. It checks a deterministic negative-rate SPD witness, 6 exact Student-versus-beta comparisons, 18 Monte Carlo quantile comparisons, 4 finite-second-moment comparisons and the exact three-row Euler stability calculation. Random sampling is only diagnostic and does not establish the claimed infinite moments or all-parameter statements.

The statement is restricted to the fixed one-dimensional real Gaussian-sketched Galerkin model, exact arithmetic, and the two explicit sketch-reuse conventions. The independent audit remains unperformed.
