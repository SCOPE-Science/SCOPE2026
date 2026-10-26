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

# Verification evidence and limits

Run `python3 verify.py` with a standard Python 3 interpreter. It completed locally with `VERIFY_OK`.

The exact checker performs independent projective-fiber and character-trace counts for all \(32\) quadratic-twist labels over \(\mathbf F_7\), direct enumerations over \(\mathbf F_{49}\), and untwisted elliptic/genus-two quotient point counts. A third check enumerates the actual homogeneous complete intersection over \(\mathbf F_7\) for all \(32\) labels, independently of the base-line parameter. It verifies the genus-two numerator using its first two extension counts and checks that every elliptic quotient has trace in \(\{0,4,-4\}\) with the prescribed multiplicities.

The reusable verification code has no network dependencies or imported scientific packages. The infinite-extension zeta identity, geometric integrality, smoothness, tame ramification, and compatibility of the \(7\)-divisible group with prime-to-\(7\) isogenies require the explicit mathematical proof in RESULT.md; finite enumeration is not a substitute. Independent audit has not been performed.
