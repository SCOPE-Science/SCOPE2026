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
# Verification of the finite rare-region theorem

`verify.py` was run as a standalone standard-library program and reported 25,026 passing assertions. For all binary words of lengths 2 through 12, it directly computes the exact regional sum and checks expectation against the separate analytical interior/boundary run-count formula for three choices of parameters. It also checks zero-time expectation identities, branch formulas for the constrained and unconstrained minima, positivity of the post-threshold gap, and seeded finite samples.

The exact expectation can be independently checked from \(\mathbb E N_{L,m}=p^2(L-m-1)(1-p)^m+2p(1-p)^m\) for \(1\le m<L\), together with the all-lossfree event of probability \((1-p)^L\). No numerical tests have been represented as proof of the asymptotic quenched theorem: the run-count concentration/constructive block arguments and deterministic saddle analysis in RESULT.md are the justification. Numerical convergence can be slow because the asymptotic scale is \(\log L\).

The scope explicitly excludes exact survival of a finite microscopic dissipative quantum chain. All comments and quantities in the standalone program concern only the finite Bernoulli surrogate.
