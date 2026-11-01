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

# Reproducible verification

The derivation reduces the three-dimensional sampling law to a polynomial axial density and uniform conditional disks. The supplied independent executable `cap_verify.py` performs the following actual checks:

1. Exact symbolic integration of axial moments through degree four, comparison with the stated \(M_1\) and \(M_2\) rational formulas, and exact differentiation of the normalized ratio.
2. Exact endpoint evaluations \(Q(0)=10/7\), \(Q(2^-)=7/4\), and the cubic coefficient \(25/63\) in the full-ball expansion.
3. Separate floating-point quadrature of the axial physical-density integral at five cap heights.
4. Direct independent simulation of two volume-uniform points, at four different cap heights, with deterministic random seed and stated loose Monte Carlo tolerances.

Invocation: `python -m pip install -r requirements.txt && python cap_verify.py`.

Actual terminal checks included `EXACT_AXIAL_MOMENT_AND_INVERSE_MONOTONICITY_IDENTITIES_PASSED`, `INDEPENDENT_AXIAL_QUADRATURE_PASSED`, `INDEPENDENT_VOLUME_POINT_PAIR_SIMULATION_PASSED`, and `ALL_CHECKS_PASSED`.

The identity and monotonicity proofs are analytical. Simulation is finite and cannot certify the statements for all parameters. There is no numerical-noise reconstruction bound and no independent mathematical audit.
