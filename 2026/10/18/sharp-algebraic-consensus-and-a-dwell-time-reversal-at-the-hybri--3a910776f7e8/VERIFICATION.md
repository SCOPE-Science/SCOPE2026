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

# Verification of the critical hybrid dyad theorem

The proof is the mathematical argument in `RESULT.md`. The standalone program `verification/check.py` uses only the Python standard library and can be executed via `python3 verification/check.py` after extracting the bundled files to the same directory. It checks the exact left Perron weight and critical Jacobian, integrates the flow by RK4 with step subdivisions, checks quadrant preservation and strict sup-norm decay, and tests five parameter regimes up to 60,000 jumps. It compares the computed rescaled states with the explicit \((2C)^{-1/2}\), and checks that doubling the dwell length raises \(C\) while lowering \(C/h\).

The five verified parameter tuples in the order \((d,\alpha,\gamma_r,h,\gamma_h)\) were \((1,0.7,1.1,1.6,0.55)\), \((1,0,1.3,0.5,1)\), \((0.8,0.5,0.8,2,0.25)\), \((1.3,1.4,0.3,3,0.75)\), and \((0.9,1.7,0.9,1,0.4)\). All programmatic assertions passed. The largest limiting-amplitude relative discrepancy after 60,000 jumps was less than \(0.00021\). This numerical agreement is diagnostic only: the long-time limit, global attraction and strict parameter monotonicities rest on the proof, not on finite simulation.

Independent audit has not been performed.
