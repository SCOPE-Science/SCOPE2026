---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At the equilibrium approaching (1,1/c), the Jacobian has trace tending to -b²/c and determinant -b² r+O_a(r²), so the positive-rate branch is a saddle in the stipulated time. At r=0 the fast eigenvalue is separated from the center eigenvalues. Translating by the continued equilibrium and including r'=0 gives a smooth local strong-stable family with a nonvertical tangent; its r=0 graph is horizontal. Differentiating g=h'f twice shows that its curvature at the saddle is O_a(r²), since f_uu at the undeformed saddle is zero, g_uu is identically zero, and the denominator tends to 2b²/c. The third graph derivative at the saddle is O_a(r) and fourth derivatives are bounded. Thus on the section, which is O_a(r) away, all nonlinear graph terms are O_a(r⁴). Independent symbolic jet calculation and inversion give the stated cubic and a0=0.44330690496759439175… . The section map has derivative 2/(bc)>0, giving a unique local positive rate. The polynomial 4b³+b²−1 increases strictly from −1 to 4 on [0,1], and the sign as a increases is reversed because b=1−a. The error convention is exact threshold minus the quadratic approximation.

## originality

PASS

The model and quadratic threshold are prior. The model-specific curvature cancellation justifying the cubic for the true separatrix, and the explicit crossover obtained from it, were not covered by the strongest available comparisons. This is a best-of-knowledge assessment, not a priority certificate.

## value

PASS

The third-order term answers a concrete question left by the published threshold: on which side of the true threshold the quadratic falls. The unique reversal shows that one cannot assign a uniform direction of bias as Allee strength varies. It is not merely an extra coefficient of an uncontrolled tangent approximation: the cancellation shows why the true graph agrees through the necessary order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
