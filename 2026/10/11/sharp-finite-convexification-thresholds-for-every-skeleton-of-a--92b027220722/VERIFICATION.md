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

The included standalone `verify.py` uses only Python standard-library `fractions.Fraction` and `random.Random` and executes with `python verify.py` from the extracted directory. It tested 4410 deterministic rational target barycentric vectors over dimensions 2–21, every proper positive skeleton order, and several summand counts at/above the derived threshold. For each case, it checked nonnegative row entries, unit row sums, at most \(r+1\) positive coordinates per row, and coordinate-wise exact reconstruction. It also checked the strict near-vertex obstruction inequalities for below-threshold cases. The observed result was `VERIFY_OK 4410 exact rational decompositions; sharpness inequalities checked`.

The finite tests do not establish all-dimensional validity, real-valued completeness, or originality. Those rely on the fully stated inductive proof and literature comparison. No independent audit has been performed.
