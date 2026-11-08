---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS. Polynomial convolution gives identically 27X(t)^2+343Z(t)^2=250Y(t)^2; quartic difference positive for t>=2 ensures increasing positive AP. Independently computed resultant of quadratics X,Y is 90724673403000=2^3*3^3*5^3*7^6*13^4, hence any common factor of first two AP terms is among 2,3,5,7,13; t congruent 1 mod 2730 agrees at each with coprime t=1 case, so pairwise gcd=1 because A+C=2B and oddness. CRT residues t=5 mod 11², t=0 mod17², t=3 mod19² impose exact exponent 2 in squared polynomial terms alongside fixed cube exponents 3 at 3,5,7; therefore each term is powerful but no perfect power, for infinitely many distinct t. Independently factored all integers <=57967 using SPF: exactly 186 Achilles numbers; exhaustive ordered pair / third-term membership check yields only primitive (14283,36125,57967), establishing sharp least largest term. The finite certificate proves only bounded minimality; the polynomial/CRT argument separately proves infinitude.

## originality

PASS

PASS best-of-knowledge. Chan and Bajpai–Bennett–Chan establish infinitely many primitive progressions of powerful numbers but their exhibited entries are perfect squares, thus not Achilles. Van Doorn likewise includes square entries. Their ambient powerful-number existence does not imply the stronger all-Achilles primitive construction. OEIS lists the three values separately, not a certified least primitive progression. No direct dominating prior theorem found.

## value

PASS

PASS. Primitive APs composed exclusively of powerful non-perfect-powers are naturally constrained additive-number-theory objects. Infinite pairwise-coprime construction plus a sharp minimal first occurrence pinpoints an arithmetic existence problem not settled by powerful-number AP examples containing perfect powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
