# Sharp fourth moment and Euclidean distortion of the real \(Q_3\) edge Walsh chaos

## Finding

Let \(G=Q_3\) be the graph on \(V=\{0,1\}^3\) whose two vertices are adjacent precisely when they differ in one coordinate. Let \((\varepsilon_v)_{v\in V}\) be independent uniform signs. For each of the twelve edges \(e=\{u,v\}\), put \(w_e=\varepsilon_u\varepsilon_v\). For any real coefficients \(a=(a_e)_{e\in E(G)}\), define
\[
F_a=\sum_{e\in E(G)}a_e w_e,\qquad B=\sum_{e\in E(G)}a_e^2.
\]
The optimal homogeneous fourth-moment bound is
\[
\mathbb E(F_a^4)\le4B^2,\qquad
\sup_{a\ne0}\frac{\|F_a\|_4}{\|F_a\|_2}=\sqrt2.
\]
For nonzero \(a\), equality holds precisely when its support is the four edges of **one square face** of \(Q_3\), all four coefficient magnitudes are equal, and the product of the four nonzero coefficients is positive. In particular the maximizer is localized on one face, not spread uniformly over all edges.

For the twelve-dimensional real Banach subspace
\[
X_G=\operatorname{span}_{\mathbb R}\{w_e:e\in E(G)\}\subset L^4(\{-1,1\}^{V}),
\]
with uniform probability measure, the multiplicative Banach--Mazur distance to Euclidean space is exactly
\[
d_{\mathrm{BM}}(X_G,\ell_2^{12})=\sqrt2.
\]

## Assumptions and scope

All scalar coefficients and norms are real. The underlying cube has exactly eight independent signs and twelve edges. The moment is with respect to the uniform probability measure on its \(256\) sign assignments. The space \(X_G\) is homogeneous Walsh degree two; this statement neither treats complex coefficients nor gives constants for larger hypercubes. The identification of \(Q_3\) with the bipartite graph \(K_{4,4}\) with a perfect matching removed gives an equivalent zero-diagonal bilinear-form formulation.

## Proof

The Walsh characters indexed by distinct graph edges are orthonormal in \(L^2\), so \(\|F_a\|_2^2=B\). Let \(\mathcal F\) denote the six four-edge square faces. In the fourth-power expansion, an edge multiset contributes only if every vertex has even incidence. Beyond repetitions, four distinct edges must make a four-cycle; in \(Q_3\), these are exactly the six square faces. Consequently
\[
\mathbb E F_a^4=3B^2-2\sum_e a_e^4+24\sum_{C\in\mathcal F}\prod_{e\in C}a_e.\tag{1}
\]
Set \(b_e=a_e^2\ge0\). Define the symmetric twelve-by-twelve integer matrix \(M\) by \(M_{ee}=3\), \(M_{ef}=-1\) when distinct edges \(e,f\) belong to a common square face, and \(M_{ef}=1\) otherwise. Two distinct cube edges belong to at most one square face. If \(\Pi(C)\) consists of the three partitions of the four edges of \(C\) into two unordered pairs, straightforward expansion of (1) yields the exact quartic identity
\[
4B^2-\mathbb E F_a^4
=b^{\mathsf T}Mb+
4\sum_{C\in\mathcal F}\sum_{\{\{e,f\},\{g,h\}\}\in\Pi(C)}(a_ea_f-a_ga_h)^2.\tag{2}
\]

The remaining fact is **copositivity of \(M\)**, verified by a complete exact-rational finite certificate, not a floating-point experiment. Homogeneity reduces the assertion to the simplex \(\Delta=\{b\in\mathbb R^{12}:b_e\ge0,\sum b_e=1\}\). For every nonempty support \(S\subseteq E(G)\), choose its last edge \(t\). Write \(b_t=1-\sum_{e\in S\setminus\{t\}}b_e\), and set
\[
H_{ef}=M_{ef}-M_{et}-M_{tf}+M_{tt},\qquad
h_e=M_{et}-M_{tt}\qquad(e,f\in S\setminus\{t\}).
\]
A constrained stationary point satisfies \(Hx=-h\). If a global minimum of \(b^{\mathsf T}Mb\) is negative, choose one with minimal support. The Hessian \(2H\) on that face must be positive definite: negative curvature contradicts minimality, while a nonzero Hessian null direction would keep the stationary quadratic constant until the support shrinks, contradicting minimal support. Thus any negative minimum would occur at an interior stationary point of a positive-definite support face.

The accompanying standalone program `verify_cube.py` enumerates **all \(4095\) nonempty supports**. Exact \(LDL^{\mathsf T}\) rational elimination classifies \(1475\) positive-definite tangent matrices, solves each corresponding stationary equation exactly, and checks all \(539\) solutions lying strictly inside the relative simplex. Every such candidate has nonnegative \(b^{\mathsf T}Mb\); its minimum is zero. The other \(2620\) supports cannot furnish the negative minimal-support minimizer. Therefore \(M\) is copositive and (2) proves the bound.

For the equality classification, the same exact enumeration finds only six zero-valued strictly interior positive-definite stationary supports: precisely the six square-face supports, each with \(b_e=1/4\) on its four edges. Any degenerate zero-minimum point is a convex combination of boundary zero-minimum points, obtained by moving along a tangent Hessian null direction; induction on support reduces these to the six face points. Their pairwise cross-energies \(b_C^{\mathsf T}M b_D\) are strictly positive when \(C\ne D\), so a nontrivial mixture has positive energy. Hence \(b\) must be a single uniform face point. The square terms in (2) then vanish exactly when the product of its four nonzero coefficients is positive. Conversely this face pattern gives \(\mathbb E F_a^4=4B^2\).

For the Banach--Mazur assertion, sign changes \(\varepsilon_v\mapsto\sigma_v\varepsilon_v\) induce isometries of \(X_G\), diagonal on its edge-coefficient basis, and separate any two distinct edges. Averaging a candidate optimal Euclidean quadratic form over these signs makes it diagonal; averaging further over edge-transitive cube automorphisms makes it a scalar multiple of \(\sum_e a_e^2\). Convexity of the two quadratic norm-domination inequalities preserves the same distortion bound under this averaging. Thus the Euclidean coefficient norm is optimally positioned. Its least ratio \(\|F_a\|_4/\|a\|_2\) equals \(1\) by \(L^4\)-\(L^2\) monotonicity and a single Walsh character, while the greatest ratio is \(\sqrt2\). Their quotient is the asserted exact distance.

## Verification

Run `python3 verify_cube.py` (standard library only). It constructs the cube edges and six faces; exactly enumerates the fourth-moment polynomial and the decomposition (2); enumerates all support-face stationary minima with rational \(LDL^{\mathsf T}\); tests the six zero supports, their uniform entries and pairwise strict cross-energies; and prints `EXACT_CUBE_CERTIFICATE_OK` if every assertion passes. The exact support enumeration is finite and exhaustive. The proof for all real coefficients additionally uses the analytically justified minimal-support reduction above. No numerical search or random sampling is used to establish the continuum claim.

## Relationship to prior work

Nourdin--Peccati--Reinert introduce and analyze homogeneous multilinear sums and their universality, including quadratic forms; their main theorems concern distributional approximation rather than the exact norm of the specified graph-supported Banach subspace [1]. Ledoux studies Markov-chaos fourth-moment conditions and the discrete sign-cube framework rather than this sharp finite coefficient inequality [2]. Ivanisvili--Tkocz prove dimension-independent comparison constants for all homogeneous Rademacher chaoses, including the general degree-two \(L^2\)-to-\(L^4\) bound, but do not obtain this precise twelve-dimensional graph-specific constant or face-localization classification [3]. Published related Walsh-support and moment studies were compared by their conclusions, not only their titles; none of the inspected identified statements subsumes the present claim. A previously established sharp inequality for the complete degree-two Walsh space has a larger constant and does not imply this subspace optimum or its equality cases.

## Limitations

This is a finite-graph sharp result, not a dimension-independent inequality for all graph chaoses. Copositivity relies on a reproducible exact-rational exhaustive finite support certificate rather than a closed-form symbolic sum-of-squares representation of the twelve-variable quadratic. The result is restricted to real \(L^4\) and precisely \(Q_3\). Literature searches and inspected primary results cannot exclude all unindexed equivalent statements; no independent mathematical audit has been performed.

## References

[1] I. Nourdin, G. Peccati, and G. Reinert, *Invariance principles for homogeneous sums: Universality of Gaussian Wiener chaos*, arXiv:0904.1153; first submitted 2009-04-07. https://arxiv.org/abs/0904.1153

[2] M. Ledoux, *Chaos of a Markov operator and the fourth moment condition*, arXiv:1210.7587; first submitted 2012-10-29. https://arxiv.org/abs/1210.7587

[3] P. Ivanisvili and T. Tkocz, *Comparison of moments of Rademacher chaoses*, arXiv:1807.04358; first submitted 2018-07-11. https://arxiv.org/abs/1807.04358
