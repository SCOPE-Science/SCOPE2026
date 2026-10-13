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
# Mathematical and computational verification

The proof derives the identity from the actual MPS amplitudes and pairwise channel action. The fixed-wall crossing bound, binomial-to-Poisson convergence, summable/non-summable regime separation, and critical \(1/\log n\) asymptotic together establish the infinite-volume result for the stated domains. Independent audit is not performed.

The included `verify_purity.py` uses Python's standard library only and requires no input files. Running it produces:

```
VERIFY_OK 5095 MPS amplitudes, quantum-channel matrices, Markov-wall sums, and boundary products
```

It directly multiplies the two matrix-product tensors with the symmetric boundary vectors (independent of the domain-wall Born formula), applies individual commuting \(Z_iZ_j\) channels to explicit density matrices for small chains, reconstructs purity separately by enumerating XOR wall configurations, verifies both finite-size benchmark formulas, checks single-wall pair-crossing multiplicities for all lengths through 24, and checks convergence trends for the infinite product and marginal logarithmic limit.

Finite enumeration does not prove a general-size theorem, a large-\(n\) limit, nor novelty. The infinite results use the analytic estimates in the proof. The strict source parameter exclusion \(\alpha=1\) and possible zero factor at \(p=1/2\) are explicitly addressed.
