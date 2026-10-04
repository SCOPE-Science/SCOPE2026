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

The analytic proof was replayed by coefficient comparison. In particular, with
\[
D=c_sd_r-c_rd_s,\qquad
\gamma_r=\frac{d_s}{2D},\qquad
\gamma_s=-\frac{d_r}{2D},
\]
the identities
\[
2(\gamma_rc_r+\gamma_sc_s)=-1,\qquad
2(\gamma_rd_r+\gamma_sd_s)=0
\]
give
\[
(\gamma_r+\gamma_s)a_0-a_1=\gamma_rt(r)+\gamma_st(s).
\]
The sign relations \(d_r<0<d_s\) and \(c_r,c_s<0\) imply positive quadrature weights.

The accompanying `verify.py` was executed successfully. It checks \(1\le n\le100\) numerically for grid nonnegativity, positive quadrature weights, the basis coefficient identities, and equality of the two closed forms. The finite check is not an infinite proof; the universal conclusion rests on the analytic argument in `RESULT.md`.

The first-public-date field uses the journal issue posting date 2018-11-29. The article page itself was posted 2018-12-03; received, revised, and accepted dates were not used as public-source dates.
