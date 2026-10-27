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

## Checks and limits

The graph-counting proof was reconstructed directly from the definitions. The number of reversal-pairs in the graph with symmetric length-four words removed is \((k^4-k^2)/2\). The complement of the sequence-subgraph is reversal-closed; its divergence over \(P=\{aab:a\ne b\}\) is \(k(k-1)\). Pairwise contributions are bounded by \(2\) only for \(\{aacc,ccaa\}\), with at most \(\binom{k}{2}\) such pairs, and by \(-1\) for every omitted pair incident to a uniform triple. Since each uniform triple has odd out-degree before deletion and even out-degree in the sequence-subgraph, at least \(k\) such pairs are omitted. The resulting inequality is \(r\ge\binom{k}{2}+2k\), hence \(m\le(k^4-2k^2-3k)/2\).

No computation is required for the proof. The result is an upper bound only; it does not certify attainability or optimality. No independent audit or independent validation is claimed.
