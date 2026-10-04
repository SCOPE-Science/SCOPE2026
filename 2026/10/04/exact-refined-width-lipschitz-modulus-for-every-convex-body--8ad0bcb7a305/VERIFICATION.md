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

For a fixed \(u\), choose \(A\) and \(B\) from the two opposite support faces with
\[
\lVert A-B\rVert=s_K(u).
\]
Writing
\[
A-B=w_K(u)u+y,
\qquad y\perp u,
\]
gives
\[
\lVert y\rVert=p_K(u).
\]
If \(p_K(u)>0\), set
\[
\xi=y/p_K(u),
\qquad
v_t=\cos(t)u+\sin(t)\xi.
\]
Then the same support pair is an admissible lower-bound witness at the perturbed direction:
\[
w_K(v_t)
\ge
\langle A-B,v_t\rangle
=
w_K(u)\cos t+p_K(u)\sin t.
\]
Since \(\rho(u,v_t)=t\) for sufficiently small positive \(t\),
\[
\limsup_{t\downarrow0}\Delta w_K(u,v_t)\ge p_K(u).
\]
The inspected published Proposition 4.4 gives the reverse inequality, so equality follows. At \(p_K(u)=0\), the published upper bound already forces equality.

The same witness at a direction maximizing \(p_K\) gives the global lower bound \(\sup\Delta w_K\ge\widehat M_K\); Proposition 4.4 gives the reverse global inequality.

The embedded `verify.py` was replayed from its actual package path. It checks the support-pair/tangential-component construction on a cube at a facet normal and other nonsmooth polytopes, where opposite support faces are not singletons, and on a smooth ellipsoid. The replay output was:

`VERIFY_OK exact refined width modulus`

Finite computations are consistency checks only. The all-dimensional proof is the support inequality above.
