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

Execute `python3 verify_cosine.py` with the standard Python library. The program checks the defining formula, implicit threshold, analytical two-step derivative identity, numerical root counts across five choices of \(a\), and the fold separation/multiplier asymptotics at two positive offsets for each choice. It reports `PASS` when all finite assertions hold. The complete parametric theorem is proved in `RESULT.md`; no finite sampling is claimed to certify continuous-parameter uniqueness.

The publication-priority comparison relies on the original full-text paper and additional indexed records. A 2024 related accepted manuscript was listed as open access, but the attempted document retrieval was denied; its abstract and the available preview were inspected. Independent mathematical and publication-priority audits have not been performed.
