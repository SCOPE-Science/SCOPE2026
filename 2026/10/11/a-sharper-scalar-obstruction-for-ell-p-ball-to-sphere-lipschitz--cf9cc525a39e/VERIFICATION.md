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

The critical source premise is the exact pre-simplification inequality in Mahesh, arXiv:2609.13342v1. The proof here does not use the source's subsequent coarse replacement of the second radical.

The new check is analytic. Differentiating \(F_{p,K}\) gives the ratio bound
\[
\frac{B(r)}{A(r)}\le1+\left(\frac{1-r}{r}\right)^{p-1}.
\]
On \(r\ge2^{1/p}/K\), this is at most \(K\) when \(K\ge3\) and \(1<p\le2\), by splitting according to whether \(K/2^{1/p}-1\) is at most or at least one. Therefore \(F_{p,K}\) is nonincreasing on the necessary interval.

Limits: this verifies only a necessary lower-bound obstruction. It does not establish an exact value of \(k_0(\ell_p)\), does not claim optimality of \(\Lambda_p\), and does not extend the monotonicity argument to \(p>2\).
