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
# Verification of the topological calculation

The complete analytic proof is in `RESULT.md`. Its pivotal steps are the support-stratum exhaustion for exactly one extra output coordinate, the quotient of each moving complex two-coordinate unit sphere \(S^3\) by a circle phase to the Hopf base \(S^2\), and surjectivity of the resulting torus-bundle boundary homomorphism. These imply the exact free fundamental-group rank for every admitted dimension and exponent; they are not certified by finite computation.

Run `python3 verify_graph.py` with Python 3's standard library to reproduce the finite support-graph check. Verified dimensions \(2\) through \(7\) have, respectively, vertex counts \(2,6,24,120,720,5040\), edge counts \(1,6,36,240,1800,15120\), and connected-graph cycle ranks \(0,1,13,121,1081,10081\). The script checks vertex degree, edge uniqueness, connectedness and Euler-cycle count.

No finite data establishes van Kampen, Hopf boundary surjectivity, or independence of the norm exponent; those statements have explicit mathematical proofs in `RESULT.md`. No independent mathematical audit has been performed.
