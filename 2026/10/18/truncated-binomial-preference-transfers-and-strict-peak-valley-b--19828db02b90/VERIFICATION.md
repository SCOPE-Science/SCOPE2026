---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Uniform parking functions have feasible loads satisfying every prefix sum ≥prefix length, with multinomial weight n!/∏m_j!. Conditioning all bins except a<b and total T leaves only r=m_a constraints R≤r≤T and a weight proportional to binom(T,r): exact symmetric-binomial lower truncation, including T=0. Pairing r>s and swapped masses proves load pair inequality and stochastic dominance. For three car preferences, equal endpoints contribute m_a m_b(m_a-m_b) to peak-minus-valley; Pollak cyclic shift controls equality patterns and yields p+ +p-=2p0. The feasible profile (n−1,0,...,0,1) but impossible swap makes positivity ≥(n+1)^(−n+1). Independent complete preference word enumeration gives (peaks,valleys) (4,3),(33,27),(355,305) for n=3,4,5. Analytic proof handles all n; finite experiments do not.

## originality

PASS

Diaconis-Hicks previously observed strict-peak failure of ensemble equality, so that observation is not counted as new. The current statement gives a strict direction for every n, exact signed occupancy cubic moment, and arbitrary two-label conditional truncated symmetric-binomial law. Searches and accessible primary abstract supplied no evident equivalent load theorem. Best-of-knowledge originality with incomplete primary-body access.

## value

PASS

The strict versus weak peak ensemble discrepancy is an explicit question raised in primary parking-function probability. The theorem establishes the finite-n direction and a general arbitrary-two-preference-label mass-transfer principle, with exact occupancy moment connecting dependent car preferences to order-pattern bias. This is structural and all-size, not a trivial table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
