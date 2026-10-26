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
# Reproducibility notes

The self-contained \(\texttt{verify.py}\) uses no external libraries. It independently tests positive-integer digit supports and counts three-summand sums by exhaustive unordered triple enumeration, including repeated summands. Directly checked configurations are \((g,k)\in\{(4,1),(4,2),(4,3),(5,1),(5,2),(6,1),(6,2),(7,1),(7,2)\}\). The executed code returned \(\texttt{CERTIFICATE\_OK}\), with counts \(28,829,22599,46,2107,68,4485,94,8467\), respectively.

These finitely many cases do not prove the formula for arbitrary \(g,k\). The full proof uses absence of interblock carries and an exhaustive classification of all ways to distribute digit mass among three strictly positive summands. The arXiv motivation and the exact domain appear in RESULT.md. No independent mathematical audit was performed.
