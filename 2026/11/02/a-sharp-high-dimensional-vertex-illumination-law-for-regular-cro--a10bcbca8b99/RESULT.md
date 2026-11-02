# A sharp high-dimensional vertex-illumination law for regular cross-polytopes

## Finding

Let \(P_d=\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}\) be the standard regular cross-polytope in \(\mathbb R^d\), for integer \(d\ge2\). Let \(U\) be Haar-uniform on \(S^{d-1}\), and let \(p_d\) be the probability that the ray from at least one vertex of \(P_d\) in direction \(U\) enters its interior.

If \((T_1,\ldots,T_d)\sim\operatorname{Dirichlet}(1,\ldots,1)\), put \(S_d=\sum_{j=1}^{d-1}T_j^2\). The exact law and its two-term asymptotic are

\[
p_d=\frac{d\,\pi^{(1-d)/2}}{\Gamma((d+1)/2)}\;\mathbb E(1+S_d)^{-d/2}
=\frac{d\,\pi^{(1-d)/2}}{e\,\Gamma((d+1)/2)}\left(1+\frac{7}{2d}+O(d^{-3/2})\right).
\]

Moreover, conditioned on \(U\) illuminating the vertex \(-e_1\), for each fixed positive integer \(k\),

\[
(dU_2,\ldots,dU_{k+1})\ \Longrightarrow\ (L_1,\ldots,L_k),\qquad d(1-U_1)\xrightarrow{\mathsf P}1,
\]

where the \(L_j\) are independent symmetric Laplace variables with density \(e^{-|x|}/2\). The exact finite-dimensional Gaussian-angle identity underlying the first formula is previously known; the assessed results are the displayed sharp asymptotic expansion and conditional local-direction law.

## Assumptions and scope

A direction \(u\) illuminates a vertex \(v\) exactly when \(v+tu\) belongs to the interior of \(P_d\) for some \(t>0\). The random direction is uniform with respect to normalized spherical surface measure, not a random external point or a random affine line. Boundary directions have spherical measure zero. The asymptotic is for dimension \(d\to\infty\) along integers; \(k\) remains fixed in the conditional limit. The probability refers to illumination of at least one vertex by a **single** direction, not to a covering or the minimum number of directions needed to illuminate the whole body.

## Proof

**1. Geometric reduction.** The defining inequality for \(P_d\) is \(\|x\|_1\le1\). The tangent cone at \(-e_1\) has strict interior characterized by \(u_1>\sum_{j=2}^d|u_j|\). Correspondingly, illumination of any one of the other \(2d-1\) vertices is described by signed coordinate permutations. For generic \(u\), at most one such strict inequality can hold: two would require two distinct absolute coordinates to dominate the sum of all other absolute coordinates. Thus the cones are pairwise disjoint up to null boundaries. If \(G_1,\ldots,G_d\) are independent standard Gaussians, then \(G/\|G\|_2\) is Haar-uniform, and

\[
p_d=2d\,\Pr\{G_1>\sum_{j=2}^d|G_j|\}.
\]

**2. Exact Dirichlet integral.** Using the Gaussian and half-normal densities, integrate over \(x=G_1>0\) and \(y_j=|G_j|\ge0\) constrained by \(\sum_{j=2}^d y_j<x\). Set \(y_j=xt_{j-1}\), with \(t_j\ge0\) and \(\sum_{j=1}^{d-1}t_j<1\). The Jacobian is \(x^{d-1}\). Integrating out \(x\) uses

\[
\int_0^\infty x^{d-1}e^{-ax^2/2}\,dx
=2^{d/2-1}\Gamma(d/2)a^{-d/2}\qquad(a>0).
\]

The standard simplex in the \(t\)-variables has volume \(1/(d-1)!\); uniform measure on it is the distribution of \((T_1,\ldots,T_{d-1})\) from a \(d\)-coordinate unit-parameter Dirichlet vector. The gamma duplication identity gives the prefactor in the Finding, including its exact normalization.

**3. Sharp expansion.** Write \(Y_d=dS_d/2\) and \(W_d=(1+S_d)^{-d/2}\). The Dirichlet mixed-moment identity

\[
\mathbb E\prod_{j=1}^d T_j^{a_j}
=\frac{\prod_{j=1}^d a_j!}{d(d+1)\cdots(d+A-1)},\qquad A=\sum_j a_j
\]

for nonnegative integer exponents yields

\[
\mathbb EY_d=\frac{d-1}{d+1},\quad
\operatorname{Var}(Y_d)=\frac{(d-1)(d^2+3d+6)}{(d+1)^2(d+2)(d+3)},\quad
\mathbb ES_d^2=\frac{4(d-1)(d+4)}{d(d+1)(d+2)(d+3)}.
\]

The same identity shows \(\mathbb E(Y_d-1)^4=O(d^{-2})\) and \(\mathbb ES_d^r=O(d^{-r})\) for \(r=3,4\). Taylor expansion around \(Y_d=1\), with the absolute cubic remainder bounded by the fourth-moment estimate, gives

\[
\mathbb Ee^{-Y_d}=e^{-1}\bigl(1+\tfrac{5}{2d}+O(d^{-3/2})\bigr).
\]

Because \(S_d\ge0\), the elementary bounds \(0\le S_d-\log(1+S_d)\le S_d^2/2\) and \(|S_d-\log(1+S_d)-S_d^2/2|\le S_d^3/3\), together with the indicated third and fourth moments, imply

\[
\mathbb EW_d
=\mathbb Ee^{-Y_d}+\frac d4\mathbb E(S_d^2 e^{-Y_d})+O(d^{-2})
=e^{-1}\bigl(1+\tfrac{7}{2d}+O(d^{-3/2})\bigr).
\]

For the last step, Cauchy–Schwarz and the same Dirichlet moment bounds show \(\mathbb E[S_d^2 e^{-Y_d}]=e^{-1}(4/d^2+O(d^{-5/2}))\). Substitution into the exact integral proves the two-term expansion.

**4. Conditional geometry.** Under the event that \(-e_1\) is illuminated, the direction can be written exactly as

\[
U=\frac{(1,\sigma_1T_1,\ldots,\sigma_{d-1}T_{d-1})}{\sqrt{1+S_d}},
\]

where the signs are independent fair signs and the Dirichlet vector has probability law with Radon–Nikodym derivative \(W_d/\mathbb EW_d\) relative to the uniform Dirichlet law. Write \(T_j=E_j/(E_1+\cdots+E_d)\) for independent mean-one exponentials. The strong law gives \(dS_d\to2\) in probability under the untilted Dirichlet law, hence \(W_d\to e^{-1}\) in probability. Since \(0<W_d\le1\) and \(\mathbb EW_d\to e^{-1}\), the tilted law converges to the untilted law in total variation. For fixed \(k\), \((dT_1,\ldots,dT_k)\) therefore converges to independent \(\operatorname{Exp}(1)\) variables, and independent signs turn them into symmetric Laplace variables. Finally \(d(1-1/\sqrt{1+S_d})\to1\) in probability. This proves the joint conditional law.

## Verification

The standalone program `check_illumination.py` tests the exact \(d=2\) identity, numerically integrates the exact \(d=3\) simplex integral and independently simulates Gaussian directional illumination for dimensions \(3,4,5,8\). It also samples Dirichlet ratios through dimension \(320\) and tests the limiting conditional mean and normalization. The standalone symbolic program `check_dirichlet_moments.py` reconstructs the necessary fourth central moment from Dirichlet factorial moments, checking its exact factorization and leading asymptotic. These tests corroborate, but are not substitutes for, the all-dimensional analytic argument.

## Relationship to prior work

The Gaussian dominance integral for the **solid angle at a vertex of the regular cross-polytope** is established in Kabluchko–Seidel (2020), notably their cross-polytope cone-angle formulas. A previously published exact two-point face-vector law for central four-cube sections also uses the equivalent coordinate-dominance event in dimension four; that finite-dimensional event probability is likewise not new. The exact reduction here is therefore a proof tool and is **not claimed as a new vertex-angle identity**. Donoho–Tanner (2006) develop asymptotic angle tools for cross-polytope random projections, in different dimensional scalings and for projection face counts. Kabluchko–Schange (2026) give a newer and stronger family of exact curvature-dependent cross-polytope angle integrals (Theorem 1.3); their stated results likewise do not contain the present fixed-vertex asymptotic expansion or conditional local law. Naszódi (2009) studies fractional illumination covering quantities rather than the Haar probability of a *single* direction. The addition assessed here is the explicit sharp fixed-vertex high-dimensional correction and the conditional microscopic Laplace geometry. See the companion review for the priority limits of this comparison.

## Limitations

The error term is dimension-asymptotic, not a uniform explicit remainder constant for all finite dimensions. Conditional convergence concerns finitely many transverse coordinates; the result does not determine the distribution of the entire growing-dimensional vector in total variation. The work does not change or estimate deterministic illumination numbers. Prior formulas imply the **possibility** of further asymptotic evaluation, so the novelty assessment is specifically for the evaluated constants and conditional endpoint law, subject to independent literature assessment.

## References

1. D. L. Donoho and J. Tanner, *Counting faces of randomly-projected polytopes when the projection radically lowers dimension*, arXiv:math/0607364v1 (first posted 2006-07-15), especially §§4–6 on cross-polytope angles; https://arxiv.org/abs/math/0607364 .
2. M. Naszódi, *Fractional illumination of convex bodies*, 2009, https://cdm.ucalgary.ca/article/download/62022/46694/177154 .
3. Z. Kabluchko and H. Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492v1 (first posted 2020-06-16), especially cone-angle formulas; https://arxiv.org/abs/2006.09492 .
4. Z. Kabluchko and P. Schange, *Angles and volumes of simplices, boxes, and crosspolytopes in constant curvature*, arXiv:2609.21571 (September 2026), Theorem 1.3 and Remark 1.4; https://arxiv.org/abs/2609.21571 .
