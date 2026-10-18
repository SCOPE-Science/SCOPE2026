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

Eventually order four distinct positive-slope integral affine arguments a1>a2>a3>a4. If the top slopes differed, PNT supplies a prime p between max(a2,a1/2) and a1, giving odd valuation 1 in the top factorial only. Hence a1-a2=d>0 constant. After removing (a2!)^2, if slopes a3,a4 differed, PNT supplies more than d primes in (max(a4,a3/2),a3], each odd in a3! and absent a4!, with at most d capable of dividing the d fixed-block integers a2+j; contradiction. Hence a3-a4=e>0 constant. Removing (a4!)^2 leaves polynomial F=prod_{j=1}^d(a2+j)*prod_{j=1}^e(a4+j), whose large integer values are perfect squares. With y_n=sqrt(F(n)) in integers and k=floor(deg F/2)+1, the kth finite difference is integral and o(1), hence eventually zero: F equals a rational polynomial square. Both block root sets have simple roots, so equality of their two root multisets forces d=e, and if common length>=2 their equal-step arithmetic progressions force a2=a4, impossible. Thus d=e=1, a1*a3 is a polynomial square, so a1/a3=(r/s)^2 with coprime r>s>=1. Coefficient integrality gives a1=r^2 H, a3=s^2 H with integral affine H. Direct factorial algebra proves the converse. Independent integer checks of paired identities corroborate; proof uses PNT and polynomial identities, not finite extrapolation.

## originality

PASS

Yudin 2026 Appendix A gives existence of some bounded affine-factorial families for every exponent; the concrete four-factor paired-consecutive construction is known to Erdős–Graham. The reviewed result proves exhaustiveness and rational-square normal form for every four-factor affine square family. The fully accessible Bérczes–Dujella–Hajdu–Saradha–Tijdeman 2019 paper addresses fixed largest arguments, prime-power exponents, and existence, not every-integer affine parametrization. No inspected stronger result implies the necessity classification; residual risk of older factorial literature is explicit.

## value

PASS

Four factorials are a naturally minimal nontrivial square construction in recent and classical work, and eventual affine families are explicitly singled out by Yudin Appendix A. The result is a complete unrestricted-in-parameter necessity classification with a rational-square scaling form rather than a new example or partial enumeration. The rigidity mechanism and exact converse answer a motivated algebraic-number-theoretic classification problem that cannot be read from the known sufficient identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
