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

# Reproduction instructions and limits

Run `python verify_matching.py` and `python verify_colouring.py` with Python 3.9 or later. No third-party Python libraries, network connectivity or external datasets are required.

The matching-based verifier constructs all 120 perfect matchings, identifies all even complementary two-factors, enumerates 504 proper three-edge-colourings with named colours, and builds 1,674 switching edges by two-colour connected-component swaps. It computes 144/360 components, exact all-pairs distances and degree spectra. It also constructs three explicit underlying graph automorphisms and their 144-element subgroup, checks its free transitive action on the 144-colouring sector, and verifies six involutory generators. A parity-lift BFS checks odd girth.

The direct-colouring verifier uses a distinct recursive edge-colour constraint solver rather than matching enumeration. It independently walks bichromatic cycles by original-graph vertices and reconstructs every Kempe move and all-pairs distances. The programs use different fixed edge orders but produce the identical isomorphism-invariant counts and sector cycle-type criterion.

Both programs assert their critical outputs. They are exhaustive finite proofs for the stated 24-vertex graph, not an infinite-family certificate. The priority search is subject to the historical-source access limitations detailed in the scientific document; no independent scholarly audit has been performed.
