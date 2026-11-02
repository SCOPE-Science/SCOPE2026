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

# Reproducibility and boundaries

With Python 3, run `python3 verify_igusa.py` in a directory containing the supplied files. It creates `s6_orbit_table.csv` and prints `VERIFY_OK`; the packaged transcript is in `verify_igusa_output.txt`.

The exact checks enumerate all fifteen matchings of six symbols, all fifteen duads, forty-five flags and all 105 unordered line pairs. Integer maximal-minor gcds exclude extra intersections for characteristic greater than three. Triple-point tangent minors verify independent tangent directions. The verifier checks the quartic identity at integer evaluation witnesses, while the **symbolic identity is separately proved** in RESULT.md. It exhaustively enumerates all eleven integer partitions of six and all 720 permutations, confirming the 144 five-cycle point-free cases and nine distinct rational zeta functions. An explicit five-cycle incidence-graph quotient has six vertices and nine edges; the integral covering-graph argument is in RESULT.md. Direct rational-point enumeration over \(\mathbb F_5\) and \(\mathbb F_7\) checks the identity twist only.

The verifier does not independently prove the infinite-field normalization and torus-identification theorems, and the finite evaluation witnesses alone are not a universal polynomial-identity proof. No independent scientific audit has been performed. Characteristic two and three and forms outside coordinate-\(S_6\) descent are excluded.
