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

The standalone `verify.py` was executed successfully with Python 3. Its stdout is recorded verbatim in `verification_output.txt`. The program validates direct and symbolic steps, a finite candidate-maxima box, and fixed families. Its range is finite and does not constitute a proof.

The proof covers arbitrary positive integers and all eligible primes via exact divisibility and orbit-maximality arguments. The premise that only supported-prime factors can occur in derivative coefficients on a periodic orbit is proved by monotonicity of outside-prime valuations. A key boundary is \(k<p\), forced by \(p^k<q\le p^p\). All other primes and all other periods are quantified symbolically.
