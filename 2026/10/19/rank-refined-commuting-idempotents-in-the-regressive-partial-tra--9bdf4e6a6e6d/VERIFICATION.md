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

The self-contained \(\texttt{verify.py}\) directly enumerates all ordered pairs of idempotents in the semigroup of partial order-preserving regressive maps for \(n=0,\ldots,7\), compares composition and product ranks, and verifies all rank polynomial coefficients. It separately uses twelve state descriptions to check the derived bivariate generating function through \(n=16\), with integer arithmetic only. The program finished with \(\texttt{VERIFY\_OK}\).

Observed totals, for chain sizes \(0,\ldots,7\): \(1,4,21,124,769,4876,31269,201844\). The rank polynomial at size four was \(227+373y+147y^2+21y^3+y^4\). Those computations are finite corroborations; the general proof is the state-transition and renewal derivation in the result document.

The primary bibliographic page for Zhao et al. was read, but the article's full text could not be obtained. The complete Fernandes article was inspected as an accessible primary comparison. Literature uniqueness and independent mathematical validation remain unverified.
