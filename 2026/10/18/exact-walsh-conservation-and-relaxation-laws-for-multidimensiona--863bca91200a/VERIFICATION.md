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

The ordered-pair rate is gamma_i x_s x_(s xor d) K_i(d)/n, giving mass conservation, nonnegative inflow at a zero coordinate, and stationary uniform frequencies. At the uniform state a character perturbation gives a contribution proportional to (chi_A(e_i)-1)(1+chi_A(d))/(n Q) in each i,d term: the factor 1+chi_A(d) is from differentiating both quadratic inputs. Thus only i in A and even A-parity active displacements contribute, each with coefficient -4 gamma_i/(n Q). Nonempty characters span the simplex tangent space. For the full equation, exchanging the two inputs at fixed displacement d multiplies the quadratic A-moment by chi_A(d); it is zero at odd A-parity. Positivity of all rates therefore gives exact nonlinear conservation for each zero mode, and a nonzero negative linearization excludes conservation of that moment. Split into fixed conserved coordinates z and decaying coordinates y; the y-Jacobian is diagonal negative at uniform frequencies, so the analytic implicit-function theorem gives the unique nearby stationary y=h(z). Its symmetric part stays uniformly negative near the graph; integrating the Jacobian along the segment from h(z) to y gives a differential inequality for squared transverse distance on an invariant small ball. This also covers the degenerate case of no decaying directions, when the local field is zero. At the strict high threshold the active displacements are precisely d!=0 with d_i=0. Counting even parity among the remaining selected coordinates gives 2^(n-1)-1 for singletons and 2^(n-2)-1 otherwise; minimizing each group yields the asserted gap for n>=3 and the pair slow modes at equal rates. For n=2, d=00 and d=11 can never flip under the strict admissible rules, leaving only odd total parities and exact conservation. The supplied `checker.py` and its finite verification description were inspected, not executed; the decisive conclusions are symbolic and local, not global or finite-population convergence claims.

## originality

PASS

Credit the explicit all-n active-even-parity spectrum and exact zero-Walsh-mode characterization for this fixed deterministic model, with the analytic local selection theorem and sharp high-threshold spectrum. Mintz et al. previously introduced precisely this normalized model, studied neutral manifolds, and in Supplement §9 observed conservation of equilibrium class masses and linked zero eigenvalue multiplicity with manifold dimension. That is material same-model overlap, not merely related terminology. Neither the observation nor the finite symmetry tables gives the character-by-character active-set test, the proof of necessity and sufficiency for individual Walsh moments, or the general unequal-rate gap. The mechanism of Fourier diagonalization and the idea of neutral or constrained equilibrium manifolds are not originality claims. The independently retrieved supplement informs this verdict; the frozen note about unavailable supplementary material is not an ongoing access limitation for the inspected sections.

## value

PASS

For a concrete opinion-dynamics model known through finite symmetry tables, the all-dimensional formulas distinguish a merely linear neutral mode from an exact nonlinear invariant, determine the local equilibrium selected by initial conserved data, and identify what actually controls the relaxation timescale. In particular the slow equal-rate high-threshold perturbations are two-issue correlations, not singleton marginals, and the two-issue parity exception holds at all admissible thresholds. These are useful exact local predictions, not global or stochastic claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
