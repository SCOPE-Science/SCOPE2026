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

For a strictly convex centrally symmetric C² plane curve with positive C² π-periodic polar radius r and positive C¹ π-periodic normalized angular density f, all n>=3 sampled angles are i.i.d. The unique occupied open semicircle on the origin-miss event has initial sampled anchor T_n; choose its index in n ways, with all other n-1 angles independently falling in a half-mass interval, giving P(M_n)=n/2^(n-1) and exact conditional density f(T_n). Given anchor θ, the endpoint deficit δ_n has survivor (1-2∫_{θ-s}^{θ} f(u)du)^(n-1), so nδ_n→Exp(rate 2f(θ)) uniformly for fixed threshold. The separating hull edge’s Euclidean origin distance is r(θ)δ_n/2+O(δ_n²), uniformly by the smooth polar determinant, yielding joint (T_n,nD_n)→(T,r(T)E/(4f(T))) with independent unit exponential E. Positive inf f gives exponential envelope on nδ_n, uniform integrability and all fixed positive moment limits. Thus limiting mean Z/4 independent of f and second moment ∫r²/f /8. Jensen conditioning on E proves convex order lower bound at constant m=Z/4, equality uniquely f=r/Z; circle exact finite law from Dirichlet circular gaps n[arccos(t)/π]^(n-1) validates normalization. This is a genuine rare-event conditional law, not typical random-hull approximation.

## originality

PASS

Best-of-knowledge new marked conditional miss-distance law and convex-order optimal radial density beyond classical Wendel center-exclusion probability. Published area/Hausdorff sampling optima concern typical approximation errors; Liu–Yang deals interior disk points; exact circle gap law is explicitly presented only as calibration.

## value

PASS

Sharp conditional asymptotics for a geometrically meaningful rare failure event, including an exact marked law, all fixed moments, a surprising density-invariant mean and the unique convex-order optimal boundary sampling density. The different optimal density from typical Hausdorff/area loss illustrates why this exact invariant matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
