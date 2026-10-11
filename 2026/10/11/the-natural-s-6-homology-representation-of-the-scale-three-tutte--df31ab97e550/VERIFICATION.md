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

# Reproducibility

Run `python3 verify.py` from the extracted file directory. It must end in `VERIFY_EQUIV_OK`. It independently enumerates all 720 label permutations, all 45 incidence flags, both triangle complexes and all eleven symmetric-group characters; equality of fixed-flag and signed-chain Lefschetz traces is checked for all permutations. It verifies that the 16-dimensional cycle character equals the Specht character indexed by (3,2,1), then checks exact constituent multiplicities of its square and the invariant dimension one.

Run `python3 verify_rips.py`. It must end in `VERIFY_OK`. This separately constructs the 30-vertex incidence graph, distance matrices, exact scale-two and scale-three flag complexes and their face counts, an acyclic matching at scale two, and boundary ranks of each scale-three join factor. Its finite calculations cover only the named graph and do not establish results for all generalized quadrangles. The proof of the equivariant theorem uses the explicit join identity, the incidence chain exact sequence and equivariant join Künneth, not mod-two rank data alone.

The independent audit has not been performed.
