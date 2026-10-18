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

Run `python3 verify.py` using Python 3.8 or newer. No third-party packages or external inputs are required. The script enumerates forbidden three-edge matchings using all six-vertex subsets and all perfect pairings, enumerates every allowed face in the chain ranges, constructs each actual mod-two boundary column, checks every relevant boundary-square identity, and calculates exact pivot ranks. Its assertions compare all face counts, forbidden matching counts, ranks, and both fourth- and fifth-degree dimensions with the stated results. The successful observed terminal line was `VERIFY_OK`.

The check is a complete finite matrix computation over \(\mathbb F_2\); it does not establish integral torsion or a homotopy classification. It uses no precomputed published rank table.
