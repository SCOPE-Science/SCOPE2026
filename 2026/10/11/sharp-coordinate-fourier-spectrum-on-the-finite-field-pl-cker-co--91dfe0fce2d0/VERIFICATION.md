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

# Reproducible checks

Execute `python3 checks/verify.py` from the extracted finding directory. This checker uses only Python standard-library packages.

For fields \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), it independently constructs exterior products from all ordered input pairs, checks the number of distinct bivectors and every entry of the full complex Gram matrix, and tests explicit coefficient eigenvectors. The eight full cases are \((q,m)=(2,4),(2,5),(2,6),(2,7),(3,4),(3,5),(4,4),(5,4)\), with cone cardinalities \(36,156,652,2668,261,2421,1072,3225\). It also verifies the crossover sign by exact integer arithmetic for 3,642 parameter pairs, including both sides of every proposed threshold.

Successful output begins `VERIFY_OK`. The universal theorem is proved by the text's exact Fourier count, complete Johnson decomposition, positivity argument, and factored inequality. Neither these finite checks nor this document constitutes independent certification or a proof of historical novelty.
