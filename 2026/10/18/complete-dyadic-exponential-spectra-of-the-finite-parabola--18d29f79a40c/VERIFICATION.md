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

# Verification
The theorem is proved for every \(k\ge1\) by an exact Fourier-sum recurrence, parity-eigenspace decomposition, and bijective recursive enumeration. The checker is a standalone Python 3 program using exact integer exponent counts and the cyclotomic factor \(X^{2^{k-1}}+1\) to decide cancellation. It does not reuse the analytic Fourier-zero recurrence for its cancellation decisions. Execute `python3 check_dyadic.py`. The supplied output contains the 21,844 exhaustive pairwise Fourier comparisons for levels one through seven, and the 16,452 maximal cliques across the complete orthogonality graphs at levels one, two, and three. Those computations corroborate but do not independently certify the all-exponent induction. The normalization is \(q^{-1/2}\) for each frequency vector. Every equality and dimension count used in the proof is explicit. No independent scientific audit has been performed.
