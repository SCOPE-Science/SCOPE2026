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
Run `python3 verify.py` with a standard Python 3 interpreter. The checker uses no external packages, internet access, or scientific input files.

The recursive dynamic enumeration treats agent labels as distinct and tabulates all feasible clique partitions by their number of mixed three-agent coalitions. On 715 nontrivial class-size profiles with each size at most eight and total size at most 21, it compares maximum triplet count and optimal-partition multiplicity with the stated formulas.

An independent unrestricted set-partition recursion computes literal utility values including every within-class penalty. For each individually rational partition it computes the exact integer product of utilities. This check covers 224,935 set partitions over 161 role-size profiles with total population between two and eight. Both modes reproduce the claimed values and multiplicities. Standard output terminates with `VERIFY_OK` and `BRUTE_OK`.

The checker is finite and is not a proof for arbitrarily large populations; the complete proof is in RESULT.md. In the zero-welfare regime the theorem does not enumerate all optimizers. No independent scientific audit has been performed.
