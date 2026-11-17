---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact full-draw missed-set model has N=binom(m,c), M=binom(m-1,c-1), omission q=c/m, and falling-factorial moments (N)_r((M)_r/(N)_r)^t. Negatively correlated label omissions give Var U_t<=E U_t. Uniform Stirling for c~log m yields log E U_(c+1)=delta-0.5 log(2pi)+o(1); fixed factorial moments imply Poisson(e^x/sqrt(2pi)). At c and c+2 Chebyshev and Markov leave a two-round law. The tail sum bound (c+1)/mu_c+mu_(c+1)q/(1-q) tends to zero even for delta->+-infinity with delta=o(log m), and star finishes after c+1 distinct centers with expectation c+1+O(c^2/m). Formula and scope reconstruct correctly. Finite moment computation for N=6,M=3,t=3,r=2 is exactly 6/25. This arithmetic check is not an infinite proof.

## originality

PASS

The theorem compares two equal-cost mechanisms at the previously unclassified defect c~log m, with explicit Poisson law and order-one mean reversal. Known fixed-c star asymptotics and fixed-round full group-draw Poisson limits do not imply the growing-round star/full joint comparison. Historical coverage is best-of-knowledge because the full relevant star paper was not retrievable through authorized access.

## value

PASS

Fair coupon mechanisms are natural objects; precise defect-dependent reversal of expected completion ordering and a two-point coverage limit at c~log m are motivated structural results with a sharp transition, not arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
