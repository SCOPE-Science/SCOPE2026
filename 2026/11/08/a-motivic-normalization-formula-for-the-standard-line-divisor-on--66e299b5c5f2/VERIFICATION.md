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

The symbolic proof is in `RESULT.md`, Steps 1–6. The critical nonstandard step is the normalization-fiber bookkeeping over nonsplit fields: the high-multiplicity support is \(6E\), its normalization preimage is \(6E^2\), the nodes are \(3E^3\), and their preimage is \(6E^3\). This gives the motivic class without falsely assuming all branches above a rational singular point are rational.

Run `python3 verify.py` with standard-library Python. Expected output:

`VERIFY_FERMAT_MOTIVIC_OK prime_degree_cases=44`

The program enumerates all projective points in each tested prime field, computes geometric line multiplicity directly from pairings, and checks three independent predicted multiplicities for 44 admissible prime-degree pairs. It does not attempt to prove the all-prime, all-degree, or all-extension claims; these follow from the geometric argument. No computer algebra system, network service, or additional data files are needed.
