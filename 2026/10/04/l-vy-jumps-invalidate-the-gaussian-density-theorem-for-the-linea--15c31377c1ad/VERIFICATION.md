---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Fresh reconstruction confirms the mathematical correction. A stable linear SDE with an additive compensated-Poisson term has a nonlocal jump generator and stationary Lévy stochastic convolution. For a scalar projection \(v^T Y\), the fourth cumulant is \(\int_0^\infty\!\int (v^\top e^{As}h(u))^4\,\nu(du)\,ds\); a nonzero value rules out a Gaussian law. Independently recomputing the package witness gives R~=26.6251093071, I*=3.3469399491, S*=0.5432290275, V*=0.5435059597, drift eigenvalues about −2.59513, −9.20189, −8.53162, and \(\kappa_4(e_1^\top Y_\infty)=2.22362604\times10^{-6}>0\). The true log-jump variance rate \(\log(1.1)^2=0.00908403037\) differs from 2(0.1−ln 1.1)=0.00937964039. Thus the displayed local Gaussian equation cannot be the exact stationary forward equation of the printed jump process.

## originality

PASS

PASS only for the source-specific correction, not for the general Lévy-OU fact. General non-Gaussian Lévy-driven Ornstein–Uhlenbeck theory is old and is excluded from the novelty claim. Fresh searches of the exact SVI title, Theorem 5.1, log-normal density and jump/Fokker–Planck correction found the original article and general Lévy-OU literature but no prior published correction applying the fourth-cumulant/nonlocal-generator objection to this theorem.

## value

PASS

The distinction between a genuine jump generator and a local diffusion equation is substantive: it changes the exact stationary law and already changes the covariance for an explicit admissible source parameter set. The correction identifies the Brownian-only exact boundary and the nonlocal term required for any exact jump-density calculation. This is more than a cosmetic notation issue, even though the source uses approximation language in places.

The dated certificate retains the supplied scientific assessment, sources and limitations.
