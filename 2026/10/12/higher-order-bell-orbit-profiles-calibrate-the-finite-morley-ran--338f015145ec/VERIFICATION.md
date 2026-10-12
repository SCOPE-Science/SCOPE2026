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
The claim has an ordinary proof from homogeneity and nested set partitions. The accompanying `verification.py` is a finite consistency check.

It performs three computational checks: direct restricted-growth-string enumeration of set partitions and their coarsening chains; dynamic computation using the Stirling transform; and a separate comparison showing that the equality-pattern transform of the rank-\(r\) injective row equals the rank-\((r+1)\) injective row.

The direct enumeration is run for ranks \(1\) through \(4\) and tuple lengths through \(7\). Recurrence and shift checks continue through tuple length \(10\). These computations do not certify the infinite theorem by exhaustion; the infinite proof is the orbit/partition bijection plus the quantifier-elimination argument for Morley rank.
