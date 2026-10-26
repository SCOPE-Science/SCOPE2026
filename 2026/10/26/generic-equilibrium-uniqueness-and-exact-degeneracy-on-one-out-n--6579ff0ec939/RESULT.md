# Generic equilibrium uniqueness and exact degeneracy on one-out-neighbor public-goods networks

## Finding

**Theorem (exact equilibrium geometry).** On every finite loopless directed network with at most one outgoing arc per vertex and arbitrary positive player-specific desired public-good provision levels, the entire pure Nash equilibrium set can be represented exactly using \(O(n)\) arithmetic operations. It is homeomorphic to a Cartesian product of closed intervals indexed by directed cycles. Every odd cycle contributes a point; every even cycle contributes either a point or one interval. Its positive-dimensional factors are characterized exactly below. In particular, an independently chosen threshold vector with a density has a unique equilibrium with probability one. A balanced two-person cycle displays discontinuous equilibrium selection under arbitrarily small asymmetric threshold changes.

## Assumptions and scope

Fix \(n\ge1\) players and a finite loopless directed graph \(G=(V,E)\), with \(|V|=n\) and outdegree at most one at every vertex. Write \(f(i)\) for the unique outgoing neighbor of \(i\), when it exists. An arc \(i\to j\) means that \(i\) benefits from \(j\)'s contribution (the convention used in the motivating directed public-goods model). Assign an arbitrary real target \(\theta_i>0\) to each player, who chooses an unbounded nonnegative contribution \(x_i\). For definiteness use the strictly increasing, strictly concave benefit and linear cost

\[
 u_i(x)= e^{\theta_i}\bigl(1-e^{-(x_i+y_i)}\bigr)-x_i,
 \qquad y_i=\begin{cases}x_{f(i)},&f(i)\text{ exists},\\0,&\text{otherwise}.\end{cases}
\]

This is a heterogeneous-threshold instance of a divisible, networked public-good game; there is no randomization, strategic evolution, or additional effort capacity. More generally, the theorem applies whenever each player's unique best response is \(\max(0,\theta_i-y_i)\). Define \(T_a(t)=\max(0,a-t)\) for \(a>0\), and \(\operatorname{clip}(t,L,U)=\min(U,\max(L,t))\) for \(0\le L\le U\).

## Proof

**1. Exact best responses.** The payoff derivative with respect to \(x_i\) is \(e^{\theta_i-x_i-y_i}-1\), strictly decreasing in \(x_i\). The unique constrained maximizer is therefore \(x_i=T_{\theta_i}(y_i)\). If a vertex has no outgoing edge, it must contribute \(\theta_i\). Every other vertex has precisely one successor, so each weak component consists either of a directed cycle with inward predecessor trees or of an outgoing chain ending at an outdegree-zero vertex. Values at cycle vertices determine their predecessors uniquely by this best-response equation. Thus only cycles can create multiplicity.

**2. A composition lemma.** Fix a directed cycle with distinct vertices \(v_0\to v_1\to\cdots\to v_{m-1}\to v_0\), where \(m\ge2\), and write \(a_j=\theta_{v_j}\). Every equilibrium coordinate belongs to \([0,M]\) with \(M=\max_j a_j\). The cycle equation for \(t=x_{v_0}\) is

\[
 t=F(t),\qquad F=T_{a_0}\circ T_{a_1}\circ\cdots\circ T_{a_{m-1}},\qquad 0\le t\le M.
\]

For \(0\le t\le M\), any composition of these maps has the form \(H(t)=\operatorname{clip}(s t+b,L,U)\) with \(s\in\{-1,1\}\) and \(0\le L\le U\le M\). Initially the identity on \([0,M]\) has parameters \((s,b,L,U)=(1,0,0,M)\). Applying \(T_a\) on the outside transforms these parameters exactly to

\[
\left(-s,\ a-b,\ \max(0,a-U),\ \max(0,a-L)\right).
\]

Indeed, the decreasing map \(z\mapsto\max(0,a-z)\) sends an old clipping interval \([L,U]\) to the reversed interval \([\max(0,a-U),\max(0,a-L)]\) and reverses the affine slope. Process \(a_{m-1},a_{m-2},\ldots,a_0\) in that order. After \(m\) steps, \(s=(-1)^m\) and \(b=\sum_{j=0}^{m-1}(-1)^j a_j\). This computes \(F\) using constant work per vertex.

**3. All cycle fixed points.** If \(m\) is odd, \(F(t)=\operatorname{clip}(b-t,L,U)\) is nonincreasing and \(F(t)-t\) is strictly decreasing. Its unique zero is \(t=\operatorname{clip}(b/2,L,U)\). If \(m\) is even, \(F(t)=\operatorname{clip}(t+b,L,U)\). A direct check gives the exact fixed-point set

\[
 \operatorname{Fix}(F)=
 \begin{cases}
 \{L\},&b<0,\\
 \{U\},&b>0,\\
 [L,U],&b=0.
 \end{cases}
\]

These values automatically lie in \([0,M]\). For each permitted \(x_{v_0}=t\), compute the remaining cycle contributions backwards from \(v_{m-1}\) to \(v_1\), using \(x_{v_j}=T_{a_j}(x_{v_{j+1}})\) with indices cyclically. The fixed-point equation verifies the final relation at \(v_0\), so no solutions are omitted or spuriously added.

**4. Multiplicity criterion and exact dimension.** On an even cycle, there is a nontrivial continuum if and only if the alternating target sum \(b\) vanishes and the calculated bounds satisfy \(L<U\). Equivalently, there exists a strictly positive solution of all the uncapped cycle equations \(x_{v_j}+x_{v_{j+1}}=a_j\). For the nontrivial direction, take \(t\) strictly inside a fixed interval: since the composition has slope \(1\) there, none of the constituent \(T_{a_j}\) can be on its flat zero branch at that interior parameter. Hence all cycle contributions are positive and the uncapped equations hold. Conversely, strict positivity at one solution makes the uncapped equations persist for a small interval of alternating coordinate perturbations; the even cycle's alternating target sum must be zero. (The length of this interval is positive because all coordinates have positive margins.)

All directed-cycle parameters are independent. Backward propagation along acyclic predecessor trees is continuous and unique. Projection of the equilibrium set to one distinguished coordinate per cycle is a continuous bijection onto the product of the computed closed intervals; its inverse is continuous by repeated application of \(T_a\). Because the domain is compact and the codomain Hausdorff, this is a homeomorphism. Thus the topological dimension is precisely the number of even cycles with \(b=0\) and \(L<U\). This homeomorphism assertion does **not** claim that the equilibrium set is a convex subset of the original action space.

**5. Generic uniqueness and sharp selection.** A nonunique equilibrium requires that at least one even cycle satisfies the linear equation \(\sum_j(-1)^j\theta_{v_j}=0\). Each is a proper affine hyperplane in positive target space; there are finitely many cycles. Their union has Lebesgue measure zero, proving generic uniqueness. The condition is sharp: two mutually linked players with \((\theta_0,\theta_1)=(1,1)\) have the entire equilibrium segment \(\{(t,1-t):0\le t\le1\}\). With thresholds \((1+\varepsilon,1)\), \(\varepsilon>0\), the unique equilibrium becomes \((1+\varepsilon,0)\), while \((1,1+\varepsilon)\) yields \((0,1+\varepsilon)\). Both perturbations can be arbitrarily small while their selected equilibria remain separated. The balance equation alone is not sufficient for a continuum: for the six-cycle with thresholds \((10,1,1,10,1,1)\), the algorithm gives \(b=0\) but \(L=U=9\), hence a unique equilibrium \((9,1,0,9,1,0)\).

**6. Work bound.** Functional-graph cycle discovery and backward predecessor traversal visit each vertex and arc a constant number of times. Each cycle update above requires constant arithmetic operations; an equilibrium at any chosen parameter is reconstructed by one traversal. Thus the exact interval representation and evaluation each take \(O(n)\) arithmetic operations. This is an arithmetic-operation count; integer bit complexity depends on target encoding and is not asserted to be linear.

## Verification

The standalone Python 3 script `verify.py` uses exact rational arithmetic to compute both the compressed clipping formula and an independently formed piecewise-affine composition of best-response maps. It checks all \(3276\) directed cycles of lengths \(2\) through \(7\) with individual thresholds in \(\{1,2,3\}\), including \(16646\) fixed-point, identity, and reconstruction checks. It observes \(133\) nondegenerate interval cases, \(2457\) odd-cycle unique cases, and \(30\) even-cycle balanced-but-singleton cases. It reproduces the two-player jump and the balanced six-cycle singleton. Execute `python3 verify.py`. These finite tests support the algebra, but the proof above establishes the unrestricted statement.

## Relationship to prior work

Huang, Sun, Xu, and Zhao (2025) study specialized equilibria of directed public-goods games, identifying them with graph kernels and discussing a unique distributed equilibrium on a directed triangle. Their equilibrium and stability results focus on a common target and do not present the full heterogeneous-target cycle geometry or its genericity criterion. The present classification concerns **all** pure equilibria, not just zero-or-full specialists. Papadimitriou and Peng (2021/2023) prove broad computational complexity results and approximate algorithms for directed public-goods games; these do not provide the exact interval decomposition stated here. Deligkas and coauthors (2025) treat binary sharing-constrained games, including a linear-time mixed-equilibrium algorithm for a different discrete model; this is not an exact continuous-effort solution-set classification. Fu, Hua, Qian, and Sun (2022) study constrained heterogeneous public goods in weighted networks, but the full paper was not accessible for comparison; its abstract concerns an algorithm separating contributors and free-riders and does not resolve the current exact claim. General linear-complementarity theory supplies related uniqueness tools, so historical equivalence under LCP or functional-network terminology is a residual priority risk.

## Limitations

The theorem requires at most one out-neighbor, positive targets, a one-for-one linear public-good spillover, and exact best responses. It does not characterize general directed networks with two or more outgoing neighbors, weighted spillovers, dynamics of equilibrium selection, welfare comparisons, or robustness of any specific equilibrium selection at a balanced cycle. The discontinuity example concerns parameter-selected unique equilibria, not dynamical jumps. The existence of broad general LCP results and inaccessible material in older heterogeneous public-goods literature limits any claim of absolute historical priority.

## References

1. J. Huang, Y. Sun, F. Xu, and W. Zhao, *Public Goods Provision in Directed Networks: A Kernel Approach*, first submitted 2025-12-29, arXiv:2512.23193v1, https://arxiv.org/abs/2512.23193.
2. C. Papadimitriou and B. Peng, *Public Goods Games in Directed Networks*, arXiv:2106.00718v2, https://arxiv.org/abs/2106.00718 (subsequently *Games and Economic Behavior*, 2023).
3. A. Deligkas and coauthors, *Public Goods Games in Directed Networks with Constraints on Sharing*, arXiv:2511.11475v1, https://arxiv.org/abs/2511.11475.
4. W. Fu, D. Hua, X. Qian, and Y. Sun, *Constrained public goods in weighted networks with heterogeneous agents*, *Economics Letters* 213 (2022), 110332, https://doi.org/10.1016/j.econlet.2022.110332 (abstract consulted; full text not inspected).
5. R. W. Cottle, J.-S. Pang, and R. E. Stone, *The Linear Complementarity Problem*, SIAM edition (2009), for general background (not inspected in full).
