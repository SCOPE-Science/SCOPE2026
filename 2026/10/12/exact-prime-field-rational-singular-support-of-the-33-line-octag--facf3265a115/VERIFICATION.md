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

# Reproduction notes

The accompanying `verify.py` contains the complete 33-line defining data, with \(\rho^2=2\). Execute `python3 verify.py` using a standard Python 3 interpreter. It computes all pair, triple, and projective-point incidence tests exactly, checks conjugation-fixed points and norms, and directly enumerates special-prime reductions in \(\mathbb F_2\), \(\mathbb F_9\), and \(\mathbb F_7\), with additional sample-prime checks. The script completed and returned `VERIFY_OK` in the scientific check. The global prime statement uses the proved norm-prime support and finite exceptional fields; the sample-prime loop is not used as a substitute for that argument. There is no external dependency and no independent audit.
