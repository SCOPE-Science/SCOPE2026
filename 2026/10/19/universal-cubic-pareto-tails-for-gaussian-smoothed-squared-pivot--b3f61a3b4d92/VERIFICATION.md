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

Original RESULT.md line 87 overstates the deterministic minor identity: for A=[[0,1],[1,0]] the only selectable corners each leave a residual of norm 1, whereas the stated right side is 2. The repaired RESULT.md restricts the factor 4 to nonzero entries and gives the exact nonzero-corner count otherwise, by summing the squared pivot cancellation only over selectable pivots. Gaussian inputs have no zero entries almost surely, so this repair does not change the unconditional second moment or main theorem. Independently, for a fixed complement and t>||W|| the tail event is (t^2-||W||^2)x^2+2<W,uv^T>x-||u||^2||v||^2<0; its two roots multiplied by t tend to -h and h, h=||u||||v||. Integrating the x-squared selection weight gives 2 f(0)h^3/(3S). On ||W||≤t/2 the scaled integral is dominated by a constant times h^3/S≤S^2/8, and the Gaussian complement outside this event gives o(t^-3). The Gaussian chi-square Laplace integrals for E[(UV)^(3/2)/S] have total power (mn-1)/2+3, giving the displayed 8/(mn+3) times the gamma ratios. Layer cake and the radial Gaussian second-moment calculation verify the remaining assertions. These are analytic checks, not claims of a new Monte Carlo run.

## originality

PASS

The distinct claim is the unconditional sharp cubic tail for Gaussian-smoothed squared-entry RPLU, including its noncentral coefficient, the centered gamma formula and the corresponding moment frontier. The deterministic correction and Gaussian squared mean are not credited as novel. Inspected fixed-matrix and partial-pivot results do not yield the joint-law asymptotic.

## value

PASS

The exact coefficient and transition from finite squared error to infinite third moment show a real limitation of a motivated algorithm, even at arbitrarily small positive smoothing variance and in dimension 2×2. Complete pivoting has no such moment failure. This identifies an observable not determined by existing expected-error guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
