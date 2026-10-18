# Exact Mahler products for cube–cross-polytope intersections and their three-dimensional phase diagram

## Finding
For every integer \(d\geq2\) and every real \(t\in[1,d]\), let
\[
K_{d,t}=[-1,1]^d\cap\left\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\leq t\right\},\qquad k=\lfloor t\rfloor.
\]
The volume of its origin polar and its Mahler volume product are exactly
\[
\operatorname{vol}_d(K_{d,t}^{\circ})=\frac{2^d}{k!\,t^{d-k}},\qquad
\mathcal P_d(t)=\frac{4^d}{d!\,k!\,t^{d-k}}
\sum_{j=0}^{k}(-1)^j\binom dj(t-j)^d.
\]
At each internal integer \(m\in\{2,\ldots,d-1\}\), the volume product is continuous but has the strict derivative jump
\[
\mathcal P_d'(m+)-\mathcal P_d'(m-)=\frac{\mathcal P_d(m)}m>0.
\]
In dimension three the function has exactly two strict interior local maxima, separated by a strict local minimum at \(t=2\). Its unique global maximum on \([1,3]\) occurs at the unique root \(\alpha\in(1,2)\) of \(2\alpha^3-9\alpha+6=0\); a second, smaller local maximum occurs at the unique root \(\beta\in(2,3)\) of \(2\beta^3-9\beta^2+21=0\). The global minima occur precisely at \(t=1\) and \(t=3\).

## Assumptions and scope
The polar of a convex body containing the origin in its interior is
\(K^\circ=\{y:\langle x,y\rangle\leq1\text{ for all }x\in K\}\). Volume is ordinary \(d\)-dimensional Lebesgue volume. No smoothness or nondegeneracy conditions on the parameter beyond \(1\leq t\leq d\) are needed. Symmetry forces the origin to be the Santaló point, so the product of the two volumes is the affine-invariant Mahler volume product. The phase classification and locations of maxima are asserted only for \(d=3\); the exact formula and integer-knot jumps hold for all stated dimensions.

## Proof
**Primal volume.** In one coordinate orthant the body equals \([0,1]^d\cap\{\sum_i x_i\leq t\}\). The unconstrained nonnegative simplex of coordinate sum at most \(s\) has volume \(s^d/d!\) for \(s\geq0\). Inclusion–exclusion over the forbidden conditions \(x_i>1\), translating selected coordinates by one, yields
\[
\operatorname{vol}_d(K_{d,t})=\frac{2^d}{d!}
\sum_{j=0}^{d}(-1)^j\binom dj(t-j)_+^d,
\]
where \((r)_+=\max\{r,0\}\). On \(t\in[k,k+1)\) terms beyond \(j=k\) vanish. At integer endpoints the extra zero terms are harmless, giving the advertised finite sum throughout the interval.

**Polar volume.** Arrange the absolute values of a direction as \(z_1\geq\cdots\geq z_d\geq0\). By a coordinatewise rearrangement and the fractional-knapsack rule, the support function of the constrained cube fills the largest \(k\) absolute coordinates to capacity one and then allocates the remaining \(t-k\) to the next coordinate:
\[
h_{K_{d,t}}(y)=\sum_{i=1}^{k}z_i+(t-k)z_{k+1},
\]
with the final term absent when \(k=d\). Indeed, swapping mass from a smaller-weight coordinate to a larger-weight coordinate cannot decrease the objective, and nonnegative weights make using the full budget optimal unless all coordinates have been saturated. Since \(K^\circ=\{y:h_K(y)\leq1\}\), this is an exact description, not merely a bound.

Within a fixed sign-and-order chamber write \(z_i=u_i+u_{i+1}+\cdots+u_d\), with \(u_i\geq0\). The triangular linear substitution has determinant one. The polar constraint becomes
\[
\sum_{i=1}^{k}i\,u_i+t\sum_{i=k+1}^{d}u_i\leq1.
\]
Its chamber volume is \(1/(d!\,k!\,t^{d-k})\). There are \(2^d d!\) chambers; their boundaries have measure zero, giving \(\operatorname{vol}_d(K_{d,t}^{\circ})=2^d/(k!\,t^{d-k})\). Multiplication by the primal volume proves the product formula, including \(t=d\).

**Integer knots.** The truncated-power formula for the primal volume is continuously differentiable in \(t\) when \(d\geq2\). In any open interval \((k,k+1)\), the logarithmic derivative of the polar volume equals \(-(d-k)/t\). At an internal integer \(m\) these two one-sided values differ by \(1/m\); the polar volume itself is continuous because \((m-1)!\,m^{d-m+1}=m!\,m^{d-m}\). The product rule gives the asserted strictly positive jump.

**Complete three-dimensional classification.** Direct substitution gives
\[
\mathcal P_3(t)=
\begin{cases}
\dfrac{32}{3}\left(t-\dfrac{3(t-1)^3}{t^2}\right),&1\leq t\leq2,\\[3pt]
\dfrac{16}{3t}\left(6-(3-t)^3\right),&2\leq t\leq3.
\end{cases}
\]
Call the two branches \(P_1\) and \(P_2\). Their derivatives and one relevant second derivative are
\[
P_1'(t)=-\frac{32(2t^3-9t+6)}{3t^3},\qquad
P_1''(t)=-\frac{192(t-1)}{t^4}<0\quad(1<t<2),
\]
\[
P_2'(t)=\frac{16(2t^3-9t^2+21)}{3t^2}.
\]
The first derivative changes from \(P_1'(1)=32/3>0\) to \(P_1'(2)=-16/3<0\). Strict concavity gives exactly one maximizer \(\alpha\in(1,2)\), necessarily the indicated cubic root. The numerator \(2t^3-9t^2+21\) of \(P_2'\) has derivative \(6t(t-3)<0\) for \(2<t<3\), and values \(1\) at \(t=2\) and \(-6\) at \(t=3\). Hence it has exactly one root \(\beta\in(2,3)\), a strict maximum. At their common endpoint the product is \(40/3\), while \(P_1'(2-)=-16/3\) and \(P_2'(2+)=4/3\); thus \(t=2\) is a strict cusp minimum.

To compare the two peaks, \(P_1(3/2)=128/9>14\). On the entire second branch put \(u=t-2\in[0,1]\). A direct expansion gives
\[
3t(14-P_2(t))=2(2-3u+24u^2-8u^3)
\geq2(2-3u+16u^2)>0,
\]
using \(u^3\leq u^2\) and the negative discriminant of the final quadratic. Thus the first peak alone is the global maximum. Finally,
\[
P_1(t)-\frac{32}{3}=-\frac{32(t-1)(2t^2-6t+3)}{3t^2}>0\quad(1<t\leq2),
\]
\[
P_2(t)-\frac{32}{3}=\frac{16(t-3)(t^2-6t+7)}{3t}>0\quad(2\leq t<3).
\]
Both endpoint values are \(32/3\), completing the global classification.

Numerically, \(\alpha=1.63122329229207\ldots\), \(\mathcal P_3(\alpha)=14.3750855157127\ldots\), \(\beta=2.08525365289105\ldots\), and \(\mathcal P_3(\beta)=13.3881740727868\ldots\). These approximations are not used to prove uniqueness or strictness.

## Verification
Execute `python3 verify.py` with SymPy, NumPy, and SciPy installed. The standalone script independently reconstructs polar volumes by convex-hull computation in dimensions two through five, compares exact rational evaluations at 170 parameter samples, solves linear programs for support-function identities, and checks the explicit cubics and derivative identities. Its expected completion begins with `VERIFY_OK`. These are supplementary finite checks only: the all-dimensional assertion follows from the geometric integrations and symbolic derivative argument above.

## Relationship to prior work
The Mahler problem asks for a sharp lower bound on the volume product of centrally symmetric bodies. The bound \(\mathcal P(K)\geq4^d/d!\) for unconditional convex bodies is known, as described in Artstein-Avidan–Karasev–Ostrover (2013) and Fradelizi–Meyer–Zvavitch (2023). This paper does not claim that bound, the elementary inclusion–exclusion formula alone, the fractional-knapsack support function alone, or the general polytope-computation algorithm as new. Its contribution is the complete parameterized polar-volume product formula and the exact two-peak three-dimensional classification, including an interior strict minimum and derivative jumps. Published investigations of the same cube–cross-polytope intersection family concern illumination numbers and graph metrics, different invariants which do not imply the stated volume product. Broader volume-product inequalities likewise do not determine this continuous family pointwise.

## Limitations
The formula does not classify every local extremum in dimensions above three or prove any new universal Mahler inequality. It does not establish that the all-dimensional formula has never appeared in equivalent norm-ball terminology. Historical overlap is a residual risk, particularly with work on symmetric norm balls and with older inaccessible full texts. Numerical samples and executable checks are corroboration rather than proofs. The result has received self-review only and has not undergone independent audit.

## References
1. S. Artstein-Avidan, R. Karasev, and Y. Ostrover, *From Symplectic Measurements to the Mahler Conjecture*, arXiv:1303.4197 (first posted 2013-03-18), https://arxiv.org/abs/1303.4197.
2. M. Fradelizi, M. Meyer, and A. Zvavitch, *Volume Product*, arXiv:2301.06131 (2023), especially Sections 3.4–3.5, https://arxiv.org/abs/2301.06131.
3. F. Barthe and M. Fradelizi, *The volume product of convex bodies with many hyperplane symmetries*, American Journal of Mathematics **135** (2013), 311–347, DOI:10.1353/ajm.2013.0018. Only the accessible abstract and introductory material were available for this comparison.
