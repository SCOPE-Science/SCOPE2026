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

The analytical argument in `RESULT.md` proves the exact Markov/record coupling, stochastic ordering of jump indicators, the Meixner orthogonality identity, and the three-variable real-stability phase boundary. Reproduce finite consistency checks using `python check.py`, requiring SymPy.

`check_output.txt` records 120 passed symbolic, rational, and numerical assertions. Exact algebra verifies all three Rayleigh differences and their completed-square forms. Finite enumeration is not the proof of the all-time negative correlations or the three-variable all-real criterion; those rely on the stated analytic identities and the known multiaffine stability theorem.

The Meixner factorization is a consequence of the previously published univariate generating function. The model-specific threshold remains subject to independent mathematical validation and a specialist historical-priority check; no higher-time strong-Rayleigh classification is claimed.
