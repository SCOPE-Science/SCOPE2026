# Scientific review — biclique intrapart-edge insertion

## Correctness — PASS

The proof specifies all integer parameters \(m,n\ge2\), all graphs, the relevant real edge-space operator norms, and the graph orientations. The intact biclique projection matrix is explicitly derived. The added edge is a Laplacian eigenvector, so a rank-one inverse identity determines **every entry** of the perturbed cut projector. Complementation and absolute column sums produce exactly three symmetry types, covering all edges. The signed entries are handled separately on either side of \(m=n+2\). The sharp maxima are established by algebraic orbit comparisons including \(m=2\), \(m=3\), and \(n=2,3,4\). The five-zone threshold follows from inequalities valid for every integer \(n\ge5\), not from finite extrapolation. A distinct, exact-rational direct-Laplacian checker verifies 1,858 columns in 58 parameter cases.

## Originality — PASS, qualified

The most relevant finite-graph Lipschitz-free-space framework is Dilworth–Kutzarova–Ostrovskii (2018), arXiv:1807.03814; its accessible sections concern general edge-space quotients, recursive graphs, and invariant projections, not biclique insertion. Their 2020 arXiv:2007.07949 paper analyzes Laakso and diamond projections. Basso (2021), arXiv:2104.14238, studies extension/projection constants with a different invariant and scope. Existing complete-biclique formulas, one-cross-edge deletion results, and finite edge-insertion monotonicity examples do not imply the simultaneous closed-form five-zone law. Targeted records and full-text bibliographic searches uncovered no implication that covers the claim. Remaining risk: older/unindexed electrical-network calculations or inaccessible specialized results could contain the same column-sum phase diagram; search is not proof of novelty.

## Value — PASS

The construction is a natural one-edge perturbation of a canonical edge-space Banach operator, rather than a selected small graph. Its full two-parameter classification shows strictly decreasing cut norm, unchanged cut and cycle norms over a long integer interval, cycle-only growth, and eventually growth of both. The exact onset indices differ by three. This gives a concrete infinite-family structure theorem about sparse-edge sensitivity, with sharp natural boundaries and explicit norm formulas useful for further perturbation comparisons; correctness or reproducibility alone was not used to justify value.

## Limitations

Only real, unweighted simple bicliques with one intrapart edge and their canonical Euclidean-orthogonal projections are covered. No minimum-norm claim for arbitrary projections or extrapolation to weighted perturbations is made. Independent mathematical validation is still needed.

Self-review: passed. Independent audit: not yet performed.
