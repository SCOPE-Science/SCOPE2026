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

For any fixed k distinct target s-sets, projecting H_t to its intersection with their finite union gives an exact finite reversible chain. Its limit is a pure-death chain with a unique eigenvalue one. The stationary entrance flux into the forbidden states is k binom(r-1,s-1)/binom(n,s)+O(n^(-s-1)), including overlapping targets. The bounded mean-zero inverse for I-P_n and killed-chain Perron eigenvalue give the same leading escape rate; a uniform spectral gap over finitely many overlap patterns yields survival m^(-k)e^(-kx)(1+o(1)). Factorial moments give Poisson/Gumbel, and a one-target summable tail establishes mean. Independent small Johnson-walk trajectories matched the projected safe-chain survival through five steps.

## originality

PASS

Athreya–Mukherjee–Mukherjee 2025 present precisely this Markovian transition rule as Conjecture 2.4; their Theorem 2.5 proves only diagonal r=s and their Gumbel theorem is for independent rounds. This theorem proves strict s<r conjectured mean and adds the missed-shadow Poisson and centered Gumbel limits. Searches did not identify a later stronger same-model theorem; an unindexed resolution is residual risk.

## value

PASS

Settles an explicitly published and mathematically motivated Markov-dependent cover-time conjecture for every fixed strict pair and quantifies the entire critical-window distribution, handling overlapping targets without independence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
