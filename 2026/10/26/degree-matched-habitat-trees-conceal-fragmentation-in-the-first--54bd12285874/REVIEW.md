# Review of the fragmentation cumulant theorem

## Correctness

PASS. The forest Euler identity reduces the component count to the surviving vertex count minus the surviving-edge count. Exact variance expansion leaves only the wedge count, which is fixed by the degrees. For the third cumulant, all differences except three-distinct-edge patterns cancel; their star/path/wedge-plus-isolated/matching enumeration gives the claimed \(-6\Delta L\,p^4(1-p)^2\) formula. The divisibility argument independently checks survival sets of size at most three, deletion of at most one vertex, and the first two factorial moments. The six-vertex coefficient difference is reproduced by a complete exact finite program.

## Originality

PASS under the examined literature, with explicit residual bibliographic risk. Urban–Keitt motivates habitat graph connectivity, Tittmann–Averbouch–Makowsky provides the general induced-subgraph component polynomial, Liao–Hou studies its invariants (including regular-bipartite path counting), and Allard et al. discusses percolation component-size laws. Those inspected claims do not establish this unconditional degree-matched tree third-cumulant identity, its generating-polynomial divisibility, or its sharp six-vertex witness. However general induced-subgraph polynomial theory encompasses the statistic, and unnoticed equivalent literature is possible.

## Mathematical value

PASS. Patch-degree distributions are common coarse summaries of ecological networks, so determining precisely which fragmentation statistics depend on branching placement is a motivated robustness question. Here two degree-matched landscapes have identical mean and variance, but their full fragmentation laws differ at every interior survival probability. The third moment detects this hidden difference by a specific four-vertex path count, and the minimal example is exactly classified. The proof holds for arbitrary tree size; the finite enumeration only locates the first witness.

Self-review: passed. Independent audit: not yet performed.
