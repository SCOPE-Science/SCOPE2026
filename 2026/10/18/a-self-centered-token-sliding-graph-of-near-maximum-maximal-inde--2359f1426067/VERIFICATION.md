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
# Reproducibility and limits

Run from the extracted scientific package root:

```
python3 verification/verify_direct.py
python3 verification/verify_metric.py
```

The first verifier independently recursively enumerates all maximal independent vertex sets of the required size in the *original labelled Möbius ladder*, then tests each original one-edge slide for odd \(n\in\{5,7,9,11,13,15\}\). It checks both state coverage and exact adjacency with the cyclic interval model, every state eccentricity, the degree distribution and edge count. Its exact observed stdout is `verification/direct-output.txt` and terminates with `VERIFY_OK`.

The second verifier independently enumerates maximal independent sets via combinations in the original host graph for odd \(n\in\{5,7,9,11\}\), and exhaustively compares BFS shortest-path distances with the lifted Manhattan formula on the symbolic graph for odd \(n\in\{5,7,9,11,13,15,17,19,21,25\}\). It hashes the ordered all-pairs distance tables, prints one SHA-256 digest per case, and terminates with `VERIFY_OK`. Its exact stdout is `verification/metric-output.txt`.

The scripts are standard-library-only. Their assertions check finite instances; they do not independently certify the infinite graph classification or historical originality. The infinite statement follows from the cyclic complement-gap classification and the lifted strip-geodesic proof, whose assumptions and quantifiers appear in `RESULT.md`. No third-party full text is included.
