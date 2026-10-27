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

# Verification and limits

The mathematical proof is contained in `RESULT.md`, Steps 1–4. Reproduce the finite group checks with `python CHECK.py` from the extracted directory; expected output:

`VERIFY_OK profiles=10 all_abelianization_orders_match=true`

The checker constructs the even-permutation kernel for each indicated block profile, computes its full commutator-generated subgroup, and compares the index against the closed formula. All computations use exact finite permutations and integer arithmetic; no network access, numerical tolerance or external dependency is needed.

The universal calculation is **not** inferred from these ten tests: it uses the proof that the abelianization is either that of a single alternating group or the parity-matched sign kernel, after the \(3\)-torsion from size-three/four blocks is killed by odd conjugation in another block. Independent review has not been performed. Earlier quotient and factoriality theorems are credited and not certified as original here.
