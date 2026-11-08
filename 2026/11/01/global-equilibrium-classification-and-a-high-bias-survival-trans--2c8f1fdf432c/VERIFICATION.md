---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

From positive boundary flux, exclude one-patch boundary states; add equations to derive u=K/(1+t²) and solve the linear chemical sums/differences. Independently verified the exact tanh addition identity tanh z=t+gamma t(1-t²)/(1+t²)=(t+w)/(1+tw), with w=gamma t/[1+(1-gamma)t²]. The inverse-atanh branch is strictly increasing because atanh(v)/v and the positive rational prefactors increase, w increasing throughout its admissible domain. Checked exact coefficient (4+3gamma²+gamma³)/3 of t² and t_gamma endpoint root. Endpoints force threshold chi_c and infinity; two signs generate precisely the two nonuniform states. No transient stability or general graph assertions.

## originality

PASS

Kim–Zhang–Zhao–Cooney arXiv:2610.31049 Sec.3 Example two patches establishes the homogeneous linear threshold Eq.(3.18), numerical asymmetry patterns and a Jensen mass deficit Eq.(3.19), but does not globally enumerate all stationary roots or prove a monotone inverse-tanh parametrization/high-bias survival dichotomy. Continuum PDE stationary literature is a different model. A general nonlinear network result might imply it but was not found.

## value

PASS

A complete nonlinear equilibrium diagram is independently meaningful: excludes folds, hidden branches and coexistence below threshold and identifies a sharp migration-to-growth survival transition. The result goes beyond the source linear instability and numerical plots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
