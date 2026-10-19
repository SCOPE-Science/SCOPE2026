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

The proof derives exact counts by run compositions, handles the all-one-bit boundary, compares balanced and unbalanced transition profiles, proves the discrete mode of a binomial product, and applies Stirling asymptotics. `verify.py` checks every literal binary word through length seventeen and independently evaluates every feasible four-count profile through length one hundred twenty, including all maximizing spectra. To replay, execute `python verify.py` with Python 3.9+. Exhaustive finite tests corroborate but cannot replace the global proof. No independent audit has been performed.
