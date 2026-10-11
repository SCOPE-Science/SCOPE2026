# Exact Godbersen mixed-volume profile for one-vertex simplex truncations

## Finding
For each integer \(n\ge 2\), truncation parameter \(0<t<1\), and mixed-volume index \(1\le m\le n-1\), let
\[
K_t=\bigl\{x\in\mathbb R^n:x_i\ge0\ (1\le i\le n),\quad t\le\sum_{i=1}^n x_i\le1\bigr\}.
\]
This is the simplex \(\operatorname{conv}(0,e_1,\ldots,e_n)\) after its origin vertex has been truncated by a parallel hyperplane. Its volume is \(\operatorname{vol}_n(K_t)=(1-t^n)/n!\). With the symmetric Minkowski mixed-volume normalization,
\[
\boxed{V_n(K_t[n-m],(-K_t)[m])=\frac{\binom nm}{n!}\left(1-\frac mn t^m-\frac{n-m}{n}t^{n-m}\right).}
\]
Equivalently, the exact normalized deficit in Godbersen's sharp mixed-volume inequality is
\[
\boxed{G_{n,m}(t):=1-\frac{V_n(K_t[n-m],(-K_t)[m])}{\binom nm\operatorname{vol}_n(K_t)}
=\frac{(m/n)t^m+((n-m)/n)t^{n-m}-t^n}{1-t^n}.}
\]
It is strictly positive for \(0<t<1\). In every even dimension \(n=2h\), the central index \(m=h\) simplifies exactly to
\[
\boxed{G_{2h,h}(t)=\frac{t^h}{1+t^h}.}
\]
As \(t\downarrow0\), the deficit vanishes to order \(t^{\min(m,n-m)}\), with leading coefficient \(\min(m,n-m)/n\) for unequal indices and leading coefficient \(1\) for the balanced index. This determines the full quantitative profile on the natural one-vertex truncation family; the underlying universal inequality and its simplex equality case are established earlier results.

## Assumptions and scope
The integer \(n\) ranges over \(n\ge2\), the index \(m\) over \(1\le m\le n-1\), and the depth over \(0<t<1\). The polytope \(K_t\) is full dimensional, has vertices \(e_1,\ldots,e_n,te_1,\ldots,te_n\), and is not a simplex for positive depth. Standard Lebesgue volume is used. The mixed volume is defined by the Minkowski polynomial
\[
\operatorname{vol}_n(A+rB)=\sum_{m=0}^n\binom nm V_n(A[n-m],B[m])r^m\quad(r\ge0).
\]
All expressions are invariant under invertible affine transformations of \(K_t\) after normalization by its volume. No universal stability estimate or optimal distance-to-simplex exponent is asserted.

## Proof
**1. An exact membership test.** Fix \(r>0\), let \(z\in\mathbb R^n\), and write
\[
P(z)=\sum_i(z_i)_+,\qquad N(z)=\sum_i(-z_i)_+,\qquad D(z)=P(z)-N(z)=\sum_i z_i.
\]
Then
\[
\boxed{z\in K_t-rK_t\iff P(z)\le1,\quad N(z)\le r,\quad t-r\le D(z)\le1-rt.}
\]
For necessity write \(z=x-ry\) with \(x,y\in K_t\). Every coordinate permits \(x_i=(z_i)_++w_i\) and \(ry_i=(-z_i)_++w_i\) with \(w_i\ge0\). Put \(u=\sum_iw_i\). The defining sum constraints become
\[
t\le P+u\le1,\qquad rt\le N+u\le r,\qquad u\ge0.
\]
The intersection of these three closed intervals for \(u\) is nonempty precisely when the four displayed inequalities hold (using \(0<t<1\)). This also proves sufficiency, by choosing nonnegative \(w_i\) with the admissible sum \(u\).

**2. Orthant integration.** To extract every coefficient of the volume polynomial it is enough to work with \(0<r<t\). The wholly negative orthant is empty, because there \(D\le0<t-r\). The wholly positive orthant contributes
\[
H_n(r)=\frac{(1-rt)^n-(t-r)^n}{n!}.
\]
For an orthant with exactly \(j\) positive coordinates, \(1\le j<n\), set \(N=ru\) with \(0\le u\le1\). The membership test and \(r<t\) give
\[
t-r(1-u)\le P\le 1-r(t-u)_+,\qquad (a)_+=\max\{a,0\}.
\]
The density of the sum of the \(j\) positive coordinates is \(P^{j-1}/(j-1)!\), while that of the \(n-j\) negative magnitudes is \(N^{n-j-1}/(n-j-1)!\). Summing the \(\binom nj\) congruent orthants and integrating first in \(P\) yields
\[
H_j(r)=\frac{\binom nj\,r^{n-j}}{j!(n-j-1)!}
\int_0^1 u^{n-j-1}
\left([1-r(t-u)_+]^j-[t-r(1-u)]^j\right)\,du.
\]
These are exact integrals for the full volume: \(\operatorname{vol}_n(K_t-rK_t)=\sum_{j=1}^nH_j(r)\).

**3. Exact coefficient extraction.** Write \(c_m=[r^m]\operatorname{vol}_n(K_t-rK_t)\). Fix an interior index \(1\le m\le n-1\). For \(j<n\), let \(s=m-(n-j)\). If \(s<0\) then \(H_j\) does not contribute to \(c_m\). If \(s=0\), its contribution is
\[
\frac{\binom nj}{j!(n-j)!}(1-t^j).
\]
For \(1\le s\le j\), evaluate the two beta integrals
\[
\int_0^1u^{n-j-1}(t-u)_+^s\,du
=\frac{(n-j-1)!s!}{(n-j+s)!}\,t^{n-j+s},
\]
\[
\int_0^1u^{n-j-1}(1-u)^s\,du
=\frac{(n-j-1)!s!}{(n-j+s)!}.
\]
The resulting contribution is
\[
\frac{(-1)^s\binom nj}{(j-s)!(n-j+s)!}
\left(t^{n-j+s}-t^{j-s}\right).
\]
For \(j=n\), direct expansion of \(H_n\) gives exactly the same formula with \(s=m\) and \(j=n\). Therefore, setting \(j_0=n-m\), the \(s=0\) contribution from \(j=j_0\) is
\[
\frac{\binom n m}{m!(n-m)!}(1-t^{n-m}),
\]
while all \(j_0<j\le n\) contribute together
\[
\frac{t^m-t^{n-m}}{m!(n-m)!}
\sum_{j=j_0+1}^{n}(-1)^{j-j_0}\binom nj
=-\frac{\binom{n-1}{m-1}}{m!(n-m)!}(t^m-t^{n-m}).
\]
The final identity uses the elementary alternating-binomial partial sum. Since \(\binom{n-1}{m-1}=(m/n)\binom nm\), simplification gives
\[
c_m=\frac{\binom nm^2}{n!}
\left(1-\frac mn t^m-\frac{n-m}{n}t^{n-m}\right).
\]
Because the Minkowski volume is a polynomial in \(r\) for all \(r\ge0\), coefficients determined on \(0<r<t\) are its global coefficients. Comparing with its mixed-volume expansion proves the first boxed formula. The endpoint coefficients are \(c_0=c_n=(1-t^n)/n!\), as required by the individual volumes.

**4. Exact deficit and its order.** Divide by \(\binom nm\operatorname{vol}_n(K_t)\) to obtain the second boxed formula. Both \(t^m\) and \(t^{n-m}\) are strictly larger than \(t^n\), and their weights sum to one, so \(G_{n,m}(t)>0\). If \(n=2h,m=h\), cancellation of \((1-t^h)\) yields \(t^h/(1+t^h)\). The stated asymptotic follows by taking the smallest positive power in the numerator and the constant term of the denominator.

## Verification
The accompanying `verify.py` recomputes every Minkowski-volume coefficient by finite exact rational beta-integral summation independently of the compact theorem expression. It checks \(748\) coefficient instances for \(2\le n\le18\) and four rational truncation depths, including endpoints and symmetry, and returns `VERIFY_OK`. As an additional geometric numerical check, the convex-hull volumes of all pairwise differences of the \(2n\) vertices agreed with the polynomial for \(n=2,3,4,5\), three depths and three sum coefficients (\(36\) cases). These finite tests provide reproducibility checks but are not a substitute for the all-dimensional analytic argument above.

## Relationship to prior work
Kotrbatý and Mouamine established Godbersen's inequality, and Friedland, Putterman and Szusterman established its equality case among all convex bodies; their main results concern sharp global bounds and equality, not the coefficient-by-coefficient response to removing one simplex vertex. Artstein-Avidan and Putterman established weighted and unbalanced difference-body inequalities, not this exact truncated-simplex Minkowski polynomial. Sadovsky gave mixed-volume formulas for coordinate-aligned simplices in the locally anti-blocking category; \(K_t\) is not downward closed in the positive orthant, and its reflected mixed volumes are not covered by that condition. The present computation supplies an explicit quantitative family rather than a new universal inequality or equality theorem.

## Limitations
The result treats only parallel truncation of a single simplex vertex, not general truncation shapes, multiple truncated vertices, or arbitrary convex bodies. The power \(\min(m,n-m)\) is a directional vanishing order along this family, not an established globally sharp Banach–Mazur stability exponent. No universal modulus of stability and no complete classification of near-equality bodies follows. An unindexed equivalent formula in older mixed-volume literature remains a possible originality risk.

## References
1. O. Friedland, E. Putterman and M. Szusterman, *Equality case in the Kotrbatý–Mouamine inequality*, arXiv:2610.04527v1, first submitted 3 October 2026; Theorems 2–3.
2. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers–Shephard inequality*, arXiv:2607.20387 (2026).
3. S. Artstein-Avidan and E. Putterman, *On unbalanced difference bodies and Godbersen's conjecture*, arXiv:2412.05308v2; Proceedings of the AMS 153 (2025), 5345–5359.
4. S. Sadovsky, *Godbersen's conjecture for locally anti-blocking bodies*, arXiv:2312.03473v2 (2024), especially Lemma 1.2.
5. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Archiv der Mathematik 8 (1957), 220–233.
