# Review of isolated-edge–triangle covariance reversal

## Correctness

PASS. The exact event that an edge is a two-vertex connected component leaves a uniform \(G(n-2,m-1)\) graph on the other vertices, so conditional and unconditional triangle means are hypergeometric edge probabilities. Covariance linearity yields the exact factorization; rational cancellation determines the unique real zero, lying strictly between consecutive integers. The independent-edge calculation uses the same local conditioning with independent residual edges. The finite rational checks were replayed from the supplied verification program, which tests all 33,792 graphs on five or six vertices and one hundred larger-size threshold identities. The infinite result is proved analytically, not by enumeration.

## Originality

PASS to the available-literature standard, subject to historical-priority risk. Semantic searches covered isolated-edge components, components of size two, triangles, edge-conditioned graph models, and sign reversal; no recovered statement implied the sharp threshold. The closest published component–triangle covariance concerns the **total** component count under independent-edge percolation, which is a distinct statistic and setting. A previous isolated-vertex versus subgraph-count result does not supply this isolated-edge-component covariance. Amir et al. (2005), *Giant Components in Biased Graph Processes*, full HTML introduction, principal theorems and random-process section inspected: their critical edge-count scale concerns giant components and isolated vertices, not exact joint covariance of isolated edges with triangles. Chatterjee (2010), *The missing log in large deviations for triangle counts*, HTML introduction, main theorem and proof sections inspected: these are triangle upper-tail bounds, not joint covariance identities. Kim and Vu (2004), *Divide and conquer martingales and the number of triangles in a random graph*, abstract checked only; no entire-paper exclusion is claimed. Other classical mixed-component-moment results may contain equivalent material.

## Mathematical value

PASS. The two statistics are natural competing local structures in random-graph sampling. The exact integer boundary in the fixed-edge model, the opposite sign in the independent-edge model, and the explicit sparse scaling limit show that transferring dependence assumptions between the two canonical Erdős–Rényi ensembles can reverse the answer. The critical-window placement is an interpretable structural boundary, not an arbitrary parameter slice. The theorem makes no claim of stochastic-order strengthening.

Self-review: passed. Independent audit: not yet performed.
