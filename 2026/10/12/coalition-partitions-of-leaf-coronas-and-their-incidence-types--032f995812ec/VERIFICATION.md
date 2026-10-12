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

The bundled program `verify.py` uses the standard library only and reads no external inputs. It enumerates all restricted-growth strings of length \(2n\) for core sizes \(2\le n\le5\), thus enumerating each unordered set partition once. It tests the four-block coalition-partition criterion and verifies the incidence support types and the exact number
\[
2^{n-3}(4^n-5\cdot2^n+6).
\]
For every such partition it also compares the private-leaf-pair domination test with actual adjacency-based domination on empty, complete, and path base graphs. It checks a four-block construction for every \(2\le n\le50\).

Execute `python3 verify.py` from the extracted files. The recorded output from an actual execution of that bundled code is:

```text
VERIFY_OK
n=2: partitions_checked=15, max_coalition_blocks=4, optimal_partitions=1, supporting_edge_type_counts={2: 1}
n=3: partitions_checked=203, max_coalition_blocks=4, optimal_partitions=30, supporting_edge_type_counts={2: 6, 3: 24}
n=4: partitions_checked=4140, max_coalition_blocks=4, optimal_partitions=364, supporting_edge_type_counts={2: 28, 3: 288, 4: 48}
n=5: partitions_checked=115975, max_coalition_blocks=4, optimal_partitions=3480, supporting_edge_type_counts={2: 120, 3: 2400, 4: 960}
all direct graph-domination equivalence checks passed for empty, complete and path bases n=2..5
four-block construction checked through n=50
```

The exhaustive cases comprise
\[
15+203+4140+115975=120333
\]
distinct partitions. Finite enumeration supports but does not prove the general statement: the infinite proof is the exact vertex-cover reduction, its universal four-vertex bound, three-support classification and automorphism-quotiented surjection count in `RESULT.md`.
