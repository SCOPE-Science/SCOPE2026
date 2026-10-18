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

Published Proposition 4.1 gives square iff gcd(h,u_n)=1 and pairwise coprime iterated numerators under (u,v)->(u^2+v^2,uv). For each p^alpha||h, initial ratio mod p has an absorbing pole unless v_p(x0)=alpha. In the equality case the ratio equals (x0/p^alpha)*(h/p^alpha)^(-1) mod p and iterates by T(t)=t+t^(-1) until a unique zero hit. Every finite-field hit t gives exactly one x0 class modulo p^(alpha+1). p=3 mod4 cannot hit because predecessor solves t^2=-1; p=2 is included. CRT independence across primes yields exact period and collision-aware distribution. Independent code checked 8147 local starting residues across h<=36 and h=65, including direct integer (u_n,v_n) failure indices for h<=21 and h=65; the h65 counts match 3507/714/4. h=1 empty product M=1 yields all starts zero failures.

## originality

PASS

The motivating 2026 paper establishes the non-cancellation recurrence, per-prime at-most-once obstruction and first-hit interpretation but leaves the exact starting-value proportions as an open question. The submitted p-adic class and collision-aware CRT formula are an explicit fixed-h answer not found as a theorem in the inspected primary text.

## value

PASS

The lead 2026 paper expressly asks for the starting-value proportion. A uniform exact periodicity and CRT law for every fixed h, with collisions of distinct primes at the same time correctly counted, answers that natural unresolved finite-field/arithmetic-dynamics enumeration question. It yields exact rational densities without requiring an inaccessible generic closed form for all preimage trees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
