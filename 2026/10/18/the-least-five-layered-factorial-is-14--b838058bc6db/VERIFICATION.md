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
# Exact verification

Execute `python3 verify.py` with a Python 3 standard-library interpreter from the folder containing this file and the verifier. The checker independently enumerates positive divisors by trial division, recomputes both divisor sums by Euler products, validates the complete \(49\)-divisor partial partition and its remaining complement, and checks the relevant inequality for \(13!\). The checked arithmetic proves the stated finite five-layered witness; the monotonicity step in the written proof covers all \(1\le m\le13\). This is not a verification of any classification beyond the least index.
