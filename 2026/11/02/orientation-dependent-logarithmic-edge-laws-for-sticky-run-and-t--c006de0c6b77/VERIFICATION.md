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
# Verification

The analytic proof is contained in `RESULT.md`. The reproducible computational checks are in `verify_sticky_occupation.py`, using Python 3 standard library only. Execute `python3 verify_sticky_occupation.py` from the extracted package directory.

For positive unit model parameters, the actual verification run passed **164 finite assertions**: exact transform and pole identities, sign constraints, consistency of the renewal mean with the transform derivative, numerical pole and right-edge asymptotics, and an event-driven simulation of 60,000 first adsorption durations for each velocity orientation (120,000 total). No trajectory time discretization was used. Approximate results were: negative initial orientation, pole rate 0.2329704513, pole residue 0.2490781493, analytic excursion mean 4.652233674, simulated mean 4.655468897; positive initial orientation, pole rate 0.0519069705, pole residue 0.0541709915, analytic excursion mean 20.094423248, simulated mean 20.029123706. The stationary bound fractions calculated analytically were 0.1769212063 and 0.0474058944, respectively.

**Scope of checks:** Simulation and floating-point tests sample finitely many trajectories and parameter values and cannot certify the general or infinite-time rate laws. The mathematical proof separately establishes the convergence, strict convexity, unique spectral pole, and asymptotic coefficients for every fixed strictly positive parameter choice. No independent audit or third-party validation is claimed.
