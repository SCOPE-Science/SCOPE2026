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

The supplied `verify_beta_runs.py` contains stand-alone integer/Fraction checks; run `python3 verify_beta_runs.py` in a Python 3 interpreter. The check returns the exact string stored in `verification_output.txt`. It enumerates each binary word up to length eleven, checks the conditional composition counts for folded success numbers, verifies all conditional TP2 minors through length fourteen, and checks strict/equality likelihood-ratio steps at several rational beta concentrations. It also checks the closed form for the expectation. No external Python dependencies are required.

**Proof and experimental boundary:** Exhaustive finite checks do not certify infinitely many lengths or real concentrations; these follow analytically from the positive-minor decomposition in the proof. The originality comparison examined substantive statements and excerpts of relevant primary sources, while one potentially relevant ordering paper lacked accessible theorem text. No independent external audit has been performed.
