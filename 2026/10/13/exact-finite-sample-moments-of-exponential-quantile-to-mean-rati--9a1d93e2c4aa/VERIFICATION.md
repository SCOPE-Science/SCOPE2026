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

The theorem is proved analytically for every \(n\ge1\) and \(1\le k\le n\). The computational checks below are supplementary.

`checker.py` uses exact rational arithmetic. For each \(1\le k\le n\le300\), it forms the weighted Dirichlet linear statistic directly from the moment identities
\[
\mathbb E P_i=\frac1n,\qquad
\mathbb E P_i^2=\frac{2}{n(n+1)},\qquad
\mathbb E P_iP_j=\frac1{n(n+1)}
\]
and verifies the compact harmonic expressions for \(\mathbb E Q_{n,k}\), \(\mathbb E Q_{n,k}^2\), and \(\operatorname{Var}(Q_{n,k})\).

For odd samples it also verifies, for \(1\le m\le1000\), the exact decrement
\[
\left(H_{2m+3}-H_{m+1}\right)-\left(H_{2m+1}-H_m\right)
=-\frac1{(2m+2)(2m+3)}.
\]

The checker does not certify the limiting statements by finite enumeration; those follow from the Riemann-sum argument in the proof.
