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

# Reproducibility and verification

Execute `python3 artifacts/verify_graph_rank.py` using only Python's standard library. A successful run terminates with `VERIFY_OK`. The program computes commutator matrices directly, independently groups vertex colorings by equal-edge sets, independently evaluates matroid-flat partitions, and compares the resulting rank distributions. It additionally enumerates every ordered commuting pair in small cases.

Checks exercised: one-edge graph, triangle, four-vertex path and star, four-cycle, diamond and \(K_5\), with prime fields \(\mathbf F_2\) and \(\mathbf F_3\) as feasible. The triangle over \(\mathbf F_2\) has rank multiplicities \((2,6,32,24)\); a four-vertex tree over \(\mathbf F_2\) has \((2,18,54,54)\). The ten-edge graph \(K_5\) over \(\mathbf F_2\) has maximal commutator rank nine. No non-prime extension field was directly enumerated; the characteristic-independent incidence-rank proof establishes the statement for all finite fields. No computational log substitutes for the mathematical argument, and no independent scientific audit has occurred.
