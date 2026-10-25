---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For y^5-y=x^2+x+x^(-1) over F5, poles at zero and infinity have orders one and two, giving genus six, two rational fully ramified points, and 5-rank four. Over F_(5^n), the Artin–Schreier map has five preimages precisely on trace-zero values; hence #C=2+5*#nonzero x with Tr(x²+x+x^(-1))=0. An independent finite-field enumeration for n=1..6 gave N=(2,2,77,602,3022,16337), matching the package. Weil sums S=(4,24,49,24,104,-711) and Newton identities plus the genus-six functional equation give P coefficients (1,-4,-4,21,46,-100,-85,-500,1150,2625,-2500,-12500,15625). Exact P(1)=3775; irreducibility mod 3 follows by Rabin X^(3^12)=X and gcd tests at exponents 3^6,3^4, giving base-field simple Jacobian. Valuations v5 of coefficients produce Newton hull vertices (0,0),(4,0),(8,2),(12,6), slopes 0^4,1/2^4,1^4. The finite point counts are exhaustive for the six required extension degrees; the functional equation is what completes the full zeta polynomial; simplicity is not claimed geometrically.

## originality

PASS

Tafazolian–Kazemifard arxiv:2610.13279v1 explicitly introduce the identical function and establish minimum geometric automorphism group C5, genus and p-rank, but their Question 7.5 asks how the Newton polygon can coexist with such rigidity and does not report this Weil numerator. The determined exact L polynomial, Newton polygon and F5-simplicity are additional arithmetic properties, not a claim to new genus/automorphism theory. Scholten–Zhu first-slope bounds on one-pole polynomial functions exclude this two-pole rational function; other cited tame cyclic-cover sources lack a direct specialization. Exact database duplication is still possible and is a stated risk.

## value

PASS

The smallest positive-5-rank genus-six rigid C5 example is a canonical object from a recent classification, and its exact Newton polygon supplies a concrete nonordinary answer to that classification’s explicitly posed arithmetic question. F5-simple nonordinary positive-rank Jacobian and complete extension counts are independently useful natural invariants, despite being specific to one curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
