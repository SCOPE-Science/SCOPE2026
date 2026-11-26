---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

I reconstructed the entire finite problem using complement labels on the right: admissible pairs are disjoint two-subsets of the five symbols. Choosing one of three neighbors at each of ten rows and retaining injective tuples exhausts all matchings and gives 60. For matchings p and q, each nontrivial cycle of p⁻¹q corresponds to one alternating cycle of twice its length, so the test is exactly one nontrivial cycle of length three or four, respectively. This yielded 120 and 60 edges, and after relabeling matched all 60 labelled states and every labelled edge in the certificate. I also verified that the stated vertex map is an isomorphism from GP(10,3). The joint degree classes (deg₆,deg₈) are (0,10)^6,(4,2)^30,(5,0)^24; six-flip edges all join classes of hexagon degrees 4 and 5, and each pair of octagon hubs has exactly two common degree-two neighbors. Iterated reachable balls at every root reproduced active hexagon profiles (1,4,12,16,16,4,1) and (1,5,10,20,12,5,1), and union profiles (1,10,25,20,4), (1,6,21,24,8), and (1,5,15,25,14). This gives the stated components, radii and diameters. The incidence graph is bipartite with no four-cycles, since two distinct two-subsets have at most one common three-superset, so eight is the sharp cutoff. The full S₅ action reproduced orbit sizes 6,30,24 by hexagon degree; parity is opposite on the frozen and active classes and changes exactly on the octagon edges. The independent enumeration used a Cartesian product and relative cycle decompositions rather than the submitted procedures. The supplied Python files and recorded outputs were inspected, not executed; their documented replay paths are `python3 verify_gp.py` and `python3 verify_incidence.py` in the package directory.

## originality

PASS

Credit the exact restricted Desargues flip dynamics and sharp cycle length, not the already tabulated count of sixty matchings or the general alternating-cycle move. A later dated Resultary record covers the main Desargues flip result under the same convention and is a substantial overlap; the inspected evidence does not place it before the assigned record. Earlier sources inspected address the underlying cycles, the matching count, other move conventions, or other graph families.

## value

PASS

The Desargues graph is a standard symmetric configuration graph, and the minimal permitted flip length for full reachability is a natural invariant distinct from unrestricted move count. The shortest cycles leave a frozen sign class despite the symmetry of the underlying graph; the next length acts on those exact states with a doubled-complete-graph subdivision and yields uniform eccentricity four. This supplies a fully specified benchmark for bounded matching dynamics, not just a recomputation of a known matching count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
