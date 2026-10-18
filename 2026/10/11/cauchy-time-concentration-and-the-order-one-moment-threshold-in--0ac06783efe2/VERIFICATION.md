---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

In q=arctan(√κx)/√κ, the ODE becomes Hamiltonian q′=y, y′=−V′(q) with V(q)=κ^{-1}log sec(√κ q); the energy is L_A/(2κ), domain |q|<π/(2√κ) and every positive energy gives a closed oval. The inverted potential density g(v)=√κ/(e^{2κv}−1)^{1/2} is integrable with ∫g=h, giving T_A√L_A→2π. Uniform integral control of time primitives yields the triangular physical-time phase, hence the tangent pushforward Cauchy law. Direct dt/dx produces the stated exact density. After u=log(1+κx²), fixed-p absolute moments reduce to a beta integral for p<1, exactly 4√L/(T√κ) for p=1, and endpoint Laplace/Gamma integral for p>1, giving the claimed constants. **Presentation correction:** in RESULT.md Step 2 the bound I_E−Q_A stated for ∫_q^{Q_A} over possibly negative q is too small: the universal bound is 2(I_E−Q_A), still o(1), so its proof conclusion and theorem remain valid. Independent exact algebraic inspection rather than finite logs establishes limits. The inspected verify.py quadrature is only corroboration.

## originality

PASS

The Llibre–Rondón global-center classification and linearly conjugate Appis–Llibre family cover the periodicity context; period methods can cover monotonicity/scaling, which are not claimed as new. Compared with directly relevant published records on other cubic center high-energy periods and logarithmic phases, none of the checked statements gives the complete *original-time x-coordinate* Cauchy distribution together with sharp all-p fixed-order moment threshold and coefficients. The physical-time normalization and statistic differ from velocity moments, logarithmic-energy fractions and other cubic families.

## value

PASS

This provides an explicit nontrivial weak-limit law emerging from compact periodic orbits of a concrete cubic global center and a sharp moment-integrability phase transition, including constants and uniform time-phase behavior. Such occupation statistics are a natural dynamical invariant beyond existing center-classification and period monotonicity; the p=1 critical boundary and p>1 amplitudes distinguish weak convergence from uniform integrability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
