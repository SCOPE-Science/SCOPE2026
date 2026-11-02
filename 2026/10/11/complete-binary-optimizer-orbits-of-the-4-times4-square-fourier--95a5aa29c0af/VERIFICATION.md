---
{
  "schema_version": 1,
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ],
    "status": "passed"
  }
}
---

# Verification notes

The packaged `checker.py` exhaustively computes all 8192 states normalized by the free sign-modulation action. It checks two exact moment identities and the two sixteen-member symmetry orbits. A separate full-domain enumeration has also independently checked all 65536 arrays, and a second convolution formula on all 8192 normalized representatives. Both agree on minimum moment 304, 32 total minimizers, second moment 336, and orthogonal/oblique dominant-lobe orbit invariants.

This is exhaustive finite arithmetic for the stated binary 4-by-4 aperture. No formal proof-assistant verification or expert attestation is claimed. The known scalar merit factor is not presented as a new numerical bound; historical optimizer-classification priority remains qualified by inaccessible originals. A completed scientific assessment does not constitute a proof-assistant proof or an expert attestation.
