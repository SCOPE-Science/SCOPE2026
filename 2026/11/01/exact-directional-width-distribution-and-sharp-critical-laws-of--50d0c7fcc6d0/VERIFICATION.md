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

The mathematical proof is in `RESULT.md`. The standalone `verify.py` constructs coordinates independent of the spherical Voronoi derivation, checks the twelve regular vertices and adjacent dot products, and tests eight CDF thresholds against more than one million fixed low-discrepancy random directions. It also integrates the stated CDF to recover the known unit-edge mean and second moment, and compares the critical exponent's coefficient at three offsets.

Run: `python verify.py`. Dependencies: Python 3, NumPy and SciPy. Tests check only finitely many cases; they do not certify an infinite statement or historical originality. The closed-form proof supplies the mathematical validity. No independent audit has been performed.
