# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-07df8435d587`

## Correctness — PASS

The clique-cover lower bound is exact by choosing one representative per cluster, which induces \(K_{h,h}\) and lets each clique cover at most one selected crossing edge. The Erdős–Faudree–Ordman cut inequality gives \(cp\ge S-2a-b\) because \(a\le b\). For the construction, optimal edge-colourings of \(K_r\) and \(K_s\) provide matchings with \(|R_c|\le|S_c|\). The condition \(h\ge\chi'(K_s)\) makes the scheduled cluster pairs distinct. Paired internal edges form edge-disjoint \(K_4\)'s, surplus larger-side matching edges form triangles, and all remaining crossing edges are \(K_2\)'s; the crossing-edge disjointness follows from the matching property and distinct cluster pairs. The count is exactly \(S-2a-b\). The finite verifier checks 90 cases but is not used as the infinite proof.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_joined_cluster_partition.py
- Erdős–Faudree–Ordman cut inequality
- current repeated-copy and mixed-cluster SCOPE theorems

### Correctness risks

- The threshold \(h\ge\chi'(K_s)\) is only sufficient, not claimed necessary.

## Originality — PASS

An earlier SCOPE theorem for \((aH)\vee(bH)\) covers unequal numbers of copies only when the component graph is the same on both sides; setting \(H=K_k\) therefore does not cover \(r
e s\). A later heterogeneous-cluster theorem allows unequal sizes but, when specialized to this family, requires a much stronger capacity condition such as \(h\ge\binom{s+1}{2}\). It covers only a subrange of the audited theorem, whose edge-colouring schedule works already at \(h\ge\chi'(K_s)\). Thus the exact unequal-size low-threshold theorem survives current broader records.

### equivalent_formulations

Searches:
- Resultary semantic search for joined unequal cluster graphs and clique partition formula
- comparison with SCOPE-clique-partitions-joins-repeated-graphs--40b72bad9da8 and SCOPE-mixed-cluster-joins-clique-partition-cover--9f930da59257

Evidence:
- The repeated-copy theorem fixes the same component graph on both sides; the later mixed-cluster theorem has stronger capacity hypotheses.

Reasoning:
Equivalent formulations by graph join, cluster graph, and cut-bound attainment were compared.

### broader_coverage

Searches:
- earlier repeated-graph theorem
- later heterogeneous mixed-cluster theorem
- Ning 2026 balanced construction

Evidence:
- These cover the equal-cluster-size direction or a stricter heterogeneous regime, not all \(2\le r\le s\) at the edge-chromatic threshold.

Reasoning:
The audited theorem is neither a corollary of same-\(H\) repetition nor of the later stronger-threshold heterogeneous theorem.

### exact_database_or_table

Searches:
- current Resultary clique-partition findings and older EFO/CEO-Pullman literature

Evidence:
- No exact table gives the two-parameter formula at \(h\ge\chi'(K_s)\).

Reasoning:
The result is an infinite construction theorem, not a known-table recomputation.

### claim_vs_prior_implication

Searches:
- parameter specialization into the later mixed theorem

Evidence:
- With equal cluster counts and no size-\(s+1\) clusters, the later theorem still requires internal-edge capacity on the \(K_s\) side, stronger than \(\chi'(K_s)\).

Reasoning:
Current broader coverage therefore does not imply the full audited parameter region.

### source_inspections

- **Exact clique partitions for joins of repeated graph copies** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-clique-partitions-joins-repeated-graphs--40b72bad9da8. Trigger: Closest earlier exact join theorem. Material read: Complete published RESULT.md. Method: Full parameter-domain and construction comparison. Assessment: PARTIAL COVERAGE only. Evidence: It permits unequal copy counts but requires the same graph \(H\) on both sides.
- **Mixed cluster joins and an explicit clique partition-cover deficit constant** — https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-mixed-cluster-joins-clique-partition-cover--9f930da59257. Trigger: Later heterogeneous cluster theorem. Material read: Published theorem and proof through the exact finite conditions. Method: Direct specialization of its hypotheses to \(J_h(r,s)\). Assessment: PARTIAL COVERAGE only. Evidence: Its capacity hypotheses cover only a stricter subrange than \(h\ge\chi'(K_s)\).
- **Assigned edge-partition verifier** — artifacts/verify_joined_cluster_partition.py. Trigger: Replay of the constructive packing. Material read: Complete source and saved output. Method: Line-by-line inspection. Assessment: Correct finite corroboration. Evidence: It checks exact edge multiplicity one and the claimed count in 90 representative parameter cases.

### checked_sources

- assigned RESULT.md and verifier
- SCOPE-clique-partitions-joins-repeated-graphs--40b72bad9da8
- SCOPE-mixed-cluster-joins-clique-partition-cover--9f930da59257
- Ning arXiv:2608.11536
- Erdős–Faudree–Ordman 1988
- Resultary search

### residual_risks

- Older clique-decomposition literature under different terminology remains a residual risk.

## Scientific value — PASS

The theorem identifies exact clique cover and partition numbers on a natural two-parameter extension of the construction behind the new \(n^{4/3}\) deficit result. The low edge-chromatic threshold and combined \(K_4\)/triangle packing remove both equal-size and parity restrictions in a structurally motivated way.

### Value sources

- Ning's balanced cluster construction
- Erdős–Faudree–Ordman cut bound
- audited unequal-size packing

### Value risks

- The sufficient threshold may not be sharp.

## Limitations

- The threshold is sufficient only.
- The number of clusters is the same on both sides.
- Current records partially overlap but do not cover the full audited parameter range.

## Disposition

**PASSED**
