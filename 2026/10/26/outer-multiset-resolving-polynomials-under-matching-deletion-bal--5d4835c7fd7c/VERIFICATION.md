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

The theorem concerns every pair of integers \(3\le p\le q\) and every integer \(0\le t\le p\), with all deleted edges pairwise disjoint and with labeled vertices. Each same-side distance is two, each surviving cross-edge distance one, and each removed cross-edge distance three. Those facts imply that each complement-side signature is determined by the selected count on its own side and one indicator for its deleted matched neighbor. The proof exhausts all omission sizes zero through four and rules out higher sizes.

Run `python verify.py` using a standard Python 3 installation. The program builds each graph directly, computes shortest-path distances by breadth-first search, enumerates every landmark subset for the stated finite test range, and compares the full polynomial against the theorem. The expected output begins with `PASS 46`. The script deliberately does not treat finite checks as an infinite theorem.

The four coefficient formulas, phase transitions, equality cases and crown support gap follow from the explicit signature and counting argument in `RESULT.md`. No proof assistant or independent human audit is claimed. The primary full-text literature was examined for the meaning of the invariant and the relevant known extremal cases; exhaustiveness of worldwide literature is not certified.
