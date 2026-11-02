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

# Verification of the three-phase migratory-occupancy allocation theorem

The proof is contained in `RESULT.md`, and `VERIFY.py` is a standalone Python 3 checker without external package dependencies. Run `python3 VERIFY.py` from the directory containing those two files. A successful run reports `VERIFY_OK assertions=94057 phases={1: 228, 2: 81, 3: 241}`.

The checker tests the positive-equilibrium inverse, cost value, budget target feasibility, strict threshold ordering, all three optimal branches, and random feasible perturbations for 550 seeded parameter sets. A fully exact rational construction checks the symmetric case, and the radical transition thresholds are also tested numerically. All domain parameters are positive; the two occupancy targets lie strictly between zero and one. The tests are finite observations, so universal correctness relies on the analytical radial edge-reduction and odds-coordinate AM–GM proof in `RESULT.md`.

The conservation objective is mathematical: constant positive colonization rates at linear rate-unit expense, fixed extinction rates, continuous-time two-season dynamics, and attracting equilibrium occupancy targets. It excludes finite-year discrete probability rate caps, stochastic extinction risk and empirical habitat management costs. The best-knowledge literature comparison recognizes the original seasonal occupancy equilibrium as previously published. A possible equivalent optimization statement in broader two-type SIS/positive-systems literature remains a historical-priority risk. No independent audit has been performed.
