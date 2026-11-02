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

# Reproducible checks and limits

The accompanying `verify.py` uses only the Python standard library. Run `python verify.py`; success prints `VERIFY_OK`. Its independent constructions enumerate the full and pointed semigroups from the multiplication table for six base groups: cyclic orders \(1\), \(2\), \(3\), \(4\), the Klein four-group, and the nonabelian symmetric group \(S_3\). For every group it constructs all standard group automorphisms, all candidate expansion automorphisms, checks that their numbers match the proposed exact formulas, checks their products for **all** pairs of elements, and checks inner-conjugation and pointed-subsemigroup orbit formulas.

When an expansion has at most eight elements, the checker also enumerates every permutation of its underlying set and tests the complete two-variable homomorphism identity, not merely the proposed family. This exhaustive condition applies to the full and pointed expansions of the trivial group, the full and pointed expansions of the order-two cyclic group, and the pointed expansion of the order-three cyclic group. For larger expansions (up to 384 elements in these tests), direct checking covers the explicitly constructed candidates but is not an exhaustive automorphism census. The proof's intrinsic reconstruction establishes exhaustiveness for arbitrary finite groups.

The executable is an ordinary computational corroboration, not independent verification and not a formal proof. The proof relies only on the intrinsic definability of units, idempotents, semilattice atoms, inverse-semigroup range idempotents, and the displayed multiplication. The complete 1990 Fountain–Gomes source was not available for a historical priority comparison. Self-review found the mathematical steps internally consistent; independent audit has not been performed.
