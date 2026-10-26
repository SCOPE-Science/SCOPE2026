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

# Reproducibility
Run `python3 VERIFY.py` with a standard Python 3 interpreter and no third-party packages. The script builds the actual core-plus-leaves graph, enumerates all size-minimum candidate subsets for cycle parameters 3 through 15, applies the power-domination observation process, and compares resulting counts with the theorem. In a separate enumeration of every minimum core dominating set and core-versus-leaf lift for parameters 3 through 13, it checks the cyclic-gap predicate against graph propagation. Both routes reported PASS.

# Proof and computational limits
The all-order proof is in `RESULT.md` (projection lemma, gap analysis, forcing and blocking, counting). The code only validates the stated finite range and does not certify an infinite theorem or historical priority. A full-text comparison with arXiv:2610.24214 was unavailable and remains an originality risk.
