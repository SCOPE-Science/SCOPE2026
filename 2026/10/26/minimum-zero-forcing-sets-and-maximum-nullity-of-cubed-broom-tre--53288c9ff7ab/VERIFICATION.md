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

The graph builder in `verify.py` explicitly adds the edges of the broom, computes all tree distances by breadth-first search, and constructs ordinary cube adjacencies for distance at most three. The zero forcing simulator applies one genuine force per step, recomputing white neighborhoods. For each \(2\le t\le5\) and \(2\le\ell\le9\), it enumerates all initial sets of size \(t+2\), compares them to the theorem's complete classification, and verifies the absence of forcing sets of size \(t+1\). It also verifies that the positive-semidefinite Gram construction has precisely the prescribed off-diagonal graph and rank \(\ell-1\) by exact rational elimination.

To reproduce, run `python3 verify.py` from the directory containing the standalone files. The expected output is recorded in `verify_output.txt`. The tests cover 32 pairs of parameters. Finite tests do not prove the all-order statement: the proof uses the true-twin geometry, an exhaustive first-move argument, explicit forcing schedules, and an exact rank construction. No independent mathematical audit has been undertaken.
