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

# Reproduction

Use Python 3 with the standard library only:

```sh
python3 ternary_happy_density_checker.py
```

The program asserts a full finite-cycle reduction to the basin \(\{1,3,9,13,17,23,25\}\) below \(27\), confirms direct enumeration of all happy numbers in ternary shells of lengths \(2\) through \(7\), and computes \(H_{136}\), \(D_{136}\), \(H_{224}\), and \(D_{224}\) via the coefficient recurrence stated in the result. It certifies the fractions above \(37188/100000\) and below \(110033/1000000\), respectively, using exact integer comparisons. It checks the three concrete sufficient inequalities for the published transfer theorem's size hypotheses, the \(m\)-strict partition, and the exponential-error bound by integer arithmetic.

The external mathematical input is Theorem 4.1 of Gilmer's *On the Density of Happy Numbers* (arXiv:1110.3836), whose validity is not certified by this finite program. The code neither enumerates all integers nor claims to prove asymptotic results by a finite experiment: that implication is the published theorem with hypotheses checked here. The source inspection and unresolved literature-access risk are documented in the review.
