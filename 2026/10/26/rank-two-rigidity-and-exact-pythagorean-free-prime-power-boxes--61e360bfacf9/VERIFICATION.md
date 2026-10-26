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

# Verification of the finite certificate and theoretical scope

Run `python3 verify.py` using Python 3.8 or later. It uses only the Python standard library, exact integers, and `math.isqrt`.

The script enumerates complete Pythagorean-pair edge sets for every distinct prime pair from \(\{2,3,5,7,11\}\) and for square exponent cutoffs \(1\le n\le9\). It checks equality with the classification, not merely that the predicted edges exist. For \(1\le n\le120\), graph components independently produce the stated four-case formula. It additionally searches all subsets of the first four square exponent boxes to verify the computed graph independence number. The expected final output is `CERTIFICATE_OK distinct_prime_pairs=10 supports_and_sizes=90 square_cutoffs=120 brute_independence_cutoffs=4`.

The infinite theorem does **not** follow from the finite computations: it follows from the primitive-pair lemma, the exact exponent-edge classification and the path counting proof. The verifier neither checks unrelated prime supports beyond those listed nor certifies prior-work noncoverage. Independent audit and independent mathematical validation have not been performed.
