---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Each inter-block conflict is violated exactly for offset D_ab=S_b-S_a. Any two distinct edges of the block-interaction graph have jointly uniform offsets, so their centered cost covariance vanishes. For n integers x_d in [0,n] of fixed total, balancing or concentrating gives exact lower/upper sum-of-squares bounds, realizable because offset classes partition possible conflict edges. Character expansion followed by vertex shift averages projects to divergence-zero flows; cycle rank counts flows and a forest has only zero flow. A 3-block n=2 triangle gives P(Z=3)=1/4 and P(Z=1)=3/4. Independently enumerated 27 shifts for n=q=3 with exact mean 3 and variance 2.

## originality

PASS

Yoneda–Yoneda Lemmas 5,6 and Theorem 7 establish EF1 round-robin construction and |E|/n mean guarantee; these are prior work. The exact conditional variance sharp envelopes and full random-shift flow law are additional statements for the random baseline. Finite-group Fourier-flow expansions are classical and not claimed generically new.

## value

PASS

First-moment guarantees mask large variance and cyclic dependence of conflicts. Exact attainable extrema at fixed cross-block conflict counts, a forest product law and a minimal triangle counterexample give informative sharp robustness structure for a natural random fair allocation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
