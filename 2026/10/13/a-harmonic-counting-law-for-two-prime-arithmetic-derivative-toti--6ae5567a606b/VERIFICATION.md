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

# Verification details
The exact-arithmetic script `verify.py` was run with Python 3. It computed the SPF factorization of every integer through \(500000\), independently evaluated the arithmetic derivative and the Euler totient at every integer with precisely two prime factors, and compared every coincidence whose least prime is odd to the explicit congruence-and-exponent parametrization. The two sets agreed, each containing four values: \(15,1225,3993,218491\). It also independently checked the rational harmonic identities for nineteen odd primes.

The finite regression is not an infinite proof and does not measure asymptotic convergence: the distributional statement is established by the arithmetic identity, monotone inversion of \(q\log q\), and the classical prime number theorem in arithmetic progressions for each **fixed** prime modulus. No general uniform-in-modulus asymptotic or broader prime-support claim is asserted.
