---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For any strictly improving cross-part relocation, the fractional utility inequality is d/b>(c-1)/(a-1) when b>0, and factorial potential ratio is ((a-1)d)/((c-1)b) (or times Q if c=1). For b=0 and source mixed the ratio (a-1)/(c-1) (or Q(a-1)) is >1; source occupancy one and same-part jumps cannot improve. Finite state space ensures termination for any finite types and allowed vacancies. With two types, a mixed source opposing a vacancy contradicts the sum of its two no-improvement inequalities; all stable assignments partition into globally pure, one-part-vacant with opposite full part pure, or both parts partly vacant with opposite pure occupied parts. Labeled vacancy counts give the displayed polynomial; fixed q balanced asymptotics follow from dominant 2 binom(m,q)2^{m-q+1} term. Independent exact rational enumeration checked 16,901 states, 34,776 improving jumps and 36 polynomials across bounded graphs; this is corroboration, not the all-parameter proof.

## originality

PASS

Qualified best-of-knowledge novelty of the precise additional claim only; original definitions, exact source formulas, special cases and existing methods remain prior work. Source readings and explicit residual priority risks are recorded; no assertion of exhaustive literature coverage.

## value

PASS

A single explicit ordinal Lyapunov function proves termination for arbitrary vacancies on a natural nonregular graph family, despite known improving cycles on broader networks. The closed red-population equilibrium polynomial and nonmonotone vacancy example determine a natural strategic stability distribution; no general graph conclusion is overstated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
