---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For unnormalized convolution on the additive group, the orthogonal characters diagonalize the operator, hence singular values are the absolute Fourier eigenvalues. Completing the square gives each chirp a factor chi_p(det A_j) G_p^d; the stipulated coefficient cancels its sign. The inverse pencil then yields the common unit phase times G_p^d(1+z+z^2) with z=exp(2 pi i t/p). Additive-character orthogonality and the p^{d-r} radical factor give both displayed level counts; for odd rank the sign comes from chi_p(-a)G_p times G_p^{2m+1}, with a=-4t. For r>=2 both binary types represent every residue, so every t occurs; the minimum absolute real sample brackets p/3 and the maximum is 3 at t=0. The closest grid-point distance is 1/3 and the angular derivative at the zero has magnitude sqrt(3), giving the stated asymptotic. At p=3 the rank is the zero-cone cardinality: it is minimized only at r=2 with sign -1. The exhibited binary block has determinant 1 and its three pencil determinants are 1,2,2, proving attainability in every dimension after adjoining the radical. The phrase 'only two singular values' means two possible levels: the explicit multiplicity of zero is zero when V=0. Verification code was inspected, not executed; the exact cyclotomic regressions corroborate finite cases only, and the algebra proves the all-parameter claims.

## originality

PASS

Supported distinct contribution: the full convolution census and sharp ternary rank criterion for this inverse pencil. Individual chirp transforms and quadratic level-count formulas are established ingredients; the inspected nearby results do not give or dominate the claimed joint spectrum and its arithmetic boundary.

## value

PASS

For a structured determinant-normalized sum of chirps, the census reduces all singular values and multiplicities to the rank and discriminant of one matrix, without constructing the convolution matrix. It answers practical mathematical questions about exact invertibility and conditioning and identifies a sharp low-characteristic boundary, not just another derivation of a single chirp transform. The ternary extremizer meets the nontrivial simultaneous-invertibility restrictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
