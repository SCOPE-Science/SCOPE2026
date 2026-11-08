---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For all integers n>=5,504,798 with n=4m+r, an inverted ordered Farey pair (a/b,c/d) satisfies c/d>=(a+1)/(b-1), reducing the minimal intervening count to C_n(a,b). The published Wang-Xie-Zhao uniform bound gives C>U(n) when b<=n/4 or b-2a outside {1,2}; its explicit error E(n)<n/36-4 was independently checked numerically at the stated cutoff (positive margin 0.01549...). Remaining coprime starts have nested I_t, J_t, K_t intervals. For nonterminal I/J/K families, the proof lists additional reduced fractions strictly in the corresponding intervals, increasing the known lower U(n); r=3 exceptional K_m requires an actual inverted right endpoint beyond the non-coprime immediate candidate and gains extra m/(2m-1). The sole surviving I_m for r=0 or J_m for r=1,2,3 has the known reduced right endpoint; a later endpoint adds at least one interior Farey term. Consequently exactly one minimizing ordered pair at each n in scope, with known f(n) values m+1,m+2,m+2,m+4. Independent brute exact Farey sample n=120..123 and n=144 found only the canonical pair; finite checks do not establish the cutoff theorem.

## originality

PASS

Qualified novelty lies only in the all-large-n uniqueness/equality classification; van Doorn already constructs the exact witnesses, and Wang-Xie-Zhao already proves the exact minimum and analytic off-center exclusion. Full text of Wang-Xie-Zhao was not retrieved, so it may already imply the uniqueness as a corollary; no decisive covering result was identified in accessible checked theorem statements.

## value

PASS

A sharp optimizer classification for a canonical Farey inversion problem is an independently meaningful extremal arithmetic statement even though the numerical minimum is known; the analytic cutoff is explicit and its non-optimality is disclosed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
