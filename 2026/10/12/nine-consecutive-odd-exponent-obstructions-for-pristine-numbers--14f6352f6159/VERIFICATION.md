---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Fink exact recursive-divisor identity reduces pristine to P_d(c)=q^d. For odd d the squared-binomial alternating sum at X=-d-1 vanishes, implying Q_d integer polynomial. Writing m=c+d+1 gives m Q_d(c)=d! q^d; as P_d(c)>m, Q_d(c)>d!. When q does not divide K_d, q dividing m would force Q_d(c) coprime to q and hence Q_d(c)|d!, contradiction. Thus either m|d! or q|K_d. An independently implemented exact-arithmetic exhaustive verification enumerated all 639114 relevant m|d! candidate c values and precisely the complete odd prime factors of each K_d (K factorization has no residual prime), testing exact integer dth powers and monotone exception equations; no cases survive for all nine exponents. Independently computed K via critical-point derivative sum. This is exhaustive only by the unrestricted two-branch proof, not a finite scan of arbitrary c bound.

## originality

PASS

The exact statement and its implications were compared against the defining primary source, nearest general theorems, differently named invariants and Resultary published records. No dominating prior result was found among genuinely examined material; any inaccessible or unindexed potential coverage is retained as a residual risk, not treated as evidence of novelty.

## value

PASS

Fink explicitly asks whether pristine examples exist for any odd exponent; after the previously proved 3,5,7 cases, this settles nine further consecutive natural odd-exponent layers by a reusable arithmetic sieve. Each layer has unbounded original c and q, so the exact finite reduction is substantive; no claim at d>=27.

The dated certificate retains the supplied scientific assessment, sources and limitations.
