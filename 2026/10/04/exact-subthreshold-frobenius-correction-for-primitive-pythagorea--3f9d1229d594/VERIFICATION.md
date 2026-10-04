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

The universal proof is the symbolic argument in `RESULT.md`. The executable check is finite and corroborative.

Run:

`python verify.py`

The checker uses only exact integer arithmetic. It performs two independent classes of checks:

1. For coprime \(1\le n,p\le10\) and \(1\le d\le n^2+p^2\), it compares the defining minimum \(\lambda_H(d)=\min\{h\in H:h-d\in H\}\) against the modular closed form. There are 4,418 such checks.
2. For every admissible \((n,p,m)\) with \(1\le n\le8\), \(n\le p\le9\), and \(Q<m<2Q\), it computes the Frobenius number independently by Dijkstra shortest paths on residue classes modulo the smallest generator and compares it with the theorem. There are 743 such cases.

The recorded output is:

`VERIFY_OK lambda_checks=4418 subthreshold_cases=743 exact_frobenius=all excess_positive=all min_excess=1 witness=(1, 1, 3, 2, 1, 16, 15, 1)`

Limits: this replay does not prove the theorem for unbounded parameters and is not an independent audit. The proof does not cover \(m\le Q\) or \(\gcd(n,p)>1\).
