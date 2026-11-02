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

# Reproducibility and scope

Execute `python3 verify.py` with a standard Python 3 installation. This constructs and checks circular words for every alphabet size from 2 through 50. It independently computes the shortest covers by exhaustive finite-state breadth-first search for alphabet sizes 2 and 3, obtaining 12 and 24 respectively. The program checks every palindrome target, exact lengths, and the number and types of runs. Its successful terminal marker begins `VERIFY_OK:`.

These finite checks corroborate the complete symbolic proof in `RESULT.md`. Exhaustive breadth-first search for alphabets 2 and 3 is not exhaustive for all alphabets; no claim of external or independent review is made. Exact longer-alphabet lower bounds follow from the mathematical run and parity arguments, not from the finite program.
