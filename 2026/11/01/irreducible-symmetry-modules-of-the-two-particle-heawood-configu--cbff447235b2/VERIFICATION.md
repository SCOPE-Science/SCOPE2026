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

# Reproduction
Run `python3 verify.py` with the standard Python 3 library. The package includes its recorded stdout in `verify_output.txt`; compare the full output rather than relying on the final `VERIFY_OK` alone.

The verifier constructs the fourteen Fano incidence vertices and 21 edges, all 91 unordered two-vertex cells, 252 edge–vertex cells and 168 disjoint-edge squares. It checks the two cubical boundary matrices, rank computations modulo several primes, the 28 spanning six-cycles, all 336 graph automorphisms, signed chain Lefschetz traces and character inner products. It **separately** row-reduces the square boundary matrix modulo 101 to obtain 14 explicit nullvectors and verifies the top-homology character through direct signed permutation action for all 336 group elements. The rational ranks are proved by combining the mod-three rank lower bound with the surjective graph-cycle map; finite-field agreement by itself does not certify rational homology. All group irreducibility and quotient conclusions use characteristic-zero representation theory. This verification is a self-review, not an independent external audit.
