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

The claim was reconstructed directly from the update equations with strict receptiveness, simultaneous time indexing, a stationary left eigenvector, and gap recurrences. The geometric gap law and confidence decay give an exact crossing rule. Equality \(\delta=1/2\) and the strict-test boundary \(D=c_0\) are included.

The accompanying `verify.py` is executable with standard Python and no external dependencies. It uses `fractions.Fraction` rather than floating-point tests. It executes 72 parameter families with 15 exact updates each, checks the dynamically computed edge state and the explicit formulas, and separately checks the boundary and a rational activation witness. Successful finite checks are supporting evidence only; the proof in `RESULT.md` supplies the quantified argument over real data and every integer time.

Limits: no finite experiment can prove the infinite-time result or establish publication priority. The program only checks the defined deterministic three-agent sector, not arbitrary networks or stochastic variants. Independent audit and validation have not been performed.
