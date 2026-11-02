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

# Verification

The complete analytical proof of both all-parameter sharp ratios is in `RESULT.md`. The local `verify.py` has no third-party package dependencies and can be run as `python3 verify.py`.

The verifier performs direct determinant expansions with rational coefficients over an array of small weight triples, checks the radial moment formulas and endpoint constants, and subjects random admissible fibers to the exact interval and universal ratio bounds. During preparation this program returned `PASS: 96164 finite assertions; analytic proof required for all-parameter theorem.` The program is supplementary: neither random testing nor a finite grid establishes the infinite family of inequalities. The published moment identity is used as a cited theorem, while the reductions and optimizations are proved within this package.

Independent scientific review has not been performed; no external verification channel is asserted.
