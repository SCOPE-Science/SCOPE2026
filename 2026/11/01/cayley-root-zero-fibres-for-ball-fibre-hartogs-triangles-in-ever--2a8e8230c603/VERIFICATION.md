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

The derivation uses Lebesgue-normalized monomial norms, explicit Laurent exponent summation, a parity splitting of \((1-y)^{-n-1}\), and the biholomorphism from the unit disk to the right half-plane. Every listed zero is checked to be feasible for two actual points of the domain, rather than merely a formal zero of the numerator.

The standalone program `check_hartogs.py` uses Python's standard library and completed 12,766 assertions. It tests admissibility of Laurent exponents, parity/count identities across dimensions 1–14, the exact algebraic zero equation, cancellation in the independent convergent Laurent series, and representative normalized boundary limits. Reproduce by running `python check_hartogs.py` in the directory containing this file.

The all-dimensional root-count and boundary-limit proofs are symbolic and do not depend on an exhaustive finite enumeration. Literature comparisons remain provisional and independent mathematical validation has not occurred. Scope: positive real \(w\overline\eta\), Euclidean ball fibres, fixed integer dimensions and exponent two only.
