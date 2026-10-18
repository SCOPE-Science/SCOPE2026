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

# Reproducibility and limits

Run `python verify.py` in a directory containing `verify.py` and compare its complete output with `CHECKS.txt`. The script uses the Python 3 standard library, exact `Fraction` rational arithmetic, and exhaustive binary-string enumeration. It checks every possible fringe pair up to length seven under the symmetric distribution, as well as three transition pairs for shorter fringes. It also checks the arithmetic full-middle identity on three complete finite boxes. All calculations were run successfully.

The proof of the infinite theorem is human-readable in RESULT.md: the critical analytic step is the geometric control of complex-valued fringe-probability increments on a parameter polydisc. Neither this finite checker nor its output certifies the infinite analytic assertion. The published Markov MSTD theorem is used only for the definition and identification of the pre-existing limiting probabilities. Independent verification has not been performed.
