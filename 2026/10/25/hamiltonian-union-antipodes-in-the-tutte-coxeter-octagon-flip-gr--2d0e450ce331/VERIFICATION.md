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

# Verification notes

The fully executable certificates are `verify_permutation.py` and `verify_cycles.py` (Python 3, standard library only). Invoke each from the directory containing the embedded files:

```bash
python verify_permutation.py
python verify_cycles.py
```

The corresponding stored complete stdout files are `permutation_output.txt` and `cycles_output.txt`. In the current verification, both programs exited successfully, their output bytes matched the stored records, and each ended in `VERIFY_OK`.

The permutation checker exhaustively assigns duads to synthemes and independently reconstructs exchange adjacency from relative-permutation cycles. The cycle checker enumerates all 30-vertex graph matchings and 90 actual eight-cycles, and explicitly performs each valid alternating flip. Both compute all-pairs shortest paths, two-factor types, antipodal equivalence, and the same 1440-edge adjacency digest:

`ba8739d1315a1daa2d3810948317a38cdf47b81a8cd37f5377e6825b7136e6a3`

The algorithms are exhaustive for the one specified finite graph. They do not certify results for infinite families or resolve independent publication priority. The matching count of 288 is previously tabulated and is not presented as a novel result.
