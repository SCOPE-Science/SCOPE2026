---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact checks and limits

Run `python3 CHECK.py` using standard Python 3. The program generates the integer cyclotomic polynomial \(\Phi_N\) via monic division of \(X^N-1\), builds exact residue vectors of powers \(X^j\), and computes all Weyl ambiguity sums as integer-vector combinations. It tests every \(5\le N\le35\) and \(1\le a<N\), exactly 589 cases, against the stated arithmetic expression. Expected output: `EXACT_CHECK_OK: 589 pairs (5 <= n <= 35, 1 <= a < n)`.

This finite check is not an unrestricted proof. The proof uses the character factorization and congruence inclusion–exclusion in `RESULT.md`, together with the earlier rank/ambiguity equivalence. Selected projector-matrix numerical ranks provide an additional independent finite consistency check, not exact formal certification. No assertions are made about conditioning, nonlinear phase retrieval, formal Lean verification, or expert attestation.
