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
The stationary two-state hub/count Markov generator is constructed directly in `verify.py` from the four possible leaf-spin transitions and the hub-flip transition. Running `python verify.py` with `requirements.txt` checks each row-sum generator convention, stationarity residuals, exact two-point formulas, and finite-size second/fourth/sixth moment comparisons with the beta limit. The proof itself independently establishes moment convergence by compactness and exact stationary generator identities. These computational checks cover selected finite sizes and noise rates only, and cannot certify a general theorem or historical priority. Independent audit has not been performed.
