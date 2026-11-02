---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification scope

Run `python verify_two_phase_motility.py` from the package directory with NumPy, SciPy and SymPy installed. The checker uses an independent upwind continuous-time Markov-chain generator, not the continuum integral formula, to approximate transport. It constructs stationary laws and solves a separate finite-state Poisson equation, then compares the jump quadratic-variation diffusivity against the claimed continuum expression at 80, 160 and 320 sites across three coefficient choices. Discrepancies decay linearly with grid spacing. It also checks the symbolic differentiation identities, exact optimum and enhancement relation; 240 seeded random coefficient cases; and sampled global-envelope inequalities.

## Proof-bearing steps

The infinite-dimensional correctness rests on the generator calculation, the periodic corrector with difference \(c=L/J\), boundedness of that corrector, and the martingale variance growth. The algebraic sharp maximum depends on the one-positive-root quadratic and strict signs of the logarithmic derivative. The checker cannot establish all-parameter exactness, absence of historical priority, empirical feasibility with unbounded local coefficients, or independent audit.

## Observed results

The 9 lattice diffusivities approached their analytic targets monotonically under refinement; the script finished with `PASS symbolic identities; 240 random envelope checks; 9 independently built CTMC corrector checks`. The checker is supplied as complete source. All claims are restricted to the stated model and parameter domain.
