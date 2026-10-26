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

The exact argument is in RESULT.md. It derives the bilateral probability generating function for \(q<|z|<q^{-1}\) from the established two-index displacement formula using two absolutely convergent \(q\)-binomial expansions. Evaluating the resulting product at \(z=-1\) establishes the strict parity bias; differentiating its logarithm gives the strict parameter monotonicity. The geometric-sum representation holds in distribution only, not as a claimed coupling to the original inversion-count variables.

Run `python verify_product.py` with Python 3. The checker has no third-party dependencies and passes 30 decimal diagnostic assertions at \(q\in\{0.1,0.2,0.5,0.7,0.8\}\). It computes both the joint-distribution series truncated at explicitly specified indices and the product truncated to matching depth; conservative geometric-tail bounds cover omissions, while high-precision decimal arithmetic provides a computational cross-check. The program is not an exhaustive or infinite proof.

No independent audit has been carried out. Historical priority beyond the comparisons documented in REVIEW.md is not certified.
