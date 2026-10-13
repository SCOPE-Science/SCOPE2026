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

# Reproducibility
Run the standalone `verify.py` with Python 3 and no third-party modules. It enumerates all \(n^{n-2}\) Prüfer codes at each size \(n=2,3,4,5,6,7,8\), computes \(Z\) from vertex degrees, \(W\) from edge-cut component sizes, and the marked-pair distance by graph traversal. Using exact `fractions.Fraction` arithmetic, it directly checks the two moment means, exact covariance, strict sign, conditional distance probabilities and conditional Zagreb regression. The complete census covers \(280{,}392\) labeled trees, \(28\) aggregate checks and \(56\) conditional checks; it prints `PASS` on success.

# Mathematical certificate scope
The enumeration is exhaustive only within the specified finite sizes. The infinite-size correctness argument is the forest-extension/weighted-Prüfer proof, moment telescoping and analytical four-term sign bound in `RESULT.md`. The asymptotic depends on the established Cayley Wiener mean asymptotic. No numerical simulation, incomplete search, or software log is used as a substitute for that proof. Independent audit: not performed.
