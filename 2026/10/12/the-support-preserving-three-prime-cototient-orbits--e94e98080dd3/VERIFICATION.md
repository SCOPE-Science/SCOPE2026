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

The symbolic proof uses the elementary identities \(T(2^a3^bq^c)=2^a3^{b-1}q^{c-1}(2q+1)\), \(T(2^a3^d)=2^{a+1}3^{d-1}\), and \(T(2^v)=2^{v-1}\), valid on the stated positive exponent ranges. Oddness and coprimality of \(2q+1\) with \(q\) prove the first-step necessity. Direct induction supplies the three exact orbit segments, and their lengths add to the claimed formula.

The standalone verifier `verify.py` uses pure Python exact arithmetic, a separately implemented totient function, primality/factor checks, and complete orbit replay for the finite samples stated in the result. Expected console output is included in `verification_output.txt`. This numerical replay confirms examples and edge cases without certifying infinite quantifiers.

Scientific limitations: The theorem assumes all three initial prime exponents are strictly positive and makes no assertion about unknown prime families. No third-party or independent proof audit has been carried out.
