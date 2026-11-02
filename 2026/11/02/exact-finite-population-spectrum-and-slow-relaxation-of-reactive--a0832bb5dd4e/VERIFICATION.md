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

Run `python verify_spectrum.py` in an environment providing SymPy, NumPy, and SciPy. This checks the exact rational eight-by-eight characteristic polynomial of a four-oscillator polygon; independently verifies both Hurwitz determinant identities and the leading slow-root derivative; and compares the direct real Jacobian spectrum with the factored formula for closed configurations with three, four, five, six, and eight oscillators.

The proof in RESULT.md supplies the noncomputational infinite-family argument: a rank-two determinant lemma, exact eigenspaces, Routh–Hurwitz stability, the implicit-function theorem, and local stable-foliation theory. Numerical eigenvalues alone are not an all-parameter or nonlinear certificate. The system's local behavior at degenerate collinearity, global basins, and historical priority beyond the inspected sources remain unverified. Independent audit: not performed.
