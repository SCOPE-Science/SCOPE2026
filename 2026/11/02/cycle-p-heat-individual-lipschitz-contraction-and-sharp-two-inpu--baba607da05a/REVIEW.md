# Scientific review

## Correctness — PASS

For every \(n\ge3\) and \(1<p<\infty\), the cyclic edge-difference identity (1) follows by subtracting adjacent vertex equations. Its scalar maximum principle gives single-trajectory contraction. The linear \(p=2\) case follows from the same principle applied to differences, while the complete-triangle case follows from monotone vertex-order comparison and equality between oscillation and graph-Lipschitz seminorm. For \(n\ge4\), two explicitly displayed zero-sum edge vectors exist for all orders, and differentiating the nonlinear flux at their nonzero background coordinates yields the exact quantity \((p-1)(R^{p-2}-3)\); choosing \(R\to\infty\) or \(R\downarrow0\) proves the claimed unbounded initial two-input growth. The standard-library checker confirms the edge identity and selected numerical witnesses. Global well-posedness follows directly from monotone convex-energy flow; no finite test is used as an infinite proof.

## Originality — PASS (qualified)

The closest inspected source is Mugnolo, arXiv:1207.1996: Theorem 3.4 gives nonlinear solution existence and a vertex norm contraction semigroup; Proposition 3.9 and Corollary 3.11 concern vertex order and \(\ell^q\) contractivity, not the two-input graph-Lipschitz seminorm. A second source, Münch–Wojciechowski, arXiv:1712.00875, Theorem 3.8, provides a graph-Lipschitz gradient criterion for *linear* heat. Relevant earlier results for finite trees and for edge-total-variation contraction on cycles have different graphs or seminorms and do not imply a nonlinear two-input cycle classification. Targeted literature and mathematical-record searches revealed no equivalent statement, but unindexed literature or a concealed corollary remains a risk. In particular, no claim is made that the elementary maximum-principle argument is new on its own.

## Mathematical value — PASS

The result settles a complete natural cyclic family, not a single numerical instance. It gives the smallest cyclic obstruction (four vertices), the sharp exponent/topology dichotomy, and an unbounded *infinitesimal* amplification phenomenon despite universal contraction of each single trajectory and vertexwise difference oscillation. That distinction matters when using nonlinear graph heat smoothing for perturbation stability: one-input smoothing alone cannot bound short-time sensitivity of edge gradients between two input signals. The quantity is not merely a reparameterized version of the earlier tree result because the cyclic edge constraint is essential, especially in the exceptional triangle.

## Scope and residual risks

All conductances, masses and edge lengths are one. No fixed-positive-time sharp Lipschitz norm or weighted-cycle classification is obtained. The theorem does not imply failure of vertex \(\ell^\infty\) contraction; indeed vertex order comparison still holds. Novelty is assessed relative to accessible sources and prior claim records; exhaustive historical coverage and independent mathematical validation are not asserted.

Self-review: passed. Independent audit: not yet performed.
