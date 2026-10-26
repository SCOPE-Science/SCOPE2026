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

# Verification instructions and limits

Execute `python3 check_implication_spectrum.py` from the directory containing the extracted files. The program has no nonstandard dependencies.

Expected final output:

`IMPLICATION_EQUATIONAL_SPECTRUM_EXACT_OK 651 constructive_checks clone_sizes [2, 6, 38, 942]`

The program independently checks three finite components: every constructed term truth count for one through eight variables; every constructed equation agreement count for two through eight variables; and complete closure of the implication term clone at arities one through four, followed by all pairwise agreement counts of the closed clones. The closure is exhaustive at those particular arities because it begins with all projections, closes under all applications of the only primitive operation, and terminates when no new functions are generated.

The Python results are finite evidence only. The universal spectrum, the sharp lower bound and the general arity quantifiers require the structural induction and four construction families proved in `RESULT.md`. No independent audit, formal-proof certification or priority certification is claimed.
