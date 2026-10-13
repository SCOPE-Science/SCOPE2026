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

The verifier rebuilds the finite problem from the cyclic-distance definition. It fixes one word by translation symmetry, enumerates every size-\(10\) code through that word, proves by exhaustive branch-and-bound that no size-\(11\) code through it exists, and directly rechecks the pairwise nonconfusability condition for all enumerated maxima.

It then canonically normalizes all maxima through the fixed word under anchor changes, independent coordinate reflections, and coordinate permutations. For each resulting representative it exhausts every element of the natural group \(G=(D_{10})^3\rtimes S_3\), recomputes the stabilizer, and verifies the packaged `ORBITS.csv` row. The orbit-size total must equal the independent incidence count \(125\cdot31{,}328/10=391{,}600\).

Expected terminal line:

`VERIFY_OK vertices=125 origin_candidates=98 origin_maxima=31328 maximum=10 labeled_maxima=391600 natural_group=6000 orbits=85 stabilizers=1x53,2x19,3x2,4x7,8x1,10x2,40x1 nodes9=262869 nodes10=22757 special_stabilizer=40`

Replay with a C++17 compiler:

`g++ -O2 -std=c++17 verify.cpp -o verify && ./verify ORBITS.csv`

The computation is exhaustive only for the finite three-use pentagon instance. It is not an infinite-family proof and makes no claim about higher powers.
