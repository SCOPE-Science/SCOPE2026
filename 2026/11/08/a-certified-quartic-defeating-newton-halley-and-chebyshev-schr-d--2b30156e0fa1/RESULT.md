# A certified quartic defeating Newton, Halley, and Chebyshev–Schröder root finding

## Finding

Let
\[
Q(z)=395z^{4}-576z^{3}-33z+33.
\]
For a polynomial \(Q\), define the rational root-finding maps on their domains of definition by
\[
\begin{aligned}
N(z)&=z-\frac{Q(z)}{Q'(z)},\\
H(z)&=z-\frac{2Q(z)Q'(z)}{2Q'(z)^2-Q(z)Q''(z)},\\
S(z)&=z-\frac{Q(z)}{Q'(z)}-\frac{Q(z)^2Q''(z)}{2Q'(z)^3}.
\end{aligned}
\]
Here \(S\) is the Chebyshev iteration called Schröder's method in the motivating work. **For this same quartic, all three maps have an attracting periodic orbit not containing a zero of \(Q\).** Newton has a superattracting two-cycle; Halley has an attracting two-cycle with multiplier modulus below \(3/20\); and \(S\) has an attracting primitive three-cycle with multiplier modulus below \(27/250\). Each therefore fails to converge to a polynomial root on a nonempty open set of complex initial values.

The quartic and the numerical candidate cycles were given by Basti and Cremaschi [1]. The new assertion here is the fully rational certificate establishing the Halley and Schröder cycles without relying on numerical iteration or a floating-point root finder. The source expressly left their certificates unproved.

## Assumptions and scope

All calculations use exact arithmetic and the unmodified rational maps displayed above, with their removable singularities filled in where appropriate. The statement concerns ordinary iteration on \(\mathbb C\); no damping, safeguarding, finite-precision effects, or pole-handling heuristic is assumed. A periodic orbit is *extraneous* if none of its points is a zero of \(Q\). A primitive period-\(q\) cycle is attracting if the product of its \(q\) complex derivatives has modulus less than one.

The two certified Halley intervals are \(I_1=[c_1-r_1,c_1+r_1]\) and \(I_2=[c_2-r_2,c_2+r_2]\), where
\[
(c_1,c_2)=(-0.0995631,-0.51938703),\qquad
(r_1,r_2)=(10^{-4},2\cdot10^{-5}).
\]
The three certified Schröder intervals are \(J_i=[d_i-s_i,d_i+s_i]\), in the cyclic order \(J_1\to J_2\to J_3\to J_1\), where
\[
\begin{aligned}
(d_1,d_2,d_3)&=(-0.691524324611229810,\,-0.347921163893610440,\,0.061148311552932509),\\
(s_1,s_2,s_3)&=(10^{-6},10^{-6},3\cdot10^{-6}).
\end{aligned}
\]
All terminating decimals in these definitions denote *exact rational numbers*.

## Proof

**Step 1: Exact Newton cycle and simple roots.** Direct substitution gives \(Q(0)=33\), \(Q'(0)=-33\), \(Q(1)=Q'(1)=-181\), and \(Q''(0)=0\). Hence \(N(0)=1\) and \(N(1)=0\); since \(N'(z)=Q(z)Q''(z)/Q'(z)^2\), the two-cycle multiplier vanishes. Neither orbit point is a root. Exact Euclidean division yields \(\gcd(Q,Q')=1\), so the quartic has four simple complex roots (also independently checked by the attached exact-arithmetic program).

**Step 2: Derivative identities.** Writing \(u=Q'\), \(v=Q''\), and \(w=Q'''\), elementary differentiation of the displayed maps gives
\[
H'(z)=\frac{Q(z)^2(3v(z)^2-2u(z)w(z))}{(2u(z)^2-Q(z)v(z))^2},\qquad
S'(z)=\frac{Q(z)^2(3v(z)^2-u(z)w(z))}{2u(z)^4}.
\]
For the second expression, its critical numerator factor is exactly
\[
3v(z)^2-u(z)w(z)=52424400z^4-76446720z^3+29859840z^2+312840z-114048.
\]
The equality is an integer polynomial identity, checked independently by polynomial arithmetic in the verifier.

**Step 3: Rigorous rational interval certificate.** For each interval, evaluate \(Q,u,v,w\), the appropriate map, and its derivative using exact rational interval arithmetic. Horner evaluation encloses every polynomial value; addition, multiplication, and division by a sign-separated interval enclose every resulting rational value. Subdivide each full interval into 64 equal rational pieces when bounding the derivative to limit interval overestimation. The attached standalone script `verify_cycles.py` proves all of the following strict bounds, including nonvanishing of \(Q\) and each rational map's denominator on the stated intervals:

| Map and interval | Exact upper bound on absolute derivative | Absolute error of mapped center versus next center |
|---|---:|---:|
| \(H\), \(I_1\) | \(1/10\) | \(<10^{-8}\) |
| \(H\), \(I_2\) | \(3/2\) | \(<10^{-8}\) |
| \(S\), \(J_1\) | \(9/10\) | \(<10^{-17}\) |
| \(S\), \(J_2\) | \(12/5\) | \(<10^{-17}\) |
| \(S\), \(J_3\) | \(1/20\) | \(<10^{-17}\) |

For a real point \(x\) in a center-radius interval, the mean value theorem bounds the displacement of its image from the next center by the center error plus the derivative bound times the source radius. The five strict inequalities give \(H(I_1)\subset\operatorname{int}(I_2)\), \(H(I_2)\subset\operatorname{int}(I_1)\), and \(S(J_i)\subset\operatorname{int}(J_{i+1})\) cyclically. The intervals in each family are pairwise disjoint.

**Step 4: Existence, period and attraction.** The self-maps \(H^2:I_1\to I_1\) and \(S^3:J_1\to J_1\) are contractions with derivative-norm bounds
\[
\frac1{10}\frac32=\frac3{20}<1,
\qquad
\frac9{10}\frac{12}{5}\frac1{20}=\frac{27}{250}<1.
\]
The contraction theorem yields a unique fixed point of each respective return map inside its first interval. Iterating the map through the disjoint consecutive intervals creates a primitive two-cycle or three-cycle. Exact interval signs exclude polynomial zeros and poles on all five intervals. Both rational maps are therefore holomorphic near these cycles, and the stated derivative-product estimates prove attraction in the full complex plane, not merely on the real axis. A complex attracting periodic orbit has an open local basin; points in that basin cannot converge to a root of \(Q\).

## Verification

Run `python3 verify_cycles.py` with Python 3 standard-library support. It reports `VERIFY_OK` after independently checking polynomial derivatives, squarefreeness, all interval separations from zeros and poles, 64 exact rational subinterval derivative bounds for each orbit interval, strict center-image containment, the contraction multipliers, and the Newton two-cycle. All bound checks use `fractions.Fraction`; floating-point conversions are used **only in diagnostic printing**, never in a comparison or proof decision. On the supplied file, the result was `VERIFY_OK`.

The finite certificate is a proof for all points in each of the five continuous intervals because exact interval arithmetic encloses full subinterval ranges; it is not an inference from sampling a finite set of orbit points.

## Relationship to prior work

Basti and Cremaschi [1, Section 5] explicitly give this same quartic, its Newton two-cycle, and numerical Halley and Schröder orbit multipliers, while stating that additional interval certificates are not included. Their rigorous Theorem 1.1 concerns a *different* quartic for the Newton–Halley pair. The present result supplies the missing complete mathematical certification for the three-method example; the polynomial, the computational suggestion, and Newton's cycle are not claimed as discoveries here.

Collins and Hunter [2], as characterized in [1], establish simultaneous obstruction for degrees at least five, which does not imply the particular degree-four assertion. Collins [3] constructs prescribed attracting cycles for Halley and Schröder methods, but the abstract theorem on those maps does not itself establish a common degree-four example defeating Newton as well. Statements of individual cycles or numerical evidence are strictly weaker than certified attracting, extraneous cycles for all three maps of this same quartic.

## Limitations

This establishes existence of three individual nonempty open failure basins. It does **not** prove that those three basins have a nonempty common intersection, nor that degree four is the minimal possible degree (the cubic question remains open in [1]). It does not address safeguarded root solvers or floating-point behavior. Independent mathematical audit has not been performed. Historical-priority search is incomplete: the full text of [2] was not available through checked sources, although [1] directly discusses its degree range.

## References

[1] A. Basti and T. Cremaschi, *Simultaneous Global Convergence Failure of Newton's and Halley's Methods in Degree Four*, arXiv:2610.03246v1, first submitted 2026-10-02, particularly Sections 2 and 5 and Appendix A. https://arxiv.org/html/2610.03246v1

[2] J. Collins and G. Hunter, *A family of polynomials that defy general convergence in three methods*, Examples and Counterexamples 8 (2025), 100191. https://doi.org/10.1016/j.exco.2025.100191

[3] J. T. Collins, *Constructing attracting cycles for Halley and Schröder maps of polynomials*, Discrete and Continuous Dynamical Systems 37 (2017), 5455–5465. https://doi.org/10.3934/dcds.2017237
