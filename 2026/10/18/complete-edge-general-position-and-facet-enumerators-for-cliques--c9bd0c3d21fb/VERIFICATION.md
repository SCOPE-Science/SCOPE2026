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
# Verification record

Reproduction command (Python 3, standard library only):

```sh
python3 verify.py
```

The script constructs each graph directly, enumerates every graph-distance shortest path by BFS and predecessor backtracking, and independently generates forbidden edge-triples. It tests all edge subsets against those geodesic triples, then tests maximality by every one-edge extension. It independently expands both counting formulas and verifies exact bivariate coefficient dictionaries and optimum sizes. Six parameter profiles were exhausted: `(1,1,1)`, `(2,3,2)`, `(1,1,1,1)`, `(2,1,2,1)`, `(2,2,2,2)`, `(1,1,1,1,1)`, totaling 55,360 subsets. The exact observed output is embedded as `verify_output.txt`.

All computations are finite; the symbolic geodesic argument in `RESULT.md` supplies the proof for arbitrary positive multiplicities. An exhaustive run for the listed small instances cannot certify the universal theorem. The third-party 2026 corona-product article was not available in complete text for priority inspection. No independent scientific audit has been performed.
