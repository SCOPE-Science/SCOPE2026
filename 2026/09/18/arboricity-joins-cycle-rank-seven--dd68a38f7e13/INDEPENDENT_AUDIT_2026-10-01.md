# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-dd68a38f7e13`

## Correctness — PASS

Nash--Williams reduces the theorem to induced-subgraph density. For a two-sided subset of sizes \(s,t\), the record's excess term \(R_q(s,t)=q(s+t-1)-st+1=q^2-q+1-(q-s)(q-t)\) is correct, and the cycle-rank bound controls the induced excess from both factors. The three relative-size cases for \(q\ge3\), the one-sided simple-graph/cycle-rank bound, and the low-ceiling cases \(q=2,1,0\) all close with the displayed inequalities. The sharpness graph at total cycle rank 8 has full-set ceiling 3 but contains a 7-vertex 19-edge subgraph, forcing arboricity 4, while containment in \(K_8\) gives the matching upper bound.

### Correctness sources

- research package RESULT.md
- Nash-Williams 1964
- Kuanyshov--Yeginbay arXiv:2609.20606

### Correctness residual risks

- The criterion is sufficient, not necessary; the fixed-\(K\) quadratic threshold is not claimed optimal.

## Originality — PASS

The motivating join-arboricity paper gives general bounds and examples, not the cycle-rank criterion. Current Resultary search found a later exact theorem for joins of pseudotrees, but that covers only cycle rank at most one per connected factor and is therefore a narrow subfamily of the audited cycle-rank-seven theorem. No source located in the fresh searches gives the sharp universal threshold seven or the cycle-rank-eight obstruction.

### equivalent_formulations

Searches:
- Resultary: arboricity graph joins cycle rank seven
- arXiv:2609.20606 join arboricity
- synonyms: cyclomatic number, circuit rank, graph sum, complete sum

Evidence:
- The exact semantic match is the audited record.
- The motivating preprint advertises general bounds for joins rather than this exact criterion.

Reasoning:
The full-set Nash--Williams ceiling formulation and the equivalent reduced-arboricity convention were both compared.

### broader_coverage

Searches:
- Resultary 2026-09-19 Exact arboricity of joins of pseudotrees
- balanced/1-balanced join literature

Evidence:
- The later pseudotree theorem assumes each connected factor has cycle rank at most one.

Reasoning:
That result is strictly narrower and does not imply the total-cycle-rank-seven theorem or the sharp threshold-eight example.

### exact_database_or_table

Searches:
- Resultary and literature searches for cycle-rank-indexed join-arboricity tables

Evidence:
- No exact table or classification covering total cycle ranks through seven was located.

Reasoning:
The theorem is proved uniformly by inequalities; it is not a recomputation of a known finite table.

### claim_vs_prior_implication

Searches:
- claim versus Kuanyshov--Yeginbay Theorem 23 bounds
- claim versus later pseudotree exact theorem

Evidence:
- General upper/lower bounds leave a gap; the pseudotree theorem closes only a much smaller beta range.

Reasoning:
Neither prior implication determines the audited exact ceiling for all connected factors with total cycle rank at most seven.

### source_inspections
- **Arboricity and Simplicial Geometric Category of Wedges and Joins of Graphs** — https://arxiv.org/abs/2609.20606. Trigger: Direct motivating source. Material read: Current abstract and theorem scope. Method: Primary-source scope comparison. Assessment: Gives exact wedges and general join bounds, not the audited cycle-rank criterion. Evidence: The abstract explicitly characterizes the join contribution as upper/lower estimates.
- **Exact arboricity of joins of pseudotrees** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-arboricity-joins-pseudotrees--b7ba35900aa1. Trigger: Closest later current exact-join result. Material read: Complete RESULT.md. Method: Full theorem/proof comparison. Assessment: Narrow subfamily only; it does not cover beta up to seven. Evidence: Its factors are trees or unicyclic connected graphs.
- **Assigned cycle-rank criterion** — research package RESULT.md. Trigger: Correctness and implication audit. Material read: Complete file. Method: Independent algebraic reconstruction of every Nash--Williams case and the beta-eight witness. Assessment: The threshold-seven corollary and obstruction are supported without computational enumeration. Evidence: The 19-edge subgraph on seven vertices forces the stated sharp failure at beta eight.

### checked_sources

- https://arxiv.org/abs/2609.20606
- https://doi.org/10.1112/jlms/s1-39.1.12
- https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-arboricity-joins-pseudotrees--b7ba35900aa1
- research package RESULT.md

### residual_risks

- Recent join-arboricity literature creates some risk of near-simultaneous refinements, but no covering theorem was located.

## Scientific value — PASS

The total cycle rank is a canonical measure of distance from forests, and the theorem gives an exact arboricity formula on a natural bounded-cycle-complexity region plus a sharp universal cutoff at seven. The explicit beta-eight obstruction explains where full-set density can cease to control the ceiling, making this a structural boundary theorem rather than a routine example.

### Value sources

- Nash-Williams arboricity theorem
- Kuanyshov--Yeginbay join problem
- the sharp beta-eight witness

### Value residual risks

- The quadratic sufficient threshold for fixed larger \(K\) may not be optimal.

## Limitations

- The criterion is sufficient rather than necessary.
- The universal cycle-rank-seven threshold is sharp, but the fixed-ceiling quadratic bound is not claimed sharp.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
