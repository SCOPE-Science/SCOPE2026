---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For coprime a,b>=2, modular reduction of ax+by=mab forces (x,y)=(bj,a(m-j)), 0<=j<=m; endpoints are nonprimitive. The local obstruction p|gcd(bj,a(m-j)) separates primes dividing a, dividing b, or neither. Checking indices j for m=2,...,15 as in RESULT.md gives universal representability. For m=16 every even j is obstructed; j=1,15 force 3 and 5 on opposite factors, and j=3,9,11 force 13 and 7 on one factor and 11 on the other. Thus failure iff (55|a and 273|b) or reversed. Independently enumerated all 3^6 disjoint statuses of p=2,3,5,7,11,13, confirming each of 729 statuses at 2..16 and the exact m=16 failure locus; finite prime-state verification is exhaustive here because j,m-j<=15.

## originality

PASS

The gcd-restricted Frobenius problem is in the Jaffe 2026 paper, but its checked denominator/Stern-Farey equivalence and primitive Frobenius bounds do not explicitly imply the exact universal first failing diagonal multiplier and complete 55/273 locus. Classical unrestricted Frobenius formulas do not impose gcd(x,y)=1. Priority is qualified, not guaranteed.

## value

PASS

The smallest diagonal multiplier with a primitive-coefficient obstruction is a natural sharp boundary for two-generated numerical semigroups with primitive coefficients. The universal m<=15 theorem plus exact complete failure locus at 16 is motivated structural information, not an arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
