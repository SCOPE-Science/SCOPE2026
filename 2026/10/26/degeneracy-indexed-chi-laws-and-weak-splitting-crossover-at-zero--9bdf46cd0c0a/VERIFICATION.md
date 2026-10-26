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

The standalone `critical_defects_verify.py` program was executed with Python, NumPy and SciPy. Its deterministic finite-volume checks returned: 134 combinatorial / moment-limit checks; 24 nonzero weak-detuning checks; 631 finite-generator stationarity balance checks. Execution command: `python critical_defects_verify.py`.

The analytic proof uses an exact finite canonical identity followed by the lattice local central limit theorem and a log-concave negative-binomial lower-tail bound. The finite computations test these identities and compare finite sizes with the claimed integrals; they cannot replace the proof of convergence for every system size. Source comparisons are limited to the identified accessible full texts, published descriptions, and scholarly indexing; independence and historical priority have not been established.
