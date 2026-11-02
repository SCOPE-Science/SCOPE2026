# Scientific review

## Correctness

**PASS.** The proof derives the exact weighted Laplacian spectrum with one peripheral eigenvalue of multiplicity \(k-1\) and a quadratic quotient factor. Its unit-gap constraints are necessary and sufficient. The exact scalar objective is strictly convex and its two one-sided derivatives at the kink give all three regimes, including boundaries. A quotient Fiedler eigenvector and a peripheral contrast trace argument force any asymmetric maximizer to coincide with the symmetric solution. An extracted verifier reproduced five symbolic characteristic polynomials, three exact-rational examples, 54 threshold checks and 40 supplementary independent optimizations. Numerical checks are not substituted for proof.

## Originality

**PASS on inspected evidence, with residual specialist-priority risk.** Sun–Boyd–Xiao–Diaconis (2006) formulate and analyze the general continuous-time weighted mixing problem and show examples, but their examples and statements do not give the present exact three-price one-leaf-clique optimizer. Ghosh–Boyd (2006) show symmetry reduction for a different convex-hull graph-family problem. Jafarizadeh treats the same broad lollipop topology but solves discrete-time SLEM, not the cost-constrained continuous-time problem. General formulas for other objectives and topologies—including clique bouquets, resistance-based network design and one-leaf-per-vertex coronas—do not imply the claimed three-phase allocation and unrestricted uniqueness. Search cannot prove absence in uninspected specialist literature.

## Mathematical value

**PASS.** The object is a natural minimal bottleneck topology combining a dense core with one bridge. Its optimal solution is qualitatively different across three cost regimes, notably deleting all internal clique edges when the optimizer becomes a star; these thresholds and global uniqueness are exact for arbitrary clique size and all positive prices. This provides a closed-form benchmark for cost-sensitive continuous-time mixing and distinguishes it from discrete-time SLEM and resistance design. The contribution is a complete classification, not an arbitrary sampled numerical improvement.

## Scope and limitations

Only symmetric continuous-time rates, one pendant vertex, a fixed complete core and constant prices within each edge-orbit are covered. Independently heterogeneous prices and discrete-time objectives are not covered. Historical priority is assessed from identified materials, not certified exhaustively; independent mathematical validation has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
