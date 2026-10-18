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

# Reproducibility
Run `python verification.py` with SymPy installed using the declared `requirements.txt`. The program uses exact symbolic algebra over the rationals adjoined with \(\sqrt2\) and checks 367 identities/inequalities. Observed output:

`VERIFY_OK 367 exact symbolic/algebraic assertions; Bernstein certificates, cyclic transfer identities, sharp five-cycle witness`

It checks the stability-function substitution, all positive Bernstein coefficients used for the \(n=2,3,4\) cases, the exact negative witness for \(n=5\), the recursive witness inequality in several dimensions, and the exact cyclic resolvent identity and unit row sums at rational timestep substitutions for \(2\le n\le11\). The proof in `RESULT.md` separately establishes the arbitrary-\(n\) statement using symbolic identities, Descartes' rule, the intermediate-value theorem and asymptotic bracketing. The finite checks are not an exhaustive search over state dimensions, and the decimal endpoints are not treated as certificates.

No claim of independent human validation, external certification, or formal proof verification is made.
