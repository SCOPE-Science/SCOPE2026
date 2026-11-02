# Self-review

## Correctness — PASS

The theorem concerns synchronous successor-triggered CCA on \(K_{2n}\) with a perfect matching deleted, for every \(n\ge3\). It does not assert a theorem for four colors or for the related but distinct Greenberg–Hastings model. A neighbor must be adjacent (the matching partner is excluded), and all initial-coloring counts are labelled, not graph-isomorphism classes. The first-entry time is the first recurrent state, not the time of the first visit to its eventual color set.

The central invariant is the six-coordinate vector of matching-pair-type multiplicities capped at two. Exactness of this quotient follows from the successor-neighbor condition: only the tests zero, one, or at least two successors and whether the sole successor is the omitted partner matter. The 707 possible capped vectors for an initial graph with at least three matching pairs are exhaustively checked using ordered pair states. This proves the universal identity \(F^5=F^2\) and six class distinctions. An exact exponential-generating-function sum with monochromatic/mixed orientation weights one/two yields all displayed counts. The coefficient identities are verified symbolically, and independently implemented direct vertex enumeration confirms all \(5{,}380{,}749\) states for three through seven matching pairs. The finite comparison is corroboration; the all-size statement follows from the exact saturation lemma. No missing cases or computations are left as conjectures.

## Originality — PASS (qualified)

Fisch, Gravner and Griffeath's classical article treats the cyclic automaton model, not this exact family enumeration. Gravner, Lyu and Sivakoff's 2016 treatment of three-color CCA on arbitrary graphs proves synchronization iff irrotational and synchronization within graph diameter when applicable. Because the graph here has diameter two, the **consensus-only** two-update statement follows from their theorem and is expressly excluded from the novel contribution. Their inspected manuscript does not contain the six first-entry counts, the all-initial-state identity \(F^5=F^2\), the graph-specific primitive three-cycle count, or its labelled attraction-basin formula.

Known accounts for Greenberg–Hastings excitation on the same matching-defected graphs cannot imply the CCA theorem: in GH, excited/refractory colors advance automatically; in CCA, every color requires a successor neighbor. Exact CCA results on rook graphs, paths or prism ladders are likewise on graphs with different neighborhoods and do not specialize to the matching complement family. Targeted exact-phrase and structural searches for the present graph, rule and six-class census did not find an equivalent statement. This supports best-knowledge originality, not absolute historical priority; an unindexed equivalent remains possible. The 1993 original source was available here only as an abstract, not its full text; it is background, and no whole-paper noncoverage conclusion rests on it.

## Value — PASS

The cocktail-party graph is the complement of a perfect matching and a canonical complete multipartite family. Its single excluded neighbor per vertex makes it a natural stress test for whether almost-complete coupling forces immediate periodicity. The exact theorem identifies a sharp global two-step entrance clock even for oscillatory states, lists every attraction layer and primitive three-cycle, and gives the first complete probability comparison between almost-sure immediate three-cycling and exponentially rare synchronization for this family. Those quantities are not consequences of a general diameter upper bound without a graph-specific orbit/basin analysis. The six populations characterize full dynamics for all sizes, not a narrow arbitrary numerical slice.

## Closest prior literature and remaining limits

The closest primary full text is Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016-10-24), especially Theorem 3 and its proof. Historical background is Fisch, Gravner and Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001 (1993-04-02; abstract directly inspected). Other graph families and GH rules are distinct. The proof and numerical laws hold only for three-color CCA with threshold one on the specified graph at \(n\ge3\). Unindexed equivalent work and independent replication remain residual risks.

Self-review: passed. Independent audit: not yet performed.
