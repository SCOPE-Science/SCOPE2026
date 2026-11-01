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

# Reproducibility checks

Run the standard-library-only commands `python3 k33_research.py` and `python3 cubical_crosscheck.py` in the same directory. Recorded stdout is included in `reduced_check.txt` and `cubical_check.txt`.

The reduced weight-three model has ranks 164, 372 and 160 over both \(\mathbb F_{101}\) and \(\mathbb F_{103}\); its 540 degree-two and 160 degree-three boundary compositions are tested over the integers. Exact character formulas are tested on every element of the 72-element wreath product. The midpoint-subdivided cubical model separately computes 454, 946 and 432 as modulo-101 ranks, checks all composable boundary squares and compares alternating characters on every group element. Both programs terminate with confirmation messages.

**Logical scope:** A modular rank is a lower bound on rational rank, not an equality by itself. The separate geometric argument using four disjoint-complement rectangles supplies the necessary rational upper bound, and the augmented degree-zero and dimension-three bounds finish the other degrees. No Smith-normal-form claim or integral homology classification is made. All checks reported here are reproducible computations and proof inspection; no external independent mathematical audit has been performed.
