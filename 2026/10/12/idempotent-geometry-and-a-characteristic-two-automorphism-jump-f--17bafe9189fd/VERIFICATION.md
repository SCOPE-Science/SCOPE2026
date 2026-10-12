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

The formal proof is the four-part argument in `RESULT.md`. In particular, the explicit multiplication table has four independent right-annihilator tests, and the character/intertwining arguments are essential completeness steps not obtained by enumeration.

Run `python checker.py` using a standard Python 3 interpreter. It checks all idempotents and **all invertible algebra homomorphisms** over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), giving respectively \((8,32),(7,8),(13,32)\), each pair counting nonzero idempotents and automorphisms. It also directly enumerates all \(256\) coefficient vectors over \(\mathbb F_4\), finding \(33\) idempotents including zero, and checks all \(512\) distinct constructed automorphisms from the normal form. The latter GF4 test is not a full brute-force enumeration of all invertible four-by-four matrices.

Expected final stdout marker: `VERIFY_OK`. These calculations independently corroborate finite examples; they are not an infinite proof and do not constitute independent scientific audit. The complete arbitrary-field assertion is derived algebraically.
