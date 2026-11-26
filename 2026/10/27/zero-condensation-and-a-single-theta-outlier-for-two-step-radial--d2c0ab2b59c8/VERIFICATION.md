---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Integrating u^n against the weight in u=|z|² gives (1+τq^(n−N))/(n+1); reciprocal monomial norms give the stated kernel. For the shifted and normalized series on r0≤|s|≤r1 with q<r0≤r1<1, write ρ=q/r0. The absolute difference from the bilateral limit is bounded by [r1/(1−r1)²+τ^(−1)ρ/(1−ρ)²]/(N+1)+τ^(−1)ρ^(N+1)/(1−ρ), from the index correction and omitted negative tail. The DLMF summation with a=−τ,b=−τq gives the stated product, including the constant (the factor 1+τ is canceled when changing (−τq;q)∞ to (−τ;q)∞). All reciprocal-s factors have zero winding on these circles since the zero of each such factor lies at modulus at most q and its pole is at zero. Among forward factors only 1+τs can contribute, with simple zero at −1/τ. Uniform convergence and homotopy on each fixed circle preserve winding off this zero; multiplication by s^N restores the N term for the argument principle. On a small disk about −1/τ Rouché gives one zero counted with multiplicity, and smaller such disks give convergence. The normalized kernel on compact subsets of |s|<q tends uniformly to q^(−1)(1−s/q)^(−2), excluding inner zeros and proving the stated radial condensation. No moving-radius, angular uniformity or whole-disk count is inferred. The frozen code and 69-check output were inspected, not executed. Its sampled winding is numerical only; the moment-inversion assertions reuse the same expression and are an algebraic consistency check, not independent integration. The analytic checks above do not depend on either safeguard.

## originality

PASS

To the best of the inspected evidence the distinct claim is the exact radius-dependent jump and movable, isolated zero at fixed q with a nonintegral exponent offset. There is direct prior work on the weight class, existence and prescribed numbers of zeros, and a close indexed bulk-condensation theorem on the integer phase, but none of the compared statements covers this phase or implies its outlier law.

## value

PASS

Two levels give a minimal radial perturbation for testing zero geometry. At a fixed interface the phase moves one simple negative zero through the whole open radial gap (q,1) while the N bulk zeros remain near the interface. Recovering an eventually exact count on both sides, not just existence or normalized density, separates these two mechanisms and gives a useful explicit benchmark for weighted-kernel asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
