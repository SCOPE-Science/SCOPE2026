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

# Verification record

The mathematical proof uses the integral \(7\)-adic binomial interpolation of \(64^t\) and \(729^t\), checks every exponential residue class modulo \(6\), computes the reduced interpolation polynomials, identifies all simple roots explicitly, and counts the residue classes in the common exponent period. These are unrestricted symbolic checks for the stated theorem.

From the actual package file `verify.py`, run `python3 verify.py` (Python 3 standard library only). A successful execution printed the following exact markers, retained in `verification_output.txt`:

```
exact_valuations_indices_1_to_5000=PASS
period_root_counts_k_1_to_5=2_8_15_15_15_PASS
published_exceptional_subfamily_indices_j_0_to_9=PASS
reduced_binomial_coefficients=PASS
VERIFY_OK
```

The script uses modular exponentiation with a large enough modulus to distinguish each tested valuation. It exhaustively checks the stated index ranges and complete periods at the five listed levels, but finite checks alone do not establish the theorem for all exponents or all prime powers. The proof, not the test log, provides unrestricted validity.
