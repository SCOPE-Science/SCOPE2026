---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For n>=3, order-preserving decreasing f with f^2=epsilon has an initial fiber [m] mapping to 1, and all image values <=m; this yields |S_n|=2^(n-2). If h=v∘u is nonzero, the s(h) distinct nonunit h-values need s(h) distinct u-intermediates strictly above m(v), implying m(h)>=M(h)+s(h). Conversely choose u(i)=M+j for each nonunit h-value t_j and v(M+j)=t_j, with initial 1-fibers of lengths m and M: these maps are in S_n and compose to h whenever m>=M+s. Counts by distinct values and suffix runs give generating function sum b_n z^n=z(1-z)/(1-2z+z^2-z^3); nilpotency and indecomposability force the unique minimal generating set S_n\S_n^2 and rank=2^(n-2)-b_n. Independent complete compositions n=3..8 match b_n and rank, including rank(S_6)=9; proof is all-n and finite enumeration corroborative.

## originality

PASS

Complete uniform product-factor criterion, exact all-n generating rank and all-product count refine a published lower bound; n=6 already exceeds it. OEIS recurrence itself is known and not claimed as novel. Korkmaz–Ayık 2021 full text inspected: its Theorem 3.4/Examples do not give the all-n product criterion; 2023 dissertation remains uninspected.

## value

PASS

The rank and unique indecomposable generating set are natural primary invariants of the nilpotent square-zero ideal of Catalan transformations. An explicit necessary/sufficient product factorization and all-n generating function improve a recognized nonsharp lower bound, giving mathematically useful structure beyond computing the preexisting OEIS sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
