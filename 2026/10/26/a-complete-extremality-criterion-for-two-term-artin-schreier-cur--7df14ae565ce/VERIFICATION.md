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

Run `python verify.py` in a Python 3 environment. The code has no third-party dependencies and uses exact polynomial arithmetic in finite fields, not floating point. It exhaustively tests \(6400\) ordered nonzero coefficient pairs over \(\mathbb F_{3^4}\) and \(389376\) over \(\mathbb F_{5^4}\). Its quadratic-polar-matrix rank determination is independent of the polynomial norm-identity test. The two methods agree on every coefficient pair, yielding extremal counts \(240\) and \(3120\) respectively. It also directly counts points for one extremal witness at each prime, reporting \(28\) and \(1126\).

The expected final line is `VERIFY_OK`. These finite exhaustions do **not** establish the criterion for all primes; the composition identity and finite-field cyclicity argument in `RESULT.md` prove the general theorem. The program does not classify curves up to isomorphism, split maximal from minimal cases exhaustively, or assess independent audit status.
