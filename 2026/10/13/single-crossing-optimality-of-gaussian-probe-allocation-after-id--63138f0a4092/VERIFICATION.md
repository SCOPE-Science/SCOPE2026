---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Under n>=B>=2m>=2, rank k_N=B-mN and independent Gaussian quadratic forms, Var(g²)=2 makes exact MSE F_N=2T_N/N. Sorted nonnegative squared log eigenvalues define increasing block masses c_j. With T_N=T_0+sum_{j<=N}c_j, H_N=Nc_{N+1}-T_N satisfies F_{N+1}-F_N=2H_N/[N(N+1)] and H_{N+1}-H_N=(N+1)(c_{N+2}-c_{N+1})>=0. Hence minimizers are consecutive and one probe is optimal iff F_1<=F_2; all ties and nondivisible budgets are accounted for. Exact geometric sums produce q^(-m)+q^(n-B+m)>=2 and limiting q^m<=1/2. Independently checked 2,690 rational decreasing spectral-weight profiles; analytic identities, not testing, prove all n.

## originality

PASS

The source published the pointwise spectral MSE and fixed-parameter comparisons, which are cited as premises. The discrete monotone block-H difference, all-count single crossing and exact geometric frontier are a natural complete optimizer theorem not explicitly established by the inspected primary Section 2. The insight is algebraically accessible but not merely renaming a known formula.

## value

PASS

Globally determines a nontrivial allocation choice for every admissible ordered spectrum without evaluating every probe count and identifies a sharp spectral-decay transition. It is a useful idealized experimental-design benchmark, even though unknown eigenvalues make it non-oracle-free and the proof is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
