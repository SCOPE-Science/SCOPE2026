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

Run `python3 verify.py` beside `ATTRACTORS.tsv`.

The verifier reconstructs \(t_4,t_5,t_6\), every distinct factor and its complete position-coverage mask, the inclusion-minimal factor-coverage hypergraph, and every position subset of cardinality at most \(4\). It checks that no smaller attractor exists, rechecks every positive size-four solution against all factor occurrences, verifies the exact counts \(87,40,32\), compares every solution with the stored table, and verifies the closed length-\(64\) classification.

The computation proves only the finite claim stated in the result. It does not certify any pattern for longer Thue–Morse words.
