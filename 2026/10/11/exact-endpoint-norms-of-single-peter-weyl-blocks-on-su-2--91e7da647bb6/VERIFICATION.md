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

The proof uses the exact Peter--Weyl central idempotent \(m\chi_r\), the \(SU(2)\) Weyl character formula \(\chi_r(\theta)=\sin(m\theta)/\sin\theta\), and the normalized Weyl integration formula. These identities reduce both endpoint norms to the same scalar integral
\[
\frac{2m}{\pi}\int_0^\pi |\sin(m\theta)|\sin\theta\,d\theta.
\]
For \(m\ge2\), splitting at every zero \(j\pi/m\) and using an exact antiderivative produces
\[
\int_0^\pi |\sin(m\theta)|\sin\theta\,d\theta=\frac{2m}{m^2-1}\cot\left(\frac{\pi}{2m}\right).
\]
The case \(m=1\) is separate and equals one after the outer normalization.

`verify_su2_projection.py` checks the partitioned antiderivative evaluation against the cotangent expression for \(2\le m\le500\), performs direct numerical quadrature at selected dimensions, and checks convergence of \(\|P_r\|/m\) toward \(8/\pi^2\). No finite computation is used to prove an all-dimension statement.

Scientific limit: this verification does not establish a higher-rank analogue or bibliographic uniqueness.
