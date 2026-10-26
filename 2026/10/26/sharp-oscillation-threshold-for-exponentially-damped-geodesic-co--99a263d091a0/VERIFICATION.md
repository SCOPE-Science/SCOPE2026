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

# Verification details

The exact symbolic checker `check_spherical_symbolics.py` was executed successfully with Python 3 and SymPy. It expands \(G_{a-1}-G_{a+1}\), verifies the factor \(4aP/(D_{a-1}D_{a+1})\), verifies the algebraic sharp root for \(\omega^2\), checks two rational-parameter spectral signs, and differentiates the polynomial with respect to \(u=\lambda^2\).

Analytic steps independent of the code: polar measure \(4\pi\sinh^2r\,dr\) and normalized spherical functions \(arphi_\lambda(r)=\sin(\lambda r)/(\lambda\sinh r)\); Laplace sine integral for \(a\pm1>0\); rational positivity and monotonicity; radial Plancherel necessity and positive principal-spherical-function inversion sufficiency. The checker is a reproducibility aid, not a replacement for these analytic steps or an independent scientific audit.

The exact scope is real hyperbolic three-space at sectional curvature \(-1\), with \(a>1\) and \(\omega\ge0\). No numerical sweep is claimed exhaustive, and no claims about \(a\le1\) or higher-dimensional hyperbolic spaces are made.
