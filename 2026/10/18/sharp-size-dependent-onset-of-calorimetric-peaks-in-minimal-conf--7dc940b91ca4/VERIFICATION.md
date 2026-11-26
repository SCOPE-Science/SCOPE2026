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

For q>1 and α>0 the full chains are irreducible. Reflection gives exactly two boundary-orientation orbits on two sites, with the center orbit added on three; row sums to each target orbit and heat agree within each orbit. The normalized Poisson equation therefore reduces to the orbit system. Integrating the centered heat semigroup gives w, and a small positive temperature step pairs w at the new temperature with old minus new stationary law, giving transient bath heat −C dT. Holding f, α and the kinetic prefactor fixed gives dq/dT=−fq/(2T²) and E=−q(∂qρ)·w/f. /workspace/replay.py (chain, Python 3 + SymPy) independently reconstructs stationarity using tree cofactors and the heat response fixing the last potential to zero; a constant shift is immaterial because (∂qρ)·1=0. It checks both exact rational functions and the derivative factors. The formulas have strictly positive numerators and denominators in scope. The two-site derivative has a strictly decreasing linear numerator with positive intercept exactly at q>√(5+2√6). The three-site numerator has negative quadratic and linear coefficients, so it is strictly decreasing on α≥0; its intercept sign reduces at z=q²+q⁻²>2 to 3z²−7z−70, strictly increasing with one zero there. The unique positive crossing, when present, is a maximum; both responses decay at large α. At either threshold the derivative is strictly negative for α>0, so the supremum is only the α→0+ limit, not a capacity claim for the reducible zero-rate chain. K(6)>0 gives q₃,c²<6<q₂,c² and a nonempty separation interval. These checks apply to two and three sites with constant unit hop prefactor, no flip heat and fixed f,T while varying α. The packaged verification was inspected, not executed.

## originality

PASS

Santra's model and heat definition match under the intended units and prefactor, and the paper already reports the broad qualitative tumbling-rate peak. Its inspected calculation concerns a channel with L=20, with numerical response and an approximate persistence-scale peak, not the exact two- and three-site thresholds, positivity and uniqueness classification or strict size separation. The accessible Drazin and active-calorimetry results supply general tools or different models, and no exact match appeared in the bounded indexed comparisons. This pass is for the quantitative minimal-size classification only.

## value

PASS

These natural minimal chain lengths separate the onset of a response peak from drive and persistence alone. The strict intermediate drive interval supplies an exact control comparison with the same kinetics in both models, and the positivity and uniqueness classification distinguishes an actual optimum from a zero-rate boundary effect. This does not claim a thermodynamic transition or predict general longer channels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
