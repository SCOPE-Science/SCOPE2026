# Sharp factor-two sparsification boundary for budgeted mixing across a single bridge

## Finding

Let \(p,q\ge2\) be integers, \(N=p+q\), and \(B>0\). Take two disjoint vertex sets of sizes \(p\) and \(q\), each with a distinguished hub \(u\) and \(v\), respectively. Include every spoke from each hub to the other vertices of its own set and the single bridge \(uv\). Any subset of the edges between nonhub vertices *within* each set may also be included; there are no other cross-set edges. Thus the class contains bridge-connected cliques, two stars joined at their centers, and every intermediate choice of internal edges.

For nonnegative conductances \(w_e\) summing to \(B\), let \(L(w)\) be the weighted combinatorial Laplacian. Define
\[
V_{p,q}=\frac{9pq}{p+q}-4>0.
\]
Then every feasible assignment satisfies
\[
\lambda_2(L(w))\le\frac{B}{V_{p,q}}.
\]
**The bound is attained if and only if** \(p\le2q\) and \(q\le2p\). In that entire closed factor-two range, the optimizing conductances are **unique**, even without any invariance assumption:
\[
\begin{aligned}
w_{ux}&=\frac{3q}{N}\frac{B}{V_{p,q}}&& (x\ne u\text{ in the first set}),\\
w_{vy}&=\frac{3p}{N}\frac{B}{V_{p,q}}&& (y\ne v\text{ in the second set}),\\
w_{uv}&=\left(\frac{3pq}{N}-1\right)\frac{B}{V_{p,q}},\\
w_e&=0&&\text{for every additional within-side edge}.
\end{aligned}
\]
Outside that size range the optimal value is *strictly less* than \(B/V_{p,q}\); no formula for its exact value is claimed here.

In particular, when two complete graphs of orders \(p,q\) are connected by one bridge, every optimally budgeted fastest continuous-time reversible mixing process assigns **zero conductance to all edges joining two nonhub vertices**, provided the clique sizes differ by at most a factor of two. The optimal support is a weighted double star.

## Assumptions and scope

The input graph is simple, undirected, and has exactly the two prescribed hubs and one inter-side bridge. The within-side optional nonhub edges may be arbitrary, unrelated across sides, and may be absent. Conductances may be zero, but never negative; the budget is the exact unweighted sum of all edge conductances. The Laplacian acts on real vertex functions and \(\lambda_2\) denotes its second eigenvalue in nondecreasing order, with multiplicity. No discrete-time Markov transition-probability constraints are imposed. The statement is uniform in every pair of integers \(p,q\ge2\), all \(B>0\), and all optional-edge subsets.

## Proof

**Universal upper bound.** Define a real test vector \(z\) by setting it equal to \(2\) on the \(p-1\) first-side nonhub vertices, \(1\) at \(u\), \(0\) at \(v\), and \(-1\) on the \(q-1\) second-side nonhub vertices. Its mean is \(\bar z=(2p-q)/N\), and direct expansion gives
\[
\sum_i(z_i-\bar z)^2=4p+q-4-\frac{(2p-q)^2}{N}=V_{p,q}.
\]
The endpoint difference is exactly \(1\) on every spoke and on the bridge, and \(0\) on every additional within-side edge. Consequently
\[
\lambda_2(L(w))\le
\frac{(z-\bar z\mathbf1)^TL(w)(z-\bar z\mathbf1)}{V_{p,q}}
=\frac{B-\sum_{e\in E_{\mathrm{optional}}}w_e}{V_{p,q}}
\le\frac{B}{V_{p,q}}.
\]

**Equality forces all rates.** Suppose equality holds. Equality in the budget inequality forces every optional-edge conductance to be zero. Equality in the minimum Rayleigh quotient forces \(z-\bar z\mathbf1\) to be a Laplacian eigenvector of eigenvalue \(\lambda=B/V_{p,q}\). At each nonhub vertex the eigenvector equation has just its hub spoke and gives \(w_{ux}=3q\lambda/N\) and \(w_{vy}=3p\lambda/N\), respectively. The eigenvector equation at \(u\) then forces \(w_{uv}=(3pq/N-1)\lambda\). Hence the displayed conductances are the sole possible equality assignment, regardless of which optional edges exist. These weights are strictly positive on all prescribed spokes and on the bridge for \(p,q\ge2\), and their sum is
\[
\lambda\left[(p-1)\frac{3q}{N}+(q-1)\frac{3p}{N}+\frac{3pq}{N}-1\right]
=\lambda V_{p,q}=B.
\]

**Exact eigenvalue check.** Scale by \(\lambda\) and abbreviate
\[
a=\frac{3q}{N},\qquad b=\frac{3p}{N},\qquad c=\frac{3pq}{N}-1.
\]
The \(p-2\)-dimensional subspace of first-side nonhub vectors having coordinate sum zero is an eigenspace with eigenvalue \(a\lambda\); similarly the \(q-2\)-dimensional second-side subspace has eigenvalue \(b\lambda\). An eigenspace with dimension zero is simply absent. The remaining invariant four-dimensional space consists of vectors constant separately on the four classes (first nonhubs, \(u\), \(v\), second nonhubs). In that ordered basis, \(L/\lambda\) acts as
\[
Q=\begin{pmatrix}
a&-a&0&0\\
-(p-1)a&(p-1)a+c&-c&0\\
0&-c&(q-1)b+c&-(q-1)b\\
0&0&-b&b
\end{pmatrix}.
\]
A direct determinant calculation yields the *exact polynomial identity*
\[
\det(tI-Q)=t(t-1)\left(t-\frac{3pq}{N}\right)
\left(t-\frac{9pq}{N}+3\right).
\]
The last two positive roots are strictly larger than \(1\) for every \(p,q\ge2\). Therefore the proposed weight assignment has \(\lambda_2=\lambda\) exactly when its existing transverse eigenvalues satisfy \(a\ge1\) and \(b\ge1\), equivalently \(p\le2q\) and \(q\le2p\). For side size \(2\), the corresponding transverse eigenspace is absent; its omitted inequality is automatically satisfied by the other side's size being at least \(2\). This establishes attainment throughout the closed factor-two range, including both equality boundaries.

**Strictness outside the range.** A maximizer exists because the nonnegative budget simplex is compact and eigenvalues depend continuously on weights. If it attained \(B/V_{p,q}\), the preceding equality argument would force exactly the displayed assignment. Outside the factor-two range an existing transverse mode has eigenvalue strictly below \(\lambda\), contradicting equality. Thus the optimum is strictly below the bound. The forced-rate argument simultaneously proves global uniqueness in the attainable range, including against asymmetric assignments.

## Verification

`verify.py` uses only the Python standard library and exact rational arithmetic. It constructs the four-class quotient, computes its determinant by the permutation formula, checks the proposed characteristic polynomial, the total budget identity, the centered Rayleigh norm, the full-vector eigenvalue equation, and the factor-two criterion for each of the \(529\) pairs \(2\le p,q\le24\). It printed `EXACT_CHECKS_OK` when run. This is a finite diagnostic; the proof above establishes the asserted infinite quantifiers by algebra and the Rayleigh principle. Run `python verify.py` in the directory containing the file.

## Relationship to prior work

The semidefinite formulation and the dual variational viewpoint for optimizing the second Laplacian eigenvalue under a linear edge-rate budget are known from Sun, Boyd, Xiao, and Diaconis (2006). Fiedler (1990) and Richter–Rocha (2015/2016) study absolute algebraic connectivity of trees, including double-broom families, which covers the tree topology but does not in itself assert optimal deletion of the extra allowed conductances in every bridged-cone supergraph. Boyd, Diaconis, Parrilo, and Xiao (2007) study a barbell under the different *discrete-time* second-largest-eigenvalue-modulus objective; the available self-loop and negative-eigenvalue constraints distinguish that optimization. Jafarizadeh (2020, section 6.3) additionally analyzes extended barbells with prescribed stationary probabilities under the *discrete-time reversible SLEM* objective; it does not impose this continuous-time total-conductance budget. Ghosh, Boyd, and Saberi (2006, section V) solve *total effective resistance* minimization on a bridged pair of cliques and find positive internal-clique rates; their objective is not \(\lambda_2\)-maximization. The present contribution is the sharp dimension-ratio criterion, the equality and strictness statement for an arbitrary allowed within-side graph, and uniqueness without symmetry of competing weights.

## Limitations

Only nonnegative real conductances and one bridge are treated. The optimal budgeted gap outside the factor-two range is not evaluated. Changes to edge costs, extra bridges, caps on individual rates, positivity constraints that exclude zero weights, or discrete-time stochastic normalization are not covered. A bibliographic search cannot establish uniqueness relative to unindexed literature; in particular the full texts of some earlier tree-optimization treatments were not completely accessible in machine-readable form.

## References

- A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS proceedings, Kyoto, 24–28 July 2006, section V. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
- J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI:10.1137/S0036144504443821. https://stanford.edu/~boyd/papers/pdf/fmmp.pdf
- S. Boyd, P. Diaconis, P. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (first posted 6 September 2007), sections 4.3.1 and 5.3.4. https://arxiv.org/abs/0709.0955
- S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6 (2020), 88–104, DOI:10.1109/TSIPN.2020.2964211. Author-readable version https://www.researchgate.net/publication/387767555_Fastest_Mixing_Reversible_Markov_Chain_Clique_Lifted_Graphs_and_Subgraphs
- M. Fiedler, *Absolute Algebraic Connectivity of Trees*, Linear and Multilinear Algebra 26 (1990), 85–106, DOI:10.1080/03081089008817967.
- S. Richter and I. Rocha, *Absolute Algebraic Connectivity of Double Brooms and Trees*, Discrete Applied Mathematics 201 (2016), 213–221, DOI:10.1016/j.dam.2015.08.009, publicly posted as an author manuscript in August 2015.
