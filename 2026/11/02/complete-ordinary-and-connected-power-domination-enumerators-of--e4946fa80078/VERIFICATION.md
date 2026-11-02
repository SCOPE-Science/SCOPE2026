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

The included Python 3 standard-library `verify.py` builds graph adjacency lists from the defining row-or-column rule, simulates closed-neighborhood observation followed by repeated unique-neighbor forcing, and counts induced connected sets using graph search. It compares every coefficient with direct inclusion-exclusion and with an independently implemented connected-component recurrence on labeled complete bipartite edge graphs.

The exhaustive comparisons use \((2,2),(2,3),(2,4),(2,6),(3,3),(3,4),(3,5),(4,4)\), totaling 107336 nonempty vertex subsets. Six of these cases also receive a full coefficient comparison for connected power domination. The source was executed from the file actually included here; its test run terminated with `VERIFY_OK`. In every tested instance all successful sets finished either after the initial domination step or one propagation wave.

A direct proof valid for every \(m,n\ge2\) appears in RESULT.md. The numerical tests do not establish any infinite statement by extrapolation. Independent mathematical auditing has not been performed.
