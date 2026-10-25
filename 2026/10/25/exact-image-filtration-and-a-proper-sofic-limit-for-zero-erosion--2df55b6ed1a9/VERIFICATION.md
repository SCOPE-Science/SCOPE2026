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

# Computational verification and scope

Run `python3 verify.py` with Python 3 and only its standard library. The code independently enumerates the finite cyclic images for every \(r\in\{2,3,4,5\}\), every checked ring length from \(r+2\) through \(12\), and time steps \(n=1,2,3,4\). It checks equality against the predicted restrictions on finite cyclic zero and one runs, including constant configurations. It also compares the finite-state recognizer against direct forbidden-subword detection and checks explicit strict-descent witnesses for \(2\le r\le7\) and \(0\le n\le10\).

The complete nonperiodic infinite-lattice theorem is not established by exhaustive periodic-ring tests. It follows from the zero-run bijection and explicit inverse in `RESULT.md`. The comparison with historical literature is evidence-bound, not an independent novelty certification.
