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

# Verification scope

The exact ordinal-type recursion in `verify_orbit.py` produces all root four-round types of step-two generalized Petersen graphs with indices from \(5\) through \(24\). It performs no probabilistic testing: every vertex extends every selected tuple. Its normalization under rotations and reflections preserves edges and pairwise equality.

The separate `verify_direct.py` constructs the edge relation directly and evaluates every ordered tuple without cyclic normalization for indices from \(5\) through \(16\). Both implementations report the same equality partition on this overlap. The executed program outputs are `verify_orbit_output.txt` and `verify_direct_output.txt`; the complete twenty-index finite table is `class_table.csv`.

The extension recurrence is an exact mathematical definition of quantifier-rank types. It is not itself a proof for unbounded indices; the invariant based on positive circular gaps and thresholds \(3\cdot2^r\) separately gives equivalence of every pair with indices at least \(24\). The finite table then establishes the earlier onset of the stable class at index \(15\).

No external independent audit or historical-priority certification has been performed. The supporting computations apply to the finite boundary and do not assert a general decision procedure for arbitrary cubic graphs or arbitrary first-order ranks.
