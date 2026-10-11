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

The theorem's infinite family is proved symbolically in `RESULT.md`. The finite tests below are supporting checks and are not a substitute for that proof.

Run `python3 verify_crown.py` in a Python 3 environment without installing third-party packages. Exact integer and rational arithmetic is used throughout. The verifier evaluates feasible potential profiles for every \(3\le n\le14\), restoring the full number of labeled potentials by factorial multiplicities. It independently enumerates the uncompressed coordinate assignments for \(n=3\) and \(n=4\). All 14 profile checks and both direct checks passed, ending with `ALL EXACT FINITE CHECKS PASS`.

The program checks exact values of the maximum squared norm in the polar and the number of maximizing potentials. A separate mathematical argument establishes that every maximizing polar potential corresponds to a distinct tangent facet and that the inscribed-ball radius is the reciprocal polar circumradius. The integer-potential reduction and regime exhaustion are also proved in `RESULT.md`, not inferred from tests.
