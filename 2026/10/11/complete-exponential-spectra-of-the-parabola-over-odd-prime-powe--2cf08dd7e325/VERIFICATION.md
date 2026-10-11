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

# Verification of the quadratic ring spectral classification

Run `python3 check_spectra.py` using only the Python standard library. The checker computes exact root-of-unity cancellation by coefficient divisibility by \(\Phi_{p^k}\), independently of the valuation criterion being tested. It verifies every coefficient pair for \((p,k)=(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)\), a total of \(1518\) pairs. It enumerates all \(89\) digit-contraction basis sets in the small cases, samples \(64\) more at larger moduli, and independently backtracks over all valid frequency assignments to recover exactly \(81\) spectra for \((3,2)\) and \(5\) spectra for \((5,1)\).

Observed output:

`VERIFY_OK exact_cyclotomic_zero_pairs=1518 all_constructed_spectra=89 sampled_deeper_spectra=64 digit_count=PASS independent_exhaustive_spectrum_census=PASS all_orthogonality=PASS`

The proof in `RESULT.md` independently covers every odd prime and every positive exponent. The finite checker does not establish completeness at untested moduli, historical novelty, or independent audit.
