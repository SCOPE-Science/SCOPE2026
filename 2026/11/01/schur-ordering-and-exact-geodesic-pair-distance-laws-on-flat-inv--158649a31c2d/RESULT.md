# Schur ordering and exact geodesic pair-distance laws on flat inversion orbifolds

## Finding

For an integer \(d\geq 2\) and positive lengths \(a_1,\ldots,a_d\), let \(T_{\mathbf a}=\mathbb R^d/(a_1\mathbb Z\oplus\cdots\oplus a_d\mathbb Z)\) be the orthogonal flat torus, and let \(P_{\mathbf a}=T_{\mathbf a}/(x\sim-x)\) have its quotient length metric and normalized Riemannian volume (the pushforward of torus Haar probability). For independent volume-uniform \(X,Y\) on \(P_{\mathbf a}\), put \(D_{\mathbf a}=d_{P_{\mathbf a}}(X,Y)\).

Let \(V=\prod_i a_i\), \(Q_{\mathbf a}=\prod_i[-a_i/2,a_i/2]\), and \(H_{\mathbf a}(r)=\operatorname{vol}_d(Q_{\mathbf a}\cap B_2^d(r))/V\) for \(r\ge0\), with \(H_{\mathbf a}(r)=0\) for \(r<0\). **The exact pair-distance law** is
\[
\Pr(D_{\mathbf a}\le r)=1-(1-H_{\mathbf a}(r))^2\qquad(r\in\mathbb R).
\]
Equivalently, \(D_{\mathbf a}\) is distributed as the minimum of two independent distances from the origin of volume-uniform points of \(T_{\mathbf a}\).

**The log-majorization theorem:** suppose \(\mathbf a,\mathbf b\in(0,\infty)^d\), \(\prod_i a_i=\prod_i b_i\), and \((\log a_1,\ldots,\log a_d)\) majorizes \((\log b_1,\ldots,\log b_d)\). Then
\[
\Pr(D_{\mathbf b}\le r)\ge\Pr(D_{\mathbf a}\le r)\quad\text{for every }r,
\]
with strict inequality for some \(r\) unless the two length multisets agree. Thus the cubic torus inversion quotient (in dimension two, the square flat pillowcase) is the **unique**, up to side permutation, minimizer of every strictly increasing continuous cost \(\mathbb E[\phi(D)]\), including every positive distance moment, among these equal-volume rectangular inversion quotients.

There are also exact universal endpoint laws. Write \(\kappa_d=\pi^{d/2}/\Gamma(1+d/2)\), \(R_{\mathbf a}=\frac12(\sum_i a_i^2)^{1/2}\), and \(m=\min_i a_i/2\). Then for \(0\le r\le m\),
\[
\Pr(D_{\mathbf a}\le r)=\frac{2\kappa_dr^d}{V}-\frac{\kappa_d^2r^{2d}}{V^2}.
\]
At the diameter \(R_{\mathbf a}\),
\[
\Pr(D_{\mathbf a}>R_{\mathbf a}-\varepsilon)
\sim \frac{(4R_{\mathbf a})^{2d}}{(d!)^2V^4}\,\varepsilon^{2d}
\quad(\varepsilon\downarrow0).
\]
The endpoint exponent doubles from \(d\) for the rectangular flat torus to \(2d\) for its inversion quotient.

## Assumptions and scope

The tori have the intrinsic Euclidean quotient distance, not an embedding-induced ambient distance. The inversion quotient may have cone singularities; the normalized volume is the pushforward of Haar measure, so singular points have measure zero. The majorization condition means equality of coordinate sums and, after sorting both vectors in decreasing order, domination of each proper initial partial sum. Length scale is arbitrary, but shape comparisons always fix \(V\) (equivalently the volume \(V/2\) of the quotient when \(d\ge2\)). The stochastic conclusion is for independent uniform samples and all dimensions \(d\ge2\); the group-theoretic distance identity itself also holds in dimension one.

For the two-dimensional rectangular pillowcase, put \(a=a_1\), \(b=a_2\), \(R=\sqrt{a^2+b^2}/2\), and define
\[
C_h(r)=\begin{cases}
0,&0\le r\le h,\\
r^2\arccos(h/r)-h\sqrt{r^2-h^2},&r>h.
\end{cases}
\]
For \(0\le r\le R\), its full elementary CDF is given by
\[
H_{a,b}(r)=\frac{\pi r^2-2C_{a/2}(r)-2C_{b/2}(r)}{ab},
\qquad \Pr(D_{a,b}\le r)=2H_{a,b}(r)-H_{a,b}(r)^2.
\]
The CDF is zero for \(r<0\) and one for \(r\ge R\). In particular, every rectangular flat pillowcase has an exact negative quartic correction in the short-distance CDF, even though its metric is flat away from four cone points.

## Proof

**1. Quotient metric and two independent displacements.** Let \(\delta(z)=d_{T_{\mathbf a}}(z,0)\), and let \(x,y\) be independent Haar-uniform lifts. Because inversion acts isometrically, the distance between the two orbits is
\[
d_{P_{\mathbf a}}([x],[y])=\min\{\delta(x-y),\delta(x+y)\}.
\]
The map \(S:T_{\mathbf a}^2\to T_{\mathbf a}^2\), \(S(x,y)=(x-y,x+y)\), is a continuous surjective group homomorphism: torus multiplication by two is surjective, so the two target coordinates admit simultaneous preimages. The pushforward of Haar probability by any surjective compact-group homomorphism is Haar probability. Therefore the two coordinates of \(S(x,y)\) are independent Haar-uniform variables. Their origin distances are independent identically distributed random variables. As the centered orthotope \(Q_{\mathbf a}\) is a nearest-lattice-point cell, each has CDF \(H_{\mathbf a}\). Taking their minimum gives the announced squared-survival formula.

**2. Schur concavity in log side lengths.** Let \(s_i=\log(a_i/2)\). Positive-orthant logarithmic coordinates \(x_i=e^{u_i}\) give
\[
\operatorname{vol}_d(B_2^d(r)\cap Q_{\mathbf a})
=2^d\int_{\substack{u_i\le s_i\ (1\le i\le d)\\
\sum_i e^{2u_i}\le r^2}}e^{\sum_i u_i}\,du_1\cdots du_d.
\]
For every \(r>0\), the domain \(\{(u,s):u_i\le s_i,\ \log(\sum_i e^{2u_i})\le 2\log r\}\) is convex: the only nonlinear constraint is a sublevel set of the convex log-sum-exp function. Its indicator multiplied by \(e^{\sum u_i}\) is jointly log-concave. The Prékopa marginal theorem (the needed classical nontrivial lemma) makes the displayed integral log-concave as a function of \(s\). It is invariant under coordinate permutations, hence Schur-concave. With the product of lengths fixed, the normalization \(V\) is constant. Since \(h\mapsto 1-(1-h)^2\) increases on \([0,1]\), the CDF is Schur-concave in \((\log a_i)\), proving the full stochastic comparison.

If the vectors are not permutations, strict convexity of \(t\mapsto e^{2t}\) and the strict majorization inequality give \(\sum_i a_i^2>\sum_i b_i^2\), hence \(R_{\mathbf a}>R_{\mathbf b}\). Every \(r\in[R_{\mathbf b},R_{\mathbf a})\) satisfies \(\Pr(D_{\mathbf b}\le r)=1>\Pr(D_{\mathbf a}\le r)\). Thus stochastic dominance is strict and every strictly increasing continuous distance cost (on the bounded support) has a strict expected-value inequality. Every vector of logs majorizes its constant-average vector, establishing cubic uniqueness.

**3. Elementary planar formula.** For \(0\le r\le R\), the disk of radius \(r\) centered at the origin meets the rectangle \([-a/2,a/2]\times[-b/2,b/2]\). A line \(x=h\) cuts off the standard circular-segment area \(C_h(r)\). Two parallel boundaries at each halfwidth account for \(2C_{a/2}\) and \(2C_{b/2}\). The outside segments beyond one vertical and one horizontal boundary do not overlap for \(r<R\), since such an overlap would require \(r^2>(a^2+b^2)/4\). The resulting intersection area is the displayed numerator, with the continuous endpoint value \(ab\).

**4. Endpoints.** For \(0\le r\le m\), the Euclidean ball is inside the nearest-lattice-point orthotope, so \(H_{\mathbf a}(r)=\kappa_dr^d/V\); the squared-survival identity gives the polynomial. Near a farthest corner of \(Q_{\mathbf a}\), write the positive local deficits as \(u_i\ge0\). The inequality \(\|x\|>R_{\mathbf a}-\varepsilon\) has, after scaling \(u_i=\varepsilon v_i\), limiting simplex \(\sum_i a_iv_i<2R_{\mathbf a}\). That simplex has volume \((2R_{\mathbf a})^d/(d!V)\). Summing over \(2^d\) corners and normalizing by \(V\) yields
\[
1-H_{\mathbf a}(R_{\mathbf a}-\varepsilon)
\sim\frac{(4R_{\mathbf a})^d}{d!V^2}\varepsilon^d.
\]
Squaring gives the claimed \(2d\)-power tail. The same construction proves that \(R_{\mathbf a}\) is the essential maximum of the pair-distance law and thus the diameter of the quotient.

## Verification

The accompanying standalone `verify.py` independently computes the planar disk–rectangle CDF by circular segments and computes intrinsic quotient distances using periodic differences of two random lifts. It passed 2,241 deterministic threshold checks and four 150,000-pair simulation ensembles, including fixed-area stochastic comparisons across seven aspect ratios. The independently integrated squared mean for the unit-square pillowcase is \(0.106818951543090\ldots\), or \(0.213637903086180\ldots\) times its area \(1/2\). An equal-area pillowcase with side ratio \(2:1\) has squared mean \(0.121695448637449\ldots\). These numbers and tests are corroboration; the all-dimensional theorem and strictness are proved analytically above. The numerical tail check uses the torus survival probability before squaring to avoid cancellation near machine precision.

## Relationship to prior work

Eskin and Okounkov (2005) introduce the flat torus involution quotient as the pillowcase in a paper on enumerating branched covers. Feldman (2015) studies independent group-valued sums and differences, including compact-group idempotent measures. Prékopa's 1973 theorem supplies preservation of log-concavity under marginalization. The present theorem applies these underlying facts to the intrinsic random-pair geodesic law and obtains log-majorization stochastic optimality, explicit rectangular CDFs, and doubled terminal-tail exponents. The theorem does not reprove or claim originality for the Haar pushforward lemma, Prékopa's marginal theorem, or classical disk–rectangle segment areas. Xu (1996) studies a fixed cube–ball intersection; the available bibliographic record does not resolve whether a stronger aspect-ratio optimization appears in unavailable text. The complete main comparison remains subject to independent historical-priority review.

## Limitations

The stochastic comparison is restricted to orthogonal rectangular lattices and their inversion quotients, not arbitrary oblique flat lattices or embedded Euclidean pillow surfaces. A pair-distance distribution does not determine all local distances or the full metric geometry. Numerical sampling cannot establish an infinite-dimensional statement; it is not used as the proof. The log-concavity step depends on Prékopa's established theorem. The manuscript's originality comparison is not a complete search of every historical source, and independent review has not been performed.

## References

- A. Eskin and A. Okounkov, *Pillowcases and quasimodular forms*, arXiv:math/0505545, first public version 2005-05-25, https://arxiv.org/abs/math/0505545.
- A. Prékopa, *On logarithmic concave measures and functions*, Acta Scientiarum Mathematicarum 34 (1973), 335–343, original article https://acta.bibl.u-szeged.hu/14411/1/math_034_335-343.pdf. The publicly verified historical reference is year-only, not an exact release day.
- G. M. Feldman, *Independent random variables on Abelian groups with independent the sum and difference*, arXiv:1510.04798, first public version 2015-10-16, https://arxiv.org/abs/1510.04798.
- L. Xu, *The Volume of the Intersection of a Cube and a Ball in N-Space*, SIAM Review 38 (1996), 669, DOI:10.1137/1038124. Full article was not available for this comparison.
