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

The following tests were executed from the included standalone `check_quartic.py` file using Python 3 and its standard library. The exact output is stored in `check_quartic.stdout`.

1. For each \(p\in\{5,11,17\}\), all \(p^4\) pairs \((a,b)\in(\mathbb Z/p^2\mathbb Z)^2\) were evaluated through integer coefficient counts of \(\sum_x X^{ax+bx^4}\), reduced modulo \(X^{p^2}-1\) before comparison to \(\Phi_{p^2}(X)\). The observed zero sets equal those specified in equation (1) of `RESULT.md`.
2. At the same primes, the proposed nonaffine spectrum with \(\beta(r)=r^2\) was checked against all frequency-pair orthogonality requirements.
3. For \(p\in\{5,11,17,23\}\), every parameter pair \(A\in\mathbb F_p\), \(B\in\mathbb F_p^\times\) was checked against the exact binomial moment identity (4).

All tests completed successfully. The proof for every admissible prime is symbolic; the finite tests do not independently certify its infinite quantifier. Independent audit has not been performed.
