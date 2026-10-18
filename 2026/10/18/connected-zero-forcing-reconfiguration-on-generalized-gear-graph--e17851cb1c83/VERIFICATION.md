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

Run `python3 verify_gear.py` with Python 3.8 or later. It requires only the standard library. The script constructs generalized gears directly from cycle and hub edges, then applies all currently available ordinary zero-forcing steps until closure. For each parameter pair \(4\le m\le8\), \(1\le r\le6\), it exhaustively checks that no pair of initial vertices forces the graph and identifies every three-vertex forcing set. It separately generates the classified triples and compares the two sets exactly.

The exchange graph is then constructed from a dictionary indexed by all two-element subsets of each optimum. The tests cover its degree histogram, total edge count, connectedness, the hub-cycle subgraph and the one-step attachment property. Across 30 graph cases, 164,295 candidate triples were tested, giving 2,250 minimum sets. The actual output is in `verification_output.txt`. This is finite verification only; arbitrary-parameter validity is supplied by the mathematical proof in RESULT.md.

No independent scientific audit has been performed.
