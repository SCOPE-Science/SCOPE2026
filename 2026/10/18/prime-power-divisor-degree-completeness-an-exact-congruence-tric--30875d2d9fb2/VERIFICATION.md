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

# Reproducibility and boundaries

From the directory containing `VERIFY.py`, execute `python VERIFY.py`. This requires only the Python 3 standard library and reports the number of exact modular-order and divisor-degree tests. It completed successfully with `PASS multiplicative-order/subset-degree tests: 1242`.

For an independent polynomial-factorization check, install SymPy separately if necessary, then run `python VERIFY.py --factor`. The second test uses actual factorization of \(X^{r^a}-1\) over \(\mathbb F_p\), not the multiplicative-order formula used in the first test; it completed with `PASS direct polynomial factorization tests: 242`. A nonfatal SymPy deprecation warning can appear.

The first test includes every prime \(r\le19\), every exponent \(a\ge1\) with \(r^a\le625\), and every prime \(p\le199\). It checks the exact least missing degree or complete coverage. The second test includes \(r\in\{3,5,7,11\}\), \(r^a\le150\), and every prime \(p<80\). These are bounded computations. No infinite mathematical conclusion is inferred from their successful termination; that conclusion relies on the printed proof using cyclotomic factorization, valuations of multiplicative orders, and contiguous subset-sum intervals.

The asymptotic prime density relies on the established prime number theorem in arithmetic progressions, not on a finite experiment. Independent scientific assessment has not been performed. No publisher-provided original paper is reproduced in these files.
