# Review of A \(2/\sqrt{3}\) lower bound for the universal edge-Riesz endpoint constant

## Correctness
PASS. The normalized core Laplacian is conjugated to the explicit symmetric matrix \(S_\varepsilon\). Its limit has nonzero spectrum \(\{2,1-\sqrt3/2,1+\sqrt3/2\}\), so generalized inverse square roots converge without an unproved near-zero mode. The \(\{1,3\}\) block gives the exact limit \((0,\sqrt3,0,\sqrt3/2)\) for the potential, hence the six asserted edge limits. The weak-level calculation uses five edge types and the exact input mass \(1+2\varepsilon\). The infinite lift preserves the normalized Laplacian on the level-constant reducing subspace up to the scalar \((1+\tau)^{-1}\), and all lifted inputs lie in both \(\ell^1\) and \(\ell^2\) because \(\sum_k a_k=6\).

## Originality
PASS. The 2026 source proves the universal upper constant \(2\) but does not state a lower bound or optimality; its full text contains no occurrence of “sharp” or “optimal”. Russ's 2000 theorem gives weak type under geometric hypotheses without this universal constant problem, while Chen--Coulhon--Hua treat \(\ell^p\) boundedness and gradient choices. Focused literature-index and web searches for normalized-graph edge-Riesz weak-endpoint lower bounds, best constants, and the value \(2/\sqrt3\) found no statement implying this result.

## Value
PASS. The source leaves the numerical quality of the new universal constant open. The explicit lower bound supplies a quantitative obstruction \(2/\sqrt{3}\approx1.1547\) and, more importantly, an a reusable exact lift from finite weighted cores to the source's infinite-graph category with asymptotically no loss. It identifies a concrete obstruction that any improvement of the universal upper bound must respect.

## Closest literature and limitations
The closest source is Wang, arXiv:2609.28531v1, Theorem 2.1. Earlier graph Riesz-transform work by Russ and by Chen--Coulhon--Hua does not supply the same best-constant statement. A residual risk remains that a lower bound is buried in older graph or Markov-chain literature under a different normalization, although targeted searches and the inspected primary texts did not reveal one. The optimal constant is not determined.

Same-model review: passed. Independent audit: not yet performed.
