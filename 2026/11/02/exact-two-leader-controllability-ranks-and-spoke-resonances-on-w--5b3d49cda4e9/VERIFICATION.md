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

The analytical proof derives the full result for all integer rim sizes, independent ring-control locations, and positive uniform spoke weights by spectral decomposition and exact rank of evaluation maps. The standalone numerical/symbolic reproducer is `check.py`; execute with `python check.py` with Python 3, NumPy and SymPy. It passed 3,286 rank comparisons when replayed, including exact rational Kalman ranks at selected resonances and independent numerical eigenspace checks through 26 rim vertices.

Finite checks cannot establish the infinite theorem or historical novelty; the supplied proof is the substantive correctness evidence. An external independent audit has not been performed. Specializing to heterogeneous edge weights, hub controls, or a single shared control input is not justified.
