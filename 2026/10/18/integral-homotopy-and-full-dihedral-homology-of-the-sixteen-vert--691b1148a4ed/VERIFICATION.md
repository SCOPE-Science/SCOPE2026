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

Run `python3 verify.py` in a clean directory; Python 3 standard library suffices. This regenerates all graph edges and simplices. It constructs and topologically sorts the full oriented matched Hasse graph (all 11,393 nonempty simplices), checks exactly 5,690 pairs, and computes the signed integer cellular boundary between five critical four-cells and seven critical five-cells. It validates a determinant of -1 for a 3-by-3 minor and zeros for all 4-by-4 minors, proving the three unit Smith factors.

It independently verifies mod-two simplicial boundary ranks, signed Lefschetz traces for all 32 dihedral automorphisms, rotation eigenspace homology over the field with 97 elements, and reflection eigenspace homology over the field with 101 elements. Torsion-freeness and homotopy equivalence rely on the integral Morse argument, not on field tests. The final verifier line must be `VERIFY_OK_MOBIUS16_ORDINARY_MATCHING_COMPLEX`.

No independent audit or external certificate is asserted.
