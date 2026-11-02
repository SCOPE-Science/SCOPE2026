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

# Reproducible checks

Run `python3 verify.py` under Python 3. The standalone script has no nonstandard dependencies and uses rational arithmetic for its core checks. It verifies 573 exact-rational instances of the leave-one-out nullspace formula, equality of endpoint indicators, compact geometric ratio and step-response formula, and one-extra-site opposite preference witnesses. Tests cover a range of polynomial degrees and positive integer geometric exponents, with exact fractional regularizers and nonlinear weight exponents. Because those loops are finite, they do not replace the proof of the universal statements. The latter relies on the full-spark rank and explicit Lagrange product arguments in RESULT.md. No external or independent validation is asserted.
