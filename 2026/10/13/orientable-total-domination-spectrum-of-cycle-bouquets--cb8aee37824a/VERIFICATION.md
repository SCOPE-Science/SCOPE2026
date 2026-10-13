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

Execute `python verify_orientable_total_cycle_bouquets.py` from a directory containing that bundled file. No external packages, environment services, or downloaded papers are required. The script checks validity by indegree, calculates the minimum total dominating set via direct enumeration of all vertex subsets, and builds the spectrum over all edge orientations for the eight printed cycle-length tuples. In particular it checks all \(4096\) edge orientations of the ten-vertex bouquet with petal lengths \((3,4,5)\), whose valid-orientation distribution is \(52z^6+36z^7+8z^8\). Every test must match the formula coefficient by coefficient, and the script terminates with `VERIFY_OK` on success.

The test is exhaustive only for the listed finite instances. For arbitrary \(t\) and \(\ell_i\) the proof in `RESULT.md`, not a finite sweep, establishes the infinite statement. Literature identification and comparison do not constitute independent validation or a global novelty proof.
