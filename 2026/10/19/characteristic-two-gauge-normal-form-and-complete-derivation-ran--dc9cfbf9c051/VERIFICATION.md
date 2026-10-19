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

# Reproducibility of the derivation-rank formula

Run `python3 verify.py` with standard Python 3, requiring no external packages. The program implements finite-field arithmetic over \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\), constructs actual model filiform Lie-algebra derivation matrices and computes ranks by independent Gaussian elimination. It compares the full empirical rank histogram to the stated formula.

Exhaustive enumeration was performed for \(q=2\) and \(4\le n\le8\), and for \(q=4\) and \(n=4,5\); further random instances were tested for \(q=4,8\). The independent four-dimensional binary test checks the derivation identity directly on every one of the \(2^{16}\) possible linear maps. Another 960 gauge-conjugation checks use randomized even and odd polynomial data. The completed execution prints `VERIFY_OK_FILIFORM_DERIVATION_RANKS 10 configurations`.

For \((q,n)=(2,4)\), the complete rank histogram in ranks \(0,1,2,3,4\) is \((1,9,30,88,0)\). For \((q,n)=(4,5)\) it is \((1,267,948,30528,132096,98304)\). Each case sums to \(q^{2n-1}\).

These finite computations do not certify the infinite theorem or novelty. The full proof is in RESULT.md. No independent mathematical audit has yet been performed.
