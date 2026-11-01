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

# Verification record

The scientific derivation is contained in `RESULT.md`; the self-contained reproducibility file is `verify.py`. The reciprocal transforms for pure quadratic and cubic pulses, the quadratic bound for four alternating windows, and the strict-concavity root count are proved symbolically without relying on finite sampling.

Run `python3 verify.py` in a Python 3 installation with only the standard library. The actual run completed with `PASS; assertions: 553`, listed the two original-coordinate initial values `2` and `6/7`, and returned the respective Floquet multipliers `9/7` and `143/161`. The checker uses exact `fractions.Fraction` arithmetic for its cycle and multiplier certificates and additional floating-point spot checks for generic parameters. The numerical spot checks are not an exhaustive root count and do not certify the universal statement.

The exact fold and threshold formulas were separately cross-checked by symbolic manipulation of the discriminant and the first two derivatives of the return-defect function. These algebraic calculations are described explicitly in the proof rather than delegated to an opaque numerical solver.

The originality assessment compared the proposed statements and hypotheses with the 2026 half-period convexity theorem, the 2025 ET-system criterion, and earlier sign-definite coefficient criteria. It is a best-knowledge literature assessment, not an assertion of proven historical priority. An independent scientific audit has not been performed.
