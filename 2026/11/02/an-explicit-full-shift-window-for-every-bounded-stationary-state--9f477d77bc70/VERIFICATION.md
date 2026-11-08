---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The bounded maximum/minimum principle confines all real stationary states to [0,1]. With r=(3−√3)/12 and m=√3/8, each of three disjoint root intervals has |g′|≥m and inverse Lipschitz ≤1/m. For any root code, T_s= (g|J_s)^{-1}(−dΔv) maps the complete supnorm product B_s into itself since 2d*(1+2r)=rm, and contracts with factor 4d/m<(4−√3)/13<1. Any bounded stationary point has |g(u_j)|≤2d; the complementary gaps in [0,1] have |g|≥rm, so no coordinate can be outside root intervals. Consequently each profile is the unique contraction fixed point for exactly one code. Finite-iteration locality and uniformly decaying contraction error yield product-topology continuity; shift equivariance is exact. Independent symbolic values and boundary derivatives were checked; periodic examples do not replace bi-infinite contraction proof.

## originality

PASS

The full accessible Hesoun–Stehlík–Volek 2026 paper Theorem 1 constructs a three-symbol shift as a subsystem for sufficiently small but unspecified positive d, not an explicit all-bounded-state classification at a numerical d interval. Its introduction sometimes says stationary solutions topologically conjugate, but formal theorem says subsystem; the assessment follows precise quantifiers and retains overlap risk. Classical 1995 Chow–Shen spatial chaos and anti-integrability may provide overlapping qualitative all-state coding; original complete text was not obtained. Distinct remaining contribution is a concrete sufficient cutoff, with uniform uniqueness/exhaustiveness certified for the cubic.

## value

PASS

An explicit uniform positive diffusion bound for *all* bounded stationary sequences is a motivated, usable quantitative spatial-chaos threshold and complete exact coding, not a routine finite periodic census. It is expressly conservative, not asserted sharp; extending a horseshoe subsystem to exhaustive bounded-profile coding and giving a numeric window is mathematically meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
