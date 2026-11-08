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

For algebraically closed characteristic-11 field, smoothness of y^3=x^5+ax+b is Δ=b^4+3a^5!=0; gcd(3,5)=1 gives genus4 by Kummer Riemann–Hurwitz. At infinity, orders of x,y,dx are -3,-5,-4, yielding differential basis dx/y,dx/y²,x dx/y²,x² dx/y². Cartier term selection at exponents 10 mod 11 in f^7,f^3 gives arrows ω0→P^(1/11)ω1+R^(1/11)ω2 and ω1→(3b)^(1/11)ω0 with P=b(9a^5-b^4), R=6ab². Semilinear stable rank is 0 for b=0 or P=0, otherwise 2; ordinary Cartier rank 0 at b=0, otherwise 2, giving (f11,a-number)=(0,4),(0,2),(2,2) on stated loci. On P=0, Δ=a^5!=0 when b!=0. Independent polynomial convolution and modular linear algebra counted exactly 10,10,90 smooth F11 coefficient pairs; this finite census does not establish the algebraically closed classification.

## originality

PASS

Kudo–Harashita (2017) enumerate isomorphism classes of superspecial genus4 curves at small primes, including 11. Kudo (2018) and Kudo–Harashita–Senda (2019) establish superspecial/supersingular existence via other genus4 models. The superspecial case b=0 and Cartier coefficient-extraction identities are acknowledged as existing general theory; no inspected text gives all three p-rank/a-number strata in this exact two-parameter cyclic trigonal family. A general computational Hasse–Witt formula could imply the answer with specialization; that remains an important residual risk.

## value

PASS

The two-parameter (3,5)-Kummer genus-four family is a natural Hurwitz family; a complete rank and a-number stratification distinguishes nilpotent nonzero Cartier action from Cartier-vanishing superspecial locus, and rules out ranks 1,3,4. Equations for the smooth strata and an exact F11 coefficient census are potentially reusable arithmetic-geometric invariants, not merely an isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
