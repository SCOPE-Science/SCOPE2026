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

# Reproducibility and exact scope

The claim is about two specific vertex-defined regular polyhedra, one shared uniformly spherical normal, the standard projected-area brightness, and the ordinary support-function width. The derivation uses Cauchy's facet formula, the exact spherical-triangle area formula and spherical integration by parts; every boundary contribution is elementary.

Run `python spherical_integrals_check.py` (SymPy) to replay the exact vertex/edge moments of both spherical triangles and their sum. Run `python covariance_certificate.py` (Python standard library) to certify strict rational bounds for each exact covariance. Both passed on the embedded code, and only those two code files are needed. The rational code uses integer-square-root bounds, Machin's identity, and strict alternating-arctangent brackets; no floating-point conclusion establishes a sign. A two-million-sample Monte Carlo agreement check was performed separately but is not needed for the proof.

The scientific claim has not been independently audited. A failed code run on another system cannot by itself disprove the analytic theorem; inspect the derivations as well as the implementation. The self-review does not assert expert approval or formal mathematical certification.
