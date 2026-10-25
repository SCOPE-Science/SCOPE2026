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

From the directory containing `verify_ternary_ranks.py` and `shortest_rank_witnesses.json`, execute:

`python3 verify_ternary_ranks.py --witnesses shortest_rank_witnesses.json`

Observed result: `TERNARY_SIX_RANKS_PASS ranks=60 min_lengths=21:24,22:12,26:12,27:12 maximally_required=27 direct_vectors_checked=21600`.

The first algorithm enumerates distinct positive integer profile coordinates whose total is at most \(27\), tests balanced indegrees and outdegrees, and optimizes within each ranking. Its range is complete below the threshold because any six distinct positive values of total at most \(27\) have maximum at most \(12\). The second algorithm independently parameterizes all balanced strict profiles by \((a,p,q,d)\) and two orientations of the triangle, and compares rank dictionaries and minimum lengths. The witness output contains all sixty explicit minimizing cyclic words; the checker recomputes every cyclic pair count from each word, including the wraparound pair.

The unrestricted existence and necessity are justified mathematically by the positive balanced Eulerian-circuit criterion and the five Dyck interleavings, not inferred from finite tests. Only the six off-diagonal transitions are required positive and distinct, and diagonal pair counts are zero by the homopolymer-free condition. The result does not apply to linear words, larger alphabets, longer reads, tied allowed frequencies, or the strict nine-coordinate rank channel. Independent review remains unperformed.
