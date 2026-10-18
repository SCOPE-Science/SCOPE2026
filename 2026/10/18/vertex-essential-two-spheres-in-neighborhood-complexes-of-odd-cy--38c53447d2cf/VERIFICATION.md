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

## Exact checks

The combinatorial proof uses the stated neighborhoods and their complete simplex-intersection nerves, with one missing nerve triangle under twin-vertex deletion. The collapse of the punctured fan nerve onto the base cycle and the naturality of the nerve lemma establish the general inclusion equivalence; the general theorem does not depend on experiments.

Run `python3 verify.py` using the standard library. The checker rebuilds the neighborhood complex from its maximal common-neighbor simplices for odd cycle lengths 5, 7, 9 and 11, computes mod-two boundary ranks, verifies vanishing homology after one representative deletion in each of the three vertex orbits, and checks both exact nerve combinatorics. Expected final line: `VERIFY_OK ODD_CYCLE_NERVE_AND_HOMOLOGY_SAMPLES`.

## Limits

Mod-two computations for four small indices cannot certify all odd indices or integral homotopy types. Those conclusions rest on the paper's general good-cover argument, homotopy-pushout lemma, and equivariant Mayer–Vietoris isomorphism. No independent scientific audit has been conducted.
