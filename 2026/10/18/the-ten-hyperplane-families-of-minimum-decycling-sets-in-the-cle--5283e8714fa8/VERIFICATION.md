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

The proof uses an exact Walsh-character edge-count identity and an exhaustive classification of the only equality cases. The two standalone programs independently enumerate all induced forests of size nine and ten, yielding eighty and zero, respectively, and match the ten-halfspace construction. They independently enumerate all eighty minimum feedback vertex sets, obtain reconfiguration components \(10K_8\) for simultaneous exchange limits one and two, and a connected 920-edge graph of diameter three at exchange limit three with distance profile \((1,23,48,8)\). The second program also checks the 40 disjoint token-slide edges and the nine-vertex subdivided-star shape.

Reproduce with `python3 verify_walsh_forest.py` and `python3 verify_parity_tree.py`. Standard Python 3 is the only dependency. The programs' recorded output files are `verification_walsh.json` and `verification_parity.json`. All listed computations were run against the files distributed with this mathematical result. The finite exhaustive checks do not establish any assertion about larger folded cubes. Scientific literature comparison is incomplete for unindexed sources and inaccessible full-text supplements.
