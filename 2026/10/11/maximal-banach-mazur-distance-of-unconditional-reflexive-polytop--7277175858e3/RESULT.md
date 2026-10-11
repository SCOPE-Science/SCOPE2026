# Maximal Banach–Mazur distance of unconditional reflexive polytopes
## Finding
For every integer \(d\ge 1\) and every \(d\)-dimensional unconditional reflexive lattice polytope \(K\subset\mathbb R^d\),
\[
d_{\mathrm{BM}}(K,B_2^d)=\sqrt d.
\]
Thus the entire unconditional reflexive class attains the largest possible Banach–Mazur distance from the Euclidean ball among origin-symmetric \(d\)-dimensional convex bodies.

Kohl, Olsen and Sanyal proved that such a polytope is exactly \(K=\mathsf U P_G\) for a perfect graph \(G\) on \(d\) vertices. Here \(P_G\) is the stable-set polytope and \(\mathsf U\) denotes unconditionalization.

## Assumptions and scope
The Banach–Mazur distance is used in the standard multiplicative convention. Since both \(K\) and \(B_2^d\) are origin-symmetric, translations may be omitted. Equivalently,
\[
d_{\mathrm{BM}}(K,B_2^d)
=\inf\{\lambda\ge1: E\subseteq K\subseteq\lambda E\text{ for some centered ellipsoid }E\}.
\]
Write a centered ellipsoid as
\[
E_Q=\{x\in\mathbb R^d:x^TQ^{-1}x\le1\},
\]
where \(Q\) is positive definite.

For a perfect graph \(G\), the stable-set polytope is
\[
P_G=\{s\in\mathbb R_+^d:\sum_{i\in C}s_i\le1\text{ for every clique }C\},
\]
and \(K=\mathsf U P_G\) contains every signed characteristic vector of a stable set. Its valid signed clique inequalities are
\[
\langle \varepsilon\mathbf 1_C,x\rangle\le1
\qquad(C\text{ a clique},\ \varepsilon_i\in\{-1,1\}).
\]

## Proof
Assume \(E_Q\subseteq K\subseteq\lambda E_Q\). Fix a clique \(C\). The support function of \(E_Q\) in direction \(a\) is \(\sqrt{a^TQa}\). Hence for every sign choice on \(C\),
\[
(\varepsilon\mathbf 1_C)^TQ(\varepsilon\mathbf 1_C)\le1.
\]
Averaging over all signs cancels the off-diagonal terms and gives
\[
\sum_{i\in C}q_{ii}\le1.
\]
Put \(s_i=q_{ii}\). Positive definiteness gives \(s_i>0\), and the perfect-graph description above yields \(s\in P_G\). Therefore there are stable sets \(T\) and coefficients \(\theta_T\ge0\), with \(\sum_T\theta_T=1\), such that
\[
s=\sum_T\theta_T\mathbf 1_T.
\]
Taking reciprocal weights and averaging over this decomposition gives the exact identity
\[
\sum_T\theta_T\sum_{i\in T}\frac1{s_i}
=\sum_{i=1}^d\frac1{s_i}\sum_{T\ni i}\theta_T
=\sum_{i=1}^d1=d.
\]
Consequently some stable set \(T\) satisfies
\[
\sum_{i\in T}\frac1{q_{ii}}\ge d.
\]

For every sign choice \(\eta\) on this \(T\), the signed characteristic vector \(\eta\mathbf 1_T\) belongs to \(K\). The outer inclusion therefore gives
\[
(\eta\mathbf 1_T)^TQ^{-1}(\eta\mathbf 1_T)\le\lambda^2.
\]
Averaging again over the signs yields
\[
\sum_{i\in T}(Q^{-1})_{ii}\le\lambda^2.
\]
For every positive-definite matrix, Cauchy–Schwarz applied to \(Q^{1/2}e_i\) and \(Q^{-1/2}e_i\) gives
\[
q_{ii}(Q^{-1})_{ii}\ge1.
\]
Thus
\[
\lambda^2\ge\sum_{i\in T}(Q^{-1})_{ii}
\ge\sum_{i\in T}\frac1{q_{ii}}
\ge d.
\]
Every ellipsoid sandwich therefore has \(\lambda\ge\sqrt d\), so \(d_{\mathrm{BM}}(K,B_2^d)\ge\sqrt d\). The symmetric John theorem gives \(d_{\mathrm{BM}}(K,B_2^d)\le\sqrt d\) for every origin-symmetric \(d\)-dimensional convex body. Equality follows.

## Verification
The proof is exact and does not use numerical approximation. The accompanying `verify.py` exhaustively enumerates every labeled graph on at most five vertices, selects the perfect graphs by direct induced-subgraph checks of \(\chi=\omega\), and tests two exact-rational positive-definite ellipsoids for each. For each case it scales the ellipsoid to satisfy every signed clique inequality and verifies both the reciprocal-diagonal lower bound and the actual worst signed stable-set quadratic form. The replay result is:

`VERIFY_OK unconditional-reflexive BM lower bound perfect_graphs=1087 ellipsoid_cases=2174 n=1..5`

This finite check is a regression test, not a substitute for the proof for arbitrary \(d\).

## Relationship to prior work
Kohl, Olsen and Sanyal characterize unconditional reflexive polytopes by perfect graphs, give the signed clique inequalities and stable-set vertices used above, and identify the signed Birkhoff polytope as a principal example. Their full text does not state a Banach–Mazur-distance or John-ellipsoid result for this class.

Grundbacher and Kobos review the sharp symmetric John bound and the difficulty of its equality case. Their work discusses general equality bodies and distance ellipsoids, but does not mention unconditional reflexive polytopes or perfect graphs. The present theorem identifies the whole perfect-graph lattice-polytope class as equality bodies by a reciprocal-weight argument specific to the stable-set representation.

As an immediate instance, the signed Birkhoff polytope \(\mathcal{BB}(n)\subset\mathbb R^{n^2}\) has Banach–Mazur distance \(n\) from the Euclidean ball in its ambient dimension.

## Limitations
The theorem is restricted to unconditional reflexive lattice polytopes. It does not classify all symmetric equality bodies for the John bound, does not assert uniqueness of an optimal distance ellipsoid, and does not extend merely from unconditionality without the perfect-graph/reflexive structure. The computational verifier covers only dimensions at most five and is auxiliary to the general argument.

## References
1. F. Kohl, M. C. Olsen, R. Sanyal, *Unconditional reflexive polytopes*, arXiv:1906.01469 (first public version 2019-06-03); Discrete & Computational Geometry 64 (2020), 427–452, DOI 10.1007/s00454-020-00199-8.
2. F. Grundbacher, T. Kobos, *On certain extremal Banach–Mazur distances and Ader's characterization of distance ellipsoids*, Mathematika, first published 2025-12-04, DOI 10.1112/mtk.70062.
