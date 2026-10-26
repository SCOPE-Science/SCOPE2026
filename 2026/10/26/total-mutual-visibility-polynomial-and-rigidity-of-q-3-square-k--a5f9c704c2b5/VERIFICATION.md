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

Run `python3 verify.py` with Python 3.10 or newer and no third-party dependencies. The program constructs the labeled graph and enumerates the admissible vertex subsets by a forbidden-pair backtracking algorithm, independently of the proof's parity-and-component enumeration. It compares complete coefficient vectors for \(1\le n\le6\), including the exceptional \(n=2\) top coefficient. A separate breadth-first search tests shortest paths whose internal vertices avoid each selected set, on deterministic samples for \(1\le n\le3\); this checks the key criterion directly from the visibility definition on those samples.

Passing output terminates with `VERIFY_OK all polynomial coefficients and sampled direct geodesics` and includes cardinality coefficient vectors for each checked \(n\). Finite verification cannot establish the formula or maximality for all \(n\); those are established by the proof. The exact sampling seed is included in the code. Independent external verification is not claimed.
