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

The analytic argument treats every finite connected undirected graph of order at least two, every positive edge rate, every common reservoir rate \(\xi>0\), and every reservoir density in \([0,1]\). The finite test below supplements and does not replace the proof.

Run `python3 check_stationary_covariances.py` with a standard Python 3 installation. The verifier constructs exact rational continuous-time generators and solves stationary equations directly, comparing with the spectral resolvent, two-particle Green operator, edge-response, and complete-graph harmonic formulas. It reports the total exact assertions and full finite-state cases. The expected output appears in `check-output.txt`.

Finite enumerations do not establish the general theorem; the unrestricted proof uses the generator identities, positive definite resolvent, rank-one matrix update, strictly positive two-particle Green kernel, and complete-graph Johnson-spectrum decomposition. The results do not claim a full law for the stationary configuration, a quantitative mixing rate, or unequal bath refresh rates.
