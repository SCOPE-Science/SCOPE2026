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

For t=2^a>=4, p odd prime, S=(t-1)p+2t-1. If D(S)=tp, valuation nu_2(S)=1 makes D(S) odd; valuation >=3 gives D(S)/S>=3/2 and S/n>3/4, contradictory. Thus S=4m odd m, with exact identities p=4D(m)+2t-1 and m-(t-1)D(m)=t(2t-1)/4. Since D(m)=Omega(m) mod2, this forces even Omega for a=2 and odd Omega for a>=3. For Omega<=2 and a>=3, m is prime and the two simultaneous prime formulas follow; conversely these imply D(S)=n. For a=2, Omega=2 gives (r-3)(s-3)=16; pairs (5,11) and (7,7), and only former gives p=71 and n=284. The first case a=3,p=19 has q=37,n=152. Independent factor/derivative calculations over 616 (a,p) pairs corroborated the logic. No assertion for higher Omega, a=1 or infinitely many simultaneous primes.

## originality

PASS

OEIS A248816 contains the equation and numerical examples 152, 284 and larger; A125246 already records the deficient-by-four family shape. Neither database observation implies the exact unconditional 2-adic/odd-Omega obstruction plus exhaustive low-complexity converse over all a. Resultary searches returned other arithmetic derivative iterations and 2^a p divisor topics without statement-equivalent coverage. Originality attaches only to this rigidity and classification, not the derivative identity, example values or family shape.

## value

PASS

This is a natural structural question for the fixed points of the arithmetic derivative of proper-divisor sums, already populated by an OEIS sequence. The two-adic rigidity excludes entire factor-complexity classes and the exhaustive Omega<=2 classification describes an infinite conditional prime-parameter family without claiming its infinitude. A researcher determining further fixed points can use the precise obstruction and terminal small-complexity layer; this is more than recomputing known terms or renaming the deficient-by-four family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
