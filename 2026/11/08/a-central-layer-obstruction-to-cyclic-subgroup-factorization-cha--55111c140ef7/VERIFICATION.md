---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For squarefree cyclic group each proper nontrivial subgroup corresponds to a proper nonempty missing-prime support and product=whole group iff missing supports are disjoint. Removing r size-(r-1) pendant supports leaves V=2^r-r-2 possible cycle vertices. For any 2-regular subgraph, twice degrees give a-b=e_A-e_B and |V(F)|<=2|B|+e_A. At even rank 2k only complementary k-set pairs yield internal A edges, at most C(2k,k)/2. At odd 2k+1 internal A edges are (k,k) or (k,k+1); incidence at k level bounds x+2y<=2c and x<=c, hence e_A<=floor(3c/2). Both yield U=2^r-2-ceil(c/2). Verified entire stated r=5,6,7 explicit disjoint cycles and symbolic level structure for ranks5..12 with independently written exact bitset certificate. These finite witnesses prove only 2-regular sharpness at those ranks; all-r bound follows from the general counting proof, not enumeration.

## originality

PASS

Previous Gutiérrez–Zuleta–García-Claro work determines the squarefree cyclic factorization graph and exact single-cycle circumferences for small ranks 5,6,7; those counts are credited, not claimed new. The new uniform central-binomial bound applies to any disjoint UNION of cycles for all r>=5. General factorization-graph origin and fixed-level Kneser Hamiltonicity do not imply this mixed-level bound. Original 2026 full preprint access failed (Oxford VPN disconnected), so comparisons beyond abstract/published summary are qualified; no contrary general all-r bound identified.

## value

PASS

Uniform structural missing-middle-layer obstruction to 2-regular coverage of an intrinsically natural subgroup-factorization graph, exact at three first nontrivial ranks with explicit witnesses. It answers a concrete all-r extremal question distinct from merely repeating existing small-r circumference numbers; the gap grows order 2^r/sqrt(r).

The dated certificate retains the supplied scientific assessment, sources and limitations.
