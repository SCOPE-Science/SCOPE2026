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

Independent mathematical audit has not been performed. Reproduce the supplied computational checks by running `python3 CHECKER.py` with `mpmath`; the captured stdout is `CHECKER_OUTPUT.txt`.

The checker separately reconstructs the ambiguity function from exact signed intervals and compares it against the closed-form sine expression at seven frequency-delay samples (absolute error below \(10^{-55}\)). Three independent nondegenerate real Doppler fold solutions of \(F=F_T=0\) were resolved at 70-digit working precision, and each has both \(F_r\ne0\) and \(F_{TT}\ne0\). Five exact cubic-jet formulas at the resonant delay were checked with high precision.

These finite calculations do **not** prove the countably infinite dense fold set. The density proof uses torus recurrence plus a two-variable inverse-function theorem, given completely in `RESULT.md`. The multiplicity exclusions follow from algebraic sine/cosine identities. No unrun code, external proof certificates or independent reviews are claimed.
