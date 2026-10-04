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
# Verification

The stated payoff and invasion-fitness formula were replayed symbolically using exact rational coefficients.  The replay verifies
\[
D_r(x)=(-2+3r)\left(x-\frac12\right),\qquad
D_r'(x)=-2+3r,
\]
and
\[
\left.\frac{\partial^2\varphi_x^r(y)}{\partial y^2}\right|_{y=x=1/2}=-1+2r,
\qquad
\varphi_{1/2}^r(y)=\frac{2r-1}{2}\left(y-\frac12\right)^2.
\]
The exact inequalities therefore give convergence stability for \(r<\tfrac23\), evolutionary stability for \(r<\tfrac12\), and the branching-point overlap \(\tfrac12<r<\tfrac23\).

A replay script is included.  It uses symbolic algebra only as a consistency check; the proof in `RESULT.md` is self-contained.  No numerical experiment is used as evidence for an infinite or continuum statement.

Limits: the checks establish the local adaptive-dynamics classification for the displayed model.  They do not establish post-branching coexistence dynamics or robustness to alternative assortment mechanisms.
