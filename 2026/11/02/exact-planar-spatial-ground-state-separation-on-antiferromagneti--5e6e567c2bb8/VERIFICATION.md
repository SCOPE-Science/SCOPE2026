---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS. Spectral decomposition of the cyclic half-adjacency gives sum s_j dot s_(j+1) >= -Nc_N+(1+c_N)|M|^2/N. Explicit three-dimensional conical spirals attain this bound; even-N planar alternating configurations and all planar triangle resultant lengths attain it too. For odd N>=5, equality for XY unit complex spins forces z_j=A+Bt^j+Ct^-j. The five independent frequencies 0,+/-1,+/-2 and |z_j|=1 force only pure spiral or constant configurations, excluding every intermediate magnetization and proving a strict compactness gap. Local Hessian Jc_N L about each zero-field spiral, L sin(qj+phi)=2(1+c_N)sin(qj+phi), and sum sin^2=N/2 give the exact XY quadratic coefficient; transverse positivity, compact phase family and implicit minimization control O(h^3). Independent numerical checks verified susceptibility-coefficient algebra for odd N=3,5,7,9,11,13; universal claims rest on the analytic proof, not numerical minimization.

## originality

PASS

PASS, qualified. Schmidt-Luban 2002 already prove the full three-dimensional spectral parabola and describe a numerically observed planar deficit on a pentagon, explicitly without rigorous proof in their Section 6.3 discussion. This claim adds all odd N>=5 exact rigorous separation and the planar weak-field susceptibility ratio, while crediting their established 3D result. Konstantinidis 2014 concerns open chains and biquadratic exchange, while Owerre-Nsofini 2015 concerns quantum/anisotropic models. An older rigorous XY odd-cycle curvature calculation under different terminology remains a priority risk.

## value

PASS

PASS. The strict gap is a nontrivial dimension obstruction for frustrated finite classical cycles and rigorously establishes a type of planar deficit left numerically observed but unproved in the pertinent 2002 paper. The exact weak-field susceptibility ratio distinguishes planar from spatial response, with a meaningful pentagon golden-ratio value and limiting half-response; not a generic restatement of the known 3D spectral lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
