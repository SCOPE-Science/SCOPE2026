---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Ren–Chen Theorem 1.2 reduces exactly-two-distinct-prime near-perfect integers to the three listed families plus 40. For odd U, U>2g>c leaves only U=q or q². The square-repunit solutions (g,ℓ,root)=(7,4,20),(3,5,11) cannot supply a Mersenne prime; U=q leaves a digit larger than the permitted range in all three families. For odd g and ℓ=2m with odd m>1, U_m(g) and (g^m+1)/(g+1) are nontrivial coprime odd factors. For 4|ℓ, (g+1)Q divides U with Q=(g²+1)/2 odd, coprime to g+1 and >g; this forces g+1=2^s. The valuation gives odd part of U >2g^(ℓ−1)/((g+1)ℓ), greater than Q² for ℓ≥8 by checking ℓ=8 and monotonicity. This contradicts the odd exponent bound. At ℓ=4, the q² case conflicts with the required Type-A valuation; Q=q exceeds the digit and excludes Type A, and Type B gives q≤g<Q (the strict q<g written at this step can be weakened to ≤ without affecting the contradiction). For Type C the only possible valuations a are 2s−2,2s−1; the resulting difference 2^s−2 or 2^(2s−1)+2^s−2 cannot be the required power of two, with s=2 excluded from the first case by a≥s+1. Independent finite check of divisors U of 40 found only (g,ℓ,U)=(3,4,40); sigma(40)=90, so d=10. The frozen parameter scan is regression evidence only and was inspected, not run.

## originality

PASS

The tuple 40=(1111)_3 and the even-base exclusion both have exact prior coverage. The distinct claim is exclusion of every unbounded odd base, including odd bases above 9; the strongest bounded odd-base result does not imply that exclusion, and the general two-prime near-perfect classification does not impose the representation condition. The prior odd-base record should be credited explicitly in any account of the extension.

## value

PASS

The results for bounded odd bases and for all even bases leave a natural unbounded family open. Resolving it gives a complete representation classification within two-prime near-perfect numbers and explains why the known base-3 exception cannot recur at large odd bases. The contribution is that uniform exclusion, not rediscovery of 40.

The dated certificate retains the supplied scientific assessment, sources and limitations.
