---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For rooted ancestor-order trees with subtree sizes h_v, the triangular coordinate B_v=(X_v−X_parent)/(1−X_parent) has Jacobian ∏(1−B_v)^{h_v−1}; hence B_v are independent Beta(1,h_v), and vol O(T)=∏ h_v^(−1). Setting t_v=h_v/(h_v+1) makes each transferred Y_v a centered conditional innovation and diagonally covariance-orthogonal with β_v=h_v/[(h_v+1)^2(h_v+2)]·∏_{strict anc} h_a/(h_a+2). Variance decomposes as β_v+(t_v−t_v*)²Var(X_parent), with strictly positive parent variance, yielding unique inertia minimizer. A unit-triangular determinant-one transfer leaves isotropic L invariant and yields L^(2n)=∏F(h_v), F(k)=k^(k+2)/[(k+1)^2(k+2)^k]. Direct log derivative shows F increasing, and sorted subtree-size bound h_(j)≤n−j+1 gives star sharp minimum and path sharp maximum. Independent rational integrations of 33 rooted-tree order polytopes up to n=5 reproduced means, covariance and orthogonal innovations. Exact finite checks are corroboration only.

## originality

PASS

QUALIFIED PASS. Stanley's standard order polytope, hook volume and Fang–Fourier–Litza–Pegel's continuous marked-poset transfer family are prior results. The full freely accessible Fang et al text, especially Section 2 transfer map, studies Ehrhart, vertices and combinatorial type, not independent Beta subtree spacings, explicit Euclidean covariance minimization, invariant isotropic product or sharp tree extremizers. Other Hanner/tree-polytope isotropic studies involve different polytopes or metrics. Equivalent probability/moment formulas from order-statistic literature remain a risk.

## value

PASS

Subtree sizes are natural hook statistics and isotropic constants are a central affine geometric invariant; exact diagonal covariance and sharp star/path extremality across all rooted trees provide reusable quantitative geometry, with a meaningful uniqueness statement inside the given transfer family. The result is neither a parameter renaming of the continuous transfer nor just a volume restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
