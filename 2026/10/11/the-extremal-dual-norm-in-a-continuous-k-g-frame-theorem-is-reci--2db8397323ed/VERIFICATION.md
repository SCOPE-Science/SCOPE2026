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

The optimal lower bound satisfies
\[
A=\sup\{\lambda>0:\lambda\|K^*f\|^2\le\|T_\Lambda^*f\|^2\ \text{for all }f\}.
\]
Therefore
\[
\inf\{\mu>0:\|K^*f\|^2\le\mu\|T_\Lambda^*f\|^2\ \text{for all }f\}=\frac1A.
\]
Douglas factorization gives \(K^*=\Phi T_\Lambda^*\) with \(\|\Phi\|^2=1/A\), and Theorem 2.2 transfers \(\Phi\) to a dual synthesis operator of the same norm.

For the exact counterexample, on a one-point measure space take \(H=\mathbb C\), \(K=I\), and \(\Lambda=I/2\). Then \(A=1/4\), while the dual equation forces \(\Gamma=2I\), so \(\|T_\Gamma\|^2=4\). The complete public preprint was inspected as text and by page image at the theorem statement and proof.
