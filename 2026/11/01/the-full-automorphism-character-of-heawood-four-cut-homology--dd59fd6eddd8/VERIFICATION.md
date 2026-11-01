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

Execute `python3 verify.py` in the directory containing this file. The expected exact output is `verification_output.txt`; the final marker is `VERIFY_HEAWOOD_4CUT_FULL_CHARACTER_OK`.

The program independently constructs the Fano incidence graph, checks 21 edges and all vertex degrees, enumerates the 98 connected and 903 disconnected four-sets, forms both dual and ordinary cut complexes, certifies 98 distinct private triangles, checks 168 preserving automorphisms against an independent 7!-permutation census, constructs 168 class-exchanging automorphisms, and verifies graph preservation. It evaluates signed simplicial traces both from every face in the original complex and from the Alexander-dual faces with the full-vertex permutation sign twist. The resulting traces match element by element, and the exact group averages are zero.

This finite computation is exhaustive **for the specified 14-vertex graph**. The integral homology argument relies on the private-triangle boundary unit minor and the full skeleton, not on modular-only or floating-point ranks. The rational quotient conclusion uses the standard finite-group invariant-homology theorem. Neither integral representation lattices nor equivariant homotopy type are checked. Scientific novelty against unindexed literature is not mechanically decidable. Independent audit has not been performed.
