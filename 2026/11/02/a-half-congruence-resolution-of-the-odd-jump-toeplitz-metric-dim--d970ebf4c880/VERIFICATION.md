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

Run `python3 verify_toeplitz.py` from the extracted artifact directory. Its code constructs each Toeplitz graph afresh, performs breadth-first search from every source vertex, compares every computed distance with the theorem's explicit formula, and checks that the given three vertices separate all graph vertices. The listed thirteen sample graphs involve \(21{,}945\) ordered source--target pairs. It additionally checks the five-row residue-difference table for every integer \(k\) between \(3\) and \(300\).

At preparation time the program completed without assertion failure and printed its per-graph `PASS` lines plus the final totals. The mathematical induction-free argument for arbitrary \(k,n\) is contained in RESULT.md, including boundary cases; the finite computations cannot by themselves establish an infinite assertion. No independent audit is claimed.
