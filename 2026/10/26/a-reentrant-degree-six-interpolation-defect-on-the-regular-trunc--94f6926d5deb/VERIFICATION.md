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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3.9 or newer. No third-party packages or remote services are needed. The program constructs the ordered twelve-point configuration and tests the Legendre Gram matrices over the prime field of order \(1000000007\). It asserts ranks \(1,3,5,7,9,11,9\) for degrees \(0\) through \(6\) and rank \(12\) separately for every integer degree \(7\) through \(324\). The three exact degree-six null vectors are checked using rational arithmetic, not modular arithmetic alone, and are checked for independence. The deformed point orbit at parameter \(a=2\) has full degree-six modular rank. Rational squared-sine and row-bound checks verify the numerical premises for the analytic high-degree proof. Expected deterministic output is `certificate.json`.

A nonzero field minor is a rigorous nonzero rational minor because all exact Gram entries have denominators invertible modulo the declared prime; the implementation explicitly checks the prime. The infinite range \(\ell\ge325\) is proved by the Legendre integral inequality and Gershgorin's theorem in `RESULT.md`, not by any finite experiment. No independent mathematical audit or external validation was performed. The calculation does not measure floating-point stability, spectral conditioning, or behavior at arbitrary deformation parameters.
