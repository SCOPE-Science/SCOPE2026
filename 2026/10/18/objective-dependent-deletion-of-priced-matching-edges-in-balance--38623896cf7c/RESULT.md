# Objective-dependent deletion of priced matching edges in balanced bipartite networks

## Finding

Let \(n\ge3\) be an integer. In the complete bipartite graph \(K_{n,n}\), fix one perfect matching. Every matching edge has linear conductance price \(t>0\); every other edge has price one. Each of the \(n^2\) edges can receive its own nonnegative conductance, with total expenditure \(B>0\). A disconnected allocation has infinite total effective resistance. For a connected weighted graph, write \(\mathcal K=\sum_{u<v}R_{uv}\), the sum of effective resistances across all unordered vertex pairs.

Define, for \(r\ge0\),
\[
X_n(r)=n-2+2r,\quad Y_n(r)=n-1+r,\quad
H_n(r)=\frac{n-1}{n}+\frac{n-1}{X_n(r)}+\frac{1}{2Y_n(r)},
\]
\[
T_n(r)=\frac{\frac{2(n-1)}{X_n(r)^2}+\frac{1}{2Y_n(r)^2}}
{\frac1n+\frac{n-2}{X_n(r)^2}+\frac{1}{2Y_n(r)^2}},
\qquad
 t_{\rm R}(n)=T_n(0)=\frac{n^2(4n^2-11n+8)}{(n-2)(4n^3-11n^2+10n-4)}.
\]

**Theorem.** There is exactly one globally optimal allocation, even among arbitrary asymmetric choices of all conductances. Every nonmatching edge has conductance \(a_*>0\), and every matching edge has conductance \(b_*\ge0\). The optimal ratio \(r_*=b_*/a_*\) is uniquely determined by
\[
 r_*=\begin{cases}
0,&t\ge t_{\rm R}(n),\\
\text{the unique positive solution to }T_n(r)=t,&0<t<t_{\rm R}(n).
\end{cases}
\]
The exact conductances and exact optimal total resistance are
\[
 a_*=\frac{B}{n(n-1+tr_*)},\qquad b_*=r_*a_*,\qquad
\mathcal K_* =\frac{2n^2}{B}(n-1+tr_*)H_n(r_*).
\]
In particular, the entire priced matching is deleted if and only if \(t\ge t_{\rm R}(n)\); at equality the unique optimum already has \(b_*=0\). In the deletion regime the optimal value simplifies to
\[
\mathcal K_*=\frac{n(4n^3-11n^2+10n-4)}{B(n-2)}.
\]

The determinant/spanning-tree design objective responds at a different price. For the same network, prices and budget, maximizing the weighted spanning-tree enumerator \(\tau\) deletes the matching at
\[
 t_{\rm D}(n)=\frac{n(2n-3)}{(2n-1)(n-2)}.
\]
These thresholds satisfy the exact strict separation
\[
 t_{\rm R}(n)-t_{\rm D}(n)
=\frac{2n(n-1)(4n^2-9n+6)}{(n-2)(2n-1)(4n^3-11n^2+10n-4)}>0.
\]
Consequently, throughout \(t_{\rm D}(n)\le t<t_{\rm R}(n)\), determinant-optimal design deletes all matching edges but resistance-optimal design still keeps all of them. Both thresholds converge to one, but their difference is \(n^{-1}+O(n^{-2})\).

For each fixed \(0<t<1\), the resistance-optimal matching/nonmatching conductance ratio grows linearly with network size:
\[
\lim_{n\to\infty}\frac{r_*}{n}=c_t
=\frac{\sqrt{2/t-1}-1}{2}>0,\qquad
\lim_{n\to\infty}\frac{ntb_*}{B}=\frac{tc_t}{1+tc_t}.
\]
For fixed \(t>1\), every sufficiently large network instead deletes its matching. At \(t=1\), the unique optimum has \(r_*=1\) for all \(n\).

## Assumptions and scope

Vertices are distinguishable; matching and nonmatching edge weights may be chosen independently and may vanish. Conductance prices are strictly positive, and the entire budget is spent. The network is finite, undirected, simple, and connected wherever effective resistance is evaluated. Theorems concern the ordinary combinatorial weighted Laplacian, not a normalized Laplacian, a Markov transition matrix, or maximum algebraic connectivity. A zero-weight matching is permitted because \(K_{n,n}\) minus its perfect matching is connected for \(n\ge3\). The theorem excludes \(n=2\), where deleting that matching disconnects the graph.

## Proof

**1. Global symmetry and uniqueness.** For a connected allocation \(w\), let \(L(w)\) be the \(2n\)-vertex Laplacian and \(P=\mathbf1\mathbf1^\top/(2n)\). The positive definite matrix \(L(w)+P\) has inverse trace satisfying
\[
\mathcal K(w)=2n\bigl(\operatorname{tr}(L(w)+P)^{-1}-1\bigr).
\]
For positive definite \(A\), the second directional derivative of \(\operatorname{tr}(A^{-1})\) in a nonzero symmetric direction \(H\) equals \(2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0\). Indeed the traced matrix is a congruence of a nonzero symmetric square by positive definite factors. Since distinct edge-weight vectors give distinct off-diagonal Laplacian entries, \(\mathcal K\) is strictly convex on its connected domain. The feasible set is compact, and the objective tends to infinity at a disconnected boundary. Thus a unique global minimizer exists. Simultaneous permutations of the matched vertex pairs, and interchange of the two bipartition classes, preserve the costs and objective; their edge orbits are precisely the matching and its complement. Uniqueness forces a common weight \(b\) on matching edges and a common weight \(a\) on all other edges.

**2. Exact spectrum.** Put \(r=b/a\). Connectivity requires \(a>0\). The weighted degree is \(d=(n-1)a+b\), and the off-diagonal biadjacency block is \(aJ+(b-a)I\). Constants of the same or opposite signs on the two parts, and symmetric/antisymmetric zero-sum vectors, yield the nonzero Laplacian spectrum
\[
\underbrace{na,\ldots,na}_{n-1},\qquad
\underbrace{(n-2)a+2b,\ldots,(n-2)a+2b}_{n-1},\qquad
2((n-1)a+b).
\]
The weighted budget constraint is \(n(n-1)a+ntb=B\), so \(a=B/[n(n-1+tr)]\). Using the spectral identity \(\mathcal K=2n\sum_{\lambda>0}\lambda^{-1}\) gives
\[
\mathcal K(r)=\frac{2n^2}{B}(n-1+tr)H_n(r),\quad r\ge0.
\]

**3. Price threshold and optimal ratio.** Write
\[
N_n(r)=\frac{2(n-1)}{X_n(r)^2}+\frac{1}{2Y_n(r)^2},\qquad
D_n(r)=\frac1n+\frac{n-2}{X_n(r)^2}+\frac{1}{2Y_n(r)^2}.
\]
Direct differentiation gives
\[
\frac{B}{2n^2}\mathcal K'(r)=(n-1)D_n(r)\bigl(t-T_n(r)\bigr),\qquad T_n(r)=N_n(r)/D_n(r).
\]
Every factor \(D_n(r)\) is positive. Furthermore, with \(X=X_n(r)\) and \(Y=Y_n(r)\), the identity \(2Y-X=n\) reduces the derivative numerator to
\[
N_n'(r)D_n(r)-N_n(r)D_n'(r)
=\frac{N_n'(r)}n-\frac{n^2}{X^3Y^3}<0.
\]
Thus \(T_n\) decreases strictly from \(t_{\rm R}(n)>1\) to zero. The sign of \(\mathcal K'\) yields the asserted two regimes, unique interior ratio or boundary zero, and exact values. At \(t=1\), substitution gives \(T_n(1)=1\).

**4. Determinant comparison.** The matrix-tree theorem and the same spectrum give, for a class-uniform allocation,
\[
\tau(r)=n^{n-2}\left(\frac{B}{n(n-1+tr)}\right)^{2n-1}
X_n(r)^{n-1}Y_n(r).
\]
Strict concavity of the logarithm of the reduced Laplacian determinant, coupled with the price-preserving automorphisms, forces a unique two-class determinant optimum. The derivative of \(\log\tau(r)\) at \(r=0\) changes sign precisely at \(t=t_{\rm D}(n)\); strict concavity and the behavior as \(r\to\infty\) then show that the determinant optimizer has zero matching weights exactly for \(t\ge t_{\rm D}(n)\). Elementary subtraction gives the positive threshold gap displayed above. Its numerator is positive since \(4n^2-9n+6>0\) and all other factors are positive for integer \(n\ge3\). Expanding the rational expressions gives \(t_{\rm R}(n)=1+2/n+O(n^{-2})\) and \(t_{\rm D}(n)=1+1/n+O(n^{-2})\).

**5. Large-network allocation.** For fixed \(c>0\), taking \(n\to\infty\) in the rational formula yields
\[
T_n(cn)\longrightarrow\frac{2}{1+(1+2c)^2}.
\]
This limit decreases strictly from one to zero. By strict monotonicity of each \(T_n\), the solution to \(T_n(r_*)=t\) for fixed \(0<t<1\) has \(r_*/n\to c_t\), the stated inverse of this limiting function. Its budget-share limit follows from \(ntb_*/B=tr_*/(n-1+tr_*)\). For fixed \(t>1\), the threshold expansion gives eventual matching deletion.

## Verification

Run `python verify.py` with Python 3, NumPy, SymPy, and SciPy. The standalone program reconstructs exact rational Laplacians and their spectra for small sizes; checks the trace-inverse and matching-class formulas; independently builds full weighted Laplacian matrices; tests budget identity, priced support regimes, and nonsymmetric feasible allocations; verifies the derivative and determinant-threshold polynomial identities symbolically; and evaluates the long-network predictions. One execution produced `PASSED 2094 finite checks`. These checks are consistency tests, not a proof by enumeration; the foregoing argument establishes the quantified infinite-family statements.

## Relationship to prior work

The general convex resistance-allocation problem, strict uniqueness, Laplacian trace identity, symmetry reduction, semidefinite formulation, and examples involving trees, wheels, and barbells are due to Ghosh, Boyd, and Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006 / SIAM Review 50 (2008), 37–66, DOI 10.1137/050645452. In particular, the general optimization framework and symmetry argument are not claimed as new. That article does not provide the present complete bipartite matching-price threshold, conductance-ratio formula, comparison with spanning-tree design, or large-network matched-edge budget law. Johnson and Walters, *Optimal resistor networks* (Mathematika 2024, DOI 10.1112/mtk.12278), optimize topologies with unit resistances under edge-count restrictions rather than independently priced conductances on this fixed bipartite graph. Standard Kirchhoff-index formulas for unweighted networks also do not optimize the weights.

## Limitations

The novelty comparison cannot rule out an equivalent specialization in unindexed literature, and a general convex-optimization theorem may imply these formulas after a nontrivial calculation. The result is exact only for balanced complete bipartite graphs with one full distinguished matching and two linear edge-price classes. It does not address independently varying individual prices, normalized-Laplacian objectives, fixed integer edge counts, or per-edge conductance caps. The determinant comparison does not assert general dominance of one objective over the other outside this family.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006, Kyoto, July 24–28, 2006; SIAM Review **50** (2008), 37–66. DOI 10.1137/050645452. Original 2006 conference version: https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf. Author-hosted expanded version: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
2. J. R. Johnson and M. Walters, *Optimal resistor networks*, Mathematika **70** (2024), article e12278. DOI 10.1112/mtk.12278.
3. E. Bendito, A. Carmona, A. M. Encinas, J. M. Gesto, *A formula for the Kirchhoff index*, International Journal of Quantum Chemistry **108** (2008), 1200–1206. DOI 10.1002/qua.21588.
