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

# Verification record

The proof is an exact trace and determinant calculation. In the \(2\times2\) positive cone, the Perron root is strictly increasing in trace at fixed determinant. Three independent nonzero pair-sum gaps give the strict classification, while positive-entry monotonicity and the limits \(s^4\) and \(+\infty\) prove three strictly separated crossing intensities. These analytical arguments establish the entire claimed real-parameter domain; finite tests alone would not establish the theorem.

`python3 check.py` runs deterministically using only the Python 3 standard library, with rational arithmetic throughout. Successful execution of the packaged script printed `EXACT_CHECKS_PASSED 7227`, 24-permutation checks on 240 reproducible random parameter sets, invariance checks for one through three seasons, and exact reproduction of the rational threshold-reversal example. The random tests are nonexhaustive; the displayed algebraic proof supplies the unbounded-domain conclusion.

The provenance comparison inspected the mathematical model and matrix stability theorem of the publicly accessible 2012 open-access malaria-mosquito article, and metadata/abstracts of the 2009 periodic matrix article and the 2014 patchy Ross–Macdonald article. The 2014 article's full technical text was not verified in this review. The example is not a calibrated infection forecast. Historical priority and independent scientific validation are not established by these checks.
