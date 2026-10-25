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

Run `python3 verify_kneser_character.py`. It uses the Python standard library only, with no network requirement.

Checks performed: invariant pair-orbit sums and signed augmented Lefschetz characters for each of 38 conjugacy-class representatives in symmetric groups of degrees four through seven; a separate exhaustive simplex-subset enumeration and oriented-sign computation for all class representatives in degrees four through six; and the two rational constituent character formulas and dimension identities. It emitted the marker `KNESER_NEIGHBORHOOD_SYMMETRY_CHARACTER_VERIFIED 38 orbit_trace_conjugacy_classes direct_simplicial_to_n6 specht_trace_identity`.

The finite experiments do not certify all values of \(n\), establish integral lattice equivalence, or provide an independent mathematical audit. The universal theorem is proved by the finite-group chain trace and Möbius calculation in `RESULT.md`, together with the published degree-concentration theorem.
