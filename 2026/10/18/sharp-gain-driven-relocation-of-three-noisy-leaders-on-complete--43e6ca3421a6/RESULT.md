# Sharp gain-driven relocation of three noisy leaders on complete bipartite networks

## Finding
For every integer \(m\ge3\), choose exactly three distinct vertices as noisy leaders on the unit-weight complete bipartite graph \(K_{m,3}\). Each selected vertex receives the same finite positive feedback gain \(\kappa\). Let \(a\in\{0,1,2,3\}\) be the number of selected vertices in the part of size \(m\), so \(3-a\) are selected in the part of size three. The total stationary variance for independent unit-variance white disturbances is \(J_a/2\), where \(J_a=\operatorname{tr}[(L+\kappa D_S)^{-1}]\).

The **complete classification** of globally optimal leader placements is as follows. In every statement, vertices chosen within a part can be arbitrary and all placements of the specified type are optimal.

- When \(m=3\), the only optimal types are \(a=0\) and \(a=3\), tied at every \(\kappa>0\).
- When \(m=4\) or \(m=5\), set
  \[\kappa_-(m)=\frac{-(m+3)+\sqrt{(m+3)^2+12m^2/(6-m)}}{2}.\]
  The only optimal type is \(a=0\) below this gain, both \(a=0,3\) tie at equality, and only \(a=3\) is optimal above it. In particular, \(\kappa_-(4)=(\sqrt{145}-7)/2\) and \(\kappa_-(5)=\sqrt{91}-4\).
- When \(m=6\) or \(m=7\), the only optimal type is \(a=0\) for every positive gain.
- When \(m\ge8\), set
  \[\kappa_+(m)=\frac{30+\sqrt{900+4(m-7)m(m^2-m+6)}}{2(m-7)}.\]
  The only optimal type is \(a=0\) below this gain, both \(a=0,1\) tie at equality, and only \(a=1\) is optimal above it. Furthermore, \(\kappa_+(m)/m\to1\) as \(m\to\infty\).

This demonstrates two qualitatively distinct gain-driven relocations: at smaller imbalances all three leaders move from the high-degree part to the larger, lower-degree part; at larger imbalances only one leader moves, leaving two in the high-degree part.

## Assumptions and scope
The undirected graph has two disjoint vertex parts \(A\) and \(B\), with \(|A|=m\), \(|B|=3\), and all \(3m\) possible cross-edges assigned unit conductance; there are no edges within either part. The combinatorial Laplacian is \(L\), and \(D_S\) is the diagonal matrix with entries \(1\) at the three selected vertices and \(0\) elsewhere. For any \(\kappa>0\), the matrix \(M_S=L+\kappa D_S\) is positive definite because the underlying graph is connected and \(S\ne\varnothing\). For the stochastic differential equation \(dx=-M_S x\,dt+dW\) with identity driving covariance, the unique stationary covariance is \(M_S^{-1}/2\). Exactly three distinct leaders, not up to three, must be chosen. No continuous optimization of feedback gains or edge weights is included.

The number \(a\) determines the objective because each vertex part is permutation-symmetric. There are exactly four orbits of three-element vertex subsets, indexed by \(a=0,1,2,3\). Equality at the listed thresholds is genuine and exhausts all additional optimal orbits.

## Proof
**1. Exact expression for all four orbits.** In the vertex ordering \((A,B)\), write
\[M_S=\begin{pmatrix}D_A&-\mathbf1_m\mathbf1_3^T\\-\mathbf1_3\mathbf1_m^T&D_B\end{pmatrix}.\]
Here \(D_A\) is diagonal with \(a\) entries \(3+\kappa\) and \(m-a\) entries \(3\); \(D_B\) is diagonal with \(3-a\) entries \(m+\kappa\) and \(a\) entries \(m\). Define
\[
\begin{aligned}
U_a&=\frac{m-a}{3}+\frac{a}{3+\kappa},
&U'_a&=\frac{m-a}{9}+\frac{a}{(3+\kappa)^2},\\
V_a&=\frac{a}{m}+\frac{3-a}{m+\kappa},
&V'_a&=\frac{a}{m^2}+\frac{3-a}{(m+\kappa)^2}.
\end{aligned}
\]
Block elimination, or the rank-two Woodbury identity, yields
\[\boxed{J_a=U_a+V_a+\frac{V_aU'_a+U_aV'_a}{1-U_aV_a}.}\]
The denominator is strictly positive: \(U_a\le m/3\) and \(V_a\le3/m\), while at least one diagonal entry is strictly raised by a leader. The inverse correction follows explicitly by inverting
\[\begin{pmatrix}-U_a&1\\1&-V_a\end{pmatrix}^{-1}
=\frac{1}{1-U_aV_a}\begin{pmatrix}V_a&1\\1&U_a\end{pmatrix}.\]
Thus this formula is exact for all finite \(\kappa>0\).

**2. Three algebraic comparisons suffice.** Simplifying the differences gives
\[
J_0-J_1=\frac{(m-7)\kappa^2-30\kappa-m(m^2-m+6)}{3(\kappa+m)((2m+1)\kappa+9m)},
\]
\[
J_0-J_3=-\frac{(m-3)\big[(m-6)\kappa(\kappa+m+3)+3m^2\big]}{9m(\kappa+3)(\kappa+m)},
\]
and
\[
J_0-J_2=-\frac{2P_m(\kappa)}{3m(\kappa+3)(\kappa+m)(m\kappa+4\kappa+9m)},
\]
where
\[
\begin{aligned}
P_m(\kappa)={}&6\kappa^3+(m^3-8m^2+30m+18)\kappa^2\\
&+(m^4-2m^3-6m^2+72m)\kappa+3m^2(m^2-2m+3).
\end{aligned}
\]
For \(y=m-3\ge0\), its coefficients in descending powers of \(\kappa\) are
\[6,\quad y^3+y^2+9y+63,\quad y^4+10y^3+30y^2+90y+189,\quad 3y^4+30y^3+117y^2+216y+162.\]
Each is positive, so \(J_0<J_2\) for every admissible \(m,\kappa\). No placements of type \(a=2\) can be optimal.

**3. Sign analysis.** When \(3\le m\le7\), the numerator of \(J_0-J_1\) is strictly negative, hence \(J_0<J_1\). When \(m\ge6\), the bracket in \(J_0-J_3\) is strictly positive, so \(J_0<J_3\). At \(m=3\), the factor \(m-3\) yields \(J_0=J_3\). For \(m=4,5\), the bracket \((m-6)\kappa(\kappa+m+3)+3m^2\) decreases strictly from a positive value to minus infinity and has the unique positive zero \(\kappa_-(m)\). This produces the first family of transitions, since types \(a=1,2\) are strictly worse than type \(a=0\).

For \(m=6,7\), \(J_0\) is strictly smaller than all alternatives. For \(m\ge8\), types \(a=2,3\) are strictly dominated by type \(a=0\), so compare only \(a=0,1\). The quadratic numerator of \(J_0-J_1\) starts negative, opens upward and has exactly one positive zero \(\kappa_+(m)\), giving the second family of transitions. Because all denominators are strictly positive, all strict and equality cases follow. Finally, dividing its defining equation by \(m^3\), and using the explicit positive-root expression, proves \(\kappa_+(m)/m\to1\).

## Verification
Run `python verification/verify.py` using Python 3 and SymPy. The standalone program independently constructs each weighted grounded Laplacian for small \(m\) and evaluates its exact inverse trace; checks the Woodbury reduction, three symbolic difference identities, polynomial coefficient positivity, all branch classifications over a rational grid, and the equations defining threshold ties. Its output is `PASS 183 exact symbolic and rational assertions`. The theorem is proved for all \(m\ge3\) and \(\kappa>0\) by the algebra above; these finite tests are supplementary.

## Relationship to prior work
Fitch and Leonard (arXiv:1407.1569, first posted 2014-07-07) introduce joint centrality for noisy consensus leaders and explicitly derive finite-gain optimality for **two** noisy leaders, with detailed cycle examples; they treat arbitrary numbers principally in the noise-free setting. Patterson, Yi and Zhang (arXiv:1708.06873) give general resistance-distance expressions and explicit special topologies (paths, cycles and trees) but not the three-leader \(K_{m,3}\) phase diagram. Mackin and Patterson (arXiv:1712.08212) develop submodular approximation guarantees for the noisy-leader objective rather than an exact three-leader placement classification in this family. Patterson, McGlohon and Dyagilev (arXiv:1412.6595) address one-dimensional paths and rings.

The matrix trace itself follows from standard inverse identities, and generic exhaustive search among four symmetry orbits is possible. The new mathematical content claimed here is the exact all-\(m\), all-positive-gain sign classification, the two different relocation mechanisms across network-size regimes, and sharp algebraic switchpoints. Existing general coherence formulas do not, without the polynomial comparisons above, directly give these switch regimes.

## Limitations
The theorem applies to unit cross-edge weights, exactly three equal finite-gain leaders, and one community of exactly three vertices. It does not classify arbitrary unequal gains, larger leader budgets, unequal edge weights or general complete bipartite sizes. Unindexed equivalent literature, especially specializations of general resistance-distance/coherence formulas, remains an originality risk.

## References
1. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public version, 2014-07-07). https://arxiv.org/pdf/1407.1569
2. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (2017). https://arxiv.org/pdf/1708.06873
3. E. Mackin and S. Patterson, *Submodular Optimization for Consensus Networks with Noise-Corrupted Leaders*, arXiv:1712.08212 (2017). https://arxiv.org/pdf/1712.08212
4. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (2014). https://arxiv.org/pdf/1412.6595
