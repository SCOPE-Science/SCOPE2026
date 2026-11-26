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

For q=ρ⁴/(8D₀), q'=ρ³/(2D₀); the drift of q is 2−α and D(q')²=2q. Under the specified instantaneous zero-flux extension this is BESQ(δ), including δ=1 (instantaneously reflecting) and δ=2 (entrance from zero). Independent Poisson resets give regeneration and a unique stationary law with age Exp(r). The BESQ Laplace transition, checked by the backward equation, has gamma law from 0. Averaging its no-reset term over the stationary state gives the first term of the joint transform; the last-reset integrand is independent of Q₀ and yields the second. The age product yields moments 2^k k!(δ/2)_k/r^k. Finite moments and full support give the orthogonal basis by degree with no completeness assumption in L² needed. The reset generator is triangular on polynomials, with highest coefficient −r for positive degrees. Independently, G P₁=−rP₁ and G P₂=−rP₂+2(δ+2)P₁, using the moment-derived coefficients. Exponentiating that two-dimensional block gives zero reverse covariance and 2(δ+2)Var(Q) t e^(−rt) forward; all the equal-degree normalized correlations follow by degree preservation and orthogonality. The moment and lag formulas invert on δ∈[1,2] and r,D₀>0 at known t>0. No finite-sample claim is supported; the supplied script and its stated diagnostics were read, not executed.

## originality

PASS

The original model and one-time law are prior and the bivariate formula is a specialization of the known last-renewal transition rule and BESQ transform. The exponential scalar lag and broad idea of identification are not standalone originality. The strongest distinct catalogue match covers equivalent BESQ scaling, quartic autocorrelation and a different set of identification statistics, but is later and its full statement and proof do not establish the stationary triangular orthogonal-polynomial hierarchy or the explicit one-way mode pair. That model-specific test of time reversal and the exact synthesis with the stated moments support the limited finding.

## value

PASS

The exact low-degree asymmetry supplies a population-level diagnostic where every single orthogonal mode has the same normalized exponential autocorrelation. It distinguishes reversible from irreversible dynamics using concrete radial observables, not an arbitrary special parameter. The parameter inversion gives a calibration-free model check in the same setting, with no claim that it is stable in noisy finite samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
