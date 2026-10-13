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

The finite proof is analytic. A second route uses the exact joint transform of the whitened Wishart matrix \(U\sim W_p(\nu,I)\):
\[
M(s,t)=\mathbb E\left[|U|^s e^{t\operatorname{tr}U}\right]
=
2^{ps}
\frac{\Gamma_p(\nu/2+s)}{\Gamma_p(\nu/2)}
(1-2t)^{-p(\nu/2+s)}.
\]
This is valid for \(\nu+2s>p-1\) and \(t<1/2\).

Differentiating the cumulant \(K=\log M\) at the origin gives
\[
\frac{\partial^2K}{\partial s\,\partial t}(0,0)=2p,
\]
which is \(\operatorname{Cov}(\log|U|,\operatorname{tr}U)\). Also
\[
\frac{\partial^2K}{\partial t^2}(0,0)=2\nu p
\]
and
\[
\frac{\partial^2K}{\partial s^2}(0,0)
=
\sum_{j=1}^{p}\psi_1\!\left(\frac{\nu-j+1}{2}\right).
\]
Thus the transform independently reproduces every finite second-order quantity used in the claim.

`verify_wishart_trace_logdet.py` evaluates this transform with central finite differences for a parameter grid, compares against the analytic derivatives, checks that every exact correlation lies in \((0,1]\), and checks convergence in thin, proportional, and near-square regimes. The replay is numerical and supplementary; it is not used as a proof.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK mixed_checks=60 t2_checks=60 s2_checks=60 corr_checks=60 aspect_checks=9`.
