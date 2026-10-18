# Exact weak-selection fixation spectra for balanced rock–paper–scissors populations on cubic six-vertex graphs

## Finding

Consider a three-strategy birth–death evolutionary game on a connected, simple, undirected, cubic graph with six vertices. For the antisymmetric rock–paper–scissors interaction matrix
\[
A=\begin{pmatrix}0&1&-1\\-1&0&1\\1&-1&0\end{pmatrix},
\]
let \(H_G(s,w)\) denote the probability that strategy \(0\) ultimately fixes when the initial vertex assignment is \(s\) and the selection intensity is \(w\). Among the \(90\) assignments with precisely two vertices of each strategy, the exact first-order coefficients in
\[
H_G(s,w)=\tfrac13+w\,d_G(s)+O(w^2)
\]
have the following **complete** distributions; each number in parentheses is its multiplicity among the \(90\) labeled assignments:

* On the triangular prism \(C_3\square K_2\): \(-22/281\) (6), \(-65/1686\) (6), \(-37/1686\) (12), \(0\) (42), \(37/1686\) (12), \(65/1686\) (6), \(22/281\) (6).
* On \(K_{3,3}\): \(-1/66\) (18), \(0\) (54), \(1/66\) (18).

There are no other connected simple cubic graphs of order six. Consequently these two distributions exhaust the graph topologies at this size, and the exact derivative is **not** determined by graph degree, population size, and initial strategy frequencies. For example, on the prism, \(s=(0,0,1,2,2,1)\) gives \(d_G(s)=22/281\), while \((0,0,2,1,1,2)\) gives \(-22/281\), with the locations of strategy \(0\) unchanged. On \(K_{3,3}\), \((2,1,2,1,0,0)\) and \((1,2,1,2,0,0)\) similarly give \(1/66\) and \(-1/66\).

## Assumptions and scope

Fix the vertex set \(\{0,1,2,3,4,5\}\), and write \(s_u\in\{0,1,2\}\) for the strategy at vertex \(u\). The prism has edges \((0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)\). The graph \(K_{3,3}\) has every edge between the parts \(\{0,1,2\}\) and \(\{3,4,5\}\), and no other edges.

At each discrete step, independently of earlier events conditional on the state, donor \(u\) is selected with probability proportional to its fitness
\[
F_u(s,w)=1+w\pi_u(s),\qquad \pi_u(s)=\sum_{z\sim u} A_{s_u,s_z},
\]
and replaces one of its three neighbors chosen uniformly. No mutations occur. For example \(0\leq w<1/3\) guarantees positive fitness, and the formulas concern the right derivative at \(w=0\). This normalization has the same first-order fixation coefficients as the convention \(F_u=1-w+w\pi_u\), since the uniform \(-w\) fitness shift cancels to first order in normalized donor probabilities.

All initial states, including those outside the balanced class, are used to solve the fixation problem. The asserted classification counts only balanced initial assignments with two occurrences of each strategy. All vertex labels and multiplicities are literal; graph automorphisms are not divided out in the reported counts.

## Proof

**Graph completeness.** The complement of a cubic simple graph on six vertices is a simple \(2\)-regular graph on six vertices. Every such graph is either a six-cycle or two disjoint triangles. Taking complements yields the triangular prism and \(K_{3,3}\), respectively. Both are connected.

**Neutral harmonic function.** There are \(3^6=729\) labeled strategy states. For state \(s\), let \(s^{v\leftarrow u}\) be the state obtained by copying the type at \(u\) to adjacent vertex \(v\). The transition operator at neutrality is
\[
(P_0f)(s)=\frac1{18}\sum_{u=0}^5\sum_{v\sim u} f(s^{v\leftarrow u}).
\]
Because the graph is undirected and cubic, the neutral count of strategy \(0\) is a martingale, so its fixation probability is \(H_G(s,0)=\#\{u:s_u=0\}/6\). On a connected finite graph, every nonmonochromatic state has a positive-probability sequence of copies leading to a monochromatic state; finite-state absorption follows. Thus the neutral Dirichlet problem is unique.

**Exact derivative equation.** For sufficiently small \(w\), all transient probabilities and the fixation probability are analytic in \(w\), since the transient substochastic matrix has spectral radius smaller than one at neutrality. Differentiating the harmonicity identity \(H_G(\cdot,w)=P_wH_G(\cdot,w)\) gives, for \(d_G(s)=\partial_w H_G(s,w)|_{w=0}\),
\[
d_G(s)-(P_0d_G)(s)=g_G(s),\qquad
 g_G(s)=\frac1{108}\sum_{u=0}^5\sum_{v\sim u}\pi_u(s)
 \bigl(\mathbf1_{s_u=0}-\mathbf1_{s_v=0}\bigr).
\]
Indeed donor probability has derivative \((\pi_u-\overline\pi)/6\). The \(\overline\pi\) part cancels after summing oriented edges, since each edge appears in both directions; the change of the neutral harmonic function upon copying is \((\mathbf1_{s_u=0}-\mathbf1_{s_v=0})/6\). The boundary values of \(d_G\) at all three monochromatic states are zero. The Dirichlet problem is unique by absorption.

**Exhaustive rational certificate.** `CERTIFICATES.json` contains, for **each graph**, exactly \(729\) exact rational values of \(d_G(s)\), ordered lexicographically as the six-digit tuples in `itertools.product(range(3), repeat=6)`. The standalone `verify_exact.py` reconstructs all \(729\) directed transition sums per graph from the stated edge sets and matrix, checks the displayed derivative equation **with exact rational arithmetic at every state**, checks the three monochromatic boundary conditions, and counts all \(90\) balanced assignments. Its comparisons return precisely the distributions stated above. Uniqueness of the Dirichlet problem upgrades this complete finite certificate to a proof of the exact derivatives; no floating-point approximation or extrapolation from a subset of configurations is used.

**Sign reversal.** Exchanging the labels \(1\) and \(2\) while keeping \(0\) fixed negates the rock–paper–scissors payoff matrix, while leaving the neutral transition kernel unchanged. The forcing \(g_G\) therefore changes sign. By uniqueness, so does \(d_G\). This independently explains the symmetric value multiplicities and supplies paired configurations with opposite fixation bias and identical frequencies and fixed positions for strategy \(0\).

## Verification

Run `python3 verify_exact.py` in a directory containing the two supplied artifacts `verify_exact.py` and `CERTIFICATES.json`. Python's standard library alone suffices. It checks \(729\) exact derivative equations for each graph, all balanced frequencies and multiplicities, and \(1458\) exact label-exchange identities. The certificate and source are fully included; the checker requires no external data, database, or solver. As a supplementary numerical check, full-state floating-point Markov solves at small positive and negative selection strengths were used as a sanity check, but these are not relied upon as proof.

## Relationship to prior work

Dubey and Chakraborty (2026) analyze three-strategy birth–death dynamics on random regular networks through a pair approximation and diffusion treatment, producing a fixation expansion in global strategy frequencies. The theorem here concerns **exact**, configuration-resolved six-vertex Markov chains, without pair approximation or diffusion scaling. It is a small-system benchmark for distinguishing within-degree topology and strategy placement; it is not an error claim against their approximation.

Chen, McAvoy, and Nowak (2016) establish configuration-dependent fixation criteria for **two** competing strategies on regular graphs. McAvoy and Allen (2019/2021) give broad weak-selection perturbation methods within a **two-type** mutant–resident framework. Their structural insight and perturbative reasoning are important precedents but neither paper's stated results enumerate this three-strategy finite rock–paper–scissors classification. Wang, Perc, and Szolnoki (2024) derive multi-strategy replicator equations using pair approximation for graph games, especially in large-population settings; those equations do not give the exact labeled finite-state spectra reported here. General finite absorbing-chain linear algebra underlies the proof, but the claimed output is the complete, explicit topology-dependent exact rational classification rather than a new Markov-chain method.

## Limitations

The findings are confined to cubic graphs with six vertices, the displayed antisymmetric three-strategy game, birth–death replacement, and an initial \(2{:}2{:}2\) mixture. The spectra concern the infinitesimal selection derivative; they do not classify fixation probabilities for arbitrary positive selection strength, other payoff matrices, other update rules, or larger graphs. In particular, the results do not establish a general graph-degree criterion or an error bound for pair approximation. Searches cannot rule out every unpublished or unindexed finite enumeration; the classification and its certificate are supplied as directly checkable new mathematical content.

## References

1. V. K. Dubey and S. Chakraborty, *Stochastic evolutionary dynamics in structured populations: Network degree governs evolutionary stability*, arXiv:2610.05857v1 (first posted 2026-10-05), https://arxiv.org/html/2610.05857v1.
2. Y.-T. Chen, A. McAvoy, and M. A. Nowak, *Fixation probabilities for any configuration of two strategies on regular graphs*, Scientific Reports 6, 39181 (2016), https://arxiv.org/html/1605.01387v2.
3. A. McAvoy and B. Allen, *Fixation probabilities in evolutionary dynamics under weak selection*, Journal of Mathematical Biology (2021), https://arxiv.org/html/1908.03827v3.
4. C. Wang, M. Perc, and A. Szolnoki, *Evolutionary dynamics of any multiplayer game on regular graphs*, Nature Communications 15, 5349 (2024), https://www.nature.com/articles/s41467-024-49505-5.
