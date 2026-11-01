# A six-state transfer law for two-cycle orbits of parallel chip-firing on open ladders

## Finding

Let \(L_n=P_n\square K_2\) be the labelled open ladder on \(n\ge2\) rungs. In standard synchronous parallel chip-firing, a vertex holding at least its degree in chips simultaneously sends one chip to each neighbour, and all other vertices do not fire. Let \(N_n\) be the number of distinct **primitive two-cycle orbits** of the resulting update map on nonnegative integer chip configurations, with each pair of alternating configurations counted once. Then

\[
\boxed{\sum_{n\ge2}N_nz^{n-2}=\frac{18-11z-10z^2+z^3}{(1-z^2)(1-12z+z^2)}.}
\]

In particular, the initial counts for ladder lengths \(2,3,4,5,6,7,8\) are \(18,205,2450,29185,347778,4144141,49381922\), and for every \(n\ge6\),

\[
N_n=12N_{n-1}-12N_{n-3}+N_{n-4}.
\]

Writing \(\lambda_\pm=6\pm\sqrt{35}\), the explicit expression is

\[
N_n=\frac{302+51\sqrt{35}}{35}\lambda_+^{n-2}+\frac{302-51\sqrt{35}}{35}\lambda_-^{n-2}+\frac1{10}+\frac9{14}(-1)^n.
\]

Consequently \(N_n\sim \frac{302+51\sqrt{35}}{35}(6+\sqrt{35})^{n-2}\). These are counts of *initially periodic primitive orbits*, not the sizes of their eventual basins, and the theorem does not classify longer-period attractors.

## Assumptions and scope

Vertices are \((i,r)\), where \(1\le i\le n\) and \(r\in\{0,1\}\); a rung joins \((i,0)\) to \((i,1)\), and horizontal edges join \((i,r)\) to \((i+1,r)\) for \(i<n\). All edges are undirected and simple. If a configuration is \(c\in\mathbb Z_{\ge0}^{2n}\), let \(d_v\) denote the degree, \(s_v=\mathbf1_{\{c_v\ge d_v\}}\), and define the synchronous update

\[
F(c)_v=c_v-d_vs_v+\sum_{w\sim v}s_w.
\]

A primitive two-cycle is an orbit \(\{c,F(c)\}\) satisfying \(F^2(c)=c\) and \(F(c)\ne c\). The counted configurations have finite chip totals automatically; their number is finite despite the unbounded ambient state space.

## Proof

**1. Firing phases and exact local multiplicity.** Suppose \(c\) has primitive period two. Write \(s_v^{(0)},s_v^{(1)}\in\{0,1\}\) for its successive firing indicators. Summing its two updates yields the graph-Laplacian equation

\[
\Delta_G(s^{(0)}+s^{(1)})=0.
\]

Connectivity makes \(s_v^{(0)}+s_v^{(1)}\) constant across vertices. If this constant is zero or two, no vertex changes chips, so the configuration is fixed; therefore the constant is one. Thus each vertex fires in exactly one of the two rounds. Choose its phase \(\phi_v=s_v^{(0)}\in\{0,1\}\), and put

\[
b_v(\phi)=\#\{w\sim v:\phi_w\ne\phi_v\}.
\]

If \(\phi_v=1\), exactly \(b_v\) fewer chips return from neighbours than the vertex sends, so \(F(c)_v=c_v-b_v\). The necessary and sufficient conditions that it fires in round zero and not round one are

\[
d_v\le c_v\le d_v+b_v-1.
\]

If \(\phi_v=0\), its first update instead gains \(b_v\) chips, and the necessary and sufficient conditions that it waits in round zero and fires in round one are

\[
d_v-b_v\le c_v\le d_v-1.
\]

Both intervals consist of precisely \(b_v\) nonnegative integers (possibly none when \(b_v=0\)). Under these inequalities the second update restores the initial chips, and at least one firing occurs whenever the product is positive. Every vertex makes one firing per two steps. Hence the exact number of states with primitive period two is \(\sum_{\phi\in\{0,1\}^{V(G)}}\prod_vb_v(\phi)\). Each primitive orbit has exactly two states, giving

\[
\boxed{N_G=\frac12\sum_{\phi\in\{0,1\}^{V(G)}}\prod_{v\in V(G)}b_v(\phi).}
\]

This phase-cut identity is background; the new evaluation below is specific to open ladders.

**2. Four rung types and transfer.** Encode the two phases on rung \(i\) as \(a_i=(\phi_{i,0},\phi_{i,1})\in\{00,01,10,11\}\). For adjacent rung types \(a,b\), the product of opposite-phase-neighbour counts on a left endpoint is

\[
E(a,b)=(\mathbf1_{a_0\ne b_0}+\mathbf1_{a_0\ne a_1})(\mathbf1_{a_1\ne b_1}+\mathbf1_{a_0\ne a_1}).
\]

For three consecutive rung types \(a,b,c\), the corresponding interior-rung weight is

\[
W(a,b,c)=(\mathbf1_{b_0\ne a_0}+\mathbf1_{b_0\ne c_0}+\mathbf1_{b_0\ne b_1})(\mathbf1_{b_1\ne a_1}+\mathbf1_{b_1\ne c_1}+\mathbf1_{b_0\ne b_1}).
\]

The full weight on a rung sequence \((a_1,\ldots,a_n)\) is \(E(a_1,a_2)E(a_n,a_{n-1})\prod_{i=2}^{n-1}W(a_{i-1},a_i,a_{i+1})\). Accordingly, a transfer indexed by the sixteen ordered rung pairs \((a,b)\) counts exactly the phase sum in step 1.

**3. A six-orbit quotient.** Global simultaneous complementation of both phase colors and interchange of the two ladder rows preserve all weights. They act on the sixteen pair types with six orbits represented by

\[
(00,00),\ (00,01),\ (00,11),\ (01,00),\ (01,01),\ (01,10),
\]

of sizes \(2,4,2,4,2,2\), respectively. For each representative \((a,b)\), sum the weights \(W(a,b,c)\) of transitions \((a,b)\to(b,c)\) over all targets in a given symmetry orbit. The resulting integer transfer matrix is

\[
B=\begin{pmatrix}
0&0&1&0&0&0\\
0&0&0&7&2&6\\
1&4&4&0&0&0\\
0&1&2&0&0&0\\
0&0&0&4&1&4\\
0&0&0&12&4&9
\end{pmatrix}.
\]

The initial endpoint weight summed over each orbit is the row vector \(\ell=(0,0,2,8,2,8)\); the terminal endpoint weight for a representative is the column vector \(r=(0,2,1,0,1,4)^{\mathsf T}\). Therefore the exact orbit count is

\[
\boxed{N_n=\tfrac12\ell B^{n-2}r\quad(n\ge2).}
\]

This reduction is valid also at \(n=2\), when the product of internal-rung weights is empty. The accompanying independent checker reconstructs all six symmetry orbits and every entry of \(B,\ell,r\) from the defining binary rung weights rather than taking the matrix entries on trust.

**4. Rational generating function, recurrence and asymptotics.** Direct exact arithmetic in the displayed \(6\times6\) matrix gives

\[
\det(I-zB)=(1-z)^3(1+z)(1-12z+z^2)
\]

and

\[
\tfrac12\ell\operatorname{adj}(I-zB)r=(1-z)^2(18-11z-10z^2+z^3).
\]

Cancelling the common factor \((1-z)^2\) proves the stated generating function. Its denominator is \(1-12z+12z^3-z^4\), proving the fourth-order recurrence. Partial fractions yield the displayed exact closed form. Since \(6+\sqrt{35}>1\) and \(|6-\sqrt{35}|<1\), the stated exponential equivalent follows.

For independent verification of the infinite matrix computation, the checker also verifies \(\det(xI-B)=(x-1)^3(x+1)(x^2-12x+1)\) via its polynomial matrix identity, then checks six initial scalar residuals for the asserted order-four annihilator. The characteristic-degree-six identity propagates those six zero residuals to all exponents, rather than extrapolating from finitely many computed orbit counts.

## Verification

The included standalone standard-library script `verify.py` reconstructs the six-state quotient and transfer from local rung formulas, verifies a degree-six characteristic polynomial identity and six order-four annihilator seeds, and compares the exact transfer formula with independent enumeration of all \(2^{2n}\) firing-phase assignments for \(2\le n\le8\), totaling \(87{,}376\) phase assignments. It also directly applies two chip-firing updates to all \(341{,}248\) bounded chip configurations with \(0\le c_v<2d_v\) for \(2\le n\le4\); this bounded box contains every primitive two-cycle state by step 1. These checks agree exactly with the theorem, but finite enumeration alone is not its all-length proof; the preceding phase-bijection and matrix identities provide that proof. See `verification_output.txt` for recorded stdout.

## Relationship to prior work

The underlying period-two firing-phase characterization is closely related to established general parallel chip-firing results; the present contribution is not a new criterion for two-periodicity on arbitrary graphs. Dall'Asta's early ring-model analysis [1] gives exact one-dimensional fixed-energy sandpile orbit results on periodic chains, not the six-state open-ladder count above. Jiang [2] treats possible periods on graphs including complete bipartite graphs, but does not give this ladder-specific generating function or full primitive-two-cycle orbit census. Fey, Levine and Wilson [3] study a ladder in stationary-density questions for a different sandpile setup; its transfer eigenvalue \(2+\sqrt3\) concerns density rather than the synchronous chip-firing two-cycle count here. Jiang, Scully and Zhang [4] analyze firing patterns and motors and provide primary MSC \(37B15\), but do not present the ladder orbit-count formula.

The formula is a nontrivial closed evaluation of a general weighted phase-cut sum for the simplest width-two cyclic strip. Prior counts for path graphs, complete binary trees and complete bipartite graphs do not imply these ladder counts by relabelling or graph restriction. Literature and mathematical-record searches did not reveal the exact coefficient sequence, rational function or an equivalent stronger ladder enumeration. Absence of indexed matches is not proof of global historical novelty; an unindexed or inaccessible equivalent may exist.

## Limitations

The result counts only primitive period-two orbits that are already periodic, not transient basins, maximum eventual period or chip-mass refinements. Graph vertices and edges are labelled as described; reversing the ladder or exchanging its rows does not identify chip configurations as the same orbit. Every time-phase pair is counted as one orbit. Completeness of the literature comparison is limited by indexing and access. Verification is a self-review and exact executable reproduction; independent audit has not been performed.

## References

1. L. Dall'Asta, *Exact solution of the one-dimensional deterministic Fixed-Energy Sandpile*, arXiv:cond-mat/0601267 (first posted 2006-01-12), https://arxiv.org/abs/cond-mat/0601267 .
2. T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (first posted 2010-03-04), https://arxiv.org/abs/1003.0943 .
3. A. Fey, L. Levine, D. B. Wilson, *The approach to criticality in sandpiles*, arXiv:1001.3401 (2010), https://arxiv.org/abs/1001.3401 .
4. T.-Y. Jiang, Z. Scully, Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (first posted 2012-11-29), https://arxiv.org/abs/1211.6786 .
