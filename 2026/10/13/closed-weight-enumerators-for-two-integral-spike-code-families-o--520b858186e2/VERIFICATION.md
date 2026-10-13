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

# Computational checks and limits

Run `python3 verify.py` using Python 3 with only the standard library. The test script reconstructs both integer generator matrices and evaluates each coordinate modulo the input integer. It compares complete enumerators against an independent residue-state dynamic program and the closed binomial-gcd identity; it also compares the printed low-parameter and full-support expressions from the cited original paper. The reported test suite passes with `VERIFY_OK` over 52 direct matrix enumerations and 84 dynamic-programming tests. The program tests finite parameter ranges only; the general quantified result is established in `RESULT.md` by an algebraic proof. No independent audit has been performed.
