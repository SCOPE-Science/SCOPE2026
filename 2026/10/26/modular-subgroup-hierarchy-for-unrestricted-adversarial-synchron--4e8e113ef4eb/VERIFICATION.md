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

Run `python3 verify.py` with Python 3.10 or later, from this directory. The script checks two independent decision mechanisms, a modular difference-subgroup iteration and a full powerset-game attractor with every possible Bob word represented by a reachability closure. It enumerates all \(n^n\) transition tables for each \(2\le n\le6\), compares the two winner predicates on every table, checks winning totals \(2,3,8,5,36\), and verifies a three-stage case at \(n=8\). The actual replay completed successfully with `VERIFY_OK`.

The code provides exact finite cross-checks of the explicit formulas and game interpretation. The arbitrary-order theorem and the semiprime enumeration rely on the mathematical proof in `RESULT.md`; finite checks alone would not establish them. No outside certification, independent audit, or larger-state exhaustive claim is made.
