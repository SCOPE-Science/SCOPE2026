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

The quantity is a relative squared residual in the stated product probability measure, not its square root or a residual on direction-dependent intervals. The section pulls back via Q^(1/2) to a ball section of squared radius 1−t²/(uᵀQu); the area multiplier is det(Q^(1/2))/||Q^(1/2)u|| by the plane cofactor formula, and continuity gives the possible tangent endpoints. The normalized kernel is f(u)−s²g(u) with f=q^(−1/2), g=q^(−3/2). In the orthonormal offset basis 1, (s²−1/3)/√(4/45), its two columns are f−g/3 and −√(4/45)g. Their Gram matrix has trace S=||F||²>0 and determinant (4/45)D. The best rank-one fit captures the top eigenvalue by maximizing over the offset factor of unit norm; arbitrary offset factors outside the two-dimensional span cannot improve it. Hence the smaller root divided by S is the claimed error, and Cauchy–Schwarz makes D zero only for q constant; continuity and polarization give Q scalar. For the local expansion use D=m_1² Var_w(q^(−1)), where w is probability density q^(−1)/m_1 relative to spherical measure. Uniformly q=1+ε(uᵀBu−c)+O(ε²), with c the least eigenvalue of B for ε>0 and greatest for ε<0. Since the variance removes the constant c and w converges uniformly to 1, D=ε² Var(uᵀBu)+o(ε²). The fourth moments yield variance (2/15)||B−tr(B)I/3||_F²; S→8/15 and the smaller-root expansion has coefficient (4/45)/(8/15)²=5/16 multiplying D, giving 1/24. For both axial families q(z)=A+Bz² and z is uniform on [0,1] after folding. Integration of (z q^(1−j))' gives (3−2j)m_{j−1}+2(j−1)A m_j=q(1)^(1−j), establishing both recurrences for j=2,3; direct integration gives the arctan and arcosh first moments. The prolate rescaling y=Lz is dominated, for L≥√2, by (1+y²/2)^(−j); the limits of Lm_j are π/2, π/4, 3π/16. Thus LS→89π/240 and L²D→π²/32. For the oblate family the recurrences give L²m_1∼log(2L), L²m_2→1/2 and L²m_3→1/4; the leading term of D is log(2L)/(4L⁴). This yields both the positive prolate limit and the oblate 1/(45 log L) asymptotic. The latter invalidates any bound on eccentricity based on uniformly small defect in this sampling model.

## originality

PASS

The supported distinct content is the geometric defect in the fixed common-offset probability model, its sharp local traceless coefficient, and its contrasting limits at equal large axis ratio. The polynomial section kernel, finite separability, and the best-rank-one singular-value principle are not new. The closest exact rank classification and the primary qualitative rigidity results determine finite separability but not the normalized tail value or its two regime limits. The bounded best-of-knowledge comparison does not certify priority.

## value

PASS

Finite separability prompts a natural quantitative question: how informative is one separated fit for a nonspherical ellipsoid? The answer distinguishes exact rigidity, local sensitivity, and a sharp obstruction to reading eccentricity from fit quality. The same axis ratio can produce a defect bounded away from zero or an error asymptotically vanishing at a quantified logarithmic rate. This is a meaningful contrast for interpreting a separability statistic and is not a reformulation of rank two or of the customary ellipsoid-section formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
