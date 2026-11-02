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

# Reproducibility and verification

Run `python3 verify.py` with the standard library of Python 3. The deterministic checker constructs the exact directed overlap graphs on all length-three vertices over alphabets of sizes two, three and four, and forms the out-Laplacian directly from every admissible four-letter edge.

It checks vertex degrees and the total admissible-edge count, computes exact integer cofactors using fraction-free Bareiss elimination, and compares them to the formula in `RESULT.md`. The rooted in-arborescence counts are \(4\), \(10{,}331{,}213{,}040\), and \(57{,}757{,}330{,}472{,}898{,}702{,}105{,}693{,}539{,}794{,}944{,}000\) for the three alphabets respectively. For two letters it independently enumerates every Euler circuit after fixing the one occurrence of a specified four-letter edge, obtaining exactly four rotation classes. The checker also verifies the higher-order imbalance witness for every vertex length from four through 150.

Expected terminating output is `VERIFY_OK`. These are finite exact checks only; the all-alphabet enumeration and infinite-order obstruction are proved by the determinant identities and explicit vertex construction in `RESULT.md`. No independent audit has been conducted.
