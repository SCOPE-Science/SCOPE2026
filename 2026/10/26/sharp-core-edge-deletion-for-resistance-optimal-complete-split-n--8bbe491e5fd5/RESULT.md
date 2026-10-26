# Sharp core-edge deletion for resistance-optimal complete split networks

## Finding

Let \(r\ge2\) and \(s\ge1\) be integers. Take the *complete split graph* \(G=K_r\vee\overline{K_s}\): its \(r\) core vertices form a complete graph; its \(s\) peripheral vertices are pairwise nonadjacent; and every core vertex is adjacent to every peripheral vertex. A conductance budget \(B>0\) may be split in any nonnegative amounts over all existing edges. The objective is the sum of effective resistances over all unordered vertex pairs (the Kirchhoff index).

**Theorem (complete optimum and its sharp support transition).** Write
\[
n=r+s,\qquad H=\sqrt{\frac{nr(r+1)}{n-1}},\qquad
 t_*=\max\left\{0,\frac{H-s}{r}\right\},
\]
\[
b_*=\frac{B}{rs+\binom r2t_*},\qquad a_*=t_*b_*.
\]
There is a **unique** global optimal conductance allocation, even among arbitrary asymmetric edge assignments. It sets every core-to-periphery edge to the same weight \(b_*\), and every core-clique edge to the same weight \(a_*\). Every cross-edge weight is strictly positive.

The exact support law is
\[
 a_*>0\quad\Longleftrightarrow\quad1\le s\le r,
 \qquad
 a_*=0\quad\Longleftrightarrow\quad s\ge r+1.
\]
Thus, once the independent peripheral set outnumbers the clique core, **all clique edges are uniquely optimal at zero conductance**, although those edges belong to the original graph.

The minimum Kirchhoff index is exactly
\[
\mathcal K_{\min}=\begin{cases}
\dfrac{\left((r-1)\sqrt{r+s}+s\sqrt{\frac{(r+s-1)(r+1)}{r}}\right)^2}{2B},&1\le s\le r,\\[6pt]
\dfrac{r(r+s)(r-1)+s^2(r+s-1)}{B},&s\ge r+1.
\end{cases}
\]
The formulas include \(s=1\), when the graph is complete and the optimum has equal conductances on all its edges. No boundary case with \(a_*=0\) and \(H=s\) occurs for the permitted integer parameters.

## Assumptions and scope

Edges are undirected, simple, and prescribed exactly by \(K_r\vee\overline{K_s}\). Each available edge \(e\) receives an individual conductance \(w_e\ge0\), with \(\sum_e w_e=B>0\). The weighted graph must remain connected; for definiteness set the objective equal to \(+\infty\) when its positive-weight support is disconnected. The conclusions concern global allocation of a *fixed total conductance* at uniform per-unit costs; they do not assert optimality under fixed edge weights, heterogeneous installation costs, or extra lower bounds on each \(w_e\).

For a connected weighted graph, let \(L\) denote its combinatorial conductance Laplacian. For each distinct pair \(u,v\), the effective resistance is \(R_{uv}=(e_u-e_v)^\top L^+(e_u-e_v)\), where \(L^+\) is the Moore–Penrose pseudoinverse. Accordingly \(\mathcal K=\sum_{u<v}R_{uv}=n\operatorname{tr}(L^+)\).

## Proof

**1. Unrestricted global uniqueness and symmetry.** On the connected part of the conductance simplex, the matrix \(X(w)=L(w)+\mathbf1\mathbf1^\top/n\) is positive definite and
\[
\mathcal K(w)=n\big(\operatorname{tr}(X(w)^{-1})-1\big).
\]
For every nonzero symmetric perturbation \(Y\), the second directional derivative of \(\operatorname{tr}(X^{-1})\) is
\[
2\operatorname{tr}(X^{-1}YX^{-1}YX^{-1})>0.
\]
This follows by writing the trace as \(2\operatorname{tr}[(X^{-1/2}YX^{-1/2})^2X^{-1}]\). Different edge-weight vectors on this simple graph produce different Laplacians (an edge weight is the negative of the corresponding off-diagonal entry), so the objective is **strictly convex in all individual weights** wherever it is finite. The feasible set of connected allocations is convex; a minimizer exists because the budget simplex is compact and the objective diverges toward disconnected supports. Therefore the minimizer is unique. Every permutation of the core vertices and every permutation of the peripheral vertices preserves both objective and budget. By uniqueness the optimizer is invariant under these permutations. Thus a symmetric description with exactly two conductance classes is justified **after** proving global optimality, not assumed in the problem.

**2. Spectrum and exact objective.** Let \(a\ge0\) be the conductance on each of the \(\binom r2\) core-clique edges, and \(b>0\) the conductance on each of the \(rs\) cross edges. The Laplacian block matrix is
\[
L=\begin{pmatrix}
(ra+sb)I_r-aJ_r&-bJ_{r\times s}\\
-bJ_{s\times r}&rbI_s
\end{pmatrix}.
\]
The core zero-sum space has eigenvalue \(ra+sb\) with multiplicity \(r-1\); the peripheral zero-sum space has eigenvalue \(rb\) with multiplicity \(s-1\). The two-dimensional space constant on each part has eigenvalues \(0\) and \((r+s)b\). Hence
\[
\mathcal K(a,b)=
\frac{n(r-1)}{ra+sb}+\frac{s(n-1)}{rb},
\qquad
\binom r2 a+rsb=B.
\]
Both spectral factors and the budget normalization therefore refer to the **same** conductance allocation.

**3. Constrained reciprocal minimization.** Substitute \(x=ra+sb\). Then the budget and nonnegativity constraints become
\[
\frac{r-1}{2}x+\frac{s(r+1)}2 b=B,\qquad x\ge sb>0.
\]
The objective is \(A/x+D/b\), where \(A=n(r-1)\) and \(D=s(n-1)/r\). For positive \(x,b\), the Cauchy–Schwarz inequality gives
\[
\left(\frac{A}{x}+\frac{D}{b}\right)
\left(\frac{r-1}2x+\frac{s(r+1)}2b\right)
\ge\left(\sqrt{\frac{A(r-1)}2}+\sqrt{\frac{Ds(r+1)}2}\right)^2.
\]
Equality holds exactly when \(x/b=H=\sqrt{nr(r+1)/(n-1)}\). When \(H\ge s\), this equality point satisfies \(x\ge sb\); it gives \(a/b=(H-s)/r\). When \(H<s\), it violates the constraint, and strict convexity on the budget segment forces the unique constrained minimum to its boundary \(x=sb\), equivalently \(a=0\). Thus \(a/b=t_*\), and solving the budget yields \(a_*\) and \(b_*\) as stated.

The equality value of the displayed Cauchy–Schwarz bound, divided by \(B\), simplifies to the first branch of \(\mathcal K_{\min}\). On the boundary \(a=0\), the budget gives \(b=B/(rs)\); substituting into the spectral objective gives the second branch. No comparison of only finitely many candidate weights is required.

**4. Exact integer phase boundary.** The inequality \(H>s\) is equivalent to
\[
\frac{s^2(r+s-1)}{r+s}<r(r+1).
\]
For fixed \(r\ge2\), the left side is strictly increasing with real \(s>0\). Moreover,
\[
H^2-s^2\big|_{s=r}=\frac{3r^2}{2r-1}>0,
\qquad
H^2-s^2\big|_{s=r+1}=-\frac{r+1}{2}<0.
\]
Thus \(H>s\) for every integer \(1\le s\le r\), and \(H<s\) for every integer \(s\ge r+1\). In particular, the equality case is impossible for integers in the stated range. Global strict convexity from step 1 proves the asserted edge support for **every** optimal allocation, including all potentially asymmetric competitors.

## Verification

A standalone program, `verify_split.py`, reconstructs Laplacians from edge lists. Running `python verify_split.py` with Python 3, NumPy, and SymPy must print the `PASS` summary in `verification_output.txt`. It checks 176 symmetric optimized spectra and budgets, 1,760 alternative symmetric budget allocations, 1,056 asymmetric allocations, six symbolic characteristic polynomials, and five exact-rational pseudoinverse-trace identities. The program uses direct matrix inversions and eigenvalues for finite instances. These computations corroborate but **do not establish** the arbitrary-integer theorem; the proof above supplies the infinite-family argument.

## Relationship to prior work

Ghosh, Boyd, and Saberi formulate convex fixed-budget effective-resistance minimization, prove uniqueness, and exploit graph automorphisms; their inspected analytic examples include trees, wheels, and barbells. Those principles are used here, but the specific complete-split core/periphery support transition and closed-form budgeted optimizer are not stated among their examples. The original proceedings version was presented in a symposium dated July 24–28, 2006; the conservative date July 28 is used as the source-date bound, rather than the later journal date.

Yang's complete-split extremum is for the **unweighted** graph among graphs of fixed order and independence number, not for the selection of individual conductances under a budget. Sedlák and Slavík likewise compute resistance distances and Kirchhoff indices for graph joins, including complete split graphs, with **unit edge resistances**. Their formulas describe the fixed-weight case but do not imply the optimized support law: a fixed-weight index cannot determine whether the optimal weight of every core edge vanishes at \(s=r+1\).

The novelty claim is for this particular optimized objective, full integer classification, and all-edge support statement—not for convexity, the Kirchhoff index, or the spectrum of an ordinary graph join. An equivalent specialized conductance-design formula outside the inspected material remains possible.

## Limitations

Only complete split graphs and equal per-unit conductance costs are treated. The budget does not count separate edge-installation charges. Zero optimal conductances are permitted; if a model requires every available edge to carry a strictly positive conductance, the deletion-regime optimum is an infimum and is not attained under that extra restriction. The literature comparison does not establish global uniqueness of the result as a published discovery. The initial public-source day is bounded conservatively by the end of the July 24–28, 2006 conference interval; an exact first-distribution day within that interval was not verified. Independent mathematical audit has not been performed.

## References

1. A. Ghosh, S. Boyd, A. Saberi, “Minimizing Effective Resistance of a Graph,” Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24–28, 2006, pp. 1185–1196. https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
2. A. Ghosh, S. Boyd, A. Saberi, “Minimizing Effective Resistance of a Graph,” *SIAM Review* **50**(1), 37–66 (2008), DOI: 10.1137/050645452. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. Y. Yang, “Some Bounds for the Kirchhoff Index of Graphs,” *Abstract and Applied Analysis* (2014), article 794781, DOI: 10.1155/2014/794781.
4. J. Sedlák, A. Slavík, “Resistance distances and Kirchhoff indices in graph joins,” *Journal of Physics A: Mathematical and Theoretical* **58** (2025), 505203, DOI: 10.1088/1751-8121/ae2997.
