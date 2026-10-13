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

# Reproducible verification

Run the standalone `verify.py` with Python 3 from the same directory as this file. It needs only the standard library. The included `verifier_output.txt` records the observed output from the packaged script.

The code computes coefficients of the four-colored odd-part generating product modulo eight independently of the proof, with one unrestricted-color factor for each even part and four for each odd part. It verifies all \(600\) positive odd indices through \(1200\) against the divisor character sum. Separately it evaluates the signed integer solutions to \(x^2+3y^2=12n+1\) and the pentagonal-plus-positive-square representation count at every tested index, confirming the required normalization. Exact integer coefficients through \(18\) give a small independent control for modular arithmetic.

Passing finite tests does not certify infinite correctness, originality, asymptotic density, or independent validation. The infinite claims follow from the written proof, including explicit formal-series reductions, exact norm representations, and the classical theorem on primes in arithmetic progressions.
