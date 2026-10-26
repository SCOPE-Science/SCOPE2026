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

The result was checked using the included standalone Python standard-library program `verify_thue_topgap.py`. The executable regenerated the exact length-four, length-six and length-eight factor sets from four length-64 morphic block pairs and agreed with an additional prefix extraction. The 24 and 720 possible coordinate permutations were each exhausted at their respective lengths. The supplied length-eight involution was tested directly: its order is two and it has exactly one two-element class meeting the factor set. Output stored in `verify_thue_topgap_output.txt` reproduces the observed counts. Logical completion relies on the two-block factor lemma and cyclic-generator reduction proved in RESULT.md, not on finite prefix sampling. No external scientific audit has been performed.
