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

The map on (R/Z)×R has yprime=y−b sin(2pi x) and xprime=x+a(1−y′²)(1−epsilon y′²) mod 1. For b>0 fixed action gives x∈{0,1/2}; angle return requires integer lift winding m, not only zero. Writing z=y² gives epsilon z²−(1+epsilon)z+1−m/a=0, discriminant (1−epsilon)²+4epsilon m/a. With 0<a<1, m≥1 has exactly one positive z hence 4 fixed points; m=0 has 8 except 4 at epsilon=1; negative m=−k gives 8,4,0 as k<B, k=B,k>B with B=a(1−epsilon)²/(4epsilon). For Y≥max(1,epsilon^(−1/2)), all negative/zero points lie inside and each m∈{1,...,floor omega(Y)} contributes four, yielding exact height census with quartic leading 4a epsilon Y^4. The determinant-one Jacobian residue at positive branch is ±b pi a sqrt(z_(m,+) D_m); two points elliptic strictly when b<1/(pi a sqrt(zD)) and the others hyperbolic. Monotone d_m gives exact ceiling staircase and cubic inversion yields two-term b^(−4/3), b^(−2/3) asymptotics. Independent small-m root tests and inspected symbolic verify.py corroborate critical discriminant, residue and sample counts; algebra proves the infinite range. Linear ellipticity does not prove nonlinear islands.

## originality

PASS

Best-of-knowledge PASS for full unbounded-cylinder global integer-winding census and elliptic cutoff. Original Grime primary defines same quartic nontwist map, analyzes eight distinguished m=0 fixed points and their residues, and does not in inspected relevant Section 3 establish the infinite all-m classification; integer winding and Greene residue themselves are prior work. A same-model outer-resonance study could dominate, retained as risk.

## value

PASS

A complete exact all-winding count and sharp linear stability staircase for a natural area-preserving map can be needed to understand high-action resonances. The unbounded-cylinder mathematical distinction from a lift and noncommuting epsilon→0/large-height limits are substantive; physical relevance outside the approximation’s action range is explicitly limited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
