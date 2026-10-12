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

The symbolic proof handles every integer index, every aperiodic binary sequence and every automorphism of the complete shift graph. The explicit noninjective witnesses are a singleton one, a singleton zero, and a binary step, together with a reflection axis for each possible pair collision. The standalone `verify_two_block.py` iterates over all four-color pair maps and confirms their witness equalities on a finite test range, then checks the exact labeled injection counts for palettes of sizes 1--4. It prints `VERIFY_OK` on success. This computation is only a sanity check; the infinite claim relies on the displayed symbolic proof. The 2026 source's abstract and publication date were independently consulted, but its full preprint was not available to inspect; originality retains the corresponding literature-overlap risk. No independent audit has been performed.
