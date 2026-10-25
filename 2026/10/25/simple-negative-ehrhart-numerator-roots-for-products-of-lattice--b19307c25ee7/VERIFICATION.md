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

# Reproduction and verification

Install Python 3.10 or later and SymPy 1.12 or later. Keep `verify.py` and `coefficient_certificate.json` in the same directory and execute `python3 verify.py`.

The program independently derives all numerator coefficients from the Ehrhart binomial basis, verifies their symbolic agreement with the displayed formula, regenerates every monomial expansion, verifies the entire stored certificate byte-for-byte after canonical JSON serialization, and checks strictly positive integer coefficients. Expected counts, in order: quartic discriminant 784, quartic root witnesses 36 and 36, one-empty-factor cubic discriminant 75, two-empty-factor cubic discriminant 25, degenerate quadratic discriminants 6 and 3. The verifier also checks the exact example with both factor numerators \(1+t+t^2\), and an exact rational parameter counterexample showing that unrestricted real polynomial parameters cannot simply replace lattice counts.

This is a complete finite certificate of the symbolic inequalities used in the proof, rather than an experiment on sample lattice polygons. The proof also invokes the standard discriminant sign theorem for real cubics and quartics, which the program does not independently reprove. This verification does not establish historical priority or provide independent scientific review.
