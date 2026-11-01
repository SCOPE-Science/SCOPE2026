# Sharp directional majorization and Euclidean radii of the crosspolytope centroid body

## Finding
For every integer \(d\ge 2\), consider the Euclidean crosspolytope
\[
C_d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le 1\}
\]
and its **unnormalized first centroid body** \(Z(C_d)\), defined by
\[
h_d(u)=h_{Z(C_d)}(u)=\frac1{\operatorname{vol}_d(C_d)}\int_{C_d}|\langle u,x\rangle|\,dx.
\]
For \(u\) on the Euclidean unit sphere put \(s_i=u_i^2\), so \(s_i\ge0\) and \(\sum_i s_i=1\). Then \(h_d\) is **strictly Schur-concave** in \(s\): whenever \(s\) majorizes \(q\), we have \(h_d(s)\le h_d(q)\), and equality holds only when the two vectors are permutations of each other. The values are independent of the signs of the components of \(u\).

Consequently the exact centered Euclidean inradius and circumradius are
\[
\boxed{r_d=\frac1{d+1},\qquad
R_d=\frac{2\sqrt{d/\pi}}{d+1}
\frac{\Gamma(d+1/2)}{\Gamma(d+1)}.}
\]
The directions attaining the inradius are **exactly** the signed coordinate axes \(\pm e_i\), and those attaining the circumradius are **exactly** the \(2^d\) signed diagonals \((\pm1,\dots,\pm1)/\sqrt d\). The inball and circumball are both uniquely centered at the origin. They touch the centroid body, respectively, at exactly \(2d\) points \(\pm r_de_i\) and \(2^d\) points \(R_d(\pm1,\dots,\pm1)/\sqrt d\).

Moreover the exact distortion \(\rho_d=R_d/r_d\) obeys
\[
\boxed{1<\rho_d<\frac2{\sqrt\pi},\quad
\left(\frac{\rho_{d+1}}{\rho_d}\right)^2
=1+\frac1{4d(d+1)},\quad
\rho_d\longrightarrow\frac2{\sqrt\pi}.}
\]
The comparison is quantitatively rigid. For every unit \(u\),
\[
\boxed{R_d-h_d(u)\ \ge\ \frac{1}{12\pi e(d+1)}
\sum_{i=1}^d\left(u_i^2-\frac1d\right)^2.}
\]
Near a signed diagonal, with \(\delta_i=u_i^2-1/d\), its exact second-order deficit is
\[
R_d-h_d(u)=
\frac{d^{3/2}\Gamma(d+1/2)}{4\sqrt\pi(d+1)\Gamma(d+2)}
\sum_i\delta_i^2+O_d(\|\delta\|_2^3).
\]

## Assumptions and scope
Here \(d\) is any integer at least two and all scalar products and Euclidean balls use the standard Euclidean metric. The body is the actual volume-averaged centroid body, not the alternative normalization scaled to fix the Euclidean ball; the latter differs by one dimension-dependent scalar, so the strict directional comparison and the radius ratio are invariant under that convention. Strict majorization means the sorted vectors are ordered by partial sums and are not permutations of one another. All assertions include directions with some zero coordinates.

## Proof
**1. Exact probabilistic representation.** Let \(E_0,E_1,\ldots,E_d\) be independent mean-one exponential random variables and let \(\varepsilon_1,\ldots,\varepsilon_d\) be independent symmetric random signs, independent of the exponentials. Put \(S=\sum_{j=0}^d E_j\) and \(X_i=\varepsilon_i E_i/S\). The exponential-to-Dirichlet change of variables gives a uniform point \(X\) of \(C_d\); the vector \(X\) is independent of \(S\), and \(\mathbb ES=d+1\). The variables \(Y_i=\varepsilon_iE_i\) are independent symmetric Laplace variables with characteristic function \(\mathbb E e^{itY_i}=(1+t^2)^{-1}\). Hence, for any \(u\in\mathbb R^d\),
\[
(d+1)h_d(u)=\mathbb E\left|\sum_i u_iY_i\right|,
\qquad
\phi_u(t)=\prod_i(1+t^2u_i^2)^{-1}.
\]
For any integrable symmetric real random variable whose characteristic function is real, the Fourier absolute-moment identity gives
\[
\mathbb E|Y|=\frac2\pi\int_0^\infty\frac{1-\phi_Y(t)}{t^2}\,dt.
\]
Here the integral is finite near zero because \(\phi_u(t)=1+O(t^2)\), and finite at infinity by \(0\le\phi_u\le1\). Therefore the exact directional support formula is
\[
\boxed{
 h_d(u)=\frac2{\pi(d+1)}\int_0^\infty
\frac{1-\prod_i(1+t^2s_i)^{-1}}{t^2}\,dt.}
\]

**2. Majorization and both equality strata.** For fixed \(t>0\), the function \(z\mapsto\log(1+t^2z)\) is strictly concave on \([0,1]\). The strict Karamata inequality implies that if \(s\) majorizes \(q\) nontrivially, then
\(\sum_i\log(1+t^2s_i)<\sum_i\log(1+t^2q_i)\), and thus
\(\prod_i(1+t^2s_i)^{-1}>\prod_i(1+t^2q_i)^{-1}\). Substitution into the positive integral proves \(h_d(s)<h_d(q)\). On the probability simplex \((1,0,\ldots,0)\) majorizes every vector, and every vector majorizes \((1/d,\ldots,1/d)\); strictness proves the exact equality directions.

**3. Sharp radii.** At a coordinate axis, \((d+1)h_d(e_i)=\mathbb E|Y_i|=1\). At a signed diagonal the characteristic function is \((1+t^2/d)^{-d}\). Integration by parts and the beta integral yield
\[
\begin{aligned}
(d+1)h_d(u_{\rm diag})
&=\frac4\pi\int_0^\infty(1+t^2/d)^{-d-1}\,dt\\
&=2\sqrt{\frac d\pi}\,\frac{\Gamma(d+1/2)}{\Gamma(d+1)}.
\end{aligned}
\]
The Euclidean inradius of an origin-symmetric convex body is the minimum of its support function on the unit sphere; the centered circumradius is the maximum. Thus these are \(r_d\) and \(R_d\). If a ball of radius \(r_d\) centered at \(z\) lies in \(Z(C_d)\), supporting inequalities at both \(\pm e_i\) give \(\pm z_i+r_d\le r_d\), forcing \(z=0\). If a ball of radius \(R_d\) centered at \(z\) contains \(Z(C_d)\), take any \(x\in Z(C_d)\) with \(\|x\|=R_d\); the parallelogram identity for \(x-z\) and \(-x-z\) forces \(z=0\). Since \(r_dB_2^d\subseteq Z(C_d)\subseteq R_dB_2^d\), every sharp inball contact is \(r_du\) at a support-minimizing direction, and every circumball contact is \(R_du\) at a support-maximizing direction. The strict majorization classification above gives exactly the stated \(2d\) and \(2^d\) contacts.

**4. Exact dimensional evolution.** The gamma recurrence gives \(\rho_{d+1}/\rho_d=(2d+1)/(2\sqrt{d(d+1)})\), whose square is \(1+1/[4d(d+1)]>1\). Since \(\rho_1=1\), this yields \(\rho_d>1\) for \(d\ge2\); Stirling's ratio formula gives \(\lim_d\rho_d=2/\sqrt\pi\), so all finite-dimensional values are strictly below the limit.

**5. Global stability and the sharp local quadratic order.** Write \(\mu=1/d\), \(s_i=\mu+\delta_i\), and \(\sum_i\delta_i=0\). For each \(t>0\), let
\[
J(t)=d\log(1+t^2\mu)-\sum_i\log(1+t^2s_i)\ge0.
\]
The second derivative of \(f_t(z)=\log(1+t^2z)\) is \(-t^4/(1+t^2z)^2\le -t^4/(1+t^2)^2\) on \([0,1]\). Strong concavity therefore gives
\(J(t)\ge t^4\sum_i\delta_i^2/[2(1+t^2)^2]\). Since \(\phi_s(t)=\phi_\mu(t)e^{J(t)}\), with \(\phi_\mu(t)=(1+t^2/d)^{-d}\), and \(e^J-1\ge J\), the support deficit is bounded below by
\[
R_d-h_d(s)\ge\frac{\sum_i\delta_i^2}{\pi(d+1)}
\int_0^\infty\frac{t^2}{(1+t^2)^2}(1+t^2/d)^{-d}\,dt.
\]
Restrict to \(0\le t\le1\). There \((1+t^2)^{-2}\ge1/4\) and \((1+t^2/d)^{-d}\ge e^{-t^2}\ge e^{-1}\). Since \(\int_0^1t^2dt=1/3\), the stated explicit global coefficient follows.

For the local coefficient, Taylor expansion of \(J(t)\) at the balanced vector gives, uniformly in \(t\ge0\) for \(\delta\) sufficiently small, \(J(t)=\frac{t^4}{2(1+t^2/d)^2}\sum_i\delta_i^2+O_d(\|\delta\|_2^3)\) after integration against the decaying kernel. Thus
\[
R_d-h_d(s)=\frac{\sum_i\delta_i^2}{\pi(d+1)}\int_0^\infty t^2(1+t^2/d)^{-d-2}\,dt+O_d(\|\delta\|_2^3).
\]
The integral is \(d^{3/2}\sqrt\pi\Gamma(d+1/2)/(4\Gamma(d+2))\), proving the displayed sharp quadratic coefficient and the claimed order. No assertion about sharpness of the coarse global constant is made.

## Verification
An accompanying standalone Python 3 script `check.py` evaluates the Fourier integral independently with numerical quadrature, tests 192 strict majorization comparisons, reproduces the exact two-dimensional support formula, checks both Euclidean extremal profiles through dimension 12, independently samples uniform points from the crosspolytope, checks eight local quadratic expansions and 100 global-stability examples, and verifies the dimension-ratio recurrence with exact rational arithmetic. The script completed with `ALL_CHECKS_PASSED`. These finite checks are corroboration, not proofs of the all-dimensional theorem, which rests on the preceding arguments. To reproduce from this self-contained package, run `python check.py` with NumPy and SciPy installed.

## Relationship to prior work
The centroid-body integral and its connection to random simplices are classical; the discussion by Haddad (2019, first posted 2019-04-23) provides the starting framework. Pei and Wang (2015) treat general \(L_p\)-centroid-body inequalities, but not the crosspolytope directional first-moment order. König (2020) studies **volumes of fixed hyperplane sections** of the crosspolytope, including a product integral at a central section; such a section extremum does not classify the integrated absolute projection moment or the full majorization order. Ambrus (2012) studies **Gaussian maximum norms and mean widths of orthogonal crosspolytopes**, not the volume-averaged centroid body. Szarek and Wolff (2024) analyze Euclidean radii of **sections of the original \(\ell_1\)-ball**, not the centroid body's radii. The new specific geometric assertion is the strict directional Schur law and its exact radius/contact/stability consequences for \(Z(C_d)\), not the general centroid-body inequality or the older section results. Literature and mathematical-record comparisons were conducted; historical priority is not independently established.

## Limitations
The theorem concerns the canonical regular Euclidean crosspolytope and the first absolute projection moment, with explicitly specified volume-average normalization. It does not determine the centroid body volume, all higher \(L_p\) centroid bodies, or anisotropically weighted crosspolytopes in arbitrary metrics. The global stability constant is explicit but not claimed optimal; the local quadratic coefficient is exact. Numerical tests do not certify the infinite-dimensional quantifiers. Historical priority remains provisional pending additional independent bibliographic review.

## References
- J. E. Haddad, *A Convex Body Associated to the Busemann Random Simplex Inequality and the Petty conjecture*, arXiv:1904.10427, first public 2019-04-23, https://arxiv.org/abs/1904.10427 .
- Y. Pei and W. Wang, *Shephard type problems for general \(L_p\)-centroid bodies*, Journal of Inequalities and Applications 2015:287 (2015), https://doi.org/10.1186/s13660-015-0812-3 .
- H. König, *Non-central sections of the simplex, the cross-polytope and the cube*, arXiv:2002.10743, first public 2020-02-25, https://arxiv.org/abs/2002.10743 .
- G. Ambrus, *Extremal cross-polytopes and Gaussian vectors*, arXiv:1208.5923, first public 2012-08-29, https://arxiv.org/abs/1208.5923 .
- S. Szarek and P. Wolff, *Radii of Euclidean sections of \(\ell_p\)-balls*, arXiv:2410.15118, first public 2024-10-19, https://arxiv.org/abs/2410.15118 .
