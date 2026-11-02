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

# Verification of the equality theorem

The proof is analytic and covers all entire pairs and every nonzero nonnegative measurable radial density with all finite moments. The key boundary condition is strict non-atomicity of the radial measure, making the scaled backward shift's adjoint strictly contractive on the positive-degree tail. The quotient construction is algebraic and does not require polynomial multiplication to be bounded on the Hilbert completion. The Schur defect identity is an exact operator equality, and the maximum-modulus step excludes nonconstant Schur tails for all such weights.

The standalone `CHECK.py` uses exact rational arithmetic to test moment log-convexity, the shift's unique norm-attainment property, and the claimed linear equality pair on two explicit nonmonotone weights: a gamma density with shape 50, and a bounded annular density. It illustrates but does not prove the universal theorem. Run using `python3 CHECK.py` with the Python standard library.

The primary complete proof is in `RESULT.md`. Neither finite checks nor failed database searches establish infinite correctness or independent originality certification. No independent mathematical validation has been performed.

Standalone checker observed output: 'nonmonotone gamma : 43 exact assertions passed annular ring : 43 exact assertions passed total: 86 exact assertions passed'.
