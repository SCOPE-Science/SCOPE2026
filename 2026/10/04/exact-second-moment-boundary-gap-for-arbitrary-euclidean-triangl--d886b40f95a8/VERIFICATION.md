---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For iid vectors, mean squared pair distance is twice the trace covariance. Dirichlet \((1,1,1)\) barycentric moments give the interior value \((a^2+b^2+c^2)/18\). Weighting the three uniform edge-segment moments by side length gives the boundary value \((a^3+b^3+c^3+3abc)/(6(a+b+c))\). Standard triangle identities yield the stated \(s,R,r\) formulas. Subtracting and setting \(x=s-a,y=s-b,z=s-c>0\) gives an explicit polynomial with only positive coefficients, proving strictness. Fresh independent numerical evaluation on three scalene/isosceles test triangles reproduced the gap identities; the universal proof is symbolic.

## originality

PASS

The accessible Lotnikov abstract treats the Zaporozhets–Tarasov mean-distance program and states a stronger triangle result in its first-moment context, but does not expose the audited \(p=2\) formulas. Tokmachev proves all moments under planar interior/boundary centroid coincidence; a triangle satisfies that centroid hypothesis only in the equilateral case, so it does not cover generic triangles. Exact formula searches returned the assigned finding rather than an older arbitrary-triangle boundary second moment. Full texts of the two recent arXiv papers were not obtained through the open route, and the combined authorized fallback attempt was safety-blocked and not retried; this remains a residual risk.

## value

PASS

The second moment is the first algebraically tractable nontrivial benchmark for the current boundary-versus-interior moment conjecture. The theorem covers every triangle, including those excluded from the known centroid-coincidence theorem, and gives an exact quantitative gap rather than only a sign.

The dated certificate retains the supplied scientific assessment, sources and limitations.
