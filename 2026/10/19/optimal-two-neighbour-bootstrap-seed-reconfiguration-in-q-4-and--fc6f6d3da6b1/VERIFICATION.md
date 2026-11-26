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

I independently enumerated each seed size up to the first percolating size, using asynchronous activation by precomputed neighbour pairs (the same least closed superset as synchronous activation). Exchanges were built by bucketing states on a common (k-1)-subset, then retaining Hamming-distance-one changes for sliding. Full translation and coordinate-permutation orbits and BFS on the full graphs reproduced 144 and 16960 states, orbit counts 2 and 18, all four edge totals, connectivity, and all eccentricities. The complete seed-list hashes match both frozen certificates. In Q5 the unique central slide orbit has 960 members, represented by {0,3,13,30}; eccentricity 10 and 11 counts are 11200 and 4800, and BFS also gives distance 11 for the exhibited endpoints. Replay: python3 branches/independent_cube.py. The proof is finite and does not cover d>=6 or inclusion-minimal states of larger cardinality.

## originality

PASS

Pass for the optimum jump/slide graphs, their exact metrics, and the Q5 central orbit. Minimum sizes already follow from the Morrison–Noel lower bound and matching seeds. The Q4 optimum census of 144 sets in two orbits also occurs in a distinct indexed record; its publication dates do not decide priority. Neither the matching census nor the inspected closure framework gives reachability, edge totals or the distance profiles without additional analysis.

## value

PASS

Minimum seed counts do not show whether one can relocate seeds without losing percolation, or what a worst-case relocation costs. The two first nontrivial cubes here separate the effects of jumping and sliding, and distinguish self-centered Q4 from a Q5 slide graph with a single central orbit and distinct radius and diameter. The exact finite graphs give a benchmark for minimum-budget reconfiguration, not a general-dimension claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
