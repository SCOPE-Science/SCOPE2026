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

# Reproducibility

Run `python3 verify.py` using Python 3 and no third-party dependencies. The program checks the predicted first index against independently accumulated modular residues, verifies the unique earlier index at that first collision, and separately checks all candidate earlier indices through the exact factorized divisibility relation. It checks primes below 50, powers through exponent 10, and all cases whose predicted first-collision index is at most 15,000.

Observed output from execution of the supplied code:

`VERIFY_OK prime_powers=94 residues_checked=108348 unique_first_pairs=94`

The computation covers only 94 finite prime-power inputs. Correctness for all primes and exponents follows from the valuation-and-parity proof in `RESULT.md`; no machine formalization or independent external validation has been performed.
