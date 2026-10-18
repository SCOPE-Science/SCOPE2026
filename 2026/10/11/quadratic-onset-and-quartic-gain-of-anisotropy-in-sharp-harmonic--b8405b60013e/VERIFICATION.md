---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Matched the source Theorem9.3 exact L_{n,r}(q) integral and q minimization (not its separate Poisson-information relaxation). Set Psi(s,r)=n log L(e^s)-s. At origin, isotropic spherical moments E t²=1/n,E t⁴=3/[n(n+2)] give H=2(n-1)(n+1)/[n(n+2)]>0. Independently expanded the source Poisson-gradient radial/tangential numerator nLq(1)-L(1) using parity r->-r,t->-t and moments: Psi_s(0,r)=A r²+O(r4), A=(n-2)(n-1)(3n+2)/[n³(n+2)]. Implicit minimizer displacement -A/H r² and quadratic optimization advantage A²/(2H) r⁴ establish c and delta. Independently integrated source exact formula at n=3,4,5,7 and r=.1,.05 with high precision; scaled derivatives approach the analytic A; numerical checks corroborate but do not prove all n.

## originality

PASS

Zhong–Kalaj Theorem9.3 identifies the exact variational problem and Prop9.4 proves only qualitative anisotropy q<1; it does not give a local radial curvature or the optimal-to-isotropic gap. Extracting these from the implicit integral demands a dimension-uniform second-order spherical-moment expansion and a fourth-order minimization argument. The other Poisson-information bound is a distinct relaxation, not the scalar q=1 comparator.

## value

PASS

Quantifies two different geometric scales for the new natural extremal family: extremizing derivatives depart from isotropy at order r² while the sharp Jacobian improvement begins at r⁴. Exact dimension-dependent curvature and gain are useful quantitative structure, not a numerical example or arbitrary specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
