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

# Reproduction and limits

Run \(\texttt{python3 verify.py}\) with Python 3's standard library. The program independently reconstructs the two-regime formula, checks 245 exact-rational constructed active-cap examples (budget, positivity, quadratic relation, all eigenvector fluxes and threshold), 585 bounded positive random inputs using a Jacobi diagonalizer independent of the algebraic proof, 3,852 sampled feasible alternative designs, and the exact four-state radical instance. The random generator is deterministic.

No finite test is claimed to prove a universal spectral theorem. The all-size correctness argument is the centered-path / eigenflux / Sturm / global Rayleigh-certificate proof in RESULT.md. Tests do not certify originality or independent validation. All source-access limitations are stated in RESULT.md and REVIEW.md.
