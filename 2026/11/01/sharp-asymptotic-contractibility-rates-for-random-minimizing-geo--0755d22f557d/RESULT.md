# Sharp asymptotic contractibility rates for random minimizing geodesic polygons on flat two-tori

## Finding

Let \(T=\mathbb R^2/\Lambda\) be any Euclidean flat two-torus. For an integer \(n\ge3\), sample \(P_1,\ldots,P_n\) independently from normalized area measure, join successive vertices cyclically by almost surely unique *minimizing* geodesics, and let \(p_n(T)\) be the probability that the resulting oriented closed curve is null-homotopic. Write \(V\) for the centered Euclidean Voronoi cell of \(\Lambda\), \(A=\operatorname{area}(V)\), and \(\Sigma=A^{-1}\int_V zz^{\mathsf T}\,dz\).

The full lattice-valued homotopy law has the exact convolution description
\[
\Pr\{W_n=\lambda\}=A f_n(\lambda),\qquad
 f_n=\bigl(A^{-1}{\bf1}_V\bigr)^{*n},\quad \lambda\in\Lambda.
\]
Here \(W_n\in\Lambda\) is the displacement of the lifted closed geodesic polygon, and convolution is Euclidean convolution. In particular \(p_n(T)=Af_n(0)\), and
\[
 p_n(T)=\frac{A}{2\pi n\sqrt{\det\Sigma}}+O_T(n^{-2}).
\]

Every similarity class has a reduced lattice representation \(\Lambda=\langle(1,0),(a,b)\rangle\), with \(0\le a\le\tfrac12\), \(b>0\), and \(a^2+b^2\ge1\). Put \(t=a(1-a)\). The exact covariance determinant identity is
\[
 \boxed{\displaystyle\frac{\det\Sigma}{A^2}=\frac1{144}\left[1-\frac{2t^2}{b^2}\left(1-\frac{t}{b^2}\right)^2\right].}
\]
Consequently the following *globally sharp large-vertex contractibility inequality* holds:
\[
 \boxed{\displaystyle \frac6\pi\ \le\ \lim_{n\to\infty}n p_n(T)\ \le\ \frac{18\sqrt3}{5\pi}.}
\]
The lower equality holds **if and only if** \(T\) is rectangular (any rectangular aspect ratio), and the upper equality holds **if and only if** \(T\) is the equilateral/hexagonal flat torus, up to similarity. No claim that these inequalities hold with \(n p_n\) substituted at each finite \(n\) is made.

For every rectangular torus the *complete finite-sample null-homotopy law* is independent of the aspect ratio:
\[
 p_n(T)=\left[\frac1{(n-1)!}\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^j\binom nj
             \left(\frac n2-j\right)^{n-1}\right]^2.
\]
The initial values are \(p_3=9/16\), \(p_4=4/9\), and \(p_5=(115/192)^2\). These rectangular special values are consistency checks, not assertions of new triangle-case priority.

## Assumptions and scope

The metric is the quotient of the Euclidean metric; \(\Lambda\subset\mathbb R^2\) is any full-rank translation lattice. The random vertices are independent and normalized-area uniform, ordered by their sample indices. The segments are shortest geodesics between consecutive vertices, including the last-to-first segment. Their nonuniqueness occurs only on a null set. The homotopy class is identified with a translation \(W_n\in\Lambda\); its vanishing is independent of a choice of lift or basis. The stated rate estimate is for each **fixed** torus and is not uniform over degenerating lattice shapes.

## Proof

**1. Independent displacement reduction and exact law.** A centered Voronoi cell is a fundamental domain and satisfies \(V=-V\). Conditional on \(P_i\), the almost surely unique displacement in \(V\) projecting to \(P_{i+1}-P_i\) is uniform on \(V\). The measure-preserving, triangular change of variables from \((P_1,\ldots,P_n)\) to \((P_1,X_1,\ldots,X_{n-1})\) proves that these first \(n-1\) displacements \(X_j\) are independent uniform points of \(V\). Set \(S=X_1+\cdots+X_{n-1}\). The closing minimizing displacement is \(-S+\lambda\in V\) for exactly one \(\lambda\in\Lambda\), almost surely, and the lifted loop displacement is \(W_n=\lambda\). Thus
\[
 \Pr\{W_n=\lambda\}=\int_{\lambda+V}f_{n-1}(z)\,dz
     =A f_n(\lambda),
\]
where the second identity uses \(V=-V\). In particular, \(p_n=Af_n(0)\). This identity holds in all Euclidean translation-lattice dimensions, although the sharp shape inequality below is specific to dimension two.

**2. Fourier local asymptotic with a quantified remainder.** The characteristic function \(\phi(\xi)=A^{-1}\int_Ve^{i\xi\cdot z}\,dz\) is real and even, since \(V=-V\), with
\[
 \phi(\xi)=1-\tfrac12\xi^{\mathsf T}\Sigma\xi+O_T(|\xi|^4).
\]
The covariance \(\Sigma\) is positive definite. The density of \(X_1\) is bounded and square integrable; Plancherel gives \(\phi\in L^2(\mathbb R^2)\). As this density is positive on a planar open set, \(|\phi(\xi)|<1\) at every nonzero \(\xi\). Continuity, the Riemann--Lebesgue lemma, and the \(L^2\) bound imply that the contribution outside a fixed neighborhood of zero to \(\int\phi(\xi)^n\,d\xi\) decays exponentially for \(n\ge3\). Inside that neighborhood, rescaling \(\xi=\eta/\sqrt n\), expanding \(n\log\phi(\eta/\sqrt n)=-\eta^{\mathsf T}\Sigma\eta/2+O_T(|\eta|^4/n)\), and dominating by a Gaussian yield
\[
 f_n(0)=\frac{1}{(2\pi)^2}\int_{\mathbb R^2}\phi(\xi)^n\,d\xi
       =\frac{1}{2\pi n\sqrt{\det\Sigma}}+O_T(n^{-2}).
\]
This proves the asymptotic formula without requiring an assumption about lattice aperiodicity, since the increments have a genuine planar density.

**3. Exact planar Voronoi covariance.** Use a scale-and-rotation normalized reduced basis \(\langle(1,0),(a,b)\rangle\) with \(0\le a\le1/2\) and \(a^2+b^2\ge1\). Put
\[
 \alpha=\frac{b^2+a^2-a}{2b},\qquad
 \beta=\frac{b^2-a^2+a}{2b}.
\]
The Voronoi polygon has the cyclic vertices
\[
 (\tfrac12,\alpha),\ (a-\tfrac12,\beta),\ (-\tfrac12,\alpha),\ (-\tfrac12,-\alpha),\ (\tfrac12-a,-\beta),\ (\tfrac12,-\alpha).
\]
For \(a=0\), repetitions make the polygon a rectangle. These coordinates follow directly from the bisectors of \((1,0)\), \((a,b)\), and \((a-1,b)\), and their negatives; these are the standard reduced-basis strict Voronoi vectors. The shoelace formula gives \(A=b\). Evaluating the three quadratic area integrals over the polygon, with \(t=a(1-a)\), gives
\[
 \Sigma=\frac1{12}
 \begin{pmatrix}
 1-2t^2/b^2 & t(2a-1)/b\\[2pt]
 t(2a-1)/b & b^2+t^2/b^2
 \end{pmatrix}.
\]
Direct determinant expansion, using \((2a-1)^2=1-4t\), gives the displayed identity
\[
 \frac{\det\Sigma}{b^2}=\frac1{144}
 \left[1-2\frac{t^2}{b^2}\left(1-\frac{t}{b^2}\right)^2\right].
\]
All formulas remain valid at the rectangular and equilateral boundary configurations.

**4. Sharp optimization and uniqueness.** Let \(u=t/b^2\). The reduced-basis inequalities give
\[
 0\le t\le\frac14,\qquad 0\le u\le\frac{a}{1+a}\le\frac13.
\]
The nonnegative determinant deficit is \(q=2t u(1-u)^2\). Both \(t=a(1-a)\) and \(u(1-u)^2\) are increasing on their permitted ranges: their derivatives are \(1-2a\) and \((1-u)(1-3u)\), respectively. Therefore \(q\le2/27\), with equality exactly at \(a=1/2\), \(b^2=3/4\), the equilateral lattice. Conversely, \(q=0\) exactly when \(a=0\), giving rectangular lattices. Substitution into \(A/(2\pi\sqrt{\det\Sigma})\) proves both sharp bounds and their complete equality cases.

**5. Exact rectangular finite-sample formula.** A rectangular cell is the Cartesian product of two centered intervals. The coordinate densities of \(n\) independent uniform steps factor, and the value at zero of the \(n\)-fold convolution of \({\rm Unif}[-1/2,1/2]\) follows from the inclusion--exclusion formula for the Irwin--Hall density:
\[
 g_n(0)=\frac{1}{(n-1)!}\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^j\binom nj(n/2-j)^{n-1}.
\]
After accounting for each interval's length, \(Af_n(0)=g_n(0)^2\), independently of the rectangular aspect ratio.

## Verification

Run `python CHECK.py` with Python 3, NumPy, and SymPy. The checker independently reconstructs the Voronoi polygon's area and quadratic moments by exact symbolic shoelace integration; proves the determinant identity by simplification; tests the two equality endpoints and the elementary derivative conditions; verifies exact rational cardinal-B-spline values; independently compares the polygon formulas with interior-point sampling and nearest-lattice-vector inequalities; checks random-geodesic triangle probabilities against known rectangular and equilateral reference values, and checks longer-loop winding from independently sampled torus vertices. Its final status on the supplied file is `ALL_CHECKS_PASSED`. Monte Carlo checks are corroborative only; the infinite-dimensional-asymptotic statement is proved by the Fourier argument above.

## Relationship to prior work

Glorieux and Yarmola, *Random triangles on flat tori* (first public version March 18, 2020, arXiv:2003.08190), determine the complete **three-vertex** contractibility probability and prove that rectangles and the equilateral torus are the extremal shapes for that event. Their explicit probability values \(9/16\) and \(7/12\) are not new here. The present result addresses arbitrary numbers of vertices, the entire lattice-valued winding law, the long-polygon return rate, and a distinct sharp determinant-of-Voronoi-covariance inequality. The exact Voronoi-cell coordinates and reduced-lattice geometry are prior standard material, also described in the cited sources. Kurlin's *Mathematics of 2-Dimensional Lattices* (arXiv:2201.05150) studies complete lattice classification and Voronoi geometry, not this stochastic geodesic-polygon statistic. The Fourier local-limit method and Irwin--Hall identity are classical inputs rather than claimed original techniques.

## Limitations

The sharp inequalities apply to the **limit** of \(np_n(T)\), not to finite \(n\); uniform-in-shape error bounds have not been established. Vertices must be independent normalized-area samples, and edges must be minimizing Euclidean geodesics. The result does not apply directly to curved tori, nonuniform measures, nonminimizing arc choices, or higher-genus surfaces. A historical-priority claim beyond the specifically compared published literature is not established. No independent mathematical review is claimed.

## References

1. O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190 (first version 2020-03-18); Rocky Mountain Journal of Mathematics 52 (2022), 1345--1354. https://arxiv.org/abs/2003.08190
2. V. Kurlin, *Mathematics of 2-Dimensional Lattices*, arXiv:2201.05150; Foundations of Computational Mathematics 24 (2024), 805--863. https://arxiv.org/abs/2201.05150
3. The classical characteristic-function inversion, Plancherel theorem, Gaussian local-limit argument, and Irwin--Hall convolution formula are used in elementary standard forms, proved or specialized explicitly above.
