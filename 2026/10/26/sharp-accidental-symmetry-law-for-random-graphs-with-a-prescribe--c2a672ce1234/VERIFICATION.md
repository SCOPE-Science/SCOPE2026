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

# Verification record

Run `python3 check_involution_graph.py` using only the standard library. This enumerates all \(2^{m^2}\) graphs for \(m=2,3,4\), where \(m\) is the number of paired orbits. It builds edge-orbit coordinate maps for every element of the wreath-product centralizer, tests every candidate automorphism, constructs the independent disagreement graph, and checks the exact kernel-cardinality identity and the equivalence between excess symmetry and either disconnected disagreement or an orbit-permuting symmetry. The generated finite summary is:

```
m 2 graphs 16 extra_aut 12 single_fiber_flip 8 extra_fraction 3/4 orbit_permutation 8 kernel_checks 16
m 3 graphs 512 extra_aut 416 single_fiber_flip 256 extra_fraction 13/16 orbit_permutation 248 kernel_checks 512
m 4 graphs 65536 extra_aut 41152 single_fiber_flip 23552 extra_fraction 643/1024 orbit_permutation 23680 kernel_checks 65536
PAIRED_GRAPH_AUT_EXACT_OK 25190528 flip_laws 45
```

The enumerations are finite checks, not proofs that the asymptotic bound holds. The latter follows analytically from the two support-size orbit-permutation union bounds and classical connectivity counting as explicitly derived in `RESULT.md`. An independent scientific audit has not been performed.
