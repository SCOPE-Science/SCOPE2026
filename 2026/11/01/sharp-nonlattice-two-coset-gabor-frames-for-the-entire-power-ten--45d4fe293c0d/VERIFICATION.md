---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For g_p(t)=(1-|t|)_+^p, all real p>=1, the Zak transform of the sum of the two integer modulation-coset frame operators has scalar multiplier 2(a^2+b^2)+2ab[cos(theta)+cos(theta-2pi delta)], a=(1-x)^p,b=x^p. Its minimum is exactly 4^(1-p)(1-|cos(pi delta)|), achieved at x=1/2 and a matching theta, by convexity of a^2+b^2 and maximal ab. Its maximum is 2, achieved at x=0, since a+b<=1 for p>=1. Essential extrema equal ordinary extrema by continuity of Zak symbol. Thus precisely offsets delta not in Z give frames, the optimal offset modulo integers is delta=1/2, and the collision scaling is quadratic. Independently sampled 20 (p,delta) combinations on a dense Zak grid; maximal gap between theoretical and sampled minima 4.89e-7. The proof applies to arbitrary real delta and p>=1, no reliance on numerical sampling for continuum claims.

## originality

PASS

The core Zak multiplier identity is standard and the p=1 half-offset lattice case is known, but full p>=1 sharp bounds for unions of arbitrary two frequency cosets (generally nonlattice) were not implied by the materially inspected rectangular-lattice results. Best knowledge only; related multiwindow theory may imply the formula implicitly.

## value

PASS

Exact extremal frame bounds and sharp conditioning for an entire real-parameter family of naturally supported tent-power windows answer a motivated redundancy-two frequency-offset design question. The universal optimizer and quadratic frame-collapse coefficient are useful natural numerical and analytic invariants beyond a lone lattice benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
