---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Explicit Gaussian integration gives p,q,b and the eigenvalue. Since the spectral gap p(0)-q(0)=2Le^{-L²}/sqrt(pi)>0, differentiating the simple top eigenvalue gives F_L(0)=4Le^{-L²}/sqrt(pi)>0 for every positive L. Uniform Taylor/analytic perturbation near a0=1/sqrt2 yields A2 prime(a0)=0, A4 prime(a0)=-sqrt2/(45sqrt(pi e)), the optimizer a_L=a0-sqrt2 L^4/180+O(L^6), and mass 4L/sqrt(pi e)[1-L²/2+41L^4/180+O(L^6)]. Gaussian tails and strict local concavity give exactly ±a_L for sufficiently small L, not for all L. Independent 65-digit central-curvature checks at five widths and optimizer O(L^6) residual at three small widths.

## originality

PASS

The older polyanalytic Fock papers establish Hermite matrix representations but not the variable-center finite-interval top-eigenvalue maximum or quartic shift. This is a precise rank-two Gaussian concentration theorem; priority remains qualified in optical spectral concentration literature.

## value

PASS

In the first nontrivial two-mode Hermite band translation breaks central optimality at every width; exact 2/sqrt(e) gain and unexpected vanishing quadratic shift answer a motivated spectral localization problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
