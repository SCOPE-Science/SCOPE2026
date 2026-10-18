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
Extract all files from this finding into one directory. With Python 3 and only standard-library modules, execute:

```
python3 verify.py
python3 check_mod2.py
```

`verification_output.txt` contains the literal expected lines from both scripts, recorded from their actual executions. The integer matching verifier enumerates precisely all 910 nonempty faces, 453 pairs, and 4 critical faces for the size-eight graph; it exhaustively verifies acyclicity in the oriented Hasse graph and computes all integral Morse boundaries, including the critical 3-to-2 boundary, using signed incidence cancellations. At sizes six and seven, it separately proves acyclic matchings leaving one vertex and one edge.

The second script independently reconstructs each neighborhood face set, forms all mod-two simplicial boundary columns, and computes exact ranks by bitset Gaussian elimination. These are finite complete enumerations for the three stated graph sizes, not sample searches. Field checks alone do not establish an integral homotopy type; that conclusion follows from the verified Morse reductions and topological attaching-map argument in the proof. This package does not contain an external or independent human audit.
