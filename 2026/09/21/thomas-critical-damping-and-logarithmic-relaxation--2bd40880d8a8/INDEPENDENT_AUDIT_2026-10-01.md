# Independent audit — 2026-10-01

## Final claim

At \(b=1\) in the cyclic Thomas sine ring, the origin is globally attracting; a codimension-one strong-stable manifold is exponentially fast, while every other orbit synchronizes and obeys the common-coordinate law \(x_i(t)^{-2}=t/3-(1/20)\log t+C+o(1)\), with \(\sqrt t\,x_i(t)\) tending to a signed \(\sqrt3\).

## Correctness — PASS

The quadratic Lyapunov estimate is strict at every nonzero point when \(b=1\), so the endpoint is globally asymptotically stable; \(b<1\) is linearly unstable in the common mode. At criticality the cyclic shift has one simple center eigenvalue and a stable transverse spectrum, while the synchronized diagonal is an exact center manifold. Standard strong-stable foliation therefore gives the codimension-one exceptional set and exponential synchronization to a nonzero diagonal orbit off it. For \(u' = \sin u-u\), the independent Taylor replay gives \(d(u^{-2})/dt=1/3-u^2/60+u^4/2520+\cdots\); bootstrapping \(u^2\sim3/t\) yields \(u^{-2}=t/3-(1/20)\log t+C+o(1)\). Exponential transverse error is negligible even after inversion, so all coordinates share the same constant.

Checked sources:
- Published Resultary finding dated 2026-09-20: Critical damping closure and sharp algebraic decay for the Thomas cyclic flow; complete RESULT inspected.
- Thomas, International Journal of Bifurcation and Chaos 9 (1999); bibliographic/abstract material.
- Chlouverakis and Sprott, Chaos 17 (2007); higher-dimensional cyclic ring and bifurcation context.
- Package scalar-series certificate independently checked.

Residual risks:
- The global extension of the local strong-stable foliation uses standard invariant-manifold theory; it is not independently formalized.

## Originality — PASS

Originality passes only for the strict strengthening beyond the already-published 2026-09-20 theorem. That earlier finding already proves the exact global threshold \(b\ge1\), the critical global \(t^{-1/2}\) envelope, and sharp leading constants. The present final claim adds a codimension-one strong-stable/generic dichotomy, exponential synchronization, an exact generic limit, and the first logarithmic correction with a common coordinate constant; those conclusions are not implied by the earlier limsup theorem.

### Equivalent formulations

Searches:
- Resultary query: Thomas cyclic sine system critical damping b=1 logarithmic relaxation t^-1/2 strong stable manifold
- Full comparison with 2026-09-20 SCOPE-thomas-critical-damping-and-sharp-algebraic-decay--4d0951ae2296

Evidence:
- The prior finding is the second semantic hit and contains the global threshold and leading envelope.
- It does not state a strong-stable manifold classification, generic exact asymptotic, or logarithmic correction.

Reasoning: Equivalent formulations of the surviving novelty are a complete asymptotic phase split at criticality and a next-order scalar normal-form invariant. Those are strictly stronger than a worst-case limsup envelope.

### Broader coverage

Searches:
- 2026-09-20 published Thomas threshold theorem
- 2007 higher-dimensional Thomas-ring literature

Evidence:
- The published prior theorem dominates the endpoint-stability and leading-envelope components.
- The older literature supplies the ring and pitchfork setting.

Reasoning: Neither inspected source dominates the full next-order dichotomy and common-constant expansion.

### Exact database or table

Searches:
- Resultary exact-topic search for the logarithmic coefficient
- Package symbolic coefficient replay

Evidence:
- No earlier published record with coefficient \(-1/20\) or a common-coordinate reciprocal-square expansion was located.
- The replay verifies the coefficient but is not novelty evidence.

Reasoning: The exact coefficient is not a database lookup; it arises from the fifth-order scalar term and the stable-fiber reduction.

### Claim versus prior implication

Searches:
- Prior limsup theorem versus final generic expansion

Evidence:
- A limsup upper bound attained on synchronized trajectories does not imply that every orbit outside a codimension-one set synchronizes to a nonzero diagonal orbit or has a convergent renormalized reciprocal-square constant.

Reasoning: The additional invariant-manifold classification and one-order-finer integration are necessary, so the full final theorem is not mechanically implied.

### Source inspections

- **Critical damping closure and sharp algebraic decay for the Thomas cyclic flow** (https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-thomas-critical-damping-and-sharp-algebraic-decay--4d0951ae2296): trigger — Earlier published theorem on the identical cyclic system and threshold; material read — Complete RESULT.md; method — Published finding full-text comparison; assessment — Covers the exact threshold and sharp leading envelope, but not the strict next-order strengthening.; evidence — Its theorem stops at limsup bounds and sharpness on synchronized trajectories.
- **Deterministic chaos seen in terms of feedback circuits: Analysis, synthesis, labyrinth chaos** (https://doi.org/10.1142/S0218127499001383): trigger — Original Thomas cyclic-feedback source; material read — Bibliographic and abstract-level material; full theorem-level text was unavailable in this run; method — Primary-source abstract inspection; assessment — Residual priority risk; no whole-document noncoverage claim is made.; evidence — Accessible material establishes the feedback-circuit/labyrinth setting, not the audited next-order critical formula.

Checked sources:
- Published Resultary finding dated 2026-09-20: Critical damping closure and sharp algebraic decay for the Thomas cyclic flow; complete RESULT inspected.
- Thomas, International Journal of Bifurcation and Chaos 9 (1999); bibliographic/abstract material.
- Chlouverakis and Sprott, Chaos 17 (2007); higher-dimensional cyclic ring and bifurcation context.
- Package scalar-series certificate independently checked.

Residual risks:
- The 1999 Thomas article was not available in full theorem-level text during this run; possible older endpoint observations remain a residual priority risk.
- The threshold and the leading sharp global \(t^{-1/2}\) envelope are already covered by the 2026-09-20 published finding and are not novel parts of this record.

## Scientific value — PASS

After subtracting the already-known threshold and leading envelope, the surviving result is still a meaningful asymptotic classification: it identifies exactly which critical trajectories are exponentially fast, proves generic synchronization and sign selection, and computes a universal logarithmic correction. That is a natural nonhyperbolic boundary refinement rather than a cosmetic constant improvement.

Checked sources:
- Published Resultary finding dated 2026-09-20: Critical damping closure and sharp algebraic decay for the Thomas cyclic flow; complete RESULT inspected.
- Thomas, International Journal of Bifurcation and Chaos 9 (1999); bibliographic/abstract material.
- Chlouverakis and Sprott, Chaos 17 (2007); higher-dimensional cyclic ring and bifurcation context.
- Package scalar-series certificate independently checked.

Residual risks:
- The 1999 Thomas article was not available in full theorem-level text during this run; possible older endpoint observations remain a residual priority risk.
- The threshold and the leading sharp global \(t^{-1/2}\) envelope are already covered by the 2026-09-20 published finding and are not novel parts of this record.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
