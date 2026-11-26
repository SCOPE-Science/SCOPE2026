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

For k≤5 the cubic edge count gives at least 30-3k edges on 20-k vertices, strictly above the forest bound 19-k. I independently enumerated every six-set using leaf stripping of its complement (empty 2-core iff forest), then grouped accepted sets by five-subsets (two distinct six-sets are adjacent iff they share a five-subset). All-source shortest-path layer expansion reproduced 2520 sets with induced-edge split (660,1860), 23940 exchange edges, eccentricity 6 at every vertex, and exact unordered distance counts (23940,162870,572230,1088390,993990,332520), totaling 3173940. Intersection sizes give excess counts (3124960,48800,180), and all sources reached all vertices. For example, in the encoding u_i=i, v_i=i+10, sets {0,1,3,5,16,17} and {0,1,5,7,13,14} have distance 5 versus Johnson distance 3. At least |S\T| moves are needed since each move removes at most one member of S not in T. The independent replay does not use the frozen checker’s union-find/DFS or enumerate swaps, and exactly confirms the frozen transcript. A documentation erratum: bit_count in the original script requires Python 3.10+, not all versions starting at 3.8.

## originality

PASS

The supported distinct claim is the quantitative unrestricted exchange geometry, especially the sharp radius, diameter, uniform eccentricity and exact pairwise detour census. The static set count and split already occur in equivalent induced-forest form in an earlier catalogue record, the minimum size is known, and connectivity is covered by a general reconfiguration theorem. None of those is credited as new. The closest later token-slide comparison echoes the coarse unrestricted profile, but does not supply its complete metric histograms.

## value

PASS

A natural question after general reachability is whether the trivial exchange lower bound is sharp for shortest routes. For this symmetric planar cubic benchmark the exact census says no, quantifies how rare detours are, and gives a sharp uniform diameter despite some detours of length two above the ambient bound. These are useful precise benchmarks for proposed reconfiguration bounds and algorithms, independent of the already known counts and connectivity. The independent distance-five witness with Johnson distance three illustrates the structural obstruction captured by the table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
