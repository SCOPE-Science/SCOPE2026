# Perron entropy flux and a four-site reversal of numerical-radius sensitivity

## Finding
For an integer \(n\ge2\), positive weights \(a_1,\ldots,a_{n-1}\), and \(1<p<\infty\), let \(T_a\) be the real or complex weighted nilpotent shift on \(\ell_p^n\), with \((T_a x)_i=a_i x_{i+1}\) for \(i<n\) and final coordinate zero. Write \(v_p(T_a)\) for its spatial numerical radius. Let \(W_a\) be the symmetric tridiagonal matrix with zeros on the diagonal and off-diagonal entries \(a_i\); let \(r>0\) be its largest eigenvalue and \(h\in(0,\infty)^n\) its Euclidean-unit Perron eigenvector. The exact first derivative at the Hilbert exponent is
\[
\left.\frac{d}{dp}v_p(T_a)\right|_{p=2}
=\frac12\sum_{i=1}^{n-1}a_i h_i h_{i+1}
\log\!\left(\frac{h_i}{h_{i+1}}\right).
\]
For three coordinates, its sign is the sign of \(a_1-a_2\). Four coordinates are the first size permitting **central-weight inversion**: for every fixed \(a>c>0\), the four-coordinate shift with weights \((a,b,c)\) has positive derivative at \(p=2\) for every sufficiently small \(b>0\), but negative derivative for every sufficiently large \(b\). Quantitatively, if \(G_{a,c}(b)=\left.d v_p(T_{a,b,c})/dp\right|_{p=2}\), then
\[
\lim_{b\downarrow0}\frac{G_{a,c}(b)}{b^2\log(1/b)}
=\frac{a}{4(a^2-c^2)}>0,
\qquad
\lim_{b\to\infty}\frac{bG_{a,c}(b)}{\log b}
=\frac{c^2-a^2}{4}<0.
\]
Consequently at least one positive central weight has vanishing derivative. Moreover, for fixed small or large \(b\), the strict inequality between the numerical radii of a shift and its reversed-weight shift near \(p=2\) reverses direction as \(b\) moves between these regimes.

## Assumptions and scope
All weights are strictly positive; dimensions are finite. The spatial numerical radius is
\[
 v_p(T_a)=\sup_{\|x\|_p=1}\left|\sum_{i=1}^{n-1}
 a_i |x_i|^{p-2}\overline{x_i}\,x_{i+1}\right|,
\]
with the usual norming functional, interpreted over either real or complex scalars. The assertion is an exact local exponent-sensitivity law and a sign-changing family, not a global monotonicity theorem in \(p\), nor a uniqueness claim for the central-weight threshold.

## Proof
**Reduction to an analytic maximization.** Positive weights and the triangle inequality show that complex phases cannot improve upon a positive real vector. Replacing \(x_i\) by \(y_i^{2/p}\) gives, with \(t=1-2/p\),
\[
 v_p(T_a)=\max_{y_i\ge0,\;\sum_i y_i^2=1}
 F_t(y),\qquad
 F_t(y)=\sum_{i=1}^{n-1}a_i y_i^{1+t}y_{i+1}^{1-t}.
\]
At \(t=0\), \(F_0(y)=\tfrac12 y^\mathsf{T}W_a y\). The irreducible nonnegative matrix \(W_a\) has a simple largest eigenvalue \(r\), and its unique nonnegative maximizing unit vector is \(h>0\). Its second variation on the sphere is strictly negative in all tangent directions (spectral gap). By the implicit-function theorem there is a smooth branch of local maximizing vectors for small \(t\); compactness and uniqueness at \(t=0\) ensure all global maximizers lie in that branch when \(t\) is small. Therefore the envelope derivative is
\[
 \left.\frac{d}{dt}\max F_t\right|_{t=0}
 =\sum_i a_i h_i h_{i+1}\log(h_i/h_{i+1}).
\]
Since \(dt/dp=2/p^2\), its value at \(p=2\) is \(1/2\). This proves the first formula.

**Why three coordinates cannot invert the endpoint ordering.** For weights \((a,c)\), set \(r=\sqrt{a^2+c^2}\) and \(u=a^2/(a^2+c^2)\). The Euclidean-unit Perron vector is \((a/r,1,c/r)/\sqrt2\). Substitution gives
\[
 \left.\frac{d}{dp}v_p(T_{a,c})\right|_{p=2}
 =\frac r8\{u\log u-(1-u)\log(1-u)\}.
\]
The expression in braces is antisymmetric about \(1/2\), positive for \(1/2<u<1\), and negative for \(0<u<1/2\). To see the strict sign, its derivative is \(2+\log(u(1-u))\), which changes sign once on \((1/2,1)\), and the expression vanishes at both endpoints of that interval. Thus the derivative's sign is fixed by the order of the two weights. With two coordinates the lone-weight shift has derivative zero by symmetry.

**Four-coordinate asymptotics.** Fix \(a>c>0\). For weights \((a,b,c)\), the largest eigenvalue \(r\) of \(W\) is the positive root satisfying
\[
 r^2=\frac{a^2+b^2+c^2+\sqrt{(a^2+b^2+c^2)^2-4a^2c^2}}2.
\]
An unnormalized Perron eigenvector is
\[
 u_1=a/r,\quad u_2=1,\quad
 u_3=(r^2-a^2)/(br),\quad u_4=c u_3/r.
\]
Write \(D=\sum_{j=1}^4u_j^2\). The derivative \(G_{a,c}(b)\) equals
\[
 \frac1{2D}\left[\frac{a^2}{r}\log(a/r)
 +b u_3\log(1/u_3)+\frac{c^2u_3^2}{r}\log(r/c)\right].
\]
Let \(\Delta=a^2-c^2>0\). As \(b\downarrow0\), the characteristic identity \((r^2-a^2)(r^2-c^2)=b^2r^2\) gives
\[
 r^2-a^2=\frac{a^2}{\Delta}b^2+O(b^4),\quad
 u_3=\frac a\Delta b+O(b^3),\quad D=2+O(b^2).
\]
The first and third bracketed terms are \(O(b^2)\), while the second is \((a/\Delta)b^2\log(1/b)+O(b^2)\). Hence \(G_{a,c}(b)=\frac{a}{4\Delta}b^2\log(1/b)+O(b^2)\).

As \(b\to\infty\), direct expansion of the same eigenvalue equation gives
\[
 r=b+O(b^{-1}),\quad u_1=a/b+O(b^{-3}),\quad
 u_3=1+O(b^{-2}),\quad u_4=c/b+O(b^{-3}),\quad D=2+O(b^{-2}).
\]
The first bracketed term is \(-a^2(\log b)/b+O(b^{-1})\); the last is \(+c^2(\log b)/b+O(b^{-1})\), and the middle term is \(O(b^{-1})\). Hence
\[
 G_{a,c}(b)=\frac{c^2-a^2}{4b}\log b+O(b^{-1}).
\]
Both signs follow, and continuity in \(b>0\) yields a zero between them. Finally, Banach duality and coordinate reversal yield \(v_p(T_{c,b,a})=v_q(T_{a,b,c})\), where \(q=p/(p-1)\). Since \(dq/dp=-1\) at \(p=2\), nonzero \(G_{a,c}(b)\) forces the asserted strict opposite inequalities for \(p>2\) sufficiently near two.

## Verification
The standalone script `verify_entropy_flux.py` uses high-precision decimal arithmetic to evaluate the closed Perron formula for weights \((2,b,1)\) at four positive values of \(b\), confirming both signs, and independently compares the slope with a Perron power iteration. Invoke `python3 verify_entropy_flux.py`. Its finite checks validate implementation and example evaluations; the derivative formula, all-weight statements, and limits are proved above.

## Relationship to prior work
The classical Hilbert-space shift calculation is the top eigenvalue of a symmetrized tridiagonal matrix, as in Chien--Nakazato (2009) and Undrakh--Nakazato--Vandanjav--Chien (2015). This is the \(p=2\) starting point, not the new assertion. The present statement concerns the derivative as the underlying Banach exponent varies and the central-weight-induced reversal in four coordinates. The general sequence-space numerical-range framework of Müller--Tomilov (2026) is a potentially relevant modern comparison, but accessible summaries do not report these claims and its primary full text was unavailable for comparison.

## Limitations
The result does not give an exact closed form for \(v_p\) at every \(p\), nor locate or count all crossover values of \(b\). It does not cover zero or negative weights without a separate reduction. The full text of a pertinent recent \(\ell_p\) numerical-range preprint could not be inspected, leaving a genuine originality risk. No independent mathematical audit has been carried out.

## References
1. M.-T. Chien and H. Nakazato, *The numerical radius of a weighted shift operator with geometric weights*, Electronic Journal of Linear Algebra 18 (2009), 58--63. DOI: 10.13001/1081-3810.1293. Full text: https://journals.uwyo.edu/index.php/ela/article/download/587/587/587.
2. B. Undrakh, H. Nakazato, A. Vandanjav, M.-T. Chien, *The numerical radius of a weighted shift operator*, Electronic Journal of Linear Algebra 30 (2015), 944--963. DOI: 10.13001/1081-3810.2821. Full text: https://journals.uwyo.edu/index.php/ela/article/download/1617/1617/1617.
3. V. Müller and Y. Tomilov, *Numerical and essential numerical ranges on* \(\ell_p\), arXiv:2606.22693 (public preprint 2026-06-21). Full text not inspected: https://arxiv.org/abs/2606.22693.
