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

For an odd regular \(n\)-gon of circumradius \(R\) and inradius
\[
r=R\cos(\pi/n),
\]
the side normals \(u_i\) satisfy
\[
\sum_i u_i=0.
\]
At a translated center \(x\), writing \(t_i=\langle x,u_i\rangle\), the exact cone-volume calculation gives
\[
\mu_p(P_n,x)^p
=
\frac1{nr}
\sum_i (R+t_i)^p(r-t_i)^{1-p}.
\]

For \(p=1\), the sum is
\[
\frac1{nr}\sum_i(R+t_i)=\frac Rr.
\]
For \(p>1\), the scalar kernel
\[
f_p(t)=(R+t)^p(r-t)^{1-p}
\]
has
\[
f_p''(t)
=
p(p-1)(R+r)^2(R+t)^{p-2}(r-t)^{-p-1}>0.
\]
Jensen's inequality therefore proves the global minimum at zero mean, with equality only when all \(t_i=0\).

At the center, every side-normal support ratio is \(R/r\), and every side has cone-volume mass \(1/n\), so the normalized log-mixed volume is also \(R/r\). The same constant-ratio observation evaluates every centered normalized \(p\)-mixed volume for \(0<p<1\).

The embedded `verify.py` was replayed from its actual package path before packaging. It reconstructs every regular polygon for \(3\le n\le31\), checks the relevant support values, tests the \(p=1\) center-independence at random interior points for odd \(n\), and checks the \(p>1\) convexity prediction. It returned:

`VERIFY_OK regular polygon p-asymmetry spectrum`

The finite replay is a consistency test only. It is not used to infer the all-\(n\) or all-\(p\) theorem.
