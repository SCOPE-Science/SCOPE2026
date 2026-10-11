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

# Reproducibility and scope

Execute `python3 check_radius.py` from the directory containing that standalone file. Python's `fractions.Fraction` is used for all rational computations; no third-party dependency or downloaded data is needed. Its successful execution was observed and returned `PASS: all polynomial identities, root bounds, Hurwitz test, and six Bernstein certificates`.

Exact checked steps include reconstruction of the analytic derivative rational functions; equality of both displayed polynomial factorizations; strict monotonicity and exact rational bracketing of the candidate radius; the quartic Routh–Hurwitz test; and six exact Bernstein-coefficient interval lower bounds for the divided-difference trigonometric polynomial on the critical circle. All six lower bounds are strictly positive, the smallest being greater than \(1.56\times10^{49}\). The proof in `RESULT.md` explains how these checks imply a continuous disk-wide statement using the harmonic minimum principle and why the real root is the sharp obstruction to local univalence.

Scope: the fixed Wang–Zhong ellipse coefficients, the centered open disk, and local—not global—univalence. No result is claimed for larger radii or other ellipse parameters, and an independent audit has not been performed.
