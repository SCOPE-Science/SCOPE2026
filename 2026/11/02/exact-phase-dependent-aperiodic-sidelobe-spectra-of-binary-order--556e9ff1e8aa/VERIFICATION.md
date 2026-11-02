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

# Reproduction and limits

From this directory, run `python3 verify_psl.py` with Python 3.10+ and no dependencies outside the standard library. The script exhausts all \(65,536\) complementary binary feedback tables, retains the \(2,048\) tables inducing a single cycle on the \(32\) five-bit states, and independently enumerates the same cycles as Euler tours on the four-bit de Bruijn graph. It compares the generated sets exactly.

For each of the \(2,048\) cycles it checks every one of the \(32\) roots and each nonzero aperiodic lag from \(1\) through \(31\). A sign-product computation is cross-checked against the integer mismatch identity \(A(t)=(32-t)-2D(t)\). The checker asserts the exact \(65,536\)-root and \(2,048\)-cycle histograms, totals, and extremal levels. It was executed from the package path and passed.

The search-space completeness and independence of the two constructions are justified in `RESULT.md`; test output alone is not relied on as a proof. All counts are integers without rounding, sampling, or a cutoff. The investigation does not prove a higher-order formula or historical priority. No independent external audit has been performed.
