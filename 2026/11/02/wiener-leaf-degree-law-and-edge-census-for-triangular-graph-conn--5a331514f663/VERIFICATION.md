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

# Reproducibility and boundaries

Run `python3 CHECK.py` using a standard Python 3 interpreter. The program builds each triangular graph from the edges of its underlying complete graph and checks domination and connectedness directly, including an explicit breadth-first search on the selected vertices of the line graph. The program does not assume the tree theorem in its eligibility test.

It exhaustively evaluates all \(33,864\) subsets for \(n\in\{3,4,5,6\}\). For every minimum solution it independently enumerates all one-for-one replacements and compares its resulting degree with the tree-distance and leaf formula; it verifies connectedness and edge count for every tested solution graph. It also checks the star/path degree difference and double-broom four-exchange discrepancy for the specified finite range. Observed counts and `ALL_CHECKS_PASSED` are printed upon successful completion.

These finite cases are checks, not an exhaustive proof of the results for all \(n\). The general proof uses a two-type exchange partition and exact Prüfer/cut enumeration; the supplied script independently checks small cases and algebraic witnesses. The cited earlier enumeration of optimal configurations is credited rather than reassessed here.
