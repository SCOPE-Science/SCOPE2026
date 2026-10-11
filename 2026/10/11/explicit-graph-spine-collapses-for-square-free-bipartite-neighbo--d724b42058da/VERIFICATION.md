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
# Verification

The proof is symbolic and applies to every finite connected simple bipartite square-free graph. The standalone program `verify.py` is a finite stress test of the claimed collapse construction.

It exhausts all connected labeled bipartite square-free graphs on 2 through 6 vertices. For each graph it reconstructs the full neighborhood complex, applies the prescribed root collapse, checks at every step that the lower simplex has exactly one remaining coface, and checks that the final complex is exactly the two target graph spines. It also checks target connectedness, edge counts, and cycle ranks.

The exhaustive run covers 1,501 graphs, 17,850 neighborhood-complex faces, and 1,530 elementary collapse pairs. Additional tests use the incidence graphs of the projective planes of prime orders 2, 3, and 5, where the target cycle ranks are 8, 27, and 125.

Running `python3 verify.py` prints `VERIFY_OK` followed by the census. These finite checks validate the implementation and typical boundary cases, including degrees beyond three, but do not replace the general proof.
