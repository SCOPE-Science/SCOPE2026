---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed all-degree proof: on each 2d-point circle the discrete Fourier transform of the real intensity difference annihilates harmonics |k|<d and leaves only collision ±d. Its coefficient is R^d(a_d conjugate(a_0)−b_d conjugate(b_0)); the two independent real projections force this common complex number to zero exactly when sin(d(psi−phi))≠0. Thus continuous moduli coincide on both distinct circles; the nonzero rational quotient f/g is invariant under positive nonunit dilation of its conjugate reflection and must be constant by its Laurent series, with modulus one. Zero-polynomial and vanishing endpoint coefficient cases are included. If r=s, f=z and g=r witness ambiguity; if the sine vanishes, 1±i exp(−id phi)z^d witness ambiguity. The normalized top-bin real 2x2 matrix has singular values sqrt(1±|cos(d(psi−phi))|), giving the exact optimal staggering. Independently reconstructed Git tree from seven actual blob identities; separate checker corroborated 3081 finite Fourier, ambiguity and singular-value comparisons over d=1..13. Finite comparisons do not establish the universal quantifier.

## originality

PASS

Best-of-knowledge priority assessment after independent Resultary and broader literature searches plus reading the closest primary constructions. The exact all-degree, equal-allocation 2d+2d regular polygon criterion with sharp sine and radius obstructions was not established by the inspected broader continuous-circle or alternative 4d-point constructions. The Fourier and rational-function ingredients themselves are standard/partly published; only their exact parameterwise balanced geometry classification and sharp demixing are assessed as original. This is not certification of historical priority.

## value

PASS

Structured finite evaluation of a degree-at-most-d polynomial from modulus-only measurements is a naturally motivated phase-retrieval problem; fixing exactly equal 2d/2d regular polygons gives an entire, simple geometric family with nontrivial sharp success and failure geometry. The theorem provides a complete all-degree if-and-only-if, explicit ambiguity witnesses, reconstructs both intensity Fourier polynomials from samples, and characterizes optimally conditioned angular top-harmonic demixing, beyond a fixed small-degree experiment or arbitrary slice. It does not purport to establish general nonlinear noise stability or globally optimal sample cardinality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
