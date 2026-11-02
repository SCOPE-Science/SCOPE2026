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

# Reproducibility and verification limits

Run `python3 verify.py` from the extracted artifact directory to reproduce `verification_output.txt`. The code checks the actual recurrence constructing the words, exact lengths, absence of the forbidden factor `00`, and count inequalities on nine word patterns through level 21. It independently checks small-level subsequence embeddings in periodic templates and the exact deleted-position count. These observations are finite checks only.

The infinite cylinder-frequency convergence follows from a summable error recurrence and a shrinking-prefix recurrence; all-word positivity follows from recurrence plus a quantitative survivor argument; entropy zero follows from the deletion-template entropy bound. Those infinite deductions require the mathematical proof in RESULT.md and are not certified by bounded enumeration. The direct literature comparison is not an independent publication-priority certification.
