---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: In the cube Q=[-1,1]^n, the exit distance in direction v is 2S_v, S_v=min_i U_i/|v_i|, where U_i are independent Uniform[0,1]. Its survival probability P(S>t)=∏(1-|v_i|t) on [0,1/max|v_i|] yields the precise finite elementary-symmetric formula for the radial-p gauge for every finite p>-1; the logarithmic p=0 limit is separate. At any zero coordinate, differentiating with respect to its absolute value gives a strictly positive axial derivative and opposite signed one-sided slopes. In an orthant and at an m-fold maximal tie, freezing the endpoint changes an interval of length O(δ) on which all m competing factors are O(δ); this gives a uniform O(δ^{m+1}) difference from an analytic continuation and hence a Peano m-jet. The one-coordinate right perturbation gives the nonzero negative (m+1)-order coefficient -a^{-p-m-1}∏_{j>m}(1-b_j/a)/[m(m+1) M_p], with no counterpart on the left. Matched second derivatives across finitely many analytic cells and bounded one-sided third derivatives yield local C^{2,1}, but generic m=2 ties preclude C³. Affine covariance follows from exit distances. The finite bundled arithmetic code was inspected; its samples are not treated as a proof.

## originality

PASS

PASS (best knowledge): Langharst–Manui–Zvavitch Proposition 34 already supplies cube radial-function integrals, and Langharst proves convexity for all p>-1. Neither full-text passage states the all-dimensional exact max-tie Peano order, its nonzero (m+1)-st boundary-layer coefficient, nor the sharp generic C^{2,1}/non-C³ transition. Existing moment formula itself is acknowledged prior; the novelty assessed is differentiability stratification.

## value

PASS

PASS: Radial mean body regularity at coordinate-zero seams and multiple-max ties is a natural precise geometry question. The theorem gives a complete affine-invariant stratification, identifies the exact first forbidden jet order at every multiplicity, and separates pointwise higher jets from neighborhood smoothness. It goes beyond a routine substitution into the known integral representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
