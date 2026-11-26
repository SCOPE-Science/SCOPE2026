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

With fixed a, luminosity and gravitational parameter, the period is fixed and the eccentric-anomaly time density is (1−e cos E)/(2π). The condition F/F₀>η is exactly e cos E>δ. No point qualifies for e≤δ (contact at e=δ is not strict); for e>δ it gives the symmetric interval bounded by E₀=arccos(δ/e). Its normalized physical-time measure is (E₀−e sin E₀)/π. Differentiation gives H'=(δ−e²)/(πe√(e²−δ²)), with a single positive-to-negative sign switch at √δ; the onset plateau is zero and the interior exceedance fraction is positive, giving the unique global maximum and its stated value. For the dose, the time-weighted integrand on that interval is (1−e cos E)^−1−η(1−e cos E); it is zero at the moving endpoint, and its e derivative is strictly positive there and throughout the nonempty interval because cos E>0. This proves strict ordering on the entire claimed range. Independently, using true anomaly ν, the inverse-square flux times dt/P is dν/(2π√(1−e²)); hence J=ν₀/(π√(1−e²))−ηH, with ν₀=arccos(((1−e²)/(1−δ)−1)/e). This reproduces the arctangent formula, gives divergence as ν₀→π, and reproduces the reported rounded example values. The e→1 limit is an ideal point-source limit, not an admissible orbit. VERIFICATION.md and verify.py report finite midpoint and Simpson quadrature comparisons; in the supplied code the excess comparison uses a second quadrature on the selected interval, not a direct coded check of the arctangent formula. The uploaded script was not executed.

## originality

PASS

The Kepler time-fraction construction is established and the duration formula itself follows immediately from it for one radius crossing. The distinct result is the sharp fixed-threshold eccentricity optimum paired with strict monotonicity of the positive-part excess at that very threshold and the resulting opposite rankings. The closest inspected sources concern time in a habitable annulus, unthresholded averages or maxima, climate response, or unrelated eccentric-orbit observables. This is a bounded best-of-knowledge comparison, not priority for the Kepler formulas or the time-in-zone method.

## value

PASS

Duration above a threshold and cumulative excess are two natural but inequivalent measures of intermittent irradiation. The sharp interior turning point and the strict opposite ranking on the entire high-eccentricity branch determine exactly when shorter exposure is a misleading proxy for lower integrated forcing. This is a useful, bounded comparison for a standard idealized orbit, with no implication asserted for actual climate or habitability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
