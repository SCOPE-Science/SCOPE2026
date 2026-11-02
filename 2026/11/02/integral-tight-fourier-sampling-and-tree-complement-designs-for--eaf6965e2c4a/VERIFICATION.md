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

# Mathematical verification

Run `python check_regular_tournaments.py` with a Python environment containing SymPy. The script independently enumerates all balanced edge orientations for orders \(3\) and \(5\). It checks the exact complete moment matrix \(C=\frac{n}{n-2}I-\frac1{n-2}B^{\mathsf T}B\), integer dimension over the rationals, and existence of every prescribed directed triangle. At order \(5\), it tests all \(125\) tree-complement choices and every same-size non-tree choice under both uniform weights and an explicitly chosen positive nonuniform weighting.

All computations are finite corroboration, not a substitute for the triangle-flip lattice proof, the fundamental-cycle unimodularity, or the all-parameter symmetry argument. There is no independent external mathematical audit or certification.
