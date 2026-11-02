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

The proof is symbolic and applies to every stated parameter pair. For a computational cross-check, execute `python checker_ideals.py` and `python checker_words.py`; compare standard output with `checker_ideals_output.txt` and `checker_words_output.txt`, respectively. Both programs produced `VERIFY_OK`.

The first checker enumerates normalized subset candidates, enforces additive closure, and evaluates both semigroup colons by bounded exact membership tests for semigroups with at most thirteen gaps and multiplicity through eight. The second independently verifies the binomial genus formula, binary-word counts, and rational generating function for word lengths at most sixteen. These checks are finite; they do not certify the theorem outside tested ranges. The all-parameter proof is in `RESULT.md`. No independent mathematical audit has been performed.
