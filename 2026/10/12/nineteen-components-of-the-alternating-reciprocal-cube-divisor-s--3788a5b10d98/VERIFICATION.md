---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Every p>=11 has tail T_{>p} below u_p(2), by exact witnesses for p=11,13,17,19,23 and Nagura three-interval prime theorem for p>=29; greedy logarithmic local interval overlap therefore fills [T,1]. The four primes 2,3,5,7 split into 4*2^3=32 exact rational local states, where neighboring exponent intervals overlap. Independent Fraction arithmetic and zeta(3) integral bounds at N=180 gave precisely 13 overlaps, 19 components, 18 strict gaps, first endpoint (15314/18375)*T..25426807/30375000, final [T,1]. This is exact rational computation with analytically justified infinite tail, not sampling.

## originality

PASS

Defant 2015 establishes the alternating family and density threshold (r=3 nondense), without the 19-component exact decomposition; Resultary primary full RESULT.md for r=2 gives exactly two intervals only and explicitly disclaims r=3. Number/locations of components not implied by nondensity or parameter change.

## value

PASS

Exact component count and all endpoints solve a natural explicit single-parameter instance of Defant’s interval-component open problem; the distinct r=3 tail cutoff and 32-block exact arithmetic make it more than a simple substitution of r=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
