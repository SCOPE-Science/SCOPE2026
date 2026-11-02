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

# Verification of the hexagon stability law

Run `python3 verification.py` from a directory containing the included program. Only the Python 3 standard library is required. The program constructs the two exact nonnegative polynomial identities \(2S^2W-DN=L\) and \(2DN-S^2W=U\), compares their coefficients with the explicit proof forms, and checks that every coefficient is nonnegative. It also evaluates \(1728\) positive-integer generator triples by exact rational arithmetic, reconstructing the associated hexagons and their polars independently through convex hull and shoelace formulas to check the Mahler product numerically. The symbolic calculations and displayed analytic positivity arguments, rather than the finite sample, establish universal validity. The sharp constants are supplied by exact limiting families in the proof.

No independent audit has been performed. The verifier does not establish historical originality or validity outside the quantified class.
