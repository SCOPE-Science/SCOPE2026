# Sharp high-dimensional minimum-angle threshold for orthogonal-edge simplices

## Finding

Let \(M_d\) be the supremum of the smallest normalized vertex solid angle among Euclidean \(d\)-simplices with one vertex having \(d\) mutually orthogonal incident edges, for \(d\ge2\). Then
\[
M_d\sim\frac{e^{-1}}{\sqrt2}\left(\frac{e}{2\pi d}\right)^{d/2},\qquad d\to\infty.
\]
In particular, the optimal threshold satisfies
\[
\lim_{d\to\infty}\frac{2\pi^{d/2}(d-1)!}{\Gamma(d/2)}M_d=e^{-1}.
\]
This sharp asymptotic, rather than the finite-dimensional cone geometry or a choice of representation for the exact angle, is the contribution. The optimal threshold uses normalized angles, i.e. fractions of the full unit sphere. It is not an optimality statement over unrestricted simplices.

## Assumptions and scope

Write the simplex, up to Euclidean isometry, as \(S(a)=\operatorname{conv}(0,a_1e_1,\dots,a_de_d)\), where the \(e_i\) are an orthonormal basis and each \(a_i>0\). A vertex angle is the probability that a standard \(d\)-dimensional Gaussian belongs to the closed tangent cone at that vertex. The limit is in the integer dimension \(d\), not in a leg ratio of a fixed-dimensional simplex.

## Proof

**Reduction to the equal-leg angle.** The right vertex has angle \(2^{-d}\). At \(a_ie_i\), the tangent cone is given by \(z_j\ge0\) for \(j\ne i\) and \(z_i\le-\sum_{j\ne i}(a_i/a_j)z_j\), as follows from its edge rays or from the active facet inequalities. This is the vertex case of the known rectangular-simplex cone description [1, Proposition 8.1]. If \(a_i\) is a largest leg, then every ratio in its inequality is at least one, so this cone is contained in the corresponding cone for equal legs. When any ratio exceeds one, taking all \(z_j>0\) for \(j\ne i\) leaves an open interval of \(z_i\) allowed by the equal-leg inequality but not the stricter inequality. That open set has positive Gaussian mass. The equal-leg nonright vertices have a common angle strictly less than \(2^{-d}\) because their cones are proper subsets of the respective sign orthants with an open complement. Thus the equal-leg angle is \(M_d\), and equality in the finite-dimensional extremal problem requires equal legs. This cone comparison is a preparatory consequence of the known geometry, not a separate priority claim.

**Normalization for the limit.** After changing the sign of the singled-out coordinate, the equal-leg cone is \(s\ge0,\ x_j\ge0,\ \sum_{j=1}^{d-1}x_j\le s\), where \(s\) is the singled-out coordinate. For \(s>0\) put \(x_j=sR_j\). The coordinate region for \((R_1,\dots,R_{d-1})\) is the ordinary simplex of volume \(1/(d-1)!\); with slack coordinate \(R_d=1-\sum_{j<d}R_j\), its normalized uniform law is \(\mathrm{Dirichlet}(1,\dots,1)\) on \(d\) coordinates. The change of variables gives a factor \(s^{d-1}\). By Tonelli, integrating \(s\) against the Gaussian density yields
\[
M_d=\frac{\Gamma(d/2)}{2\pi^{d/2}(d-1)!}\,\mathbb E (1+Q_d)^{-d/2},\qquad Q_d=\sum_{j=1}^{d-1}R_j^2,
\]
since \(\int_0^\infty s^{d-1}e^{-s^2(1+q)/2}\,ds=2^{d/2-1}\Gamma(d/2)(1+q)^{-d/2}\). The expectation representation is used here to analyze the known exact angle.

**Sharp limit.** Take a common infinite sequence of independent unit-rate exponentials \(E_j\), and at dimension \(d\) use \(R_j=E_j/\sum_{k=1}^d E_k\). The strong law applied to \(E_j\) and \(E_j^2\) gives
\[
dQ_d=\frac{d^{-1}\sum_{j=1}^{d-1}E_j^2}{(d^{-1}\sum_{j=1}^{d}E_j)^2}\longrightarrow 2\qquad\text{almost surely}.
\]
Hence \(Q_d\to0\) and \(d\log(1+Q_d)\to2\). The integrand \((1+Q_d)^{-d/2}\) is bounded between zero and one, so its expectation tends to \(e^{-1}\). Stirling's formula gives \(\Gamma(d/2)/(2\pi^{d/2}(d-1)!)\sim (e/(2\pi d))^{d/2}/\sqrt2\), proving the equivalent.

## Relationship to prior work and limitations

Kabluchko and Schange give the tangent cones and exact angles of arbitrary rectangular simplices [1, Proposition 8.1 and Theorem 8.5]; their constant-curvature treatment specializes to the same Euclidean angles [2, Theorem 6.1]. The equal-leg nonright angle is also \(2^{-(d-1)}\) times the angle of the cone \(s\ge\sum_{j=1}^{d-1}|x_j|\): reflecting across the coordinate hyperplanes decomposes the latter into equal sectors up to null boundaries. Its Gaussian probability is known from the crosspolytope cone formula of Kabluchko and Seidel [3, Corollary 2.1]. Neither an exact-angle representation nor the finite-dimensional cone comparison is treated as new here. The large-dimension evaluation retains a multiplicative constant which is not furnished by the finite-dimensional formulas without a limit argument. High-dimensional results for volumes of ideal hyperbolic crosspolytopes discussed in [2, Remark 8.5] concern a different invariant and geometry.

The general simplex bound of Karasev et al. [4, Theorem 6] is at logarithmic scale; their cited asymptotics for the regular simplex do not give a threshold in this class. Akopyan–Karasev [5] address wider regular-simplex comparisons in low dimensions. Licht [6, Theorem 1.1 and Example 3.2] relates minimum angle to fullness and treats a fixed-dimensional degenerating orthogonal-edge example. This does not determine the sharp dimension-growing constant. Equivalent high-dimensional angle results in other literature remain possible.

## Verification

The proof is analytic. The accompanying `right_simplex_checker.py` contains finite low-dimensional quadratures for the moment representation, exact symbolic moment identities, and finite samples of the expectation factor. Those checks neither determine the extremizer nor prove convergence. In particular, the almost-sure argument and bounded convergence are needed for the sharp constant. At \(d=2\) the representation yields \(M_2=1/8\); at \(d=3\) it agrees with the trihedral angle \(\arctan(3-2\sqrt2)/(2\pi)\).

## References

1. Z. Kabluchko and P. Schange, *Angles of orthocentric simplices*, [arXiv:2505.05048](https://arxiv.org/abs/2505.05048), §§8.1–8.2.
2. Z. Kabluchko and P. Schange, *Angles and volumes of regular polytopes in geometries of constant curvature*, [arXiv:2609.21571v1](https://arxiv.org/abs/2609.21571v1), Theorem 6.1 and Remark 8.5.
3. Z. Kabluchko and H. Seidel, *Convex cones spanned by regular polytopes*, [arXiv:2006.09492v2](https://arxiv.org/abs/2006.09492v2), Corollary 2.1.
4. R. Karasev, J. Kynčl, P. Paták, Z. Patáková and M. Tancer, *Bounds for Pach's selection theorem and for the minimum solid angle in a simplex*, [arXiv:1403.8147v4](https://arxiv.org/abs/1403.8147v4), §2.
5. A. Akopyan and R. Karasev, *Bounding minimal solid angles of polytopes*, [arXiv:1505.05263v2](https://arxiv.org/abs/1505.05263v2), §§2 and 4.
6. M. W. Licht, *On solid angles and simplex shape measures*, [arXiv:2610.05883v1](https://arxiv.org/abs/2610.05883v1), Theorem 1.1 and Example 3.2.
