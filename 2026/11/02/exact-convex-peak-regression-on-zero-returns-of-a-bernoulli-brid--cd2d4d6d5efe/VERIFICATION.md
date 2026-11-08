---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For a uniform bridge of 2n steps n>=2, exchangeability gives expected internal up/down adjacent peaks n/2. Under any k specified strictly interior even-time zero pins, the blocks are independent uniform bridges whose peaks contribute n/2 and their k joins contribute k/4, proving the location-free pinning identity. Expanding z^R across all pin subsets yields E[P z^R]=(n/2)G(z)+(z−1)G'(z)/4. Signed first-return excursions have generating function 1−sqrt(1−4t), with exactly r+1 excursions when R=r; Lagrange inversion yields q_r ratio 2(r+2)(n−r−1)/(2n−r−2). Coefficient comparison gives E[P|R=r]=(n−1)/2+r(r+2)/[4(2n−r−2)]. Its continuous extension has positive first and second derivative across 0..n−1, with n=2 endpoint checked directly; covariance = (4^n/binom(2n,n)−2)/4 follows from pinning and central binomial convolution. Independently enumerated 4704 balanced paths across small n and checked conditioning; original script separately checks broader sizes. No enumerative finite range is substituted for proof.

## originality

PASS

PASS, qualified. Labarbe–Marckert calculate peak marginal distributions, and Godrèche treats zero-return excursion lengths. Mortimer–Prellberg provide path bijections but their bilateral transformation need not preserve zero contacts, so its peak bijection does not imply this joint conditioning. Kreweras 1986 is a plausible same-object multi-parameter bridge joint distribution; full chapter unavailable, genuine priority risk; no decisive coverage established from available evidence.

## value

PASS

Peak versus zero-return dependence is a natural pair of path-shape statistics. An exact location-independent pinning identity and all-n strictly convex conditional regression explain their interaction structurally; the covariance follows as a useful exact invariant, not just a low-order example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
