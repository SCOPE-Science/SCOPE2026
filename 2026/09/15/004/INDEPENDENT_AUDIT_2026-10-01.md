# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260915-004`

## Correctness — PASS

For a container with \(N\) edges and a required subgraph threshold \(L\), every qualifying spanning subgraph is obtained by deleting at most \(N-L\) edges. When \(N\le (1/8+o(1))n^2\) and \(L=(1/8-ε)n^2\), the deletion fraction is at most \(8ε+o(1)\). For fixed \(0<ε<1/16\), this is below \(1/2\), so the binary-entropy tail gives at most \(2^{(H(8ε)/8+o(1))n^2}\) qualifying subgraphs per container. The function \(uH(1-a/u)\) is strictly increasing because its derivative is \(-\log_2(1-a/u)\), so the maximum occurs at the largest allowed container. Multiplying by only \(2^{o(n^2)}\) containers preserves that exponent. Since \(H(8ε)<1\) on this open range, the claimed simultaneous counting exponent \(1/8\) is impossible. The package script merely corroborates the arithmetic; an independent recomputation at ε=0.01 gives exponent about 0.0502724 and gap about 0.0747276.

Sources:
- assigned RESULT.md
- artifacts/entropy_gap.py
- Saxton–Thomason, Hypergraph containers

Risks:
- This is an incompatibility theorem about the two asserted properties; it does not determine the true counting exponent or rule out variants with ε tending to zero.

## Originality — PASS

Fresh semantic search found no earlier published SCOPE statement of this exact deletion-entropy incompatibility. Saxton–Thomason supply the general container framework, and Ramsey–Turán work supplies the \(1/8\) density scale, but neither inspected source states this dense-subgraph entropy obstruction. The final implication is therefore best-of-knowledge original.

### equivalent_formulations

Searches:
- Resultary: deletion entropy dense subgraphs sparse-edge containers K4-free counting exponent one eighth fixed epsilon
- arXiv:1204.6595

Evidence:
- The exact Resultary hit is this record; the general container paper states small container families for H-free objects but not the audited fixed-density tail incompatibility.

Reasoning:
Equivalent formulations as a deletion-tail bound, a Hamming-ball count inside each container, and an entropy obstruction were compared.

### broader_coverage

Searches:
- Saxton–Thomason, Hypergraph containers
- Ramsey–Turán K4-free density literature

Evidence:
- General container theory gives covering families; Ramsey–Turán theory motivates the edge-density threshold. Neither broader statement implies the audited simultaneous counting contradiction without the entropy-tail argument.

Reasoning:
The result combines two standard ingredients in a nontrivial implication rather than being a direct specialization of either.

### exact_database_or_table

Searches:
- Resultary published corpus search for the exact exponent obstruction

Evidence:
- No external exact table or database controls this asymptotic family count.

Reasoning:
This check is genuinely not table-driven; the target is an asymptotic implication.

### claim_vs_prior_implication

Searches:
- comparison with general hypergraph-container counting statements

Evidence:
- The general \(2^{e(C)}\) subgraph bound would only reproduce exponent \(1/8\); the dense-subgraph deletion tail is the decisive extra step.

Reasoning:
No inspected prior theorem mechanically implies the strict exponent drop for the stated fixed-ε conjunction.

### source_inspections
- **Hypergraph containers** — arXiv:1204.6595. Trigger: Foundational general container theorem cited by the record. Material read: Current arXiv abstract and scope statement. Method: Primary-source statement comparison. Assessment: General framework, not exact coverage. Evidence: The paper gives small families of containers for H-free hypergraphs and counting applications, but does not state the audited deletion-tail incompatibility.
- **Assigned entropy verifier** — artifacts/entropy_gap.py. Trigger: Arithmetic corroboration. Material read: Complete source file. Method: Line-by-line inspection and independent numerical recomputation. Assessment: Correctly evaluates the binary-entropy exponent; it is not used as the proof of the asymptotic statement. Evidence: At ε=0.01 it reproduces exponent about 0.0503 and a gap exceeding 0.07.

### checked_sources

- Resultary semantic search
- arXiv:1204.6595
- assigned RESULT.md and artifacts/entropy_gap.py

### residual_risks

- Best-of-knowledge originality cannot exclude unpublished observations or a differently phrased counting lemma in the container literature.

## Scientific value — PASS

The result directly invalidates a proposed conjunction at a natural Ramsey–Turán density scale and identifies the precise entropy mechanism causing the failure. It is a motivated structural obstruction, not a tiny-instance check, and it clarifies how a container statement must be altered before it can support the desired counting theorem.

Sources:
- Saxton–Thomason container framework
- assigned entropy proof

Risks:
- The result is negative and does not solve the true counting problem.

## Limitations

- Fixed \(0<ε<1/16\) only.
- The theorem rejects the conjunction of sparse-edge containers and the asserted counting exponent; it does not determine the actual family size.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
