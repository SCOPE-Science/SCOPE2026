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

The analytical computation derives the expressions for the logarithmic derivative and convexity factor directly from the Cayley map. The exact imaginary-residue formula is checked by multiplying a complex numerator by the conjugate of its denominator; the strict inequalities \(u>1/2\), \(v>0\), and \(0<\alpha<1\) prove the universal sign. Because the pole lies on the boundary, the proof explicitly moves to interior points by continuity.

Run `python3 verify_pole.py` using Python 3 standard-library modules. Its selected parameters and numerical interior sequences are illustrative consistency checks; no finite run certifies the infinite analytic statement.

No independent audit has been performed.
