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

# Verification notes

Run `python3 verify.py` with Python 3.11 or later. The verifier uses `decimal` standard-library transcendental functions at 74 decimal digits; it computes unique positive roots by bisection, checks the strict harmonic-number brackets, confirms the sign reversal under small perturbations at the first interior site, and checks 248 subsequent lattice sites in representative shapes. The analytic proof, not the finite check, establishes the theorem for every shape and index and the large-shape limit.

The critical exact identities are \(h_a(3)/h_a(2)=((r+3)/2)^a\), \(h_a(1)/h_a(2)=(r+2)^{-a}\), \(h_a''/h_a=aS_1^2(a-S_2/S_1^2)\), and the negative derivative of \(S_2/S_1^2\) from strict Cauchy–Schwarz. The lattice one-change lemma is supplied and proved in RESULT.md. No unproved numerical interpolation or partial exhaustive enumeration is used to justify an infinite assertion.

The results do not cover noninteger shapes and do not establish that the source's variance inequality is attained sharply by this family.
