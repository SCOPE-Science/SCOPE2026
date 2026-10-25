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

## Computational reproducibility

Run `python check.py` from the directory containing this file. The checker uses only Python standard-library modules. For dimensions \(1\le d\le9\) and every two-marker separation \(1\le t\le d\), it constructs the entire binary cube and refines all its vertex colours synchronously. At every round it compares the partition with independently computed capped Hamming-distance pairs, and at stabilization checks the prescribed round and the orbit-class multiplicities. A second calculation constructs a weighted orbit quotient from all available single-coordinate flips and checks every \(1\le d\le40\) and \(1\le t\le d\). The run in `check_output.txt` reports 45 full-cube and 820 weighted-quotient configurations, with `ALL_PASS`.

The weighted quotient uses the known coordinate-count symmetry of the cube and is therefore not a completely independent proof of the orbit statement. The complete full-cube implementation does not use that quotient. Neither finite test proves the theorem in arbitrary dimension. The proof in `RESULT.md` treats all dimensions directly.

## Scope and review status

All mathematical assertions have been subjected to the accompanying self-review correctness, originality, and value review. An independent mathematical audit has not been performed. No separate external formal certification is asserted.
