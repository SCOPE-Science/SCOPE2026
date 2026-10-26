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

# Exact computational verification

The standalone `verify.py` needs only Python 3 standard-library modules. Run `python3 verify.py` from the directory containing the program. All assertions passed when run with the packaged source, before packaging.

The program enumerates every integer from `0` through `1023` as one neutral six-voter strict-majority extension; identifies the exactly twelve degree-balanced winning-triple sets; checks the Banzhaf and Shapley–Shubik pivotal sums independently for all twelve; computes all exact nearest-fair edit distances across the entire finite domain; identifies the twelve maximal-distance words with explicit voter-specific tie-dictators and anti-dictators; checks exact design incidence, the complete fair-pair Hamming spectrum, the crown adjacency pattern, and every permutation of voter labels on a representative.

The check has no numeric tolerances or probabilistic shortcuts. It is a finite exhaustive verification and supports only the precisely stated six-voter family. It is not a search of all published literature, not an infinite-case proof, and not an independent audit.
