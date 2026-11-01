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
Run `python3 verify_pm_dihedral.py` (standard library only). The checker directly enumerates perfect matchings in six finite Möbius ladders, constructs every corresponding independent tile set, and verifies equality of facets, rotation/reflection on tile pairs, the signed action on the two exceptional cells, remaining compatible spokes in the contractible-core cover, and complete mod-two homology for the first four tested widths. Expected final line: `VERIFY_OK`.

# Scientific scope
The argument for every even width is the direct combinatorial and homotopical proof in `RESULT.md`. The finite enumerations are consistency checks only. Relative cellular generators are not incorrectly treated as simplicial cycles in the absolute chain complex; the pair long exact sequence supplies their unique integral preimages. The exact equivalence and integral basis do not require black-box integer Smith-normal-form computations.

Independent mathematical validation has not been performed.
