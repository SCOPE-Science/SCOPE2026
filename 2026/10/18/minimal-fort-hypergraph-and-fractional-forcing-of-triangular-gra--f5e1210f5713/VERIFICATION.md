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
# Reproducibility

Run `python3 verify_triangular.py` using Python 3.10+ and standard library only. The companion `verify_output.txt` is the exact recorded output. The program generates graph neighborhoods from edge incidences, tests forts by scanning all exterior vertices, and enumerates minimal forts by size in \(T(n)\) for \(n=4,5,6\). It separately verifies every classified minimal fort of \(T(7)\) against all proper subsets and checks one direction of the classification in 80,000 reproducible random subsets. The verifier does not treat forts as upward closed.

Limits: These finite computations cannot establish the general formula. General validity follows from the proof in RESULT.md, including the edge-incidence reduction, inclusion-minimal edge-cover characterization, cycle extraction, exponential enumeration, and symmetry argument. Independently audited validation has not been performed.
