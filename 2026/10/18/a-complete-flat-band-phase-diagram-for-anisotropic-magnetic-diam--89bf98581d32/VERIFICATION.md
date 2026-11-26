---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the stated cell convention, write the determinant as (u-E)(v-E)(w-E)-(w-E)|a+bz|^2-(v-E)|c+d exp(i phi) z|^2. Its three Laurent coefficients must separately vanish. For equal side potentials the nonconstant term factors as -(v-E)(ab+cd exp(i phi)); it cancels identically in E exactly at balanced products and half flux. The remaining quadratic then has two distinct roots different from v. For unequal side potentials E cannot be either side energy, the nonconstant coefficient enforces exp(i phi)=±1, and its linear equation has either the single stated candidate or no solution when ab±cd=0. The constant coefficient gives exactly the stated onsite tuning. The explicit eigenvectors are nonzero Laurent polynomials with exponents in two consecutive cells. After translating any proposed one-cell state to cell zero, its Bloch vector is constant; the lower-row z^-1 terms force its central component to vanish, and the upper row forces both side components nonzero and ad exp(i phi)=bc. Under positivity this is exactly the stated zero-flux proportionality. An independent symbolic determinant and kernel calculation and exact tuned zero- and half-flux examples were run (python3 /workspace/branches/recompute_frozen.py); the coefficient argument, not tests, establishes completeness.

## originality

PASS

The supported distinct claim is the simultaneous weighted magnetic phase diagram with arbitrary periodic potentials, in particular the unequal-side tuned branch and sharp support criterion. General Laurent methods and equal-hopping symmetric caging are prior work; related finite caging and differently connected periodic graphs do not give this classification.

## value

PASS

A complete phase diagram of an established lattice is useful for choosing periodic magnetic couplings and site energies. It distinguishes the protected flat band, full caging, and tuned unequal-side flatness; it excludes two flat energies and supplies a sharp minimum compact support rather than only a dispersionless eigenvalue. The conclusions test all positive hoppings and real periodic onsite energies, not a fixed sampled profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
