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

# Exact calculation and proof boundary

Use Python 3.9+ and execute `python3 verify.py`. The self-contained program builds \(\mathbb F_4\) and \(\operatorname{PG}(2,4)\) from first principles. It checks 21 distinct normalized points, 21 five-point lines, unique joining lines for all point pairs and five lines through every point. It solves the independent integer occupancy relaxation using exhaustive nonnegative \((n_3,n_4,n_5)\) choices and reconstructs the remaining occupancies from the three moment identities. The proof excludes the unattainable relaxation extrema at sizes 10 and 11.

The main calculation visits exactly \(2^{21}-1\) nonempty labelled point subsets. For every subset it uses a recurrence proved in `RESULT.md`, rather than probing a sample. All fifteen minimum triple-count values and counts of attaining subsets are asserted against explicit expected integer tables. The checker also recomputes each selected representative's collinear-triple count by directly summing the 21 line occupancies and independently enumerates all kernel codewords for four sizes, confirming the full weight-three multiplicity.

The checker terminates with `VERIFY_OK` only if every assertion succeeds; run output alone is not the proof of the recurrence. It does not assess any field beyond order four, does not certify global LRC optimality, and has not undergone an independent audit.
