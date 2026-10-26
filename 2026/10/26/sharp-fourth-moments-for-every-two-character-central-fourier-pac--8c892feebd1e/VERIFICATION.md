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
# Reproducibility

Run `python3 verify.py` from the directory containing the other files. The script uses only the Python standard library. It directly multiplies the two character packets using the Clebsch–Gordan fusion rule, compares the squared character-product coefficients with the asserted quartic identity, verifies the derivative factorization symbolically, and checks deterministic one-dimensional sweeps against the proposed optimizer for every tested index pair. The completed output is in `verification_output.txt`.

The exact assertions include all tested complex-coefficient phases and many opposite- and same-parity character pairs. They are finite tests, not a substitute for the paper's complete proof. The proof's unbounded-index steps are the explicit overlap-count lemma, sign uniqueness by Descartes' rule, and the quadratic endpoint comparison. No independent audit has been performed.
