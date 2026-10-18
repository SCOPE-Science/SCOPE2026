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
# Verification record

The source `verify.py` (standard Python 3 library) is part of this package. It enumerates all labelled simple core graphs on 1–4 vertices with bundle sizes 1 or 2; it additionally enumerates all cores on 1–3 vertices with bundle sizes 1, 2, or 3. The exhaustive procedure tests all vertex subsets, computes open-neighborhood traces for all omitted vertices, and independently checks domination, the complete location-domination polynomial, complementary DLDS partition counts, two-LD partition counts, and the minimum domination number.

Completed output:

`VERIFY_OK graphs=1335 vertex_subsets=1518440 full_LD_polynomial=pass DLDS_partition_count=pass two_LD_partition_count=pass domination_number=pass`

Mathematical generality is supported by the explicit all-graph proof in `RESULT.md`. Finite exhaustive testing covers only the stated parameter ranges and does not establish infinite correctness, bibliographic originality, independent validation, or formal mechanized certification.
