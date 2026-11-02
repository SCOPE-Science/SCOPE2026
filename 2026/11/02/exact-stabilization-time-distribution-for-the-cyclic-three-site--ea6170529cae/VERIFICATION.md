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

# Verification notes

Run `python3 verify.py` with an ordinary Python 3 interpreter. The expected terminal result is `VERIFY_OK`, and every discrepancy triggers an assertion.

The verifier contains three distinct cross-checks. First, it builds explicit weighted finite transfer matrices and confirms their traces against the integer recurrence extracted from the polynomial \(Q_L(u,z)\) for \(1\le L\le8\), weights \(u\in\{-1,1\}\), and ring lengths through 14. Second, it exhaustively enumerates all \(2^n\) binary initial words for each \(1\le n\le16\) and directly iterates synchronous majority to the first fixed point, or verifies the alternating two-cycle. Third, it checks for each such ring length and every feasible \(t\) that the derived generating-function coefficient equals the number found by brute enumeration, checks both exceptional states, and verifies attainment of the maximum finite time.

The all-ring, all-time proof is the domain-wall recurrence, finite run erosion, cyclic parity projection, and formal transfer-matrix determinant identity given in `RESULT.md`. The finite executable checks are consistency evidence and do not constitute an independent infinite proof or an external audit. No external dataset or third-party code is needed.
