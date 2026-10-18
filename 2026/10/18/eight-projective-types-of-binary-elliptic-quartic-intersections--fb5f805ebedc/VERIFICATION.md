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

# Computational reproducibility

The included `verify.py` uses Python 3 with SymPy, reconstructs all 174251 two-dimensional subspaces of homogeneous quadrics over F2, traverses PGL4 orbits by coordinate generators, and checks the Jacobian ideals by Gröbner basis on all four projective charts. It verifies eight smooth orbits totaling 40320 pencils and their geometric/arithmetic invariants. A positive Gröbner unit ideal on every chart is a geometric nonsingularity certificate; checks at only rational points would not suffice.

The independent `verify_orbits.py` uses only the Python standard library. It enumerates all 20160 invertible binary four-by-four matrices, independently verifies representative orbit cardinalities, rational points and coplanarity, and records the explicit rational hyperplane local intersection certificate. The short expected stdout transcripts are `verify_output.txt` and `verify_orbits_output.txt` respectively. Run `python verify.py` and `python verify_orbits.py` from a directory containing the source files and compare their complete stdout with these files.

The asserted rational fourth-order osculation for representatives is checked with exact local truncated-power-series arithmetic in `verify.py`; the `(20,609)` representative has a length-four local ideal supported at one rational point. This establishes the claimed existence and exclusion over the exact degree-four intersection. Numerical finite-extension sampling is not relied upon. This verification does not address other base fields, singular intersections, or the possibility of prior literature coverage.
