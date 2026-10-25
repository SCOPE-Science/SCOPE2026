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

Run `python checks/check_odp_nilpotency.py` in the extracted package directory, with standard Python 3. The checker lists all signed nonzero partial translations through chain length 11, eliminates the duplicate empty map, and calculates each least zero power by direct composition. Separately, a trailing-run automaton produces rank-generating polynomials for masks avoiding a prescribed run. The two constructions agree for every cumulative index and rank. The checker also checks the established formula for the total number of nilpotents.

The direct exhaustive total is 8045 distinct nilpotents for sizes 1 through 11, with per-size totals 1, 3, 9, 23, 53, 115, 241, 495, 1005, 2027, 4073. Exact integer cumulative counts evaluated at powers of two through 4096 approach the proposed lattice CDF value at one specific lattice location; those numerical checks do not prove convergence. The proof instead uses a factorial-moment Poisson limit for minimally started runs and a geometrically tight mixture over displacement sizes.

The scope is precisely the chain order-preserving partial-isometry monoid and its least zero powers. The test does not cover arbitrary partial transformations or all asymptotic subsequences. Any independent mathematical assessment remains unperformed.
