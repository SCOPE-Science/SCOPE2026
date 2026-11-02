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

Run `python verify.py` using the Python 3 standard library. The completed package replay returned:

```
PASS: 2206 exact finite rational checks
Infinite nonnegative-rank lower bound and perturbation stability require the written proof.
```

The checker performs exact rational Gaussian elimination for squared-distance kernels at sizes \(3\le n\le13\) and strict-positive rank-\(k\) kernels for \(3\le k\le\min(n,7)\). It verifies symmetry, entrywise positivity and the central-binomial threshold inequalities for sizes up to 1,000, along with explicit independent Poisson emission mean normalization for a rational factorization.

The infinite theorem is proved in `RESULT.md` by Poisson splitting, factorization equivalence, Sperner's antichain bound, normalized-factor compactness, a nonzero Vandermonde coefficient determinant, and an expected-degree bound. These proof steps are not replaceable by finite checks. In particular, the exact threshold \(\delta_{n,k}\) for positivity-preserving nonnegative-rank lower bounds is existential and was not numerically computed.

This verifies neither historical priority nor independent mathematical validation. Exact unthinned parent-independent-emission Poisson reproduction is the domain of the result; claims about more general thinned couplings are unproved.
