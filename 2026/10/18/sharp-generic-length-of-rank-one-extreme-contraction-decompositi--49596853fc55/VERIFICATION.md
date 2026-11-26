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

The frozen Finding's claim of positive factors in every signed stratum was false literally: e.g. the fully saturated row (1,−1) has no positive factorization. The complete corrected RESULT.md preserves each prescribed saturated index/sign and attaches the specified positive powers to enumerated unsaturated indices; positivity of the entire witness is asserted only in the all-positive stratum. Signed row and column flips permute the eligible atoms and preserve length. Independently, the norm is the entrywise maximum, so saturated cross entries force each positive-weight atom into the same face. In coordinates x_i,y_j,x_i y_j, these monomials and the constant are independent Walsh characters; thus D=(m−r)+(n−c)+(m−r)(n−c). Independent sign barycenters give membership, and affine Carathéodory gives D+1 terms. Each set of at most D sign vertices is contained in a rational affine hyperplane, by solving at most D homogeneous rational equations in D+1 coefficients. Pullback to rank-one factors gives a nonzero polynomial in distinct monomials, which has a closed, null, nowhere dense zero set relative to the box. At the witness the monomials are distinct binary-index powers of the transcendental number e⁻¹, so none of the rational equations vanish. This proves generic and explicit sharpness, including D=0 and r=c=1. The corrected proof also resolves the rational-hyperplane step for lower-dimensional spans and corrects the test-count wording. The verification note and checker were inspected, not executed. Independently in the 2×3 example, each conditional law of the two column signs given either row sign has marginals 3/5 and 4/7 for a positive sign. A distribution on at most two vertices of that sign square cannot have both marginals interior unless they are equal or complementary; hence at least three atoms per row sign are required, confirming the six-term witness.

## originality

PASS

The supported distinct claim is the matching generic lower bound on the rank-one locus, the saturation-sensitive exact maximum, and the uniform witness in the prescribed signed strata. Rank-invariant existence, cube atom counts, correlation feasibility and some upper bounds are prior. The sign repair does not narrow the all-stratum generic sharpness theorem or rely on a new priority assertion.

## value

PASS

The theorem settles how many eligible extreme contractions may actually be needed even for a rank-one target, which is not answered by qualitative existence or arbitrary convex-hull dimension. It detects a generic multiplicative rather than additive support requirement, gives its exact reduction under saturation, and supplies a witness in every signed stratum. The corrected sign scope retains all of that content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
