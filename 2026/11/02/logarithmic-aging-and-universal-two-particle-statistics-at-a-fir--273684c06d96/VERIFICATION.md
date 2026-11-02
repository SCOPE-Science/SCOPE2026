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

# Verification of the two-particle threshold-reset limit theorem

Run `python verify.py` from the extracted folder. Only the Python standard library is required. The script checks the exact survival and derivative, the conditioned Brownian spatial density at finite ages, the Rayleigh limiting density and its moments, the distance-ratio law, the Pearson coefficient algebra, and logarithmic truncated-mean growth using Simpson quadrature. The finite assertions are consistency evidence, not a computer proof of the renewal or asymptotic theorem.

The analytic proof relies on the source's exact killed-Brownian kernel and on the already established index-one renewal theorems of Erickson (1970). The logarithmic-age law is explicitly prior mathematics. The new combined conditional spatial conclusions follow by total-variation convergence, the continuous mapping theorem, and positive-moment asymptotics; all limiting normalizations are stated in RESULT.md. Exactness of the coefficient \(\pi/4\) follows from \(\Gamma(3/2)^2/\Gamma(2)=\pi/4\). Independent verification and a literature-wide priority assessment have not been performed.
