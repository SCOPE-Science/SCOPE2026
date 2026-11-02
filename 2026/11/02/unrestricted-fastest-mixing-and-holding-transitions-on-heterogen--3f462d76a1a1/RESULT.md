# Unrestricted fastest mixing and holding transitions on heterogeneous clique products

## Finding

For an integer \(d\ge3\) and integers \(n_1,\ldots,n_d\ge2\), not all equal, let \(G=K_{n_1}\square\cdots\square K_{n_d}\). Put
\[
C=\sum_{i=1}^{d}\left(1-\frac1{n_i}\right),\qquad
u=\min\left\{\frac2{d+1},\frac1C\right\}.
\]
Among **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices supported on edges and self-loops of \(G\), there is **exactly one** minimizing the second-largest eigenvalue modulus. It is
\[
P^*_{xy}=\begin{cases}
u/n_i,&x\ne y\text{ and they differ only in coordinate }i,\\
1-Cu,&x=y,\\
0,&\text{otherwise}.
\end{cases}
\]
The exact minimum is
\[
\boxed{\mu_* = 1-u = \max\left\{\frac{d-1}{d+1},\,1-\frac1C\right\}.}
\]
The unique optimizer holds with positive probability exactly when \(\sum_i1/n_i>(d-1)/2\). At equality or below, its holding probability is zero. For three coordinate factors, the complete list of unordered critical triples satisfying \(\sum_i1/n_i=1\) is \((2,3,6),(2,4,4),(3,3,3)\); the first two are heterogeneous.

## Assumptions and scope

The vertex set is the Cartesian product of finite coordinate alphabets of sizes \(n_i\); two distinct vertices are adjacent if and only if precisely one coordinate changes. No symmetry, equal-weight condition, positive edge lower bound, or fixed holding probability is imposed on the candidate chain. Holding probabilities are allowed and nonnegative. For each feasible \(P\), define \(N=\prod_i n_i\) and
\[
\mu(P)=\left\|P-\frac1N\mathbf1\mathbf1^{\mathsf T}\right\|_2.
\]
This is the nonconstant-mode second-largest eigenvalue modulus, including the value one if the chain is reducible. We optimize this one-step spectral contraction, not time-inhomogeneous, nonreversible, prescribed-stationary or total-variation cutoff criteria. Equal alphabet sizes are excluded from the new domain because their optimal SLEM and an invariant optimal chain were previously published; their equality cases are used only to state the elementary critical-triple arithmetic completely.

## Proof

**1. Existence of an invariant optimum.** The feasible set is compact and convex, and \(\mu(P)\) is the operator norm of an affine function, hence convex. Averaging any feasible \(P\) under the coordinatewise permutation group \(\prod_iS_{n_i}\) preserves the graph, stochasticity and feasibility without increasing \(\mu\). Every averaged chain has one edge probability \(a_i\ge0\) in direction \(i\), and a common holding probability \(1-\sum_i(n_i-1)a_i\ge0\).

**2. Spectrum and minimax optimum.** Set \(z_i=n_i a_i\) and \(c_i=(n_i-1)/n_i\). The invariant chain is \(I-\sum_i a_iL_{K_{n_i}}^{(i)}\), and the commuting coordinate Laplacians have eigenvalues zero or \(n_i\). Every nonconstant eigenspace is indexed by a nonempty set \(S\subseteq\{1,\ldots,d\}\), with eigenvalue \(1-\sum_{i\in S}z_i\) and multiplicity \(\prod_{i\in S}(n_i-1)\). Consequently
\[
\mu=\max\left\{1-\min_i z_i,\ \sum_i z_i-1\right\},
\qquad \sum_i c_i z_i\le1.
\]
If the SLEM is at most \(t\), then \(z_i\ge1-t\) for every \(i\), while \(\sum_i z_i\le1+t\) and \(\sum_i c_i z_i\le1\). Summation gives the independent lower bounds
\[
t\ge\frac{d-1}{d+1},\qquad t\ge1-\frac1C.
\]
Choosing \(z_i=u\) for all \(i\) meets both spectral and budget inequalities at the larger bound, giving the displayed optimum. It is the *only invariant optimum*: on the first bound, \(z_i\ge2/(d+1)\) and \(\sum_i z_i\le2d/(d+1)\), so every \(z_i\) is fixed. On the second bound, \(z_i\ge1/C\) and \(\sum_i c_i z_i\le1\), with every \(c_i>0\), again fixing all coordinates. Both arguments work at their equality boundary.

**3. Rigidity without a symmetry assumption.** Let \(P\) be any unrestricted global optimum and \(\overline P\) its average under the same coordinatewise group. By step 2, \(\overline P=P^*\). For each direction \(i\), define \(U_i\) to be the \((n_i-1)\)-dimensional space of functions depending only on coordinate \(i\) and having mean zero there. Each \(U_i\subset\mathbf1^\perp\), and \(P^*v=(1-u)v=\mu_*v\) for every \(v\in U_i\). Let \(Q_g\) denote the permutation matrix of a group element. Since every \(Q_gPQ_g^{\mathsf T}\) is itself optimal, for \(v\in U_i\),
\[
\langle v,Q_gPQ_g^{\mathsf T}v\rangle\le \mu_*\|v\|^2.
\]
Averaging these inequalities yields equality, because \(\overline P v=\mu_*v\). Thus equality holds for every \(g\), including the identity. As \(\mu_*I-P\) is positive semidefinite on \(\mathbf1^\perp\), equality forces \(Pv=\mu_*v\) for every \(v\in U_i\).

Fix any direction \(i\) and freeze the other coordinate values. For functions in \(U_i\), transitions in all other directions contribute zero to \((I-P)v\). Hence the weighted Laplacian \(L_i\) of the complete-graph fiber acts as \(u I\) on its entire zero-sum subspace and kills constants. Therefore \(L_i=u(I-J_{n_i}/n_i)\), where \(J_{n_i}\) is the all-ones matrix. Comparing off-diagonal entries gives every edge probability in this fiber exactly \(u/n_i\). This holds for every fiber and direction. The row-sum condition then forces every diagonal to equal \(1-Cu\), proving \(P=P^*\). Thus the optimum is unique among *all*, not merely invariant, feasible chains.

**4. The holding and three-factor boundaries.** The common holding probability is \(h=1-Cu\); it is positive if and only if \(C<(d+1)/2\), equivalent to \(\sum_i1/n_i>(d-1)/2\). For \(d=3\), sort \(2\le a\le b\le c\). The equality \(1/a+1/b+1/c=1\) forces \(a\le3\). If \(a=3\), then \(b=c=3\). If \(a=2\), then \(1/b+1/c=1/2\) and \(b\in\{3,4\}\), giving \((2,3,6)\) and \((2,4,4)\). No other critical triples exist.

## Verification

The included standalone Python program `verify.py` performs exact-rational checks of holding/budget and critical triples, compares full numerical transition-matrix eigenvalues with the complete subset-indexed spectrum, independently solves finite-dimensional minimax linear programs, and checks randomly perturbed *unrestricted* feasible chains. A replay passed 362 assertion groups on 19 graphs. These finite computations reproduce examples and test formula implementation; the all-size result and unrestricted uniqueness depend on the preceding proof, not numerical enumeration.

## Relationship to prior work

Boyd, Diaconis and Xiao introduced the symmetric fastest-mixing semidefinite program [1]. Boyd, Diaconis, Parrilo and Xiao [2] developed symmetry averaging and Cartesian-product Laplacian spectra (Section 3.2), and derived exact fastest-mixing weights for ordinary equal-alphabet Hamming graphs (Section 3.3.3). Their stated equal-factor formula is a specialization of the spectrum calculation here, not a new result. The heterogeneous alphabets break edge transitivity and require separately optimized coordinate orbits. The present theorem supplies both the exact arbitrary-alphabet boundary and the stronger pointwise **uniqueness of the unrestricted optimum**; neither assertion was found in the inspected sections of [1] or [2]. Prior work on one transitive base times one clique establishes related two-factor optimal values, but does not assert unrestricted uniqueness or solve products with several distinct coordinate alphabets. A more recent association-scheme formulation [3] supplies generic symmetry/LP machinery and illustrates ordinary Hamming schemes; its available excerpts did not settle the present heterogeneous full rigidity statement.

## Limitations

This is a spectral-radius optimization for **symmetric** stochastic matrices on Cartesian products of complete graphs; it says nothing about arbitrary stationary distributions, nonreversible chains, fixed diagonal values, or exact finite-time total-variation mixing. The theorem makes no priority claim for equal-factor Hamming spectral formulas or for the standard symmetry-reduction method. Full independent scrutiny and a specialized literature search may uncover broader prior results. The recent association-scheme study [3] was accessible in partial full-text excerpts but was not exhaustively inspected; its possible generality is a residual originality risk.

## References

[1] S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: https://doi.org/10.1137/S0036144503423264 ; author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.

[2] S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (first public arXiv posting 2007-09-06), later SIAM Journal on Optimization 20 (2009), 792–819; https://arxiv.org/pdf/0709.0955.

[3] S. Jafarizadeh, *Pareto–Optimal Design of Markov Chains on Networks Based on Association Schemes*, IEEE Access 14 (2026), DOI: https://doi.org/10.1109/ACCESS.2026.3680803.
