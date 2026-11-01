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

# Reproducibility and verification

Extract `verify_rose.py` and `verification_output.txt` from this package without changing bytes. Run `python3 verify_rose.py` with Python 3 and compare its standard output to `verification_output.txt`.

The verifier constructs vertices, radial/peripheral edges, the complete unordered cubical zero-, one- and two-cell sets, and edge-coordinate orientations independently of the symbolic character formula. For \(m=1,2,3,4,5\), it checks each prescribed free-face collapse against the then-active two-cells, verifies the residual one-skeleton is connected, and compares its rank with \(1+3\binom m2\). For each of all \(4282\) signed petal permutations across those five values, it computes three signed cellular traces directly from the mapped cells, compares the Lefschetz-derived first-homology trace to the claimed polynomial, and checks full-group and permutation-only invariant averages.

Recorded completion marker: `VERIFY_OK`. The continuous, unrestricted claims follow from the complete combinatorial cell-classification and counting proof in `RESULT.md`, not finite extrapolation. The code does not independently audit source novelty or provide an integral irreducible representation decomposition.
