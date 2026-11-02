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

The classification follows from the structural proof in `RESULT.md`; finite tests do not substitute for the all-length argument. Execute `python3 verification/verify.py` after extraction of the files in this package. The program uses only Python standard-library modules and independently builds factor-to-position coverage masks, then solves the minimum problem by checking position pairs and triples. Exhaustive cases cover every nonempty binary word through length fifteen (65,534 instances). It checks each fixed-weight class and the total counts at every tested length, as well as 299 ordinary generating-function coefficients.

Observed output terminates with `VERIFY_OK exhaustive_words=65534 coefficients_through_n=299`. The test does not inspect or make any claim about larger alphabets, circular factors, or factors longer than two. Independent audit is not performed.
