---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At m=0 the unordered-pair monomials in the complex amplitude have coefficients 1 or 2. The monomials in A and conjugate A are linearly independent as complex polynomials in the real and imaginary parts (an invertible linear change of variables), so the coefficient for each ordered selection of two distinct pair monomials forces equal phase products. Conversely those products give a common unit phase per row for every delay, including delays where some terms cancel. Adjacent equal sums make phase quotients constant within each interval; comparing (b_i+1)+b_j and b_i+(b_j+1) equates these quotients across intervals. Integer interval sums have no holes, so precisely the listed overlap relations survive after removing the uniquely fixed slope. Integral unimodular row and column operations reduce M to Smith form on the tori, giving the claimed dimension and component count. In the two-band case 2a<2b: the two possible intersection intervals [b,2a] and [2b,b+a+c] are disjoint, and either enforces equal offsets. On either nonempty intersection the flat-input intensity has a strictly positive cos(δ) coefficient; elsewhere there is only one pair type. Their inclusive endpoint counts therefore give H, also at equality in either threshold. The no-wrap bound ensures that none of these arguments misses a modular coincidence.

## originality

PASS

The standard consecutive-band scalar and frequency ramp, and the additive pair-sum viewpoint, receive no novelty credit. The supported distinct claim is the exact overlap compression for all nonwrapped interval unions, including the Smith description and the sharp two-band transition and active-row count. The strongest inspected FROG results establish known symmetries or generic reconstruction in other support classes; the closest catalog records handle quartic phase statistics or cubic invariants, not the stated classification.

## value

PASS

A support-only classification decides when a continuum of indistinguishable band phases persists despite arbitrarily many delays and nonzero amplitudes. The compressed integer matrix makes this computable from interval endpoints rather than all frequencies. The exact two-band count quantifies the rows that can carry this phase information, beyond simply noting that a gap can hide it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
