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

The identities underlying the result are derived symbolically using direct expansion of four-root intensity samples. Reproduce with `python symbolic_four_sample.py`; the program uses SymPy and prints a PASS message only if every coefficient identity vanishes identically.

Reproduce independent numerical checks with `python verify_four_sample.py`; this uses only the Python standard library, a fixed random seed, and deterministic coefficient examples. The script verifies the algebraically generated two-class and three-class collisions, 5,000 direct Fourier coefficient checks, and a generic inverse on 500 samples.

A further exact enumeration is available as `python finite_grid_check.py` (15,625 Gaussian-integer triples, grouped by eight integer intensities). This finite experiment supplies a regression check but is not exhaustive over all complex coefficients.

The proof in `RESULT.md` is self-contained: in particular, it reduces the nonzero-middle-coefficient inverse to at most two common positive roots of two monic quadratics and checks all cross-branch collisions. These programs are not substitutes for that exhaustive symbolic case argument. No independent audit is claimed.
