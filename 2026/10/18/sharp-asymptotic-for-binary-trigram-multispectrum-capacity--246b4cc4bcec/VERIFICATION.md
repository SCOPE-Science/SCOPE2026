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

# Verification of the binary trigram count

Run `python3 verify.py` in a directory containing the bundled file. It needs only the Python standard library. The program compares the **sets** of 8-dimensional trigram-multiplicity vectors from exhaustive enumeration of all \(2^n\) words and a separate de Bruijn-state dynamic program for \(3\le n\le15\). It continues dynamic-programming spectrum counts through \(n=24\), and independently checks the balanced-flow generating-function coefficients through edge total \(m=60\) against a finite, nonnegative integer summation.

Observed completion markers: `EXHAUSTIVE_DIRECT_VS_DP_OK lengths=3..15`, `BALANCED_GENERATING_FUNCTION_OK total_triples=0..60`, and `VERIFICATION_OK`. For example, the exact multispectrum counts at lengths \(n=16,18,20,23\) are \(2449,3971,6123,10876\). This is finite evidence only: the assertion \(Q_3(n)=\frac{13}{288}n^4+O(n^3)\) for all sufficiently large \(n\) uses the full proof in RESULT.md (especially Euler connectivity, the sandwich injection, and the coefficient asymptotic). No independent audit has been carried out.
