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

The theorem is proved by an all-orders structural case split. The finite computation below is a separate stress test and is not used to infer the infinite statement.

`verify.py` constructs \(H_n=K_n\odot K_1\) directly for each \(2\le n\le6\), enumerates every labeling in \(\{0,1,2\}^{2n}\), tests the Roman domination condition from adjacency, and compares the resulting weight histogram with
\[
\bigl(x+3x^2+2x^3+x^4\bigr)^n-\bigl(x+2x^2+x^3\bigr)^n+\bigl(2x^2+x^3\bigr)^n.
\]
It also verifies that the minimum weight is \(n+1\), that exactly \(n\) functions attain that weight, and that the total number is
\[
7^n-4^n+3^n.
\]

The tested range contains \(597861\) complete labelings and \(60\) nonzero coefficient comparisons. The computation does not certify any graph family beyond the stated \(H_n\), and it does not substitute for the proof for \(n>6\).
