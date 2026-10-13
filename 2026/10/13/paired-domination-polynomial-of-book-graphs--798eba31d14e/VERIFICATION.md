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

The all-orders proof is the spine/page-state argument in `RESULT.md`. The standalone script `verify.py` is a finite regression check. It constructs the square book directly from its edges, enumerates every subset for \(1\le n\le8\), checks domination vertex by vertex, and checks perfect-matchability of the selected induced graph by an independent recursive matching search.

For each \(n\ge2\), the script compares the entire brute-force coefficient vector with
\[
x^2(1+x^2)^n+n(n-1)x^4(1+x^2)^{n-2}+(2n+1)x^{2n},
\]
and separately verifies that every accepted set belongs to exactly one of the four stated structural types and every classified set is accepted. It also checks the boundary \(B_1\cong C_4\) directly without treating that boundary as part of the claimed family formula.

These finite checks do not certify arbitrary \(n\); the symbolic proof supplies the infinite-family conclusion.
