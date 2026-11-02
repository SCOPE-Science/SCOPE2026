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

## Analytical checks
The motivating bounded-monomial-support article was first publicly submitted to arXiv on 23 July 2026. The full text of the open-access 2026 journal article was examined for its stated asymptotic claim and proof scope. The subsequently posted 27 October 2026 related preprint was checked for its exact coefficient-comparability hypothesis and formula for its general threshold.

Critical proof calculations are entirely scalar: reduction to the circle, exact two-axis ellipse peak minimization via a one-parameter trust-region dual, a piecewise quadratic maximum, the discriminant \(-16\), the bounds \(16<(13/5)^3\) and \(64/9<8\), and the counterexample inequality \(27>25\). These computations establish all degrees analytically, independently of finite numerical tests.

## Reproduction
Execute `python3 checker.py` using Python 3 standard library. The script checks exact rational certificates on a grid and sampled trigonometric peaks for several coefficient configurations. Its numerical sampling does not establish the global phase lemma or claim exhaustive parameter enumeration. No external code, private files, or external certificates are required.

## Limits
No independent audit has been performed. Classical coefficient-norm consequences of more general theorems may require further literature scrutiny. The sharp threshold concerns precisely the stated tie-or-monomial class.
