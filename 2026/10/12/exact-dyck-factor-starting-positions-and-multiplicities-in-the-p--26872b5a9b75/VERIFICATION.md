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

Run `python3 verify.py` beside `certificate.json`.

The verifier independently implements the odd-part definition of the paperfolding word and the Hamming-weight formula for its Gray-code prefix heights, checking equality through \(2^{18}\) positions. For each depth \(2\le m\le12\), it enumerates **every** interval with nonnegative relative height and equal endpoint heights, then compares the entire length-to-start-position map with the theorem, not only the set of lengths.

For every \(2\le K\le12\) and \(1\le r<K\), it checks that the two canonical factors coincide only for lengths \(2\) and \(4\), compares their symbol content under eight successive modulus translations, and verifies the exact formula for the number of occurrences in dyadic prefixes.

The computation verifies finite instances; the complete infinite statement follows from the exact reflected-Gray recursion, the crossing-interval proof, and the odd-part invariance. No external mathematical certification is claimed.
