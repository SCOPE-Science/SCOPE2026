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

# Reproduction and limits

From a directory containing the standalone program, run `python3 mobius_pack_verify.py`. It uses only the Python 3 standard library. It reconstructs \(2m\) vertices and their adjacency for each integer \(5\le m\le24\), forms the closed radius-two conflict neighborhood of every vertex, and computes the exact independence polynomial by a memoized deletion-versus-selection recurrence. This code independently computes both the sizes and counts and compares each coefficient with the theorem's binomial formula.

Observed terminal line:

`VERIFY_OK m=5..24 all polynomial coefficients, exact maxima, labelled optimum counts`

Selected checks include \(m=5\): optimum size \(2\), count \(10\); \(m=6\): size \(3\), count \(4\); \(m=8\): size \(3\), count \(48\); \(m=12\): size \(5\), count \(120\); \(m=16\): size \(7\), count \(224\); and \(m=24\): size \(11\), count \(528\). Every coefficient for these and the other tested cases matched.

The exhaustive state recursion is finite-instance evidence for \(m\le24\). The general theorem relies on the complete mathematical proof using cyclic gaps and twisted lift constraints. No proof assistant, external certification, independent audit, or exhaustive historical priority proof is claimed.
