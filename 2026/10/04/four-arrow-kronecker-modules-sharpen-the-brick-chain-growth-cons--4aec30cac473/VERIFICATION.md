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

The proof uses the general \(q\)-Kronecker lower bound from arXiv:2609.10217 and then performs a new specialization and normalization. For the staircase \(\delta_n\), the exact identities
\[
d_n-d_{n-1}=n,
\qquad
\frac{H_n}{H_{n-1}}=(2n-1)!!
\]
reduce the lower-bound sequence to the exact ratio checked by `artifacts/verify.py`.

The verifier checks exact integer arithmetic for \(3\le q\le8\) and \(1\le n\le20\), evaluates the two normalized constants at high precision, and checks the integer coefficient profile through \(q=1000\). Its output is summarized in `artifacts/certificate.json` and terminates with `CHECK_OK`.

Finite computation is not used to justify the infinite asymptotic statement. The latter follows from the displayed exact ratio and Stirling's formula. The verification does not test global optimality over unequal \(a,b\), other partitions, or constructions outside the square-staircase Kronecker family.
