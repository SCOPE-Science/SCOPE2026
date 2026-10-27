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

The proof derives the two-step antipodal reduction, shows neither spatial coordinate can vanish on a nontrivial cycle, and exhausts equal-sign and opposite-sign cases. Equations (4)–(6) give the unique sum and product of any asymmetric pair, so the discriminant exhausts the remaining alternatives. Strict inequalities at the three thresholds are checked symbolically in the proof.

The attached `check_cycles.py` requires Python 3 standard library only. Run `python check_cycles.py` beside the attached files. It checks 120 exact two-step returns numerically across four positive-definite Hessians and three decay parameters, and tests three additional rational discriminant identities with `fractions.Fraction`. The expected output is in `check_output.txt`.

Floating-point residual tests establish neither an exhaustive census nor stability; both the complete enumeration and its parameter boundaries rely on the analytic proof. Independent mathematical and publication-priority audits have not been performed.
