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
The companion `certificate_knots.py` uses exact fractions to enclose every integral needed for the score, computes three centered-Gram-matrix principal minors, proves local strong convexity, and derives a certified positive coarse slope jump. It requires only the Python standard library. Execute `python3 certificate_knots.py` from the extracted files. The analytic step connecting these finite inequalities to the unconstrained global optimizer is written out in `RESULT.md`. The certificate has no need to enumerate infinitely many log-concave functions. Numerical decimals are illustrations only, and no independent audit has been conducted.
