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

The mathematical argument establishes the all-\(n\), fixed-\(r\) exact primitive two-cycle census from alternating firings and the asymptotic Gaussian law from a unique relative-entropy saddle. The proof's essential analytic facts are Pinsker's inequality, Stirling's formula, the local Taylor expansion of binary relative entropy, and dominated Riemann-sum convergence.

The standalone file `verify.py` separately simulates all \(296{,}272\) chip configurations in the confined boxes of four small complete multipartite graphs, verifies their two-step returns, and compares the numbers of genuine two-cycles against a direct product enumeration by firing sets. All four exact comparisons passed. Six additional exact finite-parameter enumerations and covariance calculations are recorded in `verification_output.txt`. These computations test small instances and trends only; they are not substitutes for the infinite-\(n\) proof or a priority examination.

Self-review: passed. Independent audit: not yet performed.
