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

# Reproducibility and limits

Run `python3 verify.py`. The script uses only the Python 3 standard library and enumerates normalized nonzero matrix lines and trace-functional matrices over four finite fields. It computes square-zero/idempotent census partitions and verifies the defining operator equation directly on matrix-unit pairs, exhaustively over all candidate pairs for three configurations and all admitted pairs for two further configurations. The expected final marker is `RANK_ONE_MATRIX_RB_EXACT_CENSUS_OK 5 9055`.

The finite fields checked are orders two, three, four and five, with dimensions two and three. The general statement for arbitrary prime powers and unbounded matrix size follows from the proof in RESULT.md, not from enumeration. No independent mathematical audit has been performed.
