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

Squaring the specified average y/2 at either face and taking the centered flux divergence gives −y³/(2h²), so freezing the coefficient in backward Euler gives exactly F_T after division by b. The cubic z+Tz³−1 is strictly increasing and has one positive root s. Expanding F_T∘F_T verifies the factored displacement in RESULT.md; its denominator is positive and the quadratic changes root count at T=4. For T≤4 the displacement points toward s on both sides. For T>4 the two roots p_± satisfy p_++p_−=1 and Tp_+p_−=1 and are exchanged by F_T, hence straddle s. The displacement points toward p_− below s and p_+ above s; because F_T² is increasing, iterates are trapped between the start and the attracting fixed point of F_T² on that side. This clarifies the proof's shorthand 'bounded by fixed points': an outer bound can be the starting value, not another fixed point. Chain differentiation on the cycle gives 4/T. At T=4 the quadratic is 4v² for v=z−1/2, the cubic is 4v+O(v²), and the denominator is 8+O(v); thus v advances to v−2v³+O(v⁴) per two steps. The inverse-square increment tends to 4, so jv_(2j)²→1/4, and the odd-to-even deviation ratio tends to −1. The full-index limit is 1/2 for every nonfixed positive start, including the assigned start 1. The damped multiplier is 1−ω(3−2s), with s→0 as T→∞; precisely 0<ω≤2/3 gives strict local linear stability at every finite T. This proves no globally damped convergence assertion. The supplied verification files were inspected; the frozen code was not run.

## originality

PASS

There is exact catalogue coverage of the undamped threshold, attracting cycle and multiplier after rescaling; those features are not credited as distinct recurrence results. The supported contribution in the bound heat-solver statement is the critical relaxation constant in the physical normalization and the sharp stiffness-uniform local damping ceiling, with the exact reduction for this centered-flux heat step. The matching wave record and the broader primary iteration do not supply those quantitative boundary/stabilization results. This is not a priority judgment based on catalogue dates.

## value

PASS

The exact positive heat-step diagnosis distinguishes failure of a practical nonlinear iteration from loss of positivity or failure of the implicit update itself. The nonhyperbolic rate explains slow convergence at the threshold even when the iteration converges in exact arithmetic. The parameter-independent damping ceiling gives a sharp local remedy for the entire stiffness range without claiming global behavior. These are meaningful solver distinctions beyond a reparameterized cycle threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
