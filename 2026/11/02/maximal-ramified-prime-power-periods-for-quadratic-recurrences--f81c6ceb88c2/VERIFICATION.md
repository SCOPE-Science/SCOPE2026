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

# Reproducibility checks
Run `python3 verify.py` with Python 3; no nonstandard package is required. The script evaluates exact matrix powers over \(\mathbb Z/p^k\mathbb Z\), for each \(p=5,7,11,13\), each coefficient pair modulo \(p^2\) satisfying the ramified and invertible hypotheses (\(3632\) pairs in total), and \(k=1,2,3\). It verifies the predicted order and excludes divisors corresponding to all prime factors of the order. It separately tests the exceptional \(p=3\) example.

Expected output: `VERIFY_OK primes=5,7,11,13 coefficient_lifts=3632 levels=1,2,3 p3_exception=yes`.

These checks cover the specified finite ranges only. The all-primes and all-powers claim is established by the independent binomial-matrix proof. The factor obstruction is also a symbolic proof, not inferred from these experiments. No independent audit has been performed.
