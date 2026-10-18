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

# Reproduction and verification

Execute `python3 checker.py` with a standard Python 3 interpreter. No third-party packages, network calls, or external data are required.

The script builds the stated Černý letter transitions directly, enumerates all proper nonempty subsets on \(3\le n\le11\), and searches reverse-preimage transitions by breadth-first search, comparing actual shortest lengths against the first cyclic \(01\) boundary. It checks the full and fixed-cardinality histograms and the first moment. For \(3\le n\le9\), it independently enumerates every word at the claimed minimum length and requires the **sole** successful one to be the predicted word. The supplied `check_output.txt` is the literal output obtained from execution.

Computational coverage ends at the finite sizes above. The general result for every \(n\ge3\) follows from the telescoping identity, the bounded short-suffix pair dynamics, and exact combinatorial counting in `RESULT.md`; finite tests do not certify all parameter sizes. No independent scientific audit or external certification has been performed.
