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

# Verification procedure and bounds

The two standalone standard-library-only programs `verify_pairwise.py` and `verify_faces.py` reconstruct the twenty-vertex dodecahedral graph independently, enumerate all perfect matchings, construct octagon flips by independent mathematical descriptions, and independently compute the complete reconfiguration distance matrix. To replay:

```
python3 verify_pairwise.py > replay_pairwise.txt
python3 verify_faces.py > replay_faces.txt
cmp replay_pairwise.txt output_pairwise.txt
cmp replay_faces.txt output_faces.txt
```

Both programs assert their full finite domain and each prints `"status": "VERIFY_OK"` with the identical normalized graph-certificate fingerprint `a70573c1719c0680ca78fc3919e5fc78b77a442c557fc17916c5968f7b23790c`. The supplied `states_edges.json` contains 36 explicit matching masks and all their adjacency lists; count the 120 edges once each, independently reconstruct distances by breadth-first search, and check the stated degree and common-neighbour distributions. The graph is only twenty vertices; these are complete enumerations rather than experimental samples. The independent-audit channel is not performed, and no claim for larger graphs has been checked.
