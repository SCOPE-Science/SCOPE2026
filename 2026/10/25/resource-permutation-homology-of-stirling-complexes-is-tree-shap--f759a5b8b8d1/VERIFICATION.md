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

# Reproducibility and limits

The embedded `stirling_resource_character_checker.py` is standalone Python requiring only the standard library. Run with `python3 stirling_resource_character_checker.py`. Its expected final line is `STIRLING_RESOURCE_CHARACTERS_OK`.

The program explicitly enumerates all cubical cells of the Stirling complex and all permutations for the eight parameter pairs \((m,n)=(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(4,5)\). For every permutation it independently evaluates (i) the signed cellular Lefschetz number from its fixed cells, (ii) the predicted homological character, and (iii) the inclusion–exclusion formula for the same Lefschetz number. It confirms that the average of the character is zero. For \(n=m\) it checks the reduced degree-zero rank.

The complete infinite-family assertion is justified by the written cellular trace proof and the cited nonequivariant sphere-wedge theorem. No finite enumeration certifies an infinite claim. This verification is not an independent audit; no independent scientific certification is asserted.
