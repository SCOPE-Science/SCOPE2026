---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

The Le--Rhaly interrupter gives unshifted \(D_{0,m}=A^*(I-P_m)A\ge0\). Finite coordinate compressions satisfy exact cancellation \(\operatorname{Tr}(E_N D_{0,m}E_N)=\sum_{j\le N,n>N}|A_{nj}|^2\). The large-n scaling \(N A_{nj}\to (m/u)(1-v/u)^{m-1}\), uniform on compact \(u\in[1,R],v\in[0,1]\), yields a double Riemann integral; the remaining tail is O(1/R) uniformly in N. After substitution the limit is \(m^2\int_0^1\int_0^1(1-vw)^{2m-2}dvdw=m^2H_{2m-1}/(2m-1)\). Positivity plus bounded trace of increasing compressions proves actual trace class. For each fixed shift, \(K=M_{\alpha,m}-M_{0,m}\) has entries O(n^-2) per n-th row, whose \(\ell^2\) norms are O(n^-3/2), giving a trace-class row decomposition. All terms in \(D_\alpha-D_0\) are trace class and cancel in trace by cyclicity; Ma's hyponormality iff \(\alpha\ge0\) identifies the trace-norm equality boundary. Independently evaluated the harmonic values m=1:1, m=2:22/9, m=3:411/100, m=4:1452/245; finite flux checks were corroborative and not substituted for the trace-class proof.

## originality

PASS

Ma gives the exact positivity/hyponormality parameter classification for the same two-parameter generalized Cesàro matrices but no trace-class formula. Le--Rhaly supplies positivity via an unshifted diagonal interrupter but no harmonic trace evaluation and no invariance under negative or positive shifts. Earlier order-by-order results concern hyponormality/posinormality; the related Cesàro Mellin product-defect trace is a different operator. The boundary-flux and nuclear perturbation arguments provide a new natural Schatten invariant. Possible Berger--Shaw trace-area identities and unindexed Hausdorff operator sources remain residual risks.

## value

PASS

An exact, parameter-invariant Schatten-1 trace for a natural two-parameter nonnormal matrix family is a meaningful infinite-dimensional operator invariant. The boundary-flux proof and summable row perturbation explain why the trace survives loss of hyponormality, yielding the precise trace-norm equality phase boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
