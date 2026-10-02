# Independent mathematical audit — 2026-10-01

## Final claim assessed

Boundary-tapered path blow-ups improve the geodesic-subpath lower bound

## Correctness — PASS

PASS. The path-blow-up formula follows from a complete partition of endpoint pairs. Distinct layers contribute the product of intervening layer sizes; same-layer pairs contribute their common-neighbor count. This gives an infinite proof. A fresh implementation reproduced the tapered closed form and exact difference \(10\cdot3^{q-2}-15\) for independent \(q\)-values; the repository BFS/enumeration is supporting evidence only.

## Originality — PASS

PASS to the best of current knowledge. The complete open-access Knor--Sedlar--Škrekovski--Zhang article was inspected at Proposition 3 and Problem 14. It treats equal-size sequential joins and explicitly asks for a graph beating the \(G_{3,n/3}\) benchmark. The tapered unequal-layer family answers that construction request for all \(n=3q\), \(q\ge3\). Searches found no earlier unequal-layer formula or tapered witness.

### equivalent_formulations

Searches: Published-record query for geodesic subpath path blow-ups and unequal layers; Knor et al. full article Proposition 3 and Problem 14

Evidence: The primary article gives only equal-layer \(G_{k,t}\); the current record is the only exact tapered match found.

Reasoning: No inspected equivalent formulation contains the unequal-layer formula.

### broader_coverage

Searches: https://doi.org/10.1007/s00009-026-03159-3

Evidence: Problem 14 explicitly asks for a graph larger than the equal-layer benchmark.

Reasoning: The primary source leaves exactly the construction gap filled here.

### exact_database_or_table

Searches: Published-record search for tapered path blow-ups

Evidence: No earlier exact record or table entry was found.

Reasoning: The result quantifies an infinite graph family rather than recomputing a known table.

### claim_vs_prior_implication

Searches: Knor et al. Proposition 3; Knor et al. Problem 14

Evidence: The equal-layer formula does not imply the tapered gain.

Reasoning: The endpoint-pair count supplies new structural information.

## Scientific value — PASS

PASS. The theorem resolves the construction side of an explicit 2026 open problem on an infinite sequence of graph orders and improves the leading construction constant by \(121/81\). The general unequal-layer formula is independently reusable.

## Source inspections

- **Counting Geodesic Paths in Graphs** — https://doi.org/10.1007/s00009-026-03159-3. Material read: Open-access full article at Proposition 3, concluding remarks, and Problem 14. Assessment: PRIMARY_SOURCE_LEAVES_CLAIM_OPEN. Evidence: Problem 14 explicitly asks for a construction beating \(G_{3,n/3}\).
- **Published-record search for tapered geodesic path blow-ups** — Resultary published record index. Material read: Ranked semantic results for unequal layers, path blow-ups, and Problem 14. Assessment: NO_EARLIER_EXACT_COVERAGE_FOUND. Evidence: The audited record was the only exact match in the inspected results.

## Limitations and residual risks

The construction improves the lower bound but does not determine the global maximum, optimize other residue classes, or improve the universal upper bound. Finite enumeration through order 18 is only supporting evidence.

- The invariant is very recent, so indexing delay remains possible.
- No optimality is claimed among all path blow-ups or all connected graphs.

## Disposition

**passed**
