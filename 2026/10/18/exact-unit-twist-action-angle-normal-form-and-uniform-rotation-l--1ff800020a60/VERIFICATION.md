---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For a>1/4, F_a(x,y)=(y,(a−y+y²)/x) is positive and smooth on (0,∞)^2; V=(x²+y²−x−y+a)/(xy) is invariant and ω=dx∧dy/(xy) is symplectically preserved. The vector field X=xy(−V_y,V_x) satisfies i_X ω=−dV and is the Lie symmetry whose EXACT time, not a time-rescaling, is conjugate on each elliptic conic h∈(h_c,2) to dz/dt=1−hz+z², period T(h)=2π/sqrt(4−h²). Diagonal high-intersection section z_+(h) is a smooth unique transversal per oval. Using flow time t mod T(h), ω=dh∧dt=(T/2π)dh∧dθ; canonical I(h)=∫_{h_c}^h ds/sqrt(4−s²)=φ_a−arccos(h/2), φ_a=arccos(h_c/2). The actual Möbius-map signed flow time from 0 to −1 yields Δθ=−arccos(h/2)=I−φ_a and ∂Δθ/∂I=1; area=2πφ_a and normalized I,deficit uniform. Independent SymPy verified V◦F=V, ω invariance and Hamiltonian components; analytic flow integration verifies all levels. Excludes central equilibrium and parabolic boundary; positivity requires a>1/4.

## originality

PASS

Best-of-knowledge: the source already establishes invariant conics, the signed pointwise rotation formula, invariant log density and Lie-flow conjugation. The final global canonical chart, energy-to-area action integral, parameter-independent unit twist, and normalized-area uniform deficit are additional explicit quantitative deductions; novelty is a synthesis rather than independent rediscovery of the recurrence.

## value

PASS

An explicit global CANONICAL annular shear converts a nonlinear map on all elliptic levels into a parameter-independent twist map and determines its full logarithmic area and exact rotation distribution. The unit twist and finite area are dynamical invariants potentially useful for resonance/measure calculations; they are not asserted to persist outside the stated elliptic region.

The dated certificate retains the supplied scientific assessment, sources and limitations.
