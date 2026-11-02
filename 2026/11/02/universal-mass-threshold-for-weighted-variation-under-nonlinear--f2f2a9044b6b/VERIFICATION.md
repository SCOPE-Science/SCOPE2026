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

# Verification of the nonlinear star variation classification

The mathematical proof is in `RESULT.md` and uses the full directional derivative of the edge \(\ell^1\) norm, retaining contributions from initially zero edge differences. For \(1<p<2\), uniqueness is supplied by weighted monotonicity of the graph \(p\)-Laplacian rather than a false local Lipschitz assumption at zero.

Run `python verify.py` with Python 3.10+ and only its standard library. The program checks 26,460 exact-rational generic initial slopes, 15,120 exact-rational one-edge equality witnesses, 1,260 exact-rational mass feasibility profiles, 5,320 floating-point fractional \(p\) profiles and 15,000 explicit-Euler inequalities at one stable nonlinear choice. The finite profile tests cannot certify every continuous parameter combination, and Euler tests do not prove a continuous-time inequality; the full proof covers those limits.

No external or independent audit is claimed.
