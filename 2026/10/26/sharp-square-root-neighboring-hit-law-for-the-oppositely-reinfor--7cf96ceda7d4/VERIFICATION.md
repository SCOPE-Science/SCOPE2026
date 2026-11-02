---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Bertoin Theorem 4.1 is correctly specialized with a_j=j-1 and A_j=sum_{r=1}^j(r-1)^2; uniform for k<=bn for any fixed b>0. Eq. (5.6) gives sqrt(k) P_k(R_k>floor(k t)) -> sqrt(6/[pi((1+t)^3-1)]). For n>=k the uniform asymptotic gives O(k n^-3/2) and for n<k a monotone coupling to simple symmetric excursions gives O(n^-1/2), providing integrable tail domination, finite mu(k) and the beta integral constant. Geometric positive excursions before a negative jump and Jensen control of successive epochs preserve the same mean asymptotic. Direct urn transition probabilities give S_s=F_{s-1}-1 and T=H_2-1. Independent exact rational DP verified shift through 42 and beta constant 3.3563383598. The infinite result uses the cited theorem and rigorous summability, not this finite test.

## originality

PASS

Bertoin proves the crucial return-to-zero tail, and Balaji–Mahmoud explicitly conjecture finite mean of the Friedman first return. The new claim concerns the adjacent-level hitting time, its geometric-excursion reconstruction, finite mean and sharp beta-valued late-start mean, none supplied verbatim by the inspected primary results. A general theorem may render the neighboring-hit reduction a corollary, but the precise implication was checked.

## value

PASS

The solution answers a published concrete finite-return-mean conjecture and gives a universal sharp asymptotic constant of an important memory process; this is a motivated probabilistic result, not a trivial translation of the original zero-excursion asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
