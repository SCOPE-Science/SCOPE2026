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

# Reproduction and limits

Run `python check_inq_kite.py` in a standard Python 3 environment. The checker enumerates actual states and substates of the explicit two-world neighborhood frame and compares formula truth for two valuations, checks the singleton-collapse of the existential modality through bounded generated formulas, and tests the one-world elimination identity on both neighborhood families. It reports 22,584 successful assertion groups.

The proof's universal quantification over formula syntax is justified by structural induction, not by bounded tests. The first public source date is the initial public submission of arXiv:2411.04031 on November 6, 2024. The originality assessment examined the original author's explicit open problem and neighboring propositions; independently duplicated work cannot be ruled out.
