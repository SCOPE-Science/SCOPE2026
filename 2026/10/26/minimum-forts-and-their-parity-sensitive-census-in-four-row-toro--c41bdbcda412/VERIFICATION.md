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

# Exact reproducibility checks

Execute `python3 verify.py` in the directory containing this file and the mathematical result. Its 255-state graph is derived from local adjacency, with 2671 legal directed transitions. The program verifies reduced nonnegative costs, the sizes and bipartiteness of all recurrent tight components, their exact characteristic polynomials, and 255 successive residuals for the odd-case recurrence.

The Cayley--Hamilton argument in `RESULT.md` is essential: a run of 255 checked residuals would not itself prove an infinite statement without this recurrence for the underlying 255-dimensional matrix. A separate direct combinatorial enumeration checks all forts on \(C_4\square C_n\) for \(3\le n\le7\). The verification reports `VERIFY_OK` and counts \(18,28,50,28,154\) respectively. This is self-review, not an independent audit. No external theorem-prover, external certification channel, or independent replication is asserted.
