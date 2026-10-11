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

The normalized norm is
\[
M(s,t)^2
=
\max\{s^2+t^2+2st/\sqrt5,\ s^2+t^2-2st/\sqrt5\}.
\]

At every smooth sphere point, the unique Birkhoff tangent reduces the line norm to the maximum of two quadratics. Their sublevel intervals have centers \(0\) and \(\gamma_0\), with
\[
|\gamma_0|
=
\frac{z(1-k^4)}{1+k^4z^2}
\le\frac12,
\qquad
k=\frac{\sqrt5-1}{2}.
\]
Hence
\[
\mathcal M(x)\le\frac{\sqrt5}{2}.
\]

At \(e=(1,0)\), Birkhoff--James directions are exactly
\[
|a|\le\frac{|b|}{\sqrt5}.
\]
For \(y_r=(r,1)\), the line norm is the maximum of two quadratics centered at \(\alpha_+\) and \(\alpha_-\). Exact simplification gives
\[
\frac85-q_-(\alpha_+)
=
\frac{8r^2(5r^2+4\sqrt5\,r+9)}
{25(1+r^2+2r/\sqrt5)^2},
\]
\[
\frac85-q_+(\alpha_-)
=
\frac{8r^2(5r^2-4\sqrt5\,r+9)}
{25(1+r^2-2r/\sqrt5)^2}.
\]
Both are nonnegative. For \(r>0\), sufficiently large equal-norm levels have midpoint \(\alpha_+\); as \(r\downarrow0\), the midpoint norm tends to \(\sqrt{8/5}\). Therefore
\[
\sup_{x\in S_M}\mathcal M(x)=\sqrt{\frac85},
\qquad
DW=2\sqrt{\frac85}=\sqrt{\frac{32}{5}}.
\]

No numerical sampling, finite approximation, or external certificate is used as proof.
