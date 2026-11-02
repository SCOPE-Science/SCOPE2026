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

# Verification

Run `python3 checks/verify.py` with Python 3. The checker enumerates the complete prime-square frequency tables for primes \(5,7,11\), constructs exact integer exponent multiplicities for the quartic graph, and tests divisibility by \(\Phi_{p^2}\). It independently verifies the primitive derivative criterion, imprimitive permutation criterion, and predicted convolution ranks. It also checks that the two exceptional nonzero quartic-linear permutation ratios occur at \(p=7\) and not at \(13,17,19\). No numerical tolerance is used. The analytic proof, together with Masuda–Zieve's prime bound and the finite \(5,7,11,13\) field census, establishes all primes; numerical experiments alone would not. Independent validation has not been performed.
