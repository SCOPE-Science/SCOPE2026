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
# Reproducibility and scope

Run `python3 verify_support.py` and `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct` in the directory containing the source files. The support checker enumerates every nonempty clique/independent color-support mask pair, executes the real update rule on one representative of each present color, checks the 49-cell table, and uses a formal monomial coefficient representation to verify the first-entry census. This is exhaustive for the entire infinite graph family **because** equal-colored vertices in each part have identical futures, a reduction established in the proof.

The separately implemented direct checker enumerates all labelled initial three-colorings for 39 size pairs with at most eleven vertices and verifies both first synchronization times and the recurrent non-synchronizing structure. Its successful run checked 923463 labelled initial configurations. The logs `support_output.txt` and `direct_output.txt` record actual successful executions from these packaged sources. This computation is reproducibility evidence and does not constitute independent external validation.

All theoretical limits are explicit: the theorem addresses synchronous three-color inhibitory dynamics on complete joins only, with any positive class sizes and the new classification emphasized for clique sizes at least two. The uniform-random asymptotics refer only to initial product measure and are proved algebraically from the exact counts.
