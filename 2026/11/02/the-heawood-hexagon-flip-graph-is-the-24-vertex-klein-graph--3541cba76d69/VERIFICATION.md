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

# Reproducibility and limits

The attached source files perform complete finite checks using no specialist mathematical libraries. Run `python3 verify_fano_permanent.py certificate.json` to reconstruct the 24 matchings from all 5040 permutations, all 84 six-flip edges, the complete 24-by-24 shortest-path table, the intersection array, and the eight antipodal triples; it also checks the provided certificate against its recomputation. Run `g++ -O2 -std=c++17 verify_fano_cycles.cpp -o verify_fano_cycles && ./verify_fano_cycles` for an independent construction using nonzero vectors of the three-dimensional binary space, recursive bipartite matching search, and explicit enumeration of all 28 hexagons.

Actual complete executions of both programs produced:

```
FANO_PERMANENT_PASS matchings=24 six_flips=84 array=[7,4,1;1,2,7] antipodal=8 triples
FANO_CYCLE_PASS matchings=24 hexagons=28 exchanges=84 array=[7,4,1;1,2,7] antipodal=8
```

These are finite exhaustive deductions. They establish the explicit reconfiguration graph without extrapolation. Identifying the resulting intersection array with the named 24-vertex Klein graph invokes the published uniqueness statement in Brouwer–Cohen–Neumaier, *Distance-Regular Graphs* (1989, p. 386). All code and the complete finite adjacency/distance certificate accompany the result. No independent scholarly audit or human certification has been performed.
