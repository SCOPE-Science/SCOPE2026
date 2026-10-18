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

Classical Kruskal–Katona Q(m)=binom(a,3)+binom(b,2) bounds the triangle count with m=binom(a,2)+b. Properly colored small explicit witnesses reach the values [0,0,0,1,1,2,4,4,5,7] for m<=9. To handle m=10,11, discard triangle-free edges; disconnected triangle-bearing components have <=6 triangles. For connected cores on >=8 vertices, minimum degree 2 and average degree <3 force a degree-2 vertex contained in exactly one triangle; deletion + Q gives subthreshold ordinary triangles. Therefore only up to seven vertices need exact finite enumeration. An independently implemented exhaustive graph-mask census checked all 709801 labeled graphs with 10 or 11 edges on 3<=n<=7, showing non-K5 maxima 7 and 8; independent coloring enumeration checked all 3^10=59049 three-colorings of K5 and maximum 7. The elementary K5 repeated-color pigeonhole proof plus edge-budget K5 obstruction completes the unrestricted-vertex result. Exact witness graphs attain 7,8. This is an exhaustive finite-computation certificate attached to an analytic reduction, not extrapolation.

## originality

PASS

Best-of-knowledge original exact 0..11 rainbow-triangle edge-budget profile. Properly credits known KK upper bound, K5 construction, and colorful inequalities. Complete finite-support reduction and independent census provide the missing 10/11 upper bounds.

## value

PASS

The first edge budget where the three-color rainbow extremum falls strictly below the ordinary Kruskal–Katona triangle maximum is a natural sharp structural boundary in extremal colored graph theory. The exact 10/11 counts answer a motivated small-edge question left open by general inequalities and give a reusable finite cutoff; this is not an arbitrary code recomputation or trivial numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
