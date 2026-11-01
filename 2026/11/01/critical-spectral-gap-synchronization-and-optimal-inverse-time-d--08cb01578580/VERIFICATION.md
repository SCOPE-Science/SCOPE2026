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
# Reproduction and mathematical checks

Execute `python3 verify.py` from the extracted package directory; Python 3 standard library only. The checker deterministically verifies 4,000 random-complex monotonicity identities and inequalities, and for complete three-vertex, path three-vertex and edge two-vertex graphs it verifies the exact centered-energy derivative and fourth-order Runge–Kutta energy upper bounds at three spectral-gap offsets. It checks the critical two-node exact trajectory and subcritical antisymmetric equilibrium at several parameters. In the saved review, the checker returned `PASS 5447 finite checks`.

The universal proof is analytical. For arbitrary graph vertices and initial data it uses (i) cubic strong monotonicity, (ii) the graph Rayleigh spectral-gap lower bound, (iii) convex quartic moment inequality, and (iv) scalar comparison for the resulting Riccati-type energy inequality. Global existence follows from a separate logistic bound on the total squared amplitude. Identification of orbit limits relies on the established analytic-gradient convergence theorem and the center-stable manifold theorem; the argument for nullness of the zero-equilibrium basin uses their standard local conclusions and time-integer preimages.

Finite trajectories do not prove all-time convergence, no random test certifies the infinite theorem, and no independent audit has been performed. The calculation establishes an optimal **rate exponent** via the two-node witness, not an optimal numerical constant in the general upper bound. Priority for the endpoint remains a risk because the full 2010 Chung–Slotine paper was inaccessible even though its abstract was checked.
