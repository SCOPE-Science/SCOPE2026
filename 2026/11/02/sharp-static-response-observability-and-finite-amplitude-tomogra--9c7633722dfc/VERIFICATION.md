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

# Reproducibility and limits

Run `python verify.py` using Python 3 and SymPy. The checker is standalone and does not require other experiment files. It checks exact rational stochasticity and return-path reachability of the six-state rank-deficient example, coprime-length period witnesses, the two graph components and the exact response rank. It reconstructs the full transition matrix of a four-state nonreversible model from three finite-amplitude stationary interventions and validates the normalized stationary-law formula for every permissible transfer in three small matrices. It also verifies the conversion between measured stationary time-occupation and jump-visit response under heterogeneous positive exit rates.

The terminal result from the performed check was:

`PASS: exact stochasticity, graph components, aperiodicity, all-amplitude line law, rank, chiral-chain finite-response tomography, and occupation conversion`

All quantities in the script are rational, and exact equalities are tested symbolically. The arbitrary-finite-order response-rank theorem is proved algebraically in `RESULT.md`; finite examples cannot establish its universal quantifier or prove priority over uninspected literature. No independent mathematical audit has been performed.
