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

# Verification and limitations

Run `python3 verify.py` in the directory containing this file. The checker uses only Python's standard library. It builds literal incidence-algebra products, enumerates actual idempotents, checks ordered pairwise-commuting pairs, and compares them with independent orbit-color sums. It includes chain and two-level examples, an automorphism swapping both sides of a four-element two-level poset, finite prime fields of orders two and three, and crown rotations for three to five index positions. Expected terminator: `VERIFY_OK_EQUIVARIANT_INCIDENCE_IDEMPOTENTS`.

The component-dimension conclusion follows from the same algebraic-group orbit and stabilizer calculation; this geometric argument was reviewed symbolically, not certified by finite-field enumeration. The proof's decisive checks are structural: an explicit simultaneous conjugator, stabilizer coefficient counts, a cycle-multigraph quotient and the two eigenvalues of its edge transfer matrix. The computational suite is finite and cannot prove the unbounded theorem. No external expert review or independent audit has taken place. Priority risk remains for prior simultaneous-idempotent lifting and equivariant coloring interpretations.
