# Independent scientific audit — 2026-10-01

Record: `SCOPE-20260920-9f930da59257`

Disposition: **passed**

The claim in `RESULT.md` is accepted unchanged. This audit assesses one final claim and requires separate correctness, originality, and scientific-value passes.

## Correctness — PASS

Choosing one representative from every cluster induces \(K_{h,\ell}\), so every clique cover needs at least \(h\ell\) cliques and the cluster-pair cover attains it. Across the two sides there are \(s\) crossing edges and \(a,b\) internal edges; the Erdős--Faudree--Ordman inequality gives \(\operatorname{cp}\ge s-a-b-\min(a,b)\), and the load hypothesis implies \(a\le b\), hence \(s-2a-b\). The cyclic assignment of each first-side internal edge uses each cluster pair at most once because \(\binom p2\le\ell\) and balances second-side loads within one; the second hypothesis supplies distinct second-side edges for all \(K_4\) pairings. In a second-side cluster, the remaining internal-edge count is at most the number of unused first-side cluster pairs because \(e_j\le\binom{q+1}2\le h\), so edge-disjoint triangles finish the internal edges and leftover crossings are single edges. Counting gives equality. For the asymptotic choice, \(p\sim c n^{1/3}\), \(q\sim c^{-1/2}n^{1/3}\), \(h\sim n/(2p)\), \(\ell\sim n/(2q)\); all capacity conditions eventually hold, and the three \(n^{4/3}\) terms are \(c/2\), \(1/(4\sqrt c)\), \(1/(4\sqrt c)\). At \(c=2^{-2/3}\) these sum to \(3/2^{5/3}=0.9449407874\ldots\), independently rechecked numerically.

The package computations, where present, were treated as supporting checks rather than substitutes for the general proof.

## Originality — PASS

### Equivalent formulations

**Searches/source IDs**
- Published SCOPE archive query: clique partition cover mixed cluster joins unequal cluster sizes q q+1
- Published SCOPE archive query: clique partition covering deficit explicit constant heterogeneous cluster join
- arXiv:2609.20305

**Evidence**
- The nearest published SCOPE records are the equal-cluster-count unequal-size theorem from 2026-09-19 and the unequal-copy-count same-base-graph theorem from 2026-09-18.
- Ning's primary abstract establishes only the \(\Theta(n^{4/3})\) deficit scale; searchable descriptions of its construction use the balanced uniform join.

**Reasoning**

Neither predecessor is equivalent to a join whose two sides simultaneously have different cluster sizes/counts and whose second side mixes \(q\) and \(q+1\) clusters.

### Broader coverage

**Searches/source IDs**
- SCOPE-2026-09-19 exact clique partitions for joined unequal cluster graphs
- SCOPE-2026-09-18 exact clique partitions for joins of repeated graph copies
- Ning arXiv:2609.20305

**Evidence**
- The 2026-09-19 theorem treats \((hK_r)\vee(hK_s)\) with the same number of clusters on both sides.
- The 2026-09-18 theorem treats \((aH)\vee(bH)\) with the same base graph on both sides.
- Ning's construction is the balanced uniform family \((hK_k)\vee(hK_k)\).

**Reasoning**

These exact formulas cover important slices but do not dominate the heterogeneous mixed family or its exact-order remainder mechanism.

### Exact database or table

**Searches/source IDs**
- Published SCOPE semantic search for the explicit coefficient \(3/2^{5/3}\) and mixed cluster joins

**Evidence**
- No prior table/database entry with the mixed finite formula or displayed limsup constant was located.

**Reasoning**

The coefficient comes from optimizing an asymptotic construction, not from a finite database.

### Claim versus prior implication

**Searches/source IDs**
- Full published SCOPE RESULT for joined unequal clusters (2026-09-19)
- Full published SCOPE RESULT for repeated-graph joins (2026-09-18)
- Ning 2026 primary abstract

**Evidence**
- The two earlier SCOPE constructions require, respectively, equal cluster counts or a common base graph; their hypotheses do not instantiate the current \(q/q+1\) mixed side.
- The primary abstract determines only the order of the deficit.

**Reasoning**

Combining the earlier statements does not mechanically imply the new load-balancing theorem: one must prove simultaneous edge assignment across nonuniform second-side clusters and then re-optimize the exact-order asymptotics.


### Source inspections

- **Exact clique partition numbers for joined unequal cluster graphs** — `SCOPE-20260919-07df8435d587`. Trigger: Closest published SCOPE result allowing unequal clique sizes. Material read: Complete published RESULT.md. Method: Published SCOPE source tree. Assessment: NOT_COVERING; it requires equal cluster counts and uniform cluster size within each side. Evidence: Its theorem is \((hK_r)\vee(hK_s)\) under an edge-chromatic threshold.
- **Exact clique partitions for joins of repeated graph copies** — `SCOPE-20260918-40b72bad9da8`. Trigger: Closest published SCOPE result allowing unequal copy counts. Material read: Complete published RESULT.md. Method: Published SCOPE source tree. Assessment: NOT_COVERING; both sides repeat the same base graph \(H\). Evidence: Its theorem is \((aH)\vee(bH)\) with \(\min(a,b)\ge\chi'(H)\).
- **On the difference between clique partition and clique covering numbers** — `https://arxiv.org/abs/2609.20305`. Trigger: Primary motivating paper for the deficit problem. Material read: Primary arXiv abstract; full text was not directly retrievable in this audit. Method: Primary arXiv metadata plus targeted literature search. Assessment: PRIMARY_FULL_TEXT_RESIDUAL_RISK; the abstract proves the \(\Theta(n^{4/3})\) scale, while searchable descriptions and complete predecessor records identify the balanced uniform lower-bound family. Evidence: The abstract defines \(d_n\) and proves \(d_n=\Theta(n^{4/3})\).
- **Clique partitions and clique coverings** — `https://doi.org/10.1016/0012-365X(88)90197-5`. Trigger: Source of the cut inequality used in the proof. Material read: Publisher/indexed abstract and bibliographic record. Method: Literature search. Assessment: METHOD_PRIOR_ART; the cut inequality is treated as prior and is not the novelty claim. Evidence: The paper develops clique-partition/covering tools and is the cited source of the crossing-edge inequality.

### Checked sources

- arXiv:2609.20305
- DOI:10.1016/0012-365X(88)90197-5
- SCOPE-20260919-07df8435d587
- SCOPE-20260918-40b72bad9da8
- published SCOPE archive search

### Residual originality risks

- Ning's full primary text was not directly retrieved in this audit; a hidden mixed-cluster variant there would affect originality, although the primary abstract and fully inspected published predecessor records do not indicate such coverage.
- Older clique-decomposition literature may contain equivalent load-balancing constructions under different terminology.

## Scientific value — PASS

The mixed-cluster theorem is a reusable exact-attainment criterion beyond uniform repeated-clique joins, and its remainder-absorbing construction yields an explicit every-order second-order deficit constant. This is a motivated refinement of the current \(\Theta(n^{4/3})\) extremal problem, not merely a renamed special case.

## Limitations

The finite capacity conditions are sufficient, not necessary. The coefficient \(3/2^{5/3}\) is an explicit construction upper bound and is not claimed optimal. Full primary text of Ning's very recent preprint was not directly retrievable in this audit, so the comparison relies on its primary abstract plus complete published SCOPE predecessor records and is retained as a residual risk.

## Final assessment

Correctness: **PASS**  
Originality: **PASS**  
Scientific value: **PASS**  
Disposition: **passed**
