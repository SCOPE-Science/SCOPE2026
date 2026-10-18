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

The proof reduces the Hilbert function to disconnected-support counts for regular bipartite multigraphs. The coefficients \(16,18,72,24\) arise from exhaustive integer partitions of four into balanced connected support blocks. A self-contained standard-library program in `verify.py` independently enumerates every four-by-four table with equal margins \(d=1,2,3,4\), checks graph connectedness and matches the polynomial exactly. It also checks the rational series numerator by finite differences. The program prints `VERIFY_OK` on success. No claim of exhaustive enumeration for all degrees is made; all-degree validity is proved combinatorially. No independent third-party audit has been performed.
