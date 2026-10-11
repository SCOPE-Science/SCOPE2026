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

The published centrally symmetric-body reduction legitimately restricts the global optimum to center-passing straight-line bisections. For a regular even polygon, after choosing one side with endpoints \(A=(a,-b)\), \(B=(a,b)\), every such line may be represented by an endpoint \(x=(a,t)\), \(-b\le t\le b\). The antipodal direction \(-x\) lies between the vertex directions \(-A\) and \(-B\), so a farthest polygon vertex from \(x\) is one of those two. Hence the maximum relative diameter squared is exactly \(\max\{4a^2+(t-b)^2,4a^2+(t+b)^2\}=4a^2+(b+|t|)^2\), uniquely minimized at \(t=0\). Substituting \(a=R\cos(\pi/n)\), \(b=R\sin(\pi/n)\) gives \(R^2(4-3\sin^2(\pi/n))\). The \(n=6\) specialization agrees with the independently published \(\sqrt{13}R/2\) standard-partition value.

## originality

PASS

The 2018 primary paper supplies the broad structural reduction from arbitrary bisections of centrally symmetric convex bodies to center-passing segments and gives general optimality criteria, but does not compute the regular-even family. The 2016 multi-rotational paper gives the regular-hexagon standard two-partition value only. Fresh Resultary and regular-polygon searches found no prior all-even-n formula or side-midpoint optimizer classification. The audited work is therefore the family-specific exact optimization left after the published general reduction, not a restatement of the reduction itself.

## value

PASS

The maximum-relative-diameter bisection problem is an established geometric optimization problem, and regular even polygons form a canonical infinite family. The theorem converts a general existence/reduction theorem into a complete closed form and optimizer direction for every even order, while recovering a known hexagon special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
