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
# Reproducibility and limits

The standalone program `spider_character_verify.py` uses Python's standard library, and can be run as `python3 spider_character_verify.py`. Its prescribed output ends with `VERIFY_OK` only if all sample character and dimension comparisons pass.

The checker constructs the quotient monomial basis and monomial ideal generators directly from each exponent tuple; it forms every pair-lcm syzygy, performs sparse modular row reduction separately in each coordinate-torus weight, and obtains the complete embedded tangent character. It computes the coordinate-derivation map independently to obtain the intrinsic \(\mathbb T^1\) character. The cases include \((2,3,4,5)\), for which \((d,\dim T,\dim\mathbb T^1)=(11,64,42)\), and \((2,3,2,4,2)\), for which the tuple is \((9,90,73)\). Three-leg inputs serve only as previously known calibrations.

These are exact finite-field computations for finitely many exponent tuples. They are **not** universal proofs. The all-parameter characteristic-zero theorem instead follows from the complete lcm-syzygy characterization and cotangent-complex exact sequence in RESULT.md. Higher obstruction groups and smoothing or formal deformation spaces have not been computed. Independent validation and definitive bibliographic priority have not been established.
