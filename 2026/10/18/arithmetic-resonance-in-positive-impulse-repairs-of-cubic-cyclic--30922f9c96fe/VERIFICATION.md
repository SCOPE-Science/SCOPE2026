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

# Verification of the arithmetic-resonance theorem

**Analytic:** The full prime-family claim follows from the exact ambiguity expansion, evaluation of nondegenerate quadratic Gauss sums, and the impossibility of \(i\omega^k\) being real for odd prime \(p\). The modular exponent \(E\) is derived algebraically; equality testing requires no asymptotic or floating-point assumption.

**Executable:** Run `python3 verification.py` from the same directory. The script uses only the Python standard library. It tests all phase-space positions at nine chosen primes, checks the exact integer-character/cosine-sign criterion for \(p=5,13,17\), reproduces exceptional positive amplitudes, and verifies the four actual numerical zeros at each of the two \(p=17\) resonances.

**Observed output:** `VERIFY_OK 4355 finite comparisons; p=5,7,11,13,17,19,23,29,37; p=17 has two resonant amplitudes, each with four ambiguity zeros`.

**Unproved computational limits:** The checker does not enumerate all primes, and floating-point near-zero tests are not certificates of exact vanishing. Exact vanishing, the all-prime assertion, and the rank-defect formula are justified by the written analytic argument. Historical priority and independent audit are not established by this script.
