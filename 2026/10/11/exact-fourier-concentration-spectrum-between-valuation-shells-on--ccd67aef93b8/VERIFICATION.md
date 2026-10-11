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

# Verification of the finite-shell concentration theorem

The exact entry formula is the character sum over \(p^sG\) minus the sum over \(p^{s+1}G\). That independently yields the block forms \(I_p-J_p/p\), \(I_{p-1}-J_{p-1}/p\), and a positive scalar multiple of an all-ones matrix in the three cases. Their eigenspaces prove the universal result, including the perfect-localization condition and all maximizing vectors.

For reproducibility, run `python3 verify_shell_spectrum.py` (Python 3, NumPy, SymPy). The packaged executable computes rational matrix entries for a finite range of prime powers; it asserts trace and squared-trace identities, checks the exact annihilating polynomial when matrix size is at most 36, and independently reconstructs sampled matrices by the complex exponential DFT. Its observed result was:

`VERIFY_OK exact_case_count=137 exact_matrix_dimensions_sum=4782 dft_cases=96 polynomial_identity_for_m_le_36=PASS trace_trace2=PASS`

Limits: the computer test is not exhaustive over primes or dimensions; its DFT calculations use floating point with a stated tolerance, while its entry matrices and algebraic assertions use exact arithmetic. The mathematical proof, not the finite test, establishes universal quantifiers. No independent audit or external certification is asserted.
