# Alternating inverse-factorial law for the mean length of random convex chains

## Finding
Let \(T=\operatorname{conv}\{(0,0),(1,0),(0,1)\}\), and take \(n\geq0\) independent points uniformly distributed in \(T\). Join them to the fixed vertices \((1,0)\) and \((0,1)\) by taking their convex hull \(H_n\). Let \(L_n\) be the Euclidean length of the lower convex chain from \((1,0)\) to \((0,1)\), excluding the fixed diagonal edge; for \(n=0\), use the line segment length \(\sqrt2\). Define the expected length deficit \(\Delta_n=2-\mathbb E L_n\).

Write \((z)_r=z(z+1)\cdots(z+r-1)\) for the rising factorial, with \((z)_0=1\), and set
\[
C=\frac{\Gamma(3/4)^2}{2},\qquad
c_k=\frac{2(3/2)_k(2k+1)!}{k!(4k+3)}\quad(k\geq0).
\]
Then, for every integer \(n\geq0\), the following **absolutely convergent exact series** holds:
\[
\boxed{\displaystyle
\Delta_n=C\frac{\Gamma(n+1)}{\Gamma(n+3/2)}
-\sum_{k=0}^{\infty}(-1)^k\frac{c_k}{(n+1)_{2k+2}}.}
\]
For the partial expression
\[
S_{m,n}=C\frac{\Gamma(n+1)}{\Gamma(n+3/2)}
-\sum_{k=0}^{m}(-1)^k\frac{c_k}{(n+1)_{2k+2}},
\]
every integer \(m\geq0\) gives the strict, explicitly bounded, alternating error
\[
\boxed{\displaystyle
0<(-1)^m(\Delta_n-S_{m,n})
<\frac{c_{m+1}}{(n+1)_{2m+4}}.}
\]
The first coefficients are \(c_0=2/3\), \(c_1=18/7\), and \(c_2=450/11\). In particular the expected deficit has the endpoint-sensitive expansion
\[
\boxed{\displaystyle
\Delta_n=Cn^{-1/2}-\frac{3C}{8}n^{-3/2}
-\frac{2}{3}n^{-2}+O(n^{-5/2}),\qquad n\to\infty.}
\]
The exact base checks are \(\Delta_0=2-\sqrt2\) and
\(\Delta_1=2-\frac{2\sqrt2}{3}-\frac23\operatorname{arsinh}(1)\).

## Assumptions and scope
The sampling law is normalized planar Lebesgue measure on the specific right triangle \(T\), all draws are independent, and Euclidean (not affine) arclength is used. The fixed hypotenuse edge has length \(\sqrt2\); hence \(\operatorname{Per}(H_n)=L_n+\sqrt2\) almost surely when \(n\ge1\), and the same equality holds by the doubled-segment convention when \(n=0\). Equivalently, \(\Delta_n=(2+\sqrt2)-\mathbb E\operatorname{Per}(H_n)\). No assertion about the distribution or variance of \(L_n\) is made.

## Proof
**1. Support deficit.** For a planar convex polygon, Cauchy's support identity is \(\operatorname{Per}(K)=\int_0^{2\pi}h_K((\cos\theta,\sin\theta))\,d\theta\). It extends to a segment with perimeter interpreted as twice its length. All support directions except the open southwest quadrant have the same support for \(T\) and \(H_n\): their maximizers can be chosen from the two fixed endpoints. In a southwest direction \((-a,-b)\), where \(a,b>0\) and \(a^2+b^2=1\), the support gap is
\[
G_n(a,b)=\min\{a,b,aX_1+bY_1,\ldots,aX_n+bY_n\},
\]
with the fixed-endpoint minimum \(\min(a,b)\) when \(n=0\). Therefore \(\Delta_n\) equals the integral of \(\mathbb E G_n\) over this quadrant, with no missing angular factor.

**2. Exact corner-cap probability.** Put \(s=\min(a,b)\). For every \(0\le t\le s\), the region \(\{(x,y)\in T:ax+by\le t\}\) is a triangle with area \(t^2/(2ab)\). Because \(\operatorname{area}(T)=1/2\), the probability for one sampled point to lie outside this cap is \(1-t^2/(ab)\). The layer-cake identity and independence give
\[
\mathbb E G_n(a,b)=\int_0^s\left(1-\frac{t^2}{ab}\right)^n\,dt.
\]
Reflecting the quadrant across its diagonal gives the exact positive integral
\[
\Delta_n=2\int_0^{\pi/4}\int_0^{\sin\theta}
\left(1-\frac{t^2}{\sin\theta\cos\theta}\right)^n\,dt\,d\theta.
\]

**3. A one-dimensional kernel.** Substitute \(t=\sqrt{\sin\theta\cos\theta}\,u\), then \(q=\tan\theta\); here \(0\le q\le1\), \(0\le u\le\sqrt q\), and
\(\sqrt{\sin\theta\cos\theta}\,d\theta=\sqrt q(1+q^2)^{-3/2}\,dq\). Tonelli's theorem yields
\[
\Delta_n=2\int_0^1(1-u^2)^n\int_{u^2}^1\frac{\sqrt q}{(1+q^2)^{3/2}}\,dq\,du.
\]
Set \(J(v)=\int_0^v\sqrt q(1+q^2)^{-3/2}\,dq\). The total angular integral equals
\[
A=2J(1)=\int_0^{\pi/2}\sqrt{\sin\theta\cos\theta}\,d\theta
=\frac{\Gamma(3/4)^2}{2\Gamma(3/2)}.
\]
As \(\int_0^1(1-u^2)^n\,du=\sqrt\pi\Gamma(n+1)/(2\Gamma(n+3/2))\), we obtain the exact identity
\[
\Delta_n=C\frac{\Gamma(n+1)}{\Gamma(n+3/2)}-R_n,\qquad
R_n=2\int_0^1(1-u^2)^n J(u^2)\,du.
\]

**4. Signed factorial bounds and convergence.** For every nonnegative integer \(m\) and \(x\in(0,1]\), Taylor's theorem applied to \((1+x)^{-3/2}\) gives
\[
0<(-1)^{m+1}\left[(1+x)^{-3/2}-
\sum_{k=0}^{m}(-1)^k\frac{(3/2)_k}{k!}x^k\right]
<\frac{(3/2)_{m+1}}{(m+1)!}x^{m+1}.
\]
Insert \(x=q^2\), multiply by \(\sqrt q\), integrate \(q\) from zero to \(u^2\), then integrate against the nonnegative weight \(2(1-u^2)^n\). The beta integral
\[
\int_0^1u^{4k+3}(1-u^2)^n\,du
=\frac{(2k+1)!}{2(n+1)_{2k+2}}
\]
shows that the polynomial terms in \(R_n\) are exactly \((-1)^kc_k/(n+1)_{2k+2}\). Because \(\Delta_n\) has the opposite sign to the Taylor remainder for \(R_n\), the claimed strict bound for \(\Delta_n-S_{m,n}\) follows.

For fixed \(n\), the next-term bound is \(O(m^{-n-3/2})\) as \(m\to\infty\), by the gamma-ratio asymptotic \((3/2)_m/m!=O(m^{1/2})\) and the factorial ratio. It tends to zero. The same estimate proves absolute convergence of the displayed series, including \(n=0\). Thus the finite partial formulas converge to the exact expectation.

**5. Asymptotics and boundaries.** Taking \(m=1\) gives
\[
\Delta_n=C\frac{\Gamma(n+1)}{\Gamma(n+3/2)}
-\frac{2}{3(n+1)(n+2)}
+\frac{18}{7(n+1)(n+2)(n+3)(n+4)}+O(n^{-6}).
\]
For example the final error is negative and bounded in magnitude by
\(450/[11(n+1)(n+2)(n+3)(n+4)(n+5)(n+6)]\).
Expanding \(\Gamma(n+1)/\Gamma(n+3/2)=n^{-1/2}(1-3/(8n)+O(n^{-2}))\) proves the asserted length-deficit expansion. For \(n=0\), the hull is just the fixed diagonal. For \(n=1\), each of the two random non-fixed sides has expectation \((\sqrt2+\operatorname{arsinh}1)/3\), obtained by integrating distance over \(T\); these give the stated exact checks. All claims include \(n=0\), and no asymptotic is invoked to justify finite-sample inequalities.

## Verification
Run `python CHECK.py` with Python 3.10 or later and SciPy available. The program independently evaluates the Cauchy angular/cap integral for \(n\in\{0,1,2,3,5,10,30,100\}\), verifies the alternating bounds, checks the exact zero- and one-point cases by different geometric integrations, and compares predicted perimeters with reproducible direct random convex hull simulations for \(n\in\{1,3,12,50\}\). It also checks the asymptotic expansion numerically. These are consistency tests; the proof of the infinite statement is the signed Taylor remainder and the exact beta integrals above, not Monte Carlo evidence.

## Relationship to prior work
Gusakova and Muranova (arXiv:2510.15807v1, first public October 17, 2025) give exact moments of **area** of this identical random hull. Besau and Thäle (arXiv:2510.16793, first public October 19, 2025) give generating functions and limit laws for the **vertex number**. Buchta's 2006 paper establishes that number's distribution; Gusakova and Thäle (2021) derive orthogonal-polynomial and probabilistic refinements. These results do not present the present Euclidean mean-length inverse-factorial series or signed finite-sample error mechanism. The Cauchy support formula and beta integrals are classical tools; generic expected-perimeter integration methods alone do not assert the evaluated coefficients and all-order explicit bounds here. The comparison is a best-knowledge literature assessment, not an independent priority certificate.

## Limitations
The exact evaluated law applies to a right triangle with the two specified fixed vertices and uniform sampling. Euclidean arclength is not affine invariant, so the formula does not automatically transfer to arbitrary non-right triangles. The theorem concerns the **mean**, not fluctuation laws or almost-sure rates. Originality remains subject to further literature and independent mathematical review; earlier overlooked perimeter calculations would require statement-level comparison. All computations use standard numerical libraries and cannot certify the infinite identity independently of the analytic argument.

## References
1. A. Gusakova and A. Muranova, *On the moments of the volume for random convex chains*, arXiv:2510.15807v1 (submitted 2025-10-17), https://arxiv.org/abs/2510.15807.
2. F. Besau and C. Thäle, *Random convex chains through the lens of analytic combinatorics*, arXiv:2510.16793v1 (submitted 2025-10-19), https://arxiv.org/abs/2510.16793.
3. C. Buchta, *The Exact Distribution of the Number of Vertices of a Random Convex Chain*, Mathematika 53 (2006), 247–254, https://www.esi.ac.at/preprints/esi1886.pdf.
4. A. Gusakova and C. Thäle, *On Random Convex Chains, Orthogonal Polynomials, PF Sequences and Probabilistic Limit Theorems*, Mathematika 67 (2021), 434–446, https://doi.org/10.1112/mtk.12081.
5. B. Efron, *The Convex Hull of a Random Set of Points*, Biometrika 52 (1965), 331–343, https://doi.org/10.1093/biomet/52.3-4.331 (general expected-perimeter integral framework).
