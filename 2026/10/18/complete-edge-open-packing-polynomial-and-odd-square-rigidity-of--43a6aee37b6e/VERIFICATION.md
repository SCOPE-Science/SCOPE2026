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

# Reproducibility and verification

Extract `verify.py` and `verification_output.txt` into one directory and execute `python3 verify.py`. The script uses only the Python 3 standard library. It reconstructs the rook graphs on labeled boards and, independently of the proposed classification, tests each edge pair for the existence of a third edge connecting their endpoints. It counts all compatible edge subsets (including the empty set) by exact backtracking through an explicit compatibility graph.

The direct method checks the complete coefficient vectors of \(13\) boards, namely \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5)\), comprising \(46{,}476\) feasible subsets. For \(190\) pairs \(2\le m\le n\le20\), separately implemented formulas compute every polynomial coefficient and compare the top coefficient and exponent with the closed extremal expressions. The expected last line of the saved output is `VERIFICATION_OK`. The program was executed successfully from these exact package components.

Finite computations do not verify the theorem for infinitely many boards. The general result follows from the row/column-disjoint tile bijection and the proof of its exact parameter constraints. A literature search, even one including several full texts, cannot establish absolute novelty or independent certification.
