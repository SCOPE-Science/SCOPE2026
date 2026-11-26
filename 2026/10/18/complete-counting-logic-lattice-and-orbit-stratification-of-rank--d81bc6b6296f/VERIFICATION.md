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

Every length-two interval forces two intermediate points, so the middle incidence graph is simple, bipartite and 2-regular. Its half-cycle partition determines the strict order, and all such partitions satisfy the Eulerian condition. One counting round separates ranks by strict in/out counts, and two-variable formulas depend only on r, the free ranks and the atomic pair relation: upon rebinding one variable, the counts in every remaining rank/relation class depend only on the rank of the other variable. Cardinality then separates different r. For C³ use the size clause 2r+2 and distance doubling over the three available symbols, reusing symbols only within disjoint scopes; D_t has rank at most t+1 and covers each component at t=ceil(log2 r), since its diameter is at most r. The two outer counts recover the number of atoms in components of size 2k and yield rank at most t+3. Each layer r≥4 has at least (r) and (2,r−2), including r=4. At singleton layers cardinality alone actually needs only one variable. Same-rank pairs fail a join or meet exactly when two common opposite-rank neighbors form a C4 component; the displayed C³ counting predicate detects it. Side-preserving cycle rotations and permutations of equal-length components give exactly the claimed orbits; the least sum of s distinct part sizes is s(s+3)/2 and surplus can be absorbed in the largest. Removing one part 2 and choosing a single divisor part size give the nonlattice and refinable counts. Independent exact check: python3 /workspace/reproductions/frozen_checks.py 2 generates 1,6,90,2040 labeled incidence matrices for r=2..5 by two disjoint permutation matchings, tests full atomic profiles and actual joins/meets, recovers parts by Boolean distance squaring, and verifies orbit sizes on a representative of each type. The frozen verify_eulerian.py does not actually contain the distance-squaring test attributed to it, and verify_incidence_enum.py writes a profile template rather than deriving it from the strict-order matrix. The independent check supplies those finite tests in its stated range; the general theorem rests on the proof, not on the advertised computational ranges.

## originality

PASS

The alternating-cycle decomposition, the general counting-refinement method, and the small collision as a construction are not credited. What passes is the class-specific classification combining the fixed-size theories, quantitative within-class C³ identification, exact lattice and orbit boundaries, and the census. The inspected near matches do not give that classification. The conclusion is bounded by the sources actually inspected.

## value

PASS

Bounded Eulerian rank-three orders are a natural thin-poset family. The theorem specifies exactly how much strict-order information two-variable counting loses at each size, how to recover isomorphism with a third variable at logarithmic rank, and when that loss conceals latticehood or automorphism orbits. Those sharp boundaries and full counts support the contribution beyond the standard cycle decomposition or one lifted counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
