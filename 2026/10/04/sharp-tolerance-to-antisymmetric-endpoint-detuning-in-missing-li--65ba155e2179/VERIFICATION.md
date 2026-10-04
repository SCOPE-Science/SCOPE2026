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

`verify_endpoint_detuning.py` reconstructs the action of the full source-normalized Hamiltonian on the three symmetry-adapted vectors for several graph sizes and endpoint mismatches.

It checks
\[
M^3=\Omega^2M,
\]
then evaluates \(e^{-iMt}\) both from the closed cubic formula and independently by a direct power-series summation. The two routes agree on deterministic test points.

The script also checks the exact maximizing times, target-fidelity threshold, fixed-error expansion, and scaled-error limit.

The replay is supplementary. Global optimality follows analytically from the exact factor
\[
[1-\cos(\Omega t)]^2.
\]

No independent audit has been performed.
