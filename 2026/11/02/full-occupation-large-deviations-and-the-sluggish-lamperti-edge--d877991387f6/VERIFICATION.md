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

# Verification and scientific limits

Run `python verify.py` from the extracted package directory. The supplied deterministic verifier requires only Python 3 standard-library modules and passed 298 checks in the reviewed package. Checks compare numerical integration of the Lamperti fraction density against its stable-variable Stieltjes transform, evaluate the unique pole for representative parameters, test reflection symmetry, verify Brownian reduction, finite-difference SCGF curvature, strict convexity sample values, and the large-tilt exponent via an independently parameterized pole.

The analytical theorem is valid for the continuum symmetric self-similar diffusion with \(\alpha>0\), \(\mu=1/(\alpha+2)\) and Poisson resetting \(r>0\), not just the finite tested values. Independent mathematical review, literature-wide priority certification, and simulation of a finite-spacing lattice have not been performed. The full LDP rests on the positive Laplace-pole renewal theorem and Gärtner–Ellis; numeric checks do not replace those arguments.
