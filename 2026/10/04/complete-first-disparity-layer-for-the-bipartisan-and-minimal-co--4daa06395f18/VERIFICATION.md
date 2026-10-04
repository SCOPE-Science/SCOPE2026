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
The embedded `verify_bp_mc_first_layer.py` performs an exact census of every labeled tournament through order \(6\).

The bipartisan set is computed primarily from positive Pfaffian null vectors of odd principal subtournaments. On every one of the \(1440\) strict order-\(6\) cases, the resulting maximal lottery is independently recomputed with exact rational Gaussian elimination.

The minimal covering set is computed by exhaustive enumeration of all covering subsets. Brandt's iterative algorithm, initialized from the bipartisan set, is independently replayed on every tournament through order \(5\) and on every strict order-\(6\) case.

The verifier confirms:
- \(BP(T)=MC(T)\) for every tournament through order \(5\);
- \(1440\) strict cases among the \(32768\) labeled order-\(6\) tournaments;
- exact incidence \(45/1024\);
- the order-\(6\) histogram
\[
(1,1):6144,\quad
(3,3):20480,\quad
(5,5):4704,\quad
(5,6):1440;
\]
- exactly two strict isomorphism classes;
- orbit size \(720\) for each class;
- canonical encodings \(344\) and \(345\);
- the two displayed maximal lotteries and payoff vectors.

Run:

`python3 verify_bp_mc_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation establishes only the complete first disparity layer.
