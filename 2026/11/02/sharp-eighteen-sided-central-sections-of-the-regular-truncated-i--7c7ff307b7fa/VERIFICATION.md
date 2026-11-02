---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The sign-enumeration proof is encoded in `CERTIFY.py`, a Python 3 standard-library script. Execute `python3 CERTIFY.py`. It constructs exact integer-pair representatives of \(\mathbb Z[\sqrt5]\) and decides their ordering by signed squared-integer comparisons, not floating-point thresholds. It enumerates the thirty original icosahedron edges, sixty truncated vertices, ninety truncated edges, twelve pentagonal and twenty hexagonal facets, all 968 octant-refined spherical regions, and all ten attainable joint facet counts. It verifies that the extremal regions correspond to exactly twenty distinct old-face-center sign chambers. For one distinguished chamber, exact cross products show six successive boundary intersections and verify all other circle constraints. Alternating exact normalized dot products imply the stated spherical hexagon area.

`CHECKS.txt` is a saved run of these checks. Floating-point spherical areas only reproduce the displayed approximate probabilities and the limiting exact angular formula to numerical precision; the exact combinatorial and angle assertions do not rely on such numerical agreement. No assertions are made about offset sections, nongeneric incidence planes, earlier uninspected sources, or independent validation.
