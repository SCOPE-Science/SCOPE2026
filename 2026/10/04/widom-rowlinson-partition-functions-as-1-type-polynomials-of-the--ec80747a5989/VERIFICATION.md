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

The bundled checker tests the metric and graph formulations independently on finite instances.

For every labeled graph on at most five vertices, it interprets edges as parameter distance \(1\) and nonedges as distance \(2\). It then enumerates all \(3^n\) candidate distance vectors \(f:V\to\{1,2,3\}\), tests the Katětov inequalities
\[
|f(u)-f(v)|\le d(u,v)\le f(u)+f(v),
\]
and records the complete coefficient dictionary indexed by the numbers of 1-, 2-, and 3-values. Separately, it evaluates
\[
\sum_{Z\subseteq V}y^{|Z|}\prod_{C\in\pi_0(G-Z)}(x^{|C|}+z^{|C|})
\]
by explicit connected-component search, and compares the dictionaries exactly.

At six vertices, where there are \(2^{15}=32768\) labeled graphs, the script independently checks the scalar count using precomputed forbidden \(1\)-\(3\) edge masks and compares it with \(\sum_Z2^{c(G-Z)}\). It also checks that the minimum and maximum are unique and equal to \(127\) and \(729\), respectively. Finally it verifies the path values through eight vertices.

Replay command:

`python3 artifacts/verify.py`

Observed output:

```
all_graph_metrics_poly_checked_n_le_5 1100
all_6_vertex_graph_metrics_scalar_checked 32768
path_counts_n_0_to_8 [1, 3, 7, 17, 41, 99, 239, 577, 1393]
extremes_n_6 127 729
VERIFY_OK
```

The computation verifies the finite combinatorial core. The identification with complete 1-types for all finite parameter sets uses universality and ultrahomogeneity of the Fraïssé limit and is proved deductively in `RESULT.md`.
