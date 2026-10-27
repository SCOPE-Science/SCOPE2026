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

# Reproducible checks and limits

Run `python3 verify.py` from the directory containing the checker. It uses only Python's standard library. It verifies the 34 listed blocks, uniqueness of all 102 pairs, the point-degree sequence, one explicit partial parallel class of size four, and all \(\binom{34}{5}=278256\) five-block subfamilies. Expected output is embedded in `verification_output.txt`.

Because every five-block subfamily is inspected, the finite check establishes that this displayed family has no five pairwise disjoint blocks. The explicit four-block witness establishes the reverse inequality, so its maximum partial parallel class is exactly four. The general upper bound of 37 follows from the point-degree count in RESULT.md. No exact upper bound below 37, isomorphism classification, independent audit, or independent validation is claimed.
