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

# Verification of the reversible-wave period census

The proof in `RESULT.md` is valid for all \(d\ge3\) and \(q=2^f\), \(f\ge1\); neither included finite test is an infinite proof. The independent algebraic implementation `check_ranks.py` constructs exact \(0/1\) matrices, multiplies powers over \(\mathbb F_2\), row-reduces \(T^t-I\), and matches the predicted nullity for every \(t=1,\ldots,24\) and \(d=2,\ldots,6\): 120 successful comparisons. Since matrix entries and elementary row pivots belong to the base field, these nullities also apply over any finite extension of \(\mathbb F_2\). The dimension \(d=2\) is a boundary regression check outside the principal scope.

The independent `check_states.py` updates individual configurations by bitwise neighbor-parity, without using matrix ranks or algebraic normal forms. It checks all \(1,024\) states at \(d=2\) and all \(262,144\) states at \(d=3\), finds each least period directly, and reproduces the formulas.

Run `python3 check_ranks.py` and `python3 check_states.py`. Expected output is embedded in `check_ranks.out` and `check_states.out`. The general proof establishes the ranks and arithmetic formulas; finite tests cannot exclude undiscovered failures at higher dimensions or other parameter settings, and no independent audit has been performed.
