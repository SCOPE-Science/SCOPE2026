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

# Reproduction and boundaries
The graph has one common edge and four private edges per page. `checks/pentabook_verify.py` builds the full face poset, applies the two-stage augmented Morse matching, checks the partner relation and the \(n\) critical faces, and topologically sorts every arrow of the oriented Hasse diagram for \(1\le n\le7\), including 70,713 faces for seven pages. `checks/pentabook_character.py` checks the signed-orbit calculation with independent invariant-face enumeration for all \(2n!\) automorphisms for \(1\le n\le5\). Run `python3 checks/pentabook_verify.py` and `python3 checks/pentabook_character.py` from the containing directory; Python standard library only. The expected output prefixes are `MATCHING_OK` (seven lines) and `CHAR_OK` (five lines).

The actual completed runs returned both expected prefixes without assertion failures. Finite checks do not establish the all-parameter theorem: that conclusion uses the explicit blocker-monotone acyclicity argument, the signed-orbit classifications for all page cycles, and rational character theory. No integral group module, equivariant wedge, or canonical equivariant collapse was tested or asserted.
