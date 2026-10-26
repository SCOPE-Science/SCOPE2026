# A conductance-independent contraction criterion for weighted tree heat flow in total variation

## Finding

**Theorem (exact weighted-tree criterion and two rigidity classifications).** Let \(T=(V,E)\) be a finite tree with at least one edge. Assign arbitrary strictly positive vertex masses \(\pi_v\), edge conductances \(c_e\), and, independently, edge-variation weights \(w_e\). Define
\[
(Lf)(v)=\frac{1}{\pi_v}\sum_{u:\,uv\in E}c_{uv}(f(v)-f(u)),\qquad H_t=\exp(-tL),\qquad J_w(f)=\sum_{uv\in E}w_{uv}|f(u)-f(v)|.
\]
For every edge \(e=uv\), write \(s_v=\sum_{a\ni v}w_a\) and
\[
\kappa_e=\frac{2w_e-s_u}{\pi_u}+\frac{2w_e-s_v}{\pi_v},\qquad \mu=\max_{e\in E}\left(-\frac{c_e\kappa_e}{w_e}\right).
\]
The optimal two-input variation amplification \(N(t)=\sup_{J_w(f)>0}J_w(H_tf)/J_w(f)\) satisfies
\[
N(t)=1+\mu t+O(t^2)\quad(t\downarrow0),\qquad N(t)\le \exp(\mu t)\quad(t\ge0).
\]
In particular, \(N(t)\le1\) **for every \(t\ge0\)** if and only if \(\kappa_e\ge0\) **for every edge \(e\)**. Hence global variation contractivity is independent of all the positive conductances. If an edge violates the criterion, its two-level cut signal witnesses variation amplification at all sufficiently small positive times.

Two natural simultaneous-weight classifications follow.

**(i) Uniform vertex masses.** There exist positive \(w_e\) making the heat flow variation-contractive if and only if \(T\) is a path or the three-leaf star. With uniform masses and a path whose consecutive edges carry \(w_1,\ldots,w_r\), admissibility is exactly
\[
2w_i\ge w_{i-1}+w_{i+1}\quad(1\le i\le r),\qquad w_0=w_{r+1}=0.
\]
For the three-leaf star the three weights must be identical. In this classification vertex masses may have any common positive value and the conductances are arbitrary positive numbers.

**(ii) Uniform variation weights.** There exist positive vertex masses \(\pi_v\) making the heat flow variation-contractive if and only if \(T\) is a path or a star (with any finite number of leaves). Every path contracts for every choice of positive vertex masses. For a star with \(r\ge3\) leaves, all of common mass \(\alpha\), and a center of mass \(\beta\), contractivity is equivalent to \(\beta\ge(r-2)\alpha\).

## Assumptions and scope

All spaces are finite-dimensional and real; every tree is undirected, connected and acyclic. A single-edge tree and all positive weights are included. Orientation of edges is arbitrary and does not affect any assertion. Vertex masses, conductances and variation weights are **three separate positive parameter arrays**. The seminorm \(J_w\) vanishes exactly on constants, and the heat semigroup preserves constants, so \(N(t)\) is the ordinary operator norm on the quotient by constants. Here \(O(t^2)\) is for each fixed finite weighted tree as \(t\downarrow0\), not a uniform estimate over changing trees or weights.

## Proof

Choose an orientation of the edges, let \(B\) be its edge-by-vertex incidence matrix, and write \(M=\operatorname{diag}(\pi_v)\), \(C=\operatorname{diag}(c_e)\), \(W=\operatorname{diag}(w_e)\). Then \(L=M^{-1}B^{\mathsf T}CB\). Because the underlying graph is a tree, \(B\colon\mathbb R^V\to\mathbb R^E\) is **onto**. Consequently, for \(g=WBf\) every edge vector \(g\in\mathbb R^E\) is realized by some \(f\), and \(J_w(f)=\|g\|_1\).

Differentiating the edge vector along \(\partial_t f=-Lf\) gives the **exact** finite-dimensional edge equation
\[
\partial_t g=Qg,\qquad Q=-WBM^{-1}B^{\mathsf T}CW^{-1}.
\]
Thus \(N(t)=\|\exp(tQ)\|_{1\to1}\) (not merely an upper bound). For \(e=uv\), direct matrix multiplication yields the diagonal entry
\[
Q_{ee}=-c_e\left(\frac1{\pi_u}+\frac1{\pi_v}\right).
\]
For distinct incident edges \(e,f\) sharing a vertex \(v\), their matrix entry has absolute value
\[
|Q_{fe}|=\frac{c_e w_f}{w_e\pi_v};
\]
other off-diagonal entries vanish. The sign, determined by the orientation, disappears from the absolute column sum. Therefore the \(e\)-th absolute logarithmic column sum is
\[
Q_{ee}+\sum_{f\ne e}|Q_{fe}|=
-\frac{c_e}{w_e}\left[
\frac{2w_e-s_u}{\pi_u}+\frac{2w_e-s_v}{\pi_v}\right]
=-\frac{c_e\kappa_e}{w_e}.
\]
For an arbitrary finite real matrix \(Q\), the induced \(\ell^1\) logarithmic norm is \(\mu_1(Q)=\max_j(Q_{jj}+\sum_{i\ne j}|Q_{ij}|)\). The elementary inequality obtained from \(\|I+hQ\|_1=1+h\mu_1(Q)+O(h^2)\) and \(e^{tQ}=\lim_{k\to\infty}(I+tQ/k)^k\) gives \(\|e^{tQ}\|_1\le e^{t\mu_1(Q)}\). The Taylor expansion \(e^{tQ}=I+tQ+O(t^2)\) gives the matching first-order expansion. These facts prove the criterion. If \(\mu>0\), select a column realizing \(\mu\); its coordinate vector is \(WBf\) for a function \(f\) taking one constant value on either side of that edge. The resulting \(J_w(H_tf)/J_w(f)=1+\mu t+O(t^2)>1\) for sufficiently small \(t>0\).

For (i), put \(\pi_v\equiv\pi>0\). Then \(\kappa_e\ge0\) is equivalent to \(2w_e\ge\sum_{f\sim e}w_f\), where adjacency denotes the line graph \(\mathcal L(T)\). In matrix form \(A_{\mathcal L(T)}w\le2w\) with \(w>0\). Perron–Frobenius / Collatz–Wielandt implies \(\rho(A_{\mathcal L(T)})\le2\). If \(T\) has a vertex of degree at least three, its line graph contains an induced triangle. If the line graph is connected and **strictly larger** than this triangle (or contains a larger clique), its spectral radius is strictly greater than two, a contradiction. Thus the only branched admissible tree is precisely the three-leaf star, whose line graph is a triangle. Its positive solutions of \(2w\ge Aw\) satisfy equality and are constant by irreducibility. If the maximum degree is at most two, the tree is a path and the line-graph inequalities become the displayed discrete concavity constraints, which have positive solutions (for example constant weights).

For (ii), set \(w_e\equiv1\). The criterion becomes
\[
\frac{2-\deg(u)}{\pi_u}+\frac{2-\deg(v)}{\pi_v}\ge0\qquad(uv\in E).
\]
An edge between a vertex of degree at least three and a nonleaf violates it irrespective of masses. Thus, if a tree has a branching vertex, it must be adjacent only to leaves, hence is a star. Conversely, all paths satisfy every inequality. On any star with \(r\) leaves, the edge inequality is \(1/\alpha-(r-2)/\beta\ge0\) when leaf masses share the common value \(\alpha\) and center mass is \(\beta\), proving the threshold and existence of suitable masses.

## Verification

The independent algebraic identities above are the proof; finite experiments are not used to infer all-dimensional statements. The optional standalone Python standard-library checker `check.py` regenerates every labeled tree through seven vertices (18,248 cases) and tests the uniform-mass topology classification; it also checks 150 randomly selected positive rational tuples of vertex masses, conductances and variation weights against the exact edge-generator column identities, plus small-time numerical semigroup diagnostics. Run with `python check.py` after extracting this package. The finite tests check normalization, signs and edge-orientation invariance; they cannot replace the Perron–Frobenius or logarithmic-norm arguments.

## Relationship to prior work

Ollivier's 2007–2009 coarse Ricci theory proves a general **Lipschitz contraction equivalence** for Markov operators (especially Proposition 29); it is a conceptual precursor, not a claim of novelty here. Its stated proposition does not itself give the present edge-\(\ell^1\) tree seminorm, the three independently chosen weight arrays, the exact \(\mu\) formula or the two positive-weight topology classifications. Bauer et al. (2013) investigate quadratic-\(\Gamma\) Li–Yau heat gradient estimates and curvature-dimension inequalities, not this sharp \(\ell^1\) edge-variation criterion. Kolmogorov, Pock and Rolinek (2015) consider minimizing tree total variation with unary terms, a different nonlinear variational problem. The potential for an implicit equivalent statement in earlier curvature or signal-processing literature is a residual originality limitation.

## Limitations

The tree incidence-surjectivity step is essential: on graphs with cycles edge gradients obey cycle constraints, and the absolute column logarithmic norm need not equal the sharp quotient norm. Results are not claimed for infinite trees, variable-in-time generators, signed parameters, nonlinear total-variation flow, or sharp long-time peak heights when the criterion fails. For all positive masses/conductances/variation weights satisfying the criterion, the global nonexpansiveness conclusion holds; when it fails, only a small-time strict increase, not monotonic increase at all times, is asserted. Independent scientific validation has not been performed.

## References

1. Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886 (first submitted 2007-01-30); Journal of Functional Analysis 256 (2009), 810–864. Proposition 29 and §2.5.
2. F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi and S.-T. Yau, *Li-Yau inequality on graphs*, arXiv:1306.2561 (first submitted 2013-06-11); Journal of Differential Geometry 99 (2015), 359–405.
3. V. Kolmogorov, T. Pock and M. Rolinek, *Total variation on a tree*, arXiv:1502.07770 (first submitted 2015-02-26); SIAM Journal on Imaging Sciences 9 (2016), 605–636.
