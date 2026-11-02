---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Binary outdegree-one synchronous firing is exactly translation by one vertex, so maximal avalanche faces are translated triples. Triangle edges follow cyclic steps a,b,c; the one-skeleton is a cyclic Cayley graph with g=gcd(a,b,c) components. For a singleton gap not equal n/2, the corresponding orbit of n undirected edges appears exactly once among n distinct translated triangles; disjoint elementary free-edge collapses remove all triangles. Equilateral support instead consists of disjoint filled triangles; {q,q,2q} instead gives g tetrahedral boundary spheres. The remaining connected graph cycle rank E-n+g yields the stated S1 wedge counts including antipodal orbit of size n/2. Independently enumerated all 1365 support triples for n=3..14, rebuilt triangle orbits, performed actual elementary collapses, and checked component and graph ranks in every case. The all-n integral proof is based on the orbit/collapse counting, not the finite check.

## originality

PASS

Riihimäki–Smith introduce avalanche homology for precisely directed cycles and treat some binary configurations; the assigned source identifies Proposition 3.23 for three grains with adjacent support and Corollary 3.22 for complements of a singleton. The present five-regime all-three-gap and gcd classification extends to separated triples. Its original full text was not accessible in this run, so exact implication of every statement in that paper is a material residual priority risk; a bibliographic abstract alone cannot establish complete noncoverage. Published related circular interval nerve classification concerns consecutive arcs rather than arbitrary translated triples.

## value

PASS

The original work identifies dependence on the initial chip placement as a central problem. This solves the natural binary three-occupied-vertex stratum uniformly, distinguishing disconnected components, exceptional 2-spheres, and integral circle ranks through gap arithmetic. It does not claim to solve arbitrary sandpile states or the full general configuration problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
