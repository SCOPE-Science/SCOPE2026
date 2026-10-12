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

The proof uses the published expression for \(\Delta_1\) in Theorem 1.1 of arXiv:2610.01524v1. Under \(A=p^{a+o(1)}\), \(B=p^{b+o(1)}\), and \(C=p^{c+o(1)}\), the direct exponent of \(\Delta_1\) is compared with
\[
2r\zeta_r=S-\left(\frac12+\frac1{2r}\right)-\max\left\{M-1-\frac1{2r},0\right\}.
\]
The exact-rational script `verify.py` checked equality of these two expressions in \(10935\) parameter/moment cases. It separately checked \(550\) rational diagonal points against Corollary 1.2 and verified \((k,a,b,c)=(2,1/20,1/5,1/5)\), including \(\zeta_4=1/320\).

Replay command: `python verify.py`

Expected and observed output: `VERIFY_OK algebra_cases=10935 diagonal_cases=550 anisotropic_example=1`

The finite replay is a consistency check only. The infinite statement is proved by exact exponent algebra and the three-case inequality \(H_r\ge H_\infty\), together with \(H_r\to H_\infty\). No assertion is made about optimal cancellation outside the region, and boundary equality is not promoted to a power saving because the theorem contains a \(p^{o(1)}\) factor.
