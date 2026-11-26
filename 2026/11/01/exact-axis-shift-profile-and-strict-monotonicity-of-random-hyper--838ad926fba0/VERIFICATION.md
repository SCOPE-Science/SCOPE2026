---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For Haar normals, orthogonality to any translated cube vertex is a null event. Away from these incidences every section vertex is a transverse intersection with exactly one edge, and conversely. At t=1, unless U is parallel to e_1 there is a tangent vector to H_t with negative first coordinate, so the section reaches the cube interior and retains dimension n-1. The endpoint sign-disagreement probability is the planar angular separation divided by pi. Edges parallel to e_1 have perpendicular radius sqrt(n-1), giving the two arctangents; the other directions split equally by the fixed first-coordinate sign, giving the radii sqrt(n-2+(1±t)^2) and the stated counts. At the center arctan(1/sqrt(n-1))=arcsin(1/sqrt(n)). Independent polynomial expansion reproduced B_c(t) and the two shifted coefficient lists of P. For c>=2, replacing t^4 and t^6 by t^2 in the negative terms gives the positive lower bound, while the axial derivative is strictly negative. At n=3 the stated phi'' certificate is valid on each z interval (on [1,2] the negative cubic and quadratic terms are dominated by the linear term after shifting; on [2,infinity) all shifted coefficients are positive). The contribution bounded by 4t/9 is strictly dominated by the axial decrease at least sqrt(2)t/3. The resulting derivative yields strict decrease on the closed interval by continuity. At zero the axial second derivative -4sqrt(n-1)/n^2 cancels the opposite term from the other directions, leaving the stated -2(n-2)/(n sqrt(n-1)) before the common prefactor. Evenness yields the fourth-order remainder. Uniform large-n expansion is legitimate for v in [0,2]; the second difference in v of the quadratic term is t^2 n^(-3/2), amplified by n-1, with total O(n^(-3/2)) error before normalization. The n=2 interior assertion follows from the line-segment section. The bundled checks were inspected, not run; sampled or Monte Carlo evidence is not used for strictness or uniformity.

## originality

PASS

The off-center face-count mechanism and the central cube expectation are prior. The explicit axial mean is a relatively direct evaluation of the earlier general edge sum; novelty is not assigned to that mechanism or to the central value. The checked strongest matches do not give, or mechanically yield as a specialized statement, strict axial decrease in every dimension n>=3 with the exceptional dimension covered, together with the exact local and uniform high-dimensional deficit. Same-day catalogue analogues were compared by object and observable, not ordered by date. The conclusion is provisional and applies to the cube's axial displacement profile and its nontrivial shape analysis as a package.

## value

PASS

Moving toward a facet center is a canonical noncentral deformation and tests whether centrality, rather than body shape or random offset, controls expected combinatorial complexity. The universal strict ordering needs a genuine comparison of edge families, particularly in dimension three. The normalized uniform deficit gives quantitative information across the whole displacement range; the local coefficient fixes the loss near the optimizer. This is more than re-evaluating the known central mean or applying the generic face-count identity at one displacement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
