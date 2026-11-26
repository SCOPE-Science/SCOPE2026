---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Conditioning on isolation of a vertex v removes its d_v incident edges from the mean retained-edge count and does not affect any other edge, so its covariance contribution is −d_v2^(−d_v)/2. The function d2^(−d) equals 1/2 at 1,2 and is strictly smaller from degree 3 onward; equality for the lower bound therefore forces the path. The degree budget is B=n−2=Σ(d−1); a positive degree list of that sum has a Prüfer realization. For the upper bound hub profits at degrees 3,4,5,6 are 4,8,11,13 in units of 1/32, at costs 2,3,4,5. Any degree ≥7 is dominated by two fours with profit 16 at cost 6 and any remaining budget can be filled with degree-two vertices. The listed exchanges with a three, four fours, or two sixes are strictly profitable. A sole three can use a spare unit to become a four for B≥3. Two spare units buy a hub; one spare unit strictly improves any surviving degree 4,5,6 by replacing it with 5,6,(4,4), respectively. Thus there is no slack in an optimum and only (a,b,c) with 3a+4b+5c=B, a≤3,c≤1 survive. The scaled profit is 11B−a−3c; checking these eight (a,c) pairs yields exactly the four residues and their listed ties, with the three-fours case infeasible at B=5. At n=4 the star yields −15/16; at n=2,3 only the path is possible.

## originality

PASS

The fixed-graph conditioning identity and path bound are elementary. The relevant distinct result is the exact unrestricted-tree covariance maximum and complete equality classification, particularly the degree-five hub economy and modulo-four corrections. The inspected adjacent results do not cover it. A possibility of coverage by generic degree-index optimization is retained as a bounded access risk, not dismissed from a snippet.

## value

PASS

The covariance measures isolation sensitivity to edge density at a central retention parameter, and the fixed-order question asks how different tree hosts can make that sensitivity. The optimum does not asymptotically select either standard example (path or star); it selects degree-five hubs with exact modular corrections and distinct ties. The classification gives sharp sensitivity and exact equality for every order, information not supplied by a generic leading-rate bound or edge-conditioning calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
