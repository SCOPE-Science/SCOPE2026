# A square-root lifting law for optimal diffusion on vertex-transitive pendant networks

## Finding

Let \(H=(V,E)\) be a finite, connected, simple vertex-transitive graph with \(N=|V|\ge3\). Assign each base edge \(e\in E\) a fixed positive *cost coefficient* \(c_e\), constant on every automorphism orbit of \(H\). For a vector \(w\ge0\) of undirected base-edge conductances, write \(L_H(w)\) for the weighted combinatorial Laplacian and define the positive base design constant

\[
\beta(H,c)=\max\left\{\lambda_2(L_H(w)):\ w_e\ge0,\ \sum_{e\in E}c_e w_e\le1\right\}>0.
\]

Fix any integer \(q\ge1\), a leaf cost \(d>0\), and a total budget \(B>0\). Attach \(q\) distinct private leaves to every core vertex of \(H\). Allow arbitrary nonnegative conductances on *all* available edges, not necessarily symmetric, with cost \(\sum_{e\in E}c_e w_e+d\sum_{v,k}y_{v,k}\le B\). Then the exact maximum spectral gap of the resulting weighted Laplacian is

\[
\boxed{\Lambda_q(B)=\frac{B}{(q+1)/\beta+Nqd+2q\sqrt{Nd/\beta}}.}
\]

Let \(r=\Lambda_q(B)\). An optimal allocation is obtained by putting the same conductance on every private leaf edge,

\[
\boxed{y_*=r\left(1+\frac1{\sqrt{\beta Nd}}\right),}
\]

and choosing on the core any base-optimal, unit-cost vector \(w^{(0)}\) realizing \(\lambda_2(L_H(w^{(0)}))=\beta\), scaled by

\[
\boxed{W_*=\frac{r}{\beta}\left(q+1+q\sqrt{\beta Nd}\right).}
\]

Thus \(w_e=W_*w^{(0)}_e\) and the base conductance cost is exactly \(W_*\). Every optimal allocation with uniform private-leaf conductances uses the displayed \(y_*\), spends exactly \(W_*\) on the core, and is base-optimal there. No uniqueness of unrestricted, asymmetric optimizers is asserted.

This is a *lifting law*: for a vertex-transitive base with orbit-invariant edge costs, all cost-optimal spectral-gap information needed to solve the pendant-decorated problem is captured by the single base constant \(\beta\). The new edges are not forced to have equal conductance in the feasible class; equality emerges for a globally optimal representative.

## Assumptions and scope

All graphs are finite, simple, and undirected; all cost coefficients are strictly positive and the conductance decisions are nonnegative. The base graph is connected, vertex-transitive, and has at least three vertices. The automorphism-invariance of the base cost coefficients is essential for the symmetrization step. Each of the \(q\) leaves is adjacent only to its own core vertex and has the common cost coefficient \(d\). No vertex-stationary probabilities, normalization by weighted degree, or stochastic holding constraints are imposed: the objective is the second eigenvalue of the *combinatorial* weighted Laplacian, for continuous-time diffusion.

The base optimum \(\beta\) is strictly positive: a small strictly positive assignment on all edges gives a connected positive-conductance base. It is attained by compactness of the unit-cost feasible polytope. The same degree of generality includes vertex-transitive, non-edge-transitive cores whose base optimal edge conductances genuinely differ between edge orbits.

## Proof

**1. A symmetric optimum exists without constraining the competing designs.** For every weighted graph the variational formula

\[
\lambda_2(L)=\min_{z\perp\mathbf1,\ \|z\|=1}\sum_{\{i,j\}}w_{ij}(z_i-z_j)^2
\]

shows that \(\lambda_2\) is concave in the conductances. Average an arbitrary feasible pendant-network assignment over the finite automorphism group of the base and the independent permutations of the \(q\) leaves at each vertex. Because the base cost coefficients are orbit-invariant, this averaging preserves cost and cannot decrease the spectral gap. Vertex transitivity makes the leaf conductances all equal, say \(y\). The core conductances may still differ across distinct base-edge orbits. It therefore suffices to solve the problem among uniform-leaf assignments.

**2. Exact spectral decomposition.** For a uniform leaf conductance \(y>0\), let \(a\) be any eigenvalue of the weighted core Laplacian. On the normalized core/leaf-sum subspace corresponding to its eigenvector, the augmented Laplacian acts as

\[
A(a,y)=\begin{pmatrix}a+qy&-\sqrt q\,y\\-\sqrt q\,y&y\end{pmatrix}.
\]

Its two eigenvalues are the roots of

\[
z^2-(a+(q+1)y)z+ay=0.
\]

The remaining leaf-difference modes, if \(q\ge2\), have eigenvalue \(y\). The base eigenvalue \(a=0\) produces \(0\) and \((q+1)y\). For each \(a>0\), the lower root \(\phi(a,y)\) lies strictly between \(0\) and \(y\): the characteristic polynomial is positive at \(0\) and equals \(-qy^2\) at \(y\). The lower root increases strictly with \(a\), by the Rayleigh variational formula for \(A(a,y)\) and its nonzero core component. Consequently, for any connected positive-conductance core,

\[
\lambda_2(L_{\mathrm{aug}})=\phi\bigl(\lambda_2(L_H(w)),y\bigr).
\]

If the core has gap zero or the leaves have zero conductance, the augmented gap is zero, so these boundary choices cannot optimize a positive budget.

**3. Replace the core design by its sharp cost-gap constant.** If the base budget is \(W=\sum c_e w_e\), the definition and homogeneity of \(\beta\) give \(\lambda_2(L_H(w))\le\beta W\). Conversely, scaling any unit-cost base optimizer achieves equality for every \(W\ge0\). Since \(\phi\) is increasing in its first argument, the augmented optimum at any fixed \((W,y)\) is obtained by such a scaled base optimizer.

**4. Optimize the split exactly.** Seek an augmented spectral gap of at least \(r>0\). The smaller eigenvalue of \(A(a,y)\) is at least \(r\) exactly when \(y>r\) and, by the Schur complement of \(A(a,y)-rI\),

\[
a\ge r\left(q+1+\frac{qr}{y-r}\right).
\]

Thus the minimum core expenditure is \(r\beta^{-1}(q+1+qr/(y-r))\). Writing \(u=y/r>1\), the total expenditure is at least

\[
r\left[\frac{q+1}{\beta}+\frac{q}{\beta(u-1)}+Nqd\,u\right].
\]

The bracket is strictly convex on \(u>1\) because its second derivative equals \(2q/[\beta(u-1)^3]>0\), tends to infinity at both endpoints, and has its unique minimum at

\[
u_*=1+\frac1{\sqrt{\beta Nd}}.
\]

Its minimum is \((q+1)/\beta+Nqd+2q\sqrt{Nd/\beta}\). Hence every feasible gap satisfies the claimed upper bound. The displayed uniform leaf rate and scaled base optimizer attain equality throughout the Schur, base-cost, and budget bounds. The strict convexity also proves the stated uniqueness of the scalar budget split among uniform-leaf optimizers.

**5. Two concrete infinite families.** For the cycle base \(H=C_s\), \(s\ge3\), with unit base-edge cost, \(\beta=4\sin^2(\pi/s)/s\). Thus the exact optimum for \(q\) leaves per cycle vertex is

\[
\Lambda_q(B)=\frac{B}{s\bigl[(q+1)/(4\sin^2(\pi/s))+qd+2q\sqrt{d}/(2\sin(\pi/s))\bigr]}.
\]

For the prism base \(H=C_s\square K_2\), \(s\ge5\), give the \(2s\) cycle-direction edges cost \(c_1>0\) and the \(s\) rung edges cost \(c_2>0\). This cost assignment is invariant under the base automorphism group, although the two edge classes have different costs. Let \(\alpha=4\sin^2(\pi/s)\). Averaging and the Cartesian-product spectrum give

\[
\beta^{-1}=\frac{2s c_1}{\alpha}+\frac{s c_2}{2}.
\]

Indeed, if core conductances on these two classes are \(a,b\), its gap is \(\min\{\alpha a,2b\}\); the least cost for unit gap is the right-hand side. Substituting this \(\beta\) gives an explicit radical optimum for an infinite family with two noninterchangeable base-edge orbits. These examples are consequences of the one lifting statement, not separate claimed findings.

## Verification

The accompanying `verify.py` checks the characteristic-polynomial and budget identities with exact symbolic algebra, and checks the strict-convexity stationary point. It assembles weighted Laplacians and compares their complete numerical spectra with the formula over 72 vertex/edge-transitive parameter combinations; it also compares 810 independently sampled asymmetric allocations, and verifies 18 two-edge-orbit prism cases. The numerical checks are finite stress tests, not a proof of optimality; the full quantified theorem follows from the concavity, spectral decomposition, sharp base-cost inequality, and scalar convex minimization above.

Run `python verify.py` with Python 3 and the documented dependencies `numpy`, `networkx`, and `sympy`.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006) formulate continuous-time fastest-mixing as a weighted-Laplacian semidefinite optimization, and establish concavity and the geometry of the dual problem. They solve basic examples including cycles; their paper does not give the above vertex-transitive, arbitrary-leaf-multiplicity lifting law. Barik, Pati, and Sarma (2007) develop the Laplacian spectrum of *unweighted* corona graphs, which motivates the block spectral decomposition here, but no conductance-budget optimization or cost-class square-root identity is derived there. Boyd, Diaconis, Parrilo, and Xiao (2009) give symmetry reduction for the **discrete-time** second-eigenvalue-modulus problem; that objective and its stochastic constraints differ from the present continuous-time spectral-gap budget. In particular, the symmetry reduction and spectrum formula separately do not specify the optimal cost split, which is determined here by the strict scalar minimization. No identical closed-form lifting theorem was located in the searches described in the scientific review; this does not establish global uniqueness in the literature.

## Limitations

Vertex transitivity and automorphism-invariant base costs are hypotheses, not cosmetic restrictions. For a general asymmetric base the private-leaf conductances cannot simply be averaged to a uniform rate, and the asserted formula is not proved. The theorem does not claim all globally optimal allocations are symmetric, nor solve the base constant \(\beta\) for an arbitrary vertex-transitive graph; it gives an exact transfer of that base constant to every integer leaf multiplicity and all positive leaf-cost coefficients. It concerns the continuous-time combinatorial Laplacian and does not assert an optimum for discrete-time fastest mixing or normalized Laplacians. Numerical tests sample finitely many graph families and weight choices.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* **48** (2006), 681–699, DOI: 10.1137/S0036144504443821. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf . First published electronically November 2, 2006.
2. S. Barik, S. Pati, and B. K. Sarma, “The Spectrum of the Corona of Two Graphs,” *SIAM Journal on Discrete Mathematics* **21** (2007), 47–56, DOI: 10.1137/050624029. Author-shared full text: https://www.researchgate.net/publication/220533743_The_Spectrum_of_the_Corona_of_Two_Graphs .
3. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” *SIAM Journal on Optimization* **20** (2009), 792–819, DOI: 10.1137/070689413. Full text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf .
