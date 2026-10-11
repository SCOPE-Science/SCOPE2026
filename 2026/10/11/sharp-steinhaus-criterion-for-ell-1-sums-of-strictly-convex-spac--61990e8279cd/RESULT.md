# Sharp Steinhaus criterion for \(\ell_1\)-sums of strictly convex spaces

## Finding
Let \(I\) be an arbitrary index set and let \((Y_i)_{i\in I}\) be nonzero strictly convex real Banach spaces. The \(\ell_1\)-sum
\[
E=\left(\bigoplus_{i\in I}Y_i\right)_{\ell_1},\qquad \|(y_i)\|=\sum_{i\in I}\|y_i\|_{Y_i}
\]
has the Steinhaus property \((S)\) **if and only if** the number of indices \(i\) for which \(\dim_{\mathbb R}Y_i=1\) is at most one. The empty sum, interpreted as the zero space, satisfies the criterion vacuously.

Every such sum of nonzero strictly convex **complex** Banach spaces has \((S)\), interpreted for the underlying real normed space, since each complex summand has real dimension at least two. A further measurable version holds: for every measure space \((\Omega,\Sigma,\mu)\), the complex Banach space \(L^1(\mu;\mathbb C)\), considered as a real normed space, has \((S)\), even for arbitrary mixtures of atoms and nonatomic parts. The corresponding real-scalar measure characterization (at most one atom) is an existing theorem and is not claimed as new.

## Assumptions and scope
The Steinhaus property is used in the equivalent **local norm-germ** form established by Kania and Kochanek [1, Theorem A]: a real normed space \(X\) has \((S)\) precisely when, for every \(x,y\in X\) with \(x\ne y\), \(\|x\|=\|y\|=1\), and every \(\delta>0\), there exists \(z\in X\) with \(\|z\|<\delta\) and \(\|x+z\|\ne\|y+z\|\). Complex Banach spaces are treated as real Banach spaces solely for this metric property. Strict convexity always refers to the underlying real unit ball.

For arbitrary \(I\), the sum norm is the supremum of finite subsums, and an element has at most countable support. The positive measurable statement makes no separability, nonatomicity, or finiteness assumption on \(\mu\), and assertions refer to equivalence classes of integrable functions.

## Proof
**Local increment separation.** If \(Y\) is strictly convex with \(\dim_{\mathbb R}Y\ge2\), then for any distinct \(u,v\in Y\) and any \(\eta>0\) some \(z\in Y\) satisfies \(\|z\|<\eta\) and
\[
\|u+z\|-\|u\|\ne\|v+z\|-\|v\|. \tag{1}
\]
To prove this, first suppose that \(u\) and \(v\) are linearly independent, with \(u\ne0\). Taking \(z=tu\) for arbitrarily small \(t>0\), the first increment is exactly \(t\|u\|\), whereas the second is strictly less, by the strict triangle inequality between the non-collinear vectors \(v\) and \(tu\). If one of \(u,v\) is zero, choose a sufficiently small perturbation in the direction opposite the nonzero vector; the two increments then have opposite signs. If \(v=\lambda u\) for nonzero \(u\) and \(\lambda<0\), take \(z=tu\) for sufficiently small \(t>0\), obtaining increments of opposite signs. If \(\lambda>0\) and \(\lambda\ne1\), interchange \(u,v\) if necessary so that \(\lambda>1\), and choose arbitrarily small \(z\) not collinear with \(u\). Strict convexity gives
\[
\|\lambda u+z\|< (\lambda-1)\|u\|+\|u+z\|,
\]
which is exactly the strict inequality between the increments. These cases exhaust \(u\ne v\).

**Positive direction.** Assume that at most one summand of \(E\) has real dimension one. Fix distinct \(x,y\in S_E\) and \(\delta>0\). If \(x_i\ne y_i\) for some index with \(\dim_{\mathbb R}Y_i\ge2\), apply (1) in that coordinate with \(\eta=\delta\), setting every other perturbation coordinate to zero. Since \(\|x\|=\|y\|\), the resulting difference of total norms is precisely the difference in (1), and so is nonzero. Otherwise all coordinates with real dimension at least two agree. There can be at most one remaining differing coordinate, in a one-dimensional summand. Write its real coordinates as \(a,b\). Unit-norm equality forces \(|a|=|b|\) and \(a\ne b\), hence \(b=-a\ne0\). A sufficiently small nonzero perturbation parallel to \(a\) changes the two absolute values in opposite directions, so separates the norms. The local characterization [1] proves \((S)\).

**Sharp negative direction.** If two distinct summands are real one-dimensional, choose their unit vectors and embed the points with coordinates \((1/3,2/3)\) and \((2/3,1/3)\), zero elsewhere. Both have norm one and are distinct. For every \(z\in E\) with \(\|z\|<1/3\), the two selected coordinates remain positive in their fixed orientations, and the remaining coordinates contribute the same absolute norms to both points. Consequently \(\|x+z\|=\|y+z\|\) on this entire neighborhood. The local characterization [1] implies failure of \((S)\).

**Complex-scalar consequences.** A strictly convex complex Banach space is also strictly convex over the reals, with real dimension at least two. Thus the first theorem applies to arbitrary \(\ell_1\)-sums of complex strictly convex blocks. To handle a general measure space, take distinct \(f,g\in L^1(\mu;\mathbb C)\) of norm one and fix \(\delta>0\). Since \(f-g\ne0\) in \(L^1\), for some integer \(m\ge1\) the measurable set
\[
A=\{\omega:|f(\omega)-g(\omega)|>1/m\}
\]
has \(0<\mu(A)<\infty\), because \(\mu(A)\le m\|f-g\|_1\). At each point of \(A\), apply (1) in the real Euclidean plane \(\mathbb C\) to the distinct complex numbers \(f(\omega),g(\omega)\). By continuity in the perturbation, there exists a rational-complex \(q\in\mathbb Q+i\mathbb Q\), with \(|q|<\delta/(2\mu(A))\), for which
\[
d_q(\omega)=|f(\omega)+q|-|f(\omega)|-|g(\omega)+q|+|g(\omega)|\ne0.
\]
The countable collection of measurable positive and negative sign sets of these \(d_q\) covers \(A\). Hence some \(q\) and some measurable \(B\subseteq A\) with \(\mu(B)>0\) have \(d_q\) strictly positive on \(B\) or strictly negative there. Set \(h=q\mathbf1_B\). Then \(\|h\|_1\le|q|\mu(A)<\delta\), while
\[
\|f+h\|_1-\|g+h\|_1=\int_B d_q\,d\mu\ne0.
\]
The integrand is bounded in absolute value by \(2|q|\), so this is a legitimate finite integral of definite strict sign. Applying the local characterization proves \((S)\) for arbitrary complex \(L^1\).

## Verification
The proof does not rely on numerical computation. Its critical reproducible checks are: (a) strict convexity gives the stated strict triangle inequality for every non-collinear perturbation; (b) the selected one-dimensional witness preserves both coordinate signs whenever \(\|z\|<1/3\); (c) every nonzero integrable complex difference has a positive, finite-measure threshold set; and (d) rational-complex perturbations form a countable dense set, allowing a measurable positive-sign or negative-sign localization. Each point is proved explicitly above. The existing equivalence of property \((S)\) and local norm-germ separation is cited rather than reproved.

## Relationship to prior work
Kania and Kochanek [1] established the local characterization of \((S)\), strict-convexity sufficiency, a proof using a mixed \(\ell_1\)- and \(\ell_2\)-sum of real spaces, and the real \(L^1\) characterization by its atomic count. The present result gives a necessary-and-sufficient endpoint \(\ell_1\)-sum criterion for arbitrary families of strictly convex blocks, which is not the published real \(L^1\) criterion and is not implied by the mixed-sum example. The two-real-scalar obstruction is elementary and agrees with the known failure of \(\ell_1^2\).

Johnson and Kania [2] study **uniform** property \((S)\) and prove that nonatomic Bochner \(L^1\) spaces have that stronger property. The atomless part of the complex \(L^1\) conclusion is therefore already covered by their stronger result. The new complex consequence here is the arbitrary-atom case and the exact direct-sum boundary under the stated strict-convexity hypothesis; no new claim is made for the atomless case in isolation. Their uniform conclusion does not provide the sharp sum classification with two real one-dimensional obstructions.

## Limitations
The sum criterion assumes every summand is strictly convex. It does not classify sums with arbitrary non-strictly-convex blocks, establish quantitative uniform property \((S)\), or extend to quasi-Banach exponents. The measure-space consequence is a basic scalar-valued result, not a statement for arbitrary Bochner-valued integrands. A logically equivalent characterization may exist in unindexed literature; novelty is not guaranteed by a negative search. Independent mathematical validation has not been performed.

## References
1. T. Kania and T. Kochanek, *Steinhaus' lattice-point problem for Banach spaces*, arXiv:1302.6443 (first publicly submitted 26 February 2013), Theorem A, Proposition 6, and the proof of Theorem B. https://arxiv.org/abs/1302.6443
2. W. B. Johnson and T. Kania, *Uniform Property (S)*, arXiv:2602.09106 (first publicly submitted 9 February 2026), Theorem A and its nonatomic Bochner-space discussion. https://arxiv.org/abs/2602.09106
