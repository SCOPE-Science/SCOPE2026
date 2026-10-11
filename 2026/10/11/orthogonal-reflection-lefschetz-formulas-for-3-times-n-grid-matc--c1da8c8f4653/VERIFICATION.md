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
# Verification and scope

Run `python verify_grid_reflection.py` using Python 3 and SymPy. The exact matrix calculation simplifies both resolvent entries to the stated rational generating functions in the field of rational functions. A separate exhaustive matching enumerator treats every width 2 through 7, both graph reflections, and every invariant matching; it explicitly counts edge orbits to incorporate oriented-simplex signs. The program prints `VERIFY_OK` after all tests.

The conceptual fixed-orbit decomposition and transfer-matrix proof apply for all widths; finite tests do not prove the infinite-family formulas. The homological information is an alternating rational character only and does not determine integral torsion or graded representation decomposition. The first public source date is documented by the September 23, 2026 arXiv posting. The 2026 paper's complete text was not available for direct comparison. No independent audit has been performed.
