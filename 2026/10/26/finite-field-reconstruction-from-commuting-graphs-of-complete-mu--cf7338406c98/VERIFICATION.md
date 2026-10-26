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

Run `python3 verify.py` from the directory containing this file and the script, using Python 3.9 or later. No third-party package or network access is needed. Expected terminal line: `VERIFY_OK 12 independent bracket cases`.

The verifier generates quotient vectors over small prime fields, constructs each edge-coordinate bracket directly, builds the entire commuting relation between nonzero quotient vectors, and checks the resulting component sizes against the stated clique formula. It also enumerates the kernel of each adjoint map from bracket vanishing and reconstructs the field order and part-size multiset from graph sizes. Test configurations include three or four total vertex generators and both singleton and larger part sizes.

For an arbitrary odd prime power, the theorem is established by the tensor centralizer argument and integer inverse-reconstruction proof in `RESULT.md`; the finite prime-field tests are only corroboration. The code does not purport to establish uniqueness among arbitrary Lie algebras or to exhaust the literature. No independent audit has been performed.
