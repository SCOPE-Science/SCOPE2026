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

# Reproducibility and limits

The three Python 3 programs are standalone except that `cycle_full_group_verifier.py` imports `cycle_action_verifier.py` from the same directory; they use only the standard library. They reconstruct polyhedral cells as tuples of singleton or two-element color sets. The exhaustive checks are finite and must not be interpreted as a computational proof of a statement for all cycle lengths.

`cycle_check.py` enumerates ten source/target pairs and measures the integral winding of the first-coordinate evaluation along graph loops, including the exceptional isolated-point components. `cycle_action_verifier.py` independently constructs oriented cubical cell actions, computes signed cellular Lefschetz numbers, and compares the resulting integral first-homology traces to the claimed signed permutation action. `cycle_full_group_verifier.py` repeats the comparison for all \(120\), \(140\), and \(192\) source-target dihedral symmetry pairs in three cases.

Expected outputs are included in `cycle_check_output.txt`, `cycle_action_output.txt`, and `cycle_full_group_output.txt`, each ending in the literal `ALL_CHECKS_PASS`. Calculations were performed against the exact contents of these scripts. All program paths are relative; no external data, services, network access, or software packages are needed.

The mathematical proof invokes Čukić–Kozlov's independently published circle-or-point and good-cover theorem. The new degree and symmetry statements are derived explicitly in RESULT.md. No independent audit has been performed. No integral quotient homology, torsion classification, equivariant homotopy equivalence, or definitive novelty certificate is claimed.
