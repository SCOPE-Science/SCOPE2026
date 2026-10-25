---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For p=11, the fixed R={0,1,2,3,4,5,7} has seven distinct elements. Each displayed length-10 integer row is nonzero; because Phi_11(t)=1+t+...+t^10 is the irreducible minimal polynomial of a primitive 11th root and has degree 10, each row represents a nonzero c_x in Z[zeta], so support is exactly seven. For every (a,b) in F_11^2 the polynomial P_{a,b}(t)=sum_x D_x(t)t^((a*x*x+b*x) mod 11) satisfies F(a,b)=P_{a,b}(zeta); F vanishes iff the remainder modulo Phi_11 is zero. Independently recomputed all 121 values WITHOUT running the submitted checker, accumulating integer coefficients by cyclic exponent shift in an 11-component vector and testing whether all 11 components were equal (the unique cyclotomic relation). Found exactly (0,4),(1,0),(1,1),(1,9),(6,6),(6,7),(6,9),(7,3),(9,9), and 112 nonzeros; for example remainder at (0,0) is (11,11,11,11,0,11,33,0,11,22), nonzero. The source verifier implements another exact 10-dimensional quotient algorithm, not a numerical floating-point approximation; checked its transformations but independently implemented a different test. This proves only the finite existence/lower bound M_{11}(7)>=9 for exact size 7; not optimality, a global 9-zero upper bound, or other primes.

## originality

PASS

Best-of-knowledge originality attaches to the explicit full-seven-support nine-zero coefficient witness over F_11, not the cyclotomic Fourier evaluation method or original source upper bounds. Independently recomputed the claim and compared the exact formula/implications with materially inspected Li v1 Section 4.1 (seven-support <=10, p=11 sharpness open), Li v2 (different weaker general odd upper estimate/global MUB), and Fiorentino–Weigert 2022 Section 4.4 (aggregate MUB non-saturation, not this construction). Three fresh Resultary semantic searches and targeted external searches returned the same assigned Resultary mirror but no separately sourced equivalent or stronger existence theorem. The five-support F_11 six-zero example is insufficient since exact seven support requires two additional nonzero coefficients. The upper bound ten does not give lower bound nine. This is a limited priority conclusion, not proof no other nine-zero witness exists.

## value

PASS

The exact-support k=7, p=11 finite-parabola maximum is a natural unresolved numerical invariant explicitly identified by Li v1 Remark 4.15. A full-support nine-zero example is an exact self-contained lower-bound witness, not an arbitrary coordinate table for its own sake: it narrows the open candidate maximum from a generic 6-equation lower baseline to at least nine, and, conditional on the v1 bound <=10, confines it to nine or ten. It also translates to a seven-component state with nine forbidden outcomes in the standard quadratic MUB family. Full exhaustive 121-point integer evaluation certifies the specific fact independently of any unfinished global census; no general theorem or paper-sized contribution is required for this motivated finite invariant. It does not claim maximum nine, uniqueness, full support census, or extension to other fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
