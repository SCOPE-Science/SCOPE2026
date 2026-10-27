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

# Verification and limits

Run `python3 verify.py` from the directory containing that standalone file. The standard-library program has no network dependency. Expected result begins `RUDIN_SHAPIRO_FOUR_PSEUDOPERIOD_PASS` and records 512 source-language factors, 33,792 closure checks, 512 distinct binary factors, 635,376 candidate quadruples, and 24 survivors.

The program derives the four-state word by substitution, verifies factor closure under the substitution, and uses that closure to justify applying finite exhaustive comparisons to *every* position of the infinite word. All qualifying tuples are compared to the included `census.tsv` ordering through the `EXPECTED` list in the code. An independent binary-digit function reproduces the substitution prefix and binary factor set; a direct nested-loop enumeration through maximum shift 32 reproduces nine survivors. The symbolic residue-class proof in `RESULT.md` is the proof for the unbounded family. Finite stress tests alone do not establish infinite correctness.

The shift-64 census makes no assertion about any tuple whose maximum shift exceeds 64. No claim of independent external certification or completeness of the entire four-pseudoperiod set is made.
