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

## Reproducibility
Run `python3 verify.py` from the package directory using Python 3.9+ with only standard-library modules. The verifier constructs every relation containing the diagonal for the one-, two-, three- and four-element flat semilattices (zero to three atoms), tests every product pair for meet closure, reconstructs its unique selected left/right markers and edge set, and tests symmetry and transitivity. It compares the resulting exact triples of counts with the analytic formulas.

Observed output includes `m= 3 direct= [322, 18, 8]` and ends with `VERIFY_OK`. Exact formula evaluations for four through seven atoms are also printed, but they are not direct exhaustive relation enumerations.

The general normal form, lattice structure and asymptotic formula are proved mathematically in RESULT.md. No external independent audit was performed.
