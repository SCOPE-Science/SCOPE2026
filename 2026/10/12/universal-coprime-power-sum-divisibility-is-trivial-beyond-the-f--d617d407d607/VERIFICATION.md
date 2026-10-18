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

For each m>=2, Faulhaber prime-power restriction F_{m,p}(X) has exact X^{1 or 2} times H_{m,p}, with degree 2 floor(m/2), nonzero Bernoulli constant and leading coefficient (p-1)/(p(m+1)). Choose p>k+2 avoiding fixed Bernoulli numerators; p H_{m,p} is Eisenstein at p for both s,k, so each H irreducible. If integer P(p^u)|Q(p^u) for all u, polynomial division Q=PA+R, clearing denominators, makes M R(p^u)/P(p^u) an integer tending to zero, forcing R=0. For k>s, H_s|H_k would force association; degrees differ except even s,k=s+1, where leading and constant ratios (s+1)/(s+2) versus (s+1)/2 disagree. For reverse distinct s>k>=2, n=3 yields phi_s(3)>phi_k(3). The proof establishes all s>=2, not just finite verifier ranges.

## originality

PASS

The 2024 initiating paper proves finiteness of these universal divisibility sets, not the exact singleton classification for every s>=2; Campbell treats the different s=1 exceptional set. Eisenstein on large prime-power Faulhaber polynomials supplies a general obstruction beyond either prior result.

## value

PASS

Resolves the higher-moment half of an explicit universal divisibility problem, with a strong prime-power witness statement, not a small numerical improvement or formula substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
