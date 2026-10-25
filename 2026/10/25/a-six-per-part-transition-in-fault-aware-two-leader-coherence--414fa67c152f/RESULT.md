# A six-per-part transition in fault-aware two-leader coherence

## Finding
Let \(n\ge3\) be an integer. Form the simple, unit-conductance graph \(G_n\) by deleting one edge \(\{a,b\}\) from the balanced complete bipartite graph \(K_{n,n}\), with \(a\) in the first part and \(b\) in the second. For every unordered two-vertex leader set \(S\), define the normalized stationary coherence loss
\[
J_n(S)=\operatorname{tr}\bigl(L_{V(G_n)\setminus S,V(G_n)\setminus S}^{-1}\bigr),
\]
where \(L\) is the combinatorial Laplacian (including original degrees in its grounded principal submatrix). Then **all** minimizers are precisely:

- If \(3\le n\le5\), the single pair \(S=\{a,b\}\) comprising the two endpoints of the missing edge.
- If \(n\ge6\), the \((n-1)(n-2)\) pairs consisting of any two **nonexceptional** vertices in the *same* bipartition part. No other pair minimizes.

There is no tie at any integer \(n\ge3\). The minimum is explicitly
\[
\min_{|S|=2}J_n(S)=\begin{cases}
\displaystyle\frac{2(n-1)(3n-2)}{n(2n-1)},&3\le n\le5,\\[6pt]
\displaystyle\frac{3n^3-10n^2+13n-5}{n(n-1)^2},&n\ge6.
\end{cases}
\]
The single removed link changes the preferred leader-pair type in small bicliques. In contrast, on intact \(K_{n,n}\), same-part pairs are always optimal when \(n\ge3\): their objective \(3-4/n\) beats a mixed-part pair's objective by \(1/(2n-1)\). For the defective graph the gap between the two competing classes is
\[
J_n(\{a,b\})-J_n(\{u,v\})=
\frac{n^3-6n^2+5n-1}{n(n-1)^2(2n-1)},
\]
where \(u,v\) are any two ordinary vertices of the same part. It changes sign *between* the integers five and six; at \(n=5\) the advantage of the defect-endpoint pair is exactly \(1/720\), and asymptotically the same-part pair wins by \(1/(2n)+O(n^{-2})\).

## Assumptions and scope
Both parts have exactly \(n\) vertices. Every retained edge has conductance one; exactly the edge \(\{a,b\}\) is absent. Write \(A\) and \(B\) for the \(n-1\) ordinary vertices in the two respective parts. The leaders are exactly two fixed, noise-free agents; all others are followers. Under independent additive unit-intensity Brownian perturbations of the follower consensus dynamics \(dx_F=-L_{FF}x_F\,dt+dW_F\) relative to fixed leaders, stationary total variance is \(J_n(S)/2\). Any common positive noise intensity only rescales the objective. Because \(G_n\) is connected for \(n\ge3\), every such \(L_{FF}\) is positive definite.

The claim is *not* made for nonbalanced graphs, multiple missing links, weighted defects, noise-corrupted leaders, or other objectives such as convergence time or controllability rank.

## Proof
**1. Complete classification of leader-pair orbits.** Interchanging the two bipartition parts and permuting ordinary vertices leaves \(G_n\) unchanged. Hence the eight formal pair types reduce to five objective values \(J_0,\ldots,J_4\):

| Type | Leader set | Exact value |
|---|---|---|
| \(J_0\) | \(\{a,b\}\) | \(\displaystyle\frac{2(n-1)(3n-2)}{n(2n-1)}\) |
| \(J_1\) | \(\{a,u\}\), \(u\in A\), or symmetrically \(\{b,v\}\), \(v\in B\) | \(\displaystyle\frac{6n^3-16n^2+19n-10}{n(2n^2-3n+2)}\) |
| \(J_2\) | \(\{a,v\}\), \(v\in B\), or symmetrically \(\{b,u\}\), \(u\in A\) | \(\displaystyle\frac{6n^3-18n^2+23n-10}{2n(n-1)^2}\) |
| \(J_3\) | \(\{u,v\}\), \(u\in A,v\in B\) | \(\displaystyle\frac{2(3n^3-11n^2+17n-10)}{n(2n^2-5n+4)}\) |
| \(J_4\) | \(\{u,u'\}\subset A\) or \(\{v,v'\}\subset B\) | \(\displaystyle\frac{3n^3-10n^2+13n-5}{n(n-1)^2}\) |

Each displayed class is realizable for every \(n\ge3\).

**2. Derivation, without matrix-size extrapolation.** Partition followers into their nonempty intersections with \(\{a\},A,\{b\},B\). If group \(g\) contains \(r_g\) vertices with original graph degree \(d_g\), every vector that sums to zero inside \(g\) and vanishes elsewhere is an eigenvector of the grounded Laplacian with eigenvalue \(d_g\). Here \(d_a=d_b=n-1\) and \(d_A=d_B=n\). These contrast eigenspaces have total dimension \(\sum_g(r_g-1)\). On the complementary subspace of vectors constant inside each group, the quotient acts by
\[
H_{gh}=d_g\mathbf1_{g=h}-\varepsilon_{gh}r_h,
\]
where \(\varepsilon_{gh}=1\) for group pairs in opposite parts, except \(\varepsilon_{ab}=\varepsilon_{ba}=0\), and is otherwise zero. The quotient is similar to a symmetric positive definite matrix, so
\[
J_n(S)=\sum_g\frac{r_g-1}{d_g}+\operatorname{tr}(H^{-1}).
\]
The quotient has size at most four, independent of \(n\), and exact inversion gives the table. For \(n=3\), when selecting both ordinary leaders in one part leaves a group empty, omit that group; direct reduced inversion produces the same formula. The included symbolic verification program independently reconstructs each orbit from this recipe and checks direct grounded inverses for all leader pairs of sizes \(3\le n\le7\).

**3. Elimination of every noncontender.** Exact subtraction of the rational expressions in the table gives
\[
J_1-J_0=\frac{4n^2-7n+2}{n(2n-1)(2n^2-3n+2)},
\]
\[
J_2-J_0=\frac{2n^3+4n^2-7n+2}{2n(n-1)^2(2n-1)},
\]
\[
J_3-J_0=\frac{2(4n^2-7n+2)}{n(2n-1)(2n^2-5n+4)}.
\]
For every integer \(n\ge3\), all denominators are positive. The common quadratic numerator is \(4(n-3)^2+17(n-3)+17>0\), and the cubic numerator has strictly positive coefficients after substituting \(n=3+k\), \(k\ge0\). Therefore \(J_1,J_2,J_3>J_0\) universally. Every optimizer consequently belongs to class \(J_0\) or \(J_4\).

**4. Sharp integer boundary and completeness.** The remaining difference is
\[
J_0-J_4=\frac{f(n)}{n(n-1)^2(2n-1)},\qquad f(n)=n^3-6n^2+5n-1.
\]
Directly \(f(3)=f(4)=-13\), \(f(5)=-1\), \(f(6)=29\), and \(f(n+1)-f(n)=3n(n-3)>0\) for all integers \(n\ge4\). Thus the difference is strictly negative for \(3\le n\le5\), strictly positive for \(n\ge6\), and never zero on the specified integer domain. In class \(J_4\), the number of distinct pairs is \(2\binom{n-1}{2}=(n-1)(n-2)\). These observations prove the minimum, every minimizing configuration, and the absence of hidden ties.

## Verification
The standalone file `verify.py` (Python 3 and SymPy) reconstructs the five rational objective expressions through eight symbolic leader-pair orbit calculations, verifies four factored comparison identities and their positive-polynomial certificates, and compares the formulas with direct exact rational inverses of all grounded Laplacians for \(3\le n\le7\) (245 leader pairs). Run `python verify.py` from the directory containing the file. Its expected successful line begins `VERIFY_OK`. The symbolic identities and positivity inequalities are *universal* algebraic proofs when combined with the stated group decomposition; the finite inverse checks alone would not prove the all-size theorem.

## Relationship to prior work
Fitch and Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first submitted 7 July 2014), derive an arbitrary-network objective through joint centrality and analyze paths and cycles. This general formulation supplies the stochastic-consensus motivation, but neither their special-graph theorems nor their general implicit maximization statement evaluates the five defective-biclique pair orbits or identifies the integer-six switch. Their earlier 2013 conference contribution provides an analogous general two-leader joint-centrality perspective. Patterson, McGlohon and Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (20 December 2014), obtain efficient optimal selection algorithms for paths and rings, not this non-one-dimensional graph. The present result is a new explicit structural specialization, not a new general leader-selection algorithm.

## Limitations
No claim is made of priority beyond the literature examined; a previously unindexed explicit equivalent classification remains possible. The result concerns precisely two pinned noise-free leaders, balanced bipartite parts and one absent edge; general perturbations need new analysis. The optimizer's objective advantage at \(n=5\) is only \(1/720\), so floating-point comparisons near the boundary are ill-conditioned in relative ranking; exact arithmetic is used here.

## References
1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, initial public version 2014-07-07, https://arxiv.org/abs/1407.1569.
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, initial public version 2014-12-20, https://arxiv.org/abs/1412.6595.
3. K. E. Fitch and N. E. Leonard, *Information Centrality and Optimal Leader Selection in Noisy Networks*, conference preprint (2013), https://naomi.princeton.edu/wp-content/uploads/sites/744/2021/03/FitchCDC2013ol.pdf.
