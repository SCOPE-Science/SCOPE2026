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

The theorem's all-\(m\) quantifier follows from the induction in `RESULT.md`; it is not certified by finite enumeration. The executable `verify.py` performs independent-clade exact-subset checks for five leaves, 48-digit outward-rounded interval-sign evaluations for the explicit 100,514-leaf three-peak witness, and a rational check of the uniform derivative perturbation bound. It runs using the Python 3 standard library via `python3 verify.py` and prints `PASS` on successful assertions. Analytical facts used in addition are Bernoulli's inequality, the exponential limit of \((1-c/k)^k\), and the Bernoulli product expectation-derivative bound \(n\operatorname{osc}(g)\).

The verifier does not enumerate all survival subsets of the 100,514-leaf tree, construct a universal tree for all \(m\) by explicit numeric cutoff, assert that exactly three extrema exist, or validate the bibliography independently.
