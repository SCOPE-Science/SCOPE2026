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

# Reproduction and limits

Extract `verify.py` from the same scientific package and run `python verify.py` using Python 3. The verifier uses only `fractions.Fraction`, performing 4,950 exact rational parameter cases \(2\le n\le100\), 1,510 projection checks including \(2\le n\le16\), and verifies the explicit positive-contact weights as well as scalar KKT conditions in both regimes. The checks were executed successfully; the printed counts and phase counts are reproduced by that file. The general theorem follows from the independently written algebraic supporting-hyperplane identities, strict logdet concavity, and global John contact-certificate proof in `RESULT.md`. Finite tests do not certify untested dimensions or bibliographic priority. No separate independent scientific audit has been performed.
