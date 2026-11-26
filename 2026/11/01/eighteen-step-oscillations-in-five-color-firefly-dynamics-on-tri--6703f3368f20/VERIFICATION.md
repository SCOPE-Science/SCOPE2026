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

On each shore the only external signal is whether either other shore contains color 2, so the image of each occupied support is determined without multiplicities. The independent replay exhausts all 31^3 ordered nonempty triples, canonicalizes directed cycles by rotation and computes color-return permutations on the actual occupied colors. It reproduces 89 cycles, the length-1,2,3,5,6 census (27,1,20,1,40), basin counts (27,24,60,28684,996), and maximum preperiod 40. On a recurrent support orbit, the local surjections are bijections because support cardinalities cannot decrease and then return. A labelled state uses every occupied color, so its least period is the support period times the least common multiple of the three permutation orders. This also proves that microscopic and support entry times coincide. The permutation census yields exactly 5,6,9,18, all realizable with shores of size at least 5. For each ordered assignment of monodromy orders (1,2,3), the period-18 size profiles are twice (1,4,3) and once (2,4,3); the three phases and the identity 2q_1(n)+q_2(n)=2^n give the stated factor 3/18=1/6. The two surjection factors give the distinct-shore criterion; (1,3,4) has 48 orbits and (2,2,2) has none. The submitted full-state run was inspected as recorded corroboration, not independently rerun.

## originality

PASS

The distinct contribution is the exact classification and primitive count for three nonempty shores. The strongest same-rule catalogue hit treats two shores and already has period 18, so the new claim is not discovery of period 18 for the automaton in general. No inspected result covers the tripartite classification or its weighting.

## value

PASS

A fixed and natural complete multipartite family with arbitrary labelled shore sizes gets an exact synchronization-failure invariant, a sharp shore-size existence criterion, a uniform transient bound and a new period spectrum. The finite quotient does substantive work: it turns a computation whose microscopic state size grows exponentially in total vertices into one fixed census sufficient for the entire infinite family. The closed orbit count is usable without running that census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
