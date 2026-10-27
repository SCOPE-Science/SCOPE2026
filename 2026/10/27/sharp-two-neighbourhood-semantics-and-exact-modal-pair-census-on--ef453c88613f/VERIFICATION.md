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

# Reproducibility and scope of verification

Run `python3 checker.py` with an ordinary Python 3 interpreter. The program prints intermediate counts and terminates with `ALL_CHECKS_OK` if every assertion succeeds. It uses only the Python standard library and a fixed seed for randomized depth-three modal-formula diagnostics.

The raw-model enumerator tests **all** neighbourhood assignments on the one- and two-world chains, filtering for continuality; it does not presume any special neighbourhood normal form. The canonical-type enumerator tests all local threshold realizations for sizes one through four. The formula experiment compares deeply nested formulas against a pointwise two-neighbourhood compression on sampled raw frames for three and four worlds, under hereditary valuations of two propositional atoms. A separate finite witness test verifies that the top-world pair of thresholds cannot arise from a single subset.

These are finite diagnostics. The proof of the infinite all-chain census, all-formula equivalence, and sharpness rests on the definitions, suffix-minimum identity, full profile realization and combinatorial enumeration written in `RESULT.md`. Experiments cannot establish novelty or independent certification; those have not been independently audited.
