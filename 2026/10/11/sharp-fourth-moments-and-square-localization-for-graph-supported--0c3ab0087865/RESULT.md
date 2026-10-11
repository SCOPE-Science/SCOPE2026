# Sharp fourth moments and square localization for graph-supported Walsh spaces

## Finding
Let \(G=(V,E)\) be a finite simple undirected graph with \(m=|E|\ge1\), and suppose every edge of \(G\) belongs to **at most one simple four-cycle**. Let \((\varepsilon_v)_{v\in V}\) be independent uniform Rademacher signs, and for real edge coefficients define
\[
F_a=\sum_{\{u,v\}\in E}a_{uv}\varepsilon_u\varepsilon_v,\qquad S=\mathbb E F_a^2=\sum_{e\in E}a_e^2.
\]
The sharp operator norm of the coefficient embedding from \(\ell_2^m\) into \(L^4\), raised to the fourth power, is
\[
\sup_{a\ne0}\frac{\mathbb E|F_a|^4}{S^2}
=\begin{cases}
3-2/m,&G\text{ has no four-cycle},\\
4,&G\text{ has at least one four-cycle}.
\end{cases}
\]
In the first case equality means \(|a_e|\) is the same for all \(e\). In the second case equality means the support is exactly one four-cycle, the four magnitudes are equal, and the product of the four signed coefficients is positive.

The four-cycle-free case has a further structural interpretation: identifying the edge coefficients with the coefficients of \(m\) independent signs is a real-linear **isometry in \(L^4\)**, not merely an equality of extremal constants.

If the graph has a four-cycle and \(0\le\delta<1/2\), then
\[
\mathbb E|F_a|^4\ge (4-\delta)S^2
\quad\Longrightarrow\quad
\max_{C\in\mathcal C_4(G)}\frac{\sum_{e\in C}a_e^2}{S}
\ge\frac{1+\sqrt{1-2\delta}}2.
\]
This bound is sharp as a universal statement across the class for every such \(\delta\).

## Assumptions and scope
All graphs are finite, simple, and undirected. A four-cycle means a set of four distinct edges forming a cycle on four distinct vertices; chords are permitted. The hypothesis means two different four-cycles may share vertices but **cannot share edges**. In the optimization, \(a\ne0\), real coefficients are arbitrary, and zero coefficients are allowed. The probability space is the finite independent sign cube. The \(L^2\) and \(L^4\) norms are probability-normalized.

## Proof
**Fourth-moment identity.** Orthogonality of distinct characters \(\varepsilon_u\varepsilon_v\) gives \(\mathbb EF_a^2=S\). In the expansion of \(\mathbb EF_a^4\), a monomial has nonzero expectation exactly when each vertex occurs an even number of times. With repeated edges, there are the fourth powers of individual coefficients and six copies of every product of two distinct squared coefficients. With four distinct edges, the only possible even-degree simple graph is a four-cycle, and its product occurs with multiplicity \(4!=24\). Thus for every simple graph, without yet assuming disjointness,
\[
\mathbb EF_a^4=3S^2-2\sum_{e\in E}a_e^4
 +24\sum_{C\in\mathcal C_4(G)}\prod_{e\in C}a_e.\tag{1}
\]

**No four-cycle.** The final sum vanishes. Cauchy--Schwarz gives \(\sum_ea_e^4\ge S^2/m\), with equality exactly for equal squared coefficients. Equation (1) proves the first branch. The fourth moment of \(m\) independent first-order Rademacher signs with identical coefficient vector is also \(3S^2-2\sum_ea_e^4\). Equality of the \(L^4\)-norm polynomial at *every* real coefficient vector establishes the stated linear isometry.

**At least one four-cycle.** Because the four-cycles are pairwise edge-disjoint, their edge sets partition a portion of \(E\). For each four-cycle \(C\), let \(s_C=\sum_{e\in C}a_e^2\) and \(P_C=\prod_{e\in C}a_e\). Write \(E_0\) for the edges in no four-cycle. Rearranging (1) gives the exact decomposition
\[
4S^2-\mathbb EF_a^4
=\biggl(S^2-\sum_Cs_C^2+2\sum_{e\in E_0}a_e^4\biggr)
 +\sum_C\biggl(s_C^2+2\sum_{e\in C}a_e^4-24P_C\biggr).\tag{2}
\]
Every term on the right is nonnegative. For the first bracket, \(S\ge\sum_Cs_C\) and the \(s_C\) are nonnegative. For each cycle, four-term arithmetic--geometric mean gives \(s_C^2\ge16|P_C|\) and \(2\sum_{e\in C}a_e^4\ge8|P_C|\), hence the second bracket is nonnegative. The last bracket can vanish with \(s_C>0\) only if the four \(|a_e|\) are equal and \(P_C>0\). The first bracket can vanish only if no mass is outside four-cycles and at most one \(s_C\) is positive. This proves the bound, existence of equality via one uniformly weighted square, and complete equality classification.

**Quantitative localization.** Normalize \(S=1\). Equation (2) implies
\[
4-\mathbb EF_a^4\ge1-\sum_Cs_C^2.
\]
If \(\mathbb EF_a^4\ge4-\delta\), then \(\sum_Cs_C^2\ge1-\delta\). Set \(t=\max_Cs_C\). The bound \(\sum_Cs_C^2\le t\sum_Cs_C\le t\) first gives \(t\ge1-\delta>1/2\). Since the sum of all other cycle masses is at most \(1-t\),
\[
1-\delta\le\sum_Cs_C^2\le t^2+(1-t)^2.
\]
The right inequality yields \(2t(1-t)\le\delta\). Solving on \(t>1/2\) gives \(t\ge(1+\sqrt{1-2\delta})/2\).

To see sharpness for every \(\delta\), take a graph consisting of two disjoint four-cycles, put coefficients of equal positive magnitudes within each, and choose the squared-mass fractions of the two cycles to be \(t=(1+\sqrt{1-2\delta})/2\) and \(1-t\). Both local cycle brackets in (2) vanish; the only deficit is the cross term \(2t(1-t)=\delta\). Thus the mass threshold is attained exactly.

## Verification
A standalone Python 3 standard-library script, `verify.py`, enumerates sign assignments with exact rational arithmetic for eight illustrative simple graphs (a square, a five-cycle, two disjoint squares, two squares sharing a vertex, a square with a tail, a chorded square, and one- and two-edge graphs). For three rational coefficient patterns each it checks the exact fourth-moment identity and the applicable bounds; two additional rational examples test the two-square sharpness formula. Running `python3 verify.py` produces `EDGE_DISJOINT_SQUARE_MOMENT_EXACT_OK 24`. The proof of the unrestricted result is (1)--(2) and the subsequent inequalities; the finite tests are not an exhaustive proof.

## Relationship to prior work
Classical hypercontractivity supplies general moment-comparison bounds for low-degree Rademacher chaos. Barak and collaborators study the importance and complexity of exact \(2\to4\) norms of subspaces on the Boolean cube, rather than the edge-disjoint-square subclass. Ivanisvili and Tkocz improve general homogeneous-chaos comparisons but do not identify graph-specific extremizers. Bhattacharya and collaborators explicitly connect graph-quadratic-chaos fourth moments with counts of four-cycles, chiefly for unweighted graph adjacency statistics and asymptotic normality. The present assertion uses arbitrary real edge coefficients and gives an exact all-size subspace norm, complete extremizer classification, and a sharp uniform near-extremizer localization law in the specified graph class. General fourth-moment counting identities are used as established background; the identity (1) alone is not claimed to be novel.

## Limitations
The sharp optimization and mass-concentration statements require four-cycles to be pairwise edge-disjoint; overlapping-square graphs can behave differently. The theorem is real-scalar and fourth-moment-specific. The stability law controls the squared mass on one four-cycle, not closeness of its four coefficient magnitudes or signs. It makes no assertion about higher moments or fourth-moment bounds for general graphs. Prior exact results in less obvious additive-energy terminology might imply the conclusion; such equivalences remain a bibliographic risk. Independent mathematical validation has not been performed.

## References
1. B. Barak, F. G. S. L. Brandão, A. W. Harrow, J. A. Kelner, D. Steurer, and Y. Zhou, *Hypercontractivity, Sum-of-Squares Proofs, and their Applications*, arXiv:1205.4484v1 (first posted 21 May 2012), https://arxiv.org/abs/1205.4484.
2. P. Ivanisvili and T. Tkocz, *Comparison of moments of Rademacher chaoses*, arXiv:1807.04358v1 (first posted 11 July 2018), https://arxiv.org/abs/1807.04358.
3. B. B. Bhattacharya, S. Das, S. Mukherjee, and S. Mukherjee, *Fluctuations of Quadratic Chaos*, arXiv:2203.02850v1 (first posted 6 March 2022), https://arxiv.org/abs/2203.02850; see Proposition 1.11 and Section 4.
