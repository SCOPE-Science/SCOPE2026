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

The primary evidence is the arbitrary-parameter mathematical proof in `RESULT.md`. The checks below independently reconstruct the finite random-walk equations using exact arithmetic rather than reading the closed-form two-shore scores as input.

To replay, run:

`python3 artifacts/verify.py`

The script creates \(K_{n,n}\) with explicit adjacency, fixes each nonempty source subset, forms the full vertexwise rational linear system for the non-source potential vector, and solves it by rational Gaussian elimination. It compares every direct uniform support to the closed forms and checks the predicted optimizing profile sets at all budgets. The exhaustive domain is \(2\le n\le5\), at the fidelities \(1/3,1/2,3/4,9/10,19/20,99/100\), including all source budgets. The script separately verifies that for \(K_{4,4}\), fidelity \(9/10\) and floor \(761/1000\), precisely eight triples qualify and all lie in one shore.

Replay result:

`ALL CHECKS PASSED; parameter_cases=168; exact_vertex_linear_systems=8136; source_subsets_checked=8136; n=2..5; lambdas=1/3,1/2,3/4,9/10,19/20,99/100; n4_threshold_example=8`

These experiments are finite corroboration only. The uniqueness of the phase threshold comes from the signed rational difference and the strict monotonicity of \(F_{n,k}\); the all-parameter optimizer classification follows from the derivative argument.
