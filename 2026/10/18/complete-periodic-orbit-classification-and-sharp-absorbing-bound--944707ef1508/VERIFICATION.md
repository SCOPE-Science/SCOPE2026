---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Actual RESULT.md blob fd9faa02b7a4b5a60b443449745ea9cd4e7cb7a3 provides a complete symbolic descent: for composite m>=26 the least prime divisor q<=sqrt(m) gives c(m)=m−φ(m)>=m/q>=sqrt(m)>3 and F(m)<m. For p>=29 prime, F(p)=p+2; if composite, c(p+2)>=sqrt(p+2)>5 gives F²(p)<p; if p+2 prime then p+4 divisible by3 and F³(p)<=2(p+4)/3+3<p. Strong induction ensures all orbits enter [1,25]. Independently recomputed the exact 25-state totient transition table, verified closure and precisely three cycles, with 23<->25 obstructing smaller invariant initial intervals. The six states are the unique smallest forward-invariant universal eventual attractor. No empirical one-million-state search used as infinite proof.

## originality

PASS

Leonetti-Luca full primary article proves eventual periodicity for all shifts with orbit bound depending on initial input, which does not imply a uniform eventual [1,25] trap or exact three cycles. Published Resultary statement about sharp bound depending on period T includes known 23↔25 but permits arbitrarily long periods; explicitly credit the known two-cycle. No located direct complete shift-3 classification; priority risk for older elementary totient iteration is retained.

## value

PASS

A complete infinite functional-graph periodic orbit classification and smallest absorbing interval are natural dynamical questions. The prime twin-case descent is a motivated obstruction to a simple monotone argument, resolved within three steps, and sharp constant 25 differs from previous initial-dependent bounds. The classification is exact, not a small data table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
