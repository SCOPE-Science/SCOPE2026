# Scientific review: exact edge-count residues given degree parities

## Correctness

**PASS.** The characteristic function is derived by exact Fourier inversion on the incidence-matrix syndrome, with the conditioning normalization \(\Pr(D=d)=2^{-(n-1)}\) and all feasible vectors counted. The even-order Krawtchouk sum vanishes exactly in the nonconstant cases; the odd-order sum evaluates to a signed nonzero power of two. Triangle symmetric difference proves conditional edge-parity balance, closing the four-root inversion. The critical formulas are checked independently with exact integer Gaussian arithmetic for 45 parameter values, and exhaustively on 33,864 graphs through order six. The proof, not the bounded checks, supports the all-order claim.

## Originality

**PASS on inspected evidence; residual historical-priority risk.** Ferber–Hardiman–Krivelevich analyze degree-congruence patterns and induced subgraphs. Balister–Powierski–Scott–Tan analyze the number of induced-partition patterns. Lengler and colleagues give edge-total residue constraints as examples for connectivity and dependence, not their full conditional law given vertex syndromes. Cameron gives a general weight-enumerator framework, which could imply parts of the computation after new specialization but does not state the evaluated all-syndrome zero classification. Actual semantic searches of published mathematical findings and primary-literature queries did not identify a stronger same-object implication. Old cycle-code coset or Ising evaluations could cover the statement; this remains a genuine risk, and the search itself does not establish priority.

## Value

**PASS.** Degree parities are a natural coarse observation of a graph, and their interaction with the global number of edges cannot be inferred from marginal degree-parity uniformity. The theorem gives an exact conditional independence regime, an exhaustive exception classification, and exact finite-order biases outside it. In particular, the parity of the graph order acts as a sharp qualitative boundary, relevant to parity-constrained random graph models and their possible global congruence leakage.

## Scope and limitations

The result is confined to independent fair-edge labeled graphs of order at least three and conditioning on feasible degree-parity vectors. No claim is made about arbitrary edge probabilities, general moduli, or complete integer degree sequences. A potential equivalent older statement under cycle-code coset enumerators remains unresolved by the literature inspected.

Self-review: passed. Independent audit: not yet performed.
