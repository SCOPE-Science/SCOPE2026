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

# Reproduction and limits

Run the two accompanying standalone Python 3 programs in the same directory; both require NumPy and SciPy. `trimer_verify.py` checks the two-component differential system against exact rational first-event calculations for independently enumerated finite rings of seven sizes and multiple unequal-rate choices; it also tests large-ring arrival-priority simulation and five slow-time crossover values. It passed 134 coded conditions. `trimer_transient.py` uses random clock orderings on a different ring to compare nine finite-time empty-triple probabilities of both parities against the differential system, passing 18 tolerance tests. Numerical tolerance and random seed are printed in the source.

Proof of the infinite-lattice identity uses the full vacancy hierarchy and bounded-solution uniqueness. The singular slow-time limit uses uniform tail bounds for one component and dominated convergence. Finite-ring checks cannot prove uniqueness on the infinite lattice, nor can they establish an exhaustive originality claim. The full text of the potentially related 1994 bipartite-lattice adsorption study was not inspected.
