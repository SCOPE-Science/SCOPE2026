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
Run `python3 verify.py` (Python 3 standard library only). The script checks (1) all six normalized length-four arch patterns and forced successors for one, two, three, and four arches; (2) all 1,830 squarefree ternary words of length nineteen, with all 243 possible five-letter scattered subsequences; (3) a squarefree length-eighteen word having exactly four arches and lacking some five-letter subsequence; (4) the local long-arch restriction in every squarefree word enumerated through length nineteen. Successful output starts with `SQUAREFREE_ARCH_RIGIDITY_PASS`.

The rigorous infinite result is proved in RESULT.md using an explicit boundary-square argument. Finite enumeration is not used as a substitute for that proof. The lower density coefficient \(4/15\) is not asserted optimal. Independent audit and independent validation are not performed.
