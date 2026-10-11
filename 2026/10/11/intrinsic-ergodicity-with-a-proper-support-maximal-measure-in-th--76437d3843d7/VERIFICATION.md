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

The verification uses the exact factor estimates in the proof of Hong--Kim Theorem 3.7. If the last factor symbol \(1\) in an \(n\)-block is at coordinate \(k\), the source proves
\[
|\pi^{-1}(w)|\le p c_Y^2\lambda^{k\alpha+(n-k)}.
\]
For the all-zero block, the source identifies the fiber with \(\mathcal B_n(Y)\), so its size is at most \(c_Y\lambda^n\). These two cases give the uniform logarithmic lift bound used in RESULT.md.

For an ergodic factor measure with positive \(1\)-frequency, the terminal zero-run length divided by \(n\) tends to zero. This was checked directly from the ergodic theorem: a terminal gap of a fixed positive fraction along infinitely many \(n\) would make the normalized one-count on two proportional prefixes have incompatible limits. Bounded convergence then controls its expectation.

The block-entropy inequality follows by conditioning the \(n\)-word partition of \(X\) on the factor \(n\)-word and bounding each conditional entropy by the logarithm of that factor word's number of lifts. Dividing by \(n\) yields
\[
h_\mu(X)\le h_{\pi_*\mu}(\mathsf X(S))+\alpha\log\lambda
\le\log\eta+\alpha\log\lambda<\log\lambda.
\]
The non-ergodic case is handled through ergodic decomposition and affinity of entropy. No numerical experiment or unverified certificate is used.
