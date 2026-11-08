---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For M_n=floor(n(log n+c)), independent rate-one Poissonization of each coupon marks rare interarrival gaps exceeding L_n=log n+c; each label has probability λ|I|/n of a start in a bounded interval, with Exp(1) overshoot. Superposition gives Poisson marked intervals of rate λ and unit exponential lifetimes; counting active intervals converges in D([0,T],Z_+) under J1 to stationary immigration-death M/M/∞ with birth λ and death j. Earlier intervals have mean ≤λe^{-B}. The coupling from Poisson time to fixed n draws controls max clock deviation O_P(sqrt(log n/n)), and the expected near-threshold mismatch O(n^{-1/3}log n) vanishes. The first zero is J1-continuous almost surely owing to positive holding at 0. Strong Markov renewal from zero and p00(t)=exp[-λ(1-e^{-t})] yield E exp(-sτ)=[s∫_0^1u^{s-1}e^{λu}du]^-1, Eτ=∫_0^1(e^{λu}-1)du/u. Verify.py finite factorial moment identities are consistent but not the J1 proof.

## originality

PASS

Best-of-knowledge originality after comparing natural equivalent, broader and table/reduction routes, including inspected primary literature and explicit residual priority risks.

## value

PASS

The stationary path limit at the n log n coverage threshold transfers a known queue law into a distinct dependent sliding-expiration model; distinguishes stationary first-completion behavior from initially empty classical collector, a mathematically natural operational cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
