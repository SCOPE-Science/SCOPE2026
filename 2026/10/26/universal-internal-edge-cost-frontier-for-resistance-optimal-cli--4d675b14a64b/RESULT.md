# Universal internal-edge cost frontier for resistance-optimal clique bouquets

## Finding

Consider the clique bouquet \(G=K_1\vee(K_{s_1}\sqcup\cdots\sqcup K_{s_t})\), with \(t\ge2\), positive integers \(s_i\), and \(N=1+\sum_i s_i\). Each edge from the common hub to a vertex in petal \(i\) costs \(c_i>0\) per unit conductance; each edge between two non-hub vertices in that petal costs \(d_i>0\) per unit conductance, when \(s_i\ge2\). Under an arbitrary positive budget \(B\), minimize the sum of pairwise effective resistances over **all nonnegative edge conductance allocations whose positive-edge subgraph is connected**.

**Theorem.** There is a unique global minimizing allocation, invariant under permutations of vertices within each petal. For every petal containing at least two vertices, its internal edges have **strictly positive** optimal conductance exactly when
\[
\frac{d_i}{c_i}<\frac{2N}{N-1}.
\]
At equality, as above it, all its internal edges optimally receive zero conductance. This exact edge-sparsification threshold is independent of the petal size \(s_i\) at fixed \(N\).

Here is the full closed-form optimizer. Define the active set \(I=\{i:s_i\ge2,\ (N-1)d_i<2Nc_i\}\). For \(i\in I\), set
\[
\alpha_i=s_ic_i-\frac{s_i-1}{2}d_i>0,\quad
\beta_i=\frac{s_i-1}{2}d_i>0,\quad
S_i=\sqrt{(N-s_i)\alpha_i}+\sqrt{N(s_i-1)\beta_i}.
\]
For \(i\notin I\), including singleton petals, put \(S_i=s_i\sqrt{(N-1)c_i}\). Let \(S=\sum_i S_i\). Then every hub-to-petal edge in petal \(i\) has conductance
\[
a_i=\begin{cases}
\displaystyle\frac{B}{S}\sqrt{\frac{N-s_i}{\alpha_i}},&i\in I,\\[4pt]
\displaystyle\frac{B}{S}\sqrt{\frac{N-1}{c_i}},&i\notin I,
\end{cases}
\]
and every within-petal edge in a nonsingleton petal has conductance
\[
b_i=\begin{cases}
\displaystyle\frac{B}{s_iS}\left(\sqrt{\frac{2N}{d_i}}-\sqrt{\frac{N-s_i}{\alpha_i}}\right),&i\in I,\\[4pt]
0,&i\notin I.
\end{cases}
\]
The minimum Kirchhoff index is
\[
\boxed{\operatorname{Kf}_{\min}(G)=\frac{S^2}{B}.}
\]
When all within-petal costs \(d_i\) agree on the active petals, all active local leaf-difference Laplacian eigenvalues \(a_i+s_ib_i\) are identical, despite differing petal sizes.

## Assumptions and scope

A petal is a clique on its \(s_i\) non-hub vertices, together with all its edges to a single common hub. There are no edges between different petals away from the hub. All design costs \(c_i\), and \(d_i\) when defined, and total budget \(B\) are fixed strictly positive real numbers. The design variables are nonnegative conductances assigned to individual existing edges, subject to the exact cost equation \(\sum_e\operatorname{cost}(e)w_e=B\). Allocations disconnecting the graph have infinite objective and are not admissible. Zero weights on a proper subset of edges are permitted. The Kirchhoff index is \(\operatorname{Kf}(G,w)=\sum_{u<v}R_{uv}(w)\), with undirected unit-current effective resistance \(R_{uv}\). The theorem includes mixed active and inactive petals and exact threshold equality; it does not claim the same threshold for arbitrary graphs or costs varying within a petal edge class.

## Proof

**1. Unrestricted global optimum is symmetric and unique.** For a connected weighted graph write its Laplacian as \(L(w)\) and its all-ones matrix as \(J\). Since \(L(w)+J/N\) is positive definite,
\[
\operatorname{Kf}(G,w)=N\bigl(\operatorname{tr}(L(w)+J/N)^{-1}-1\bigr).
\]
The map \(X\mapsto\operatorname{tr}(X^{-1})\) is strictly convex on positive definite symmetric matrices: in any nonzero symmetric direction \(H\), its second derivative is \(2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0\). Distinct edge conductance vectors give distinct graph Laplacians, because their off-diagonal entries encode every edge weight. Hence the objective is strictly convex on the connected domain. A minimizer exists: the cost simplex is compact and the objective diverges if connectivity is lost, as a nonzero Laplacian eigenvalue tends to zero. Strict convexity makes it unique. Its uniqueness and invariance under petal-wise vertex permutations force a common spoke weight \(a_i>0\) and a common internal weight \(b_i\ge0\) in each petal.

**2. Exact effective resistances.** Ground the common hub. The grounded Laplacian is block diagonal, and the block for petal \(i\) is
\[
M_i=(a_i+s_ib_i)I_{s_i}-b_iJ_{s_i}.
\]
Putting \(y_i=a_i+s_ib_i\), its inverse is
\[
M_i^{-1}=\frac1{y_i}\left(I_{s_i}-\frac1{s_i}J_{s_i}\right)+\frac1{a_i s_i}J_{s_i}.
\]
Thus two distinct leaves in the same petal have resistance \(2/y_i\); a leaf in that petal and the hub have resistance
\[
R_i=\frac{s_i-1}{s_i y_i}+\frac1{s_i a_i}.
\]
Two leaves in different petals have resistance \(R_i+R_j\), by block diagonality of the grounded inverse. Summing within-petal, hub-to-leaf and between-petal unordered pairs gives exactly
\[
\boxed{\operatorname{Kf}(G,w)=\sum_i\left(\frac{N(s_i-1)}{a_i+s_ib_i}+\frac{N-s_i}{a_i}\right).}
\]
This formula remains valid when some \(b_i=0\), and for singleton petals.

**3. A separable constrained program.** For \(s_i\ge2\), substitute \(x_i=a_i>0\), \(y_i=a_i+s_ib_i\ge x_i\). The objective contribution becomes \(C_i/x_i+A_i/y_i\), with \(C_i=N-s_i\) and \(A_i=N(s_i-1)\). The budget contribution becomes \(\alpha_i x_i+\beta_i y_i\), where \(\alpha_i=s_ic_i-(s_i-1)d_i/2\) and \(\beta_i=(s_i-1)d_i/2\). Note that \(\alpha_i\) may be negative for high internal-edge costs; it is not assumed positive before classifying the optimum. For \(s_i=1\), the contribution is \((N-1)/x_i\) with budget cost \(c_i x_i\).

Introduce a positive Lagrange multiplier \(\lambda\) for the exact budget. Minimizing a nonsingleton petal contribution plus its multiplier cost over the convex cone \(0<x_i\le y_i\) has two possible regimes. In the interior \(y_i>x_i\), stationarity requires
\[
x_i=\lambda^{-1/2}\sqrt{\frac{C_i}{\alpha_i}},\qquad
y_i=\lambda^{-1/2}\sqrt{\frac{A_i}{\beta_i}}=\lambda^{-1/2}\sqrt{\frac{2N}{d_i}}.
\]
This interior point is feasible precisely when \(A_i\alpha_i>C_i\beta_i\), which simplifies without approximation to \((N-1)d_i<2Nc_i\). This inequality also implies \(\alpha_i>0\).

Otherwise the minimizer lies on \(y_i=x_i\), hence \(b_i=0\), and direct one-variable minimization gives
\[
x_i=y_i=\lambda^{-1/2}\sqrt{\frac{N-1}{c_i}}.
\]
To verify the boundary case without any positivity assumption on \(\alpha_i\), write \(y_i=x_i+t\) with \(t\ge0\). At the displayed boundary solution, the derivative into the allowed \(t\)-direction is
\[
\lambda(s_i-1)\left(\frac{d_i}{2}-\frac{Nc_i}{N-1}\right)\ge0
\]
exactly in the claimed inactive regime. Strict convexity of the local objective proves these stationary or boundary solutions are globally optimal for each petal. A singleton obeys the same boundary formula.

**4. Exact normalization and sharpness.** Each optimal variable is a positive constant times \(\lambda^{-1/2}\). Substituting the solutions into their weighted budget contributions gives \(B=\lambda^{-1/2}\sum_i S_i\), hence \(\lambda^{-1/2}=B/S\). Substitution yields precisely the stated allocations. At the optimum the multiplier stationarity identity or the equality case of the Cauchy–Schwarz inequality gives \(\operatorname{Kf}_{\min}=S^2/B\). The strict local inequalities show \(b_i>0\) below the threshold and \(b_i=0\) on and above it; there are no unlisted optimizer branches. Global uniqueness was established in step 1.

## Verification

Running `python3 verify.py` in a Python 3 environment with the standard library checks eight distinct clique bouquets, 170 pairwise resistances by exact rational inversion of independently constructed grounded Laplacians, eight weighted-cost regimes (including equality and both sides of the threshold), 256 feasible full-matrix perturbations, and an exact radical benchmark. The program reports:

`VERIFY_OK: 8 exact grounded-matrix cases (170 pair resistances); 8 weighted-cost regimes; 256 full-matrix perturbations; bow-tie radical optimum; sharp mixed-cost threshold`

For two triangular petals with all per-edge costs equal to one and unit budget, the exact minimum is \(28+12\sqrt5\), versus \(56\) under uniform conductances. For petal sizes \((1,2,4)\), the universal threshold is \(16/7\): making the two-vertex petal's internal edge three times as expensive as its hub spokes suppresses that internal edge, while inexpensive internal edges in the size-four petal remain active. Exact finite tests independently check the matrix formulas but are not an exhaustive proof of the theorem.

## Relationship to prior work

Ghosh, Boyd and Saberi established the global effective-resistance conductance-allocation convex program, uniqueness and automorphism reductions, solving trees, wheels and a barbell example. Their published treatment does not state the heterogeneous common-hub clique bouquet optimizer, individual internal-edge cost activation condition, or the universal threshold independent of the petal size. These general convex methods motivate, but do not themselves supply, the present explicit phase classification. Haritha and Chithra computed resistances for unit-weight coalescences and windmill graphs; their reported formulas do not optimize positive and zero edge conductances under heterogeneous linear costs. The presently derived block-inverse formula extends the fixed-weight resistance calculation to that design problem. No claim is made that a negative literature search certifies uniqueness of publication.

## Limitations

The network must be a one-hub union of cliques, costs must be constant on each petal's spoke class and internal class, and the budget must be linear. This is a finite-graph algebraic theorem, not a guarantee of physical applicability when edge deletion is prohibited or additional conductance bounds apply. Only the Kirchhoff-index objective is optimized, not the spectral gap or worst-pair resistance. Independent external validation and a complete survey of unindexed literature have not been performed.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, DOI: 10.1137/050645452, full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf. A shorter proceedings version appeared at MTNS in July 2006; the source inspected with exact publication-day evidence was posted online on 2008-02-01.
2. T. Haritha and A. V. Chithra, *Resistance distance in k-coalescence of certain graphs*, arXiv:2309.02704, first version 2023-09-06, https://arxiv.org/pdf/2309.02704.
