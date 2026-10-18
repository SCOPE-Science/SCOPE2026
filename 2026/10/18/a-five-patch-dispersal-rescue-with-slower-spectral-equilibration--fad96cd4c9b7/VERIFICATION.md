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

# Reproduction of the mathematical checks

Place `RESULT.md` and `verify.py` in the same directory and execute `python3 verify.py` using the Python standard library. The program computes exact characteristic polynomials of the two five-patch adjacency matrices; verifies rational isolations for their critical eigenvalues; checks the resulting growth and damping inequalities; and enumerates every simple labeled graph of orders two, three and four, selecting connected nonbipartite graphs and verifying the polynomial classification for every available single-edge addition. The script reports the number of eligible labeled graphs and additions actually checked.

The proof of the full parameter interval is the pair of positive coefficient bounds in `RESULT.md`, not an interpolation from numerical samples. The all-orders claim here is **only** the exclusion of graphs with fewer than five vertices; no enumeration of larger graphs is used to infer optimality or uniqueness. The damping ratio describes asymptotic relative spectral decay, not a universal trajectory-dependent convergence time. No independent external mathematical audit has been performed.
