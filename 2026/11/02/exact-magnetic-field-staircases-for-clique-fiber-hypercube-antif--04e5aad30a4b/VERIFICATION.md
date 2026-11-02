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

# Reproducible finite checks and their limits

The full theorem is proved by the convex clique-occupancy lower bound and the parity balanced independent-set construction. Finite checks corroborate the proof and certify the stated \(d=3\) degeneracies.

Run `python3 verify.py` from the directory containing the embedded source. It asserts graph degree and exact edge count in dimensions \(3\) through \(8\), gives one sharp extremizer for each integer sector up to half filling (1,794 sectors), directly compares cut sizes on every extremizer for \(d=3,4\), and verifies that Euclidean distance-two neighbours in the 24-point three-dimensional realization equal the combinatorial edges. Expected final line: `d=3 coordinate embedding: every unit-edge graph relation verified`.

Compile and execute `c++ -O3 -std=c++17 census_independent.cpp -o census && ./census`. It independently compares two complete methods over \(2^{24}\) spin masks and prints 25 lines of `sector best-cut multiplicity`. The final line must be `all 25 sectors, both exhaustive methods and formula agree`. For sectors zero through twelve, the exact multiplicities are \(1,24,228,1104,2940,4368,3536,1440,234,552,444,144,18\); other sectors mirror by spin inversion. All field-degeneracy numbers are sums of the appropriate disjoint sector counts, not probabilistic estimates.

No finite enumeration proves an infinite-dimensional statement. The general theorem stands on the analytical construction. No claim is made for nonuniform exchange strengths, thermal states or quantum observables. Independent validation remains unperformed.
