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

Exact rational checks: invoke `python3 check_recinv.py` with Python 3. The program independently constructs the finite recursive-inflation probability law, rather than generating its expected weights from the binary-search-tree model. It checks all signature probabilities, conditional inversion means, position-resolved inversion covariances and individual peak covariances for the sizes and parameter values stated in RESULT.md. The bundled run gave 624 passed exact assertions.

The checker deliberately samples no random numbers: rational arithmetic exhausts the finite distributions for the tested sizes. It cannot prove all-size harmonic identities, priority-tree equivalence, strict threshold ordering beyond the tested sizes, or the asymptotic entropy profile; those assertions are proved in RESULT.md. No independent audit has been conducted.
