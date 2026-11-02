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

# Reproduction checks

Run `python3 verify_quotient.py` with Python 3 and SymPy installed. The checker exits without exception and ends with `PRYM_DECK_CUBIC_QUOTIENT_AND_A3_2A1_PASS`.

The checker verifies the exact \(a,b\)-coordinate conjugacy, the involution squared, invariants, invariant surface equation, source degeneracy divisors and their norm identity, the homogeneous cubic's four partial derivatives, both affine singular points, the unique singular point at infinity, the exact \(A_3\) completing-square identity, doubled boundary substitution and length-four boundary contact identity. It additionally enumerates all admitted coefficient points over \(\mathbb F_7\) and \(\mathbb F_{13}\) and proves directly in these finite enumerations that every invariant fiber has two points. The complete invariant ring, global lack of further singularities, and etale quotient rely on the arguments in `RESULT.md`, not finite-field enumeration.

The verification covers the displayed **coefficient-level quotient**. It neither compares all moduli identifications nor constructs a moduli-stack compactification, proves modular uniqueness, or constitutes independent scientific validation. The projective normalization construction is a standard finite-normalization argument rather than a separately implemented normalization algorithm.
