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

# Reproducible finite checks

Execute `python3 verify.py` in a directory containing the extracted `verify.py`. No packages beyond the standard library are required. The code embeds the exact witness from `witness.txt`, checks the 243 distinct length-five cyclic factors, balanced symbol totals, pairwise prefix ranges, and each of the 59,049 circular starting-position/length factors. The mathematical universal lower bound is proved separately in RESULT.md from the factor 00000. These finite calculations constitute exhaustive verification of this explicit finite witness but not an independent audit or a general n theorem.
