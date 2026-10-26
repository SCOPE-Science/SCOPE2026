# Two sharp angular transitions and spectral camouflage for quadratic ball concentration

## Finding
Let \(d\ge2\) be an integer, \(\mathbb B^d\subset\mathbb R^d\) the unit ball with normalized Lebesgue probability measure, and \(\Pi_2^d\) its complex polynomials of total degree at most two. For any measurable radial mask \(h:[0,1]\to[0,1]\) with positive mean, set \(t=\lVert x\rVert^2\) and
\[
a=d/2,\quad \mu=\frac{a}{a+1},\quad \nu=\frac{a}{a+2},\quad
b_j=\int_0^1h(t)t^j a t^{a-1}\,dt\quad(j=0,1,2).
\]
The sharp concentration ratio is
\[
\Lambda_d(h)=\sup_{0\ne f\in\Pi_2^d}
\frac{\int_{\mathbb B^d}h(\lVert x\rVert^2)|f(x)|^2\,dx}
{\int_{\mathbb B^d}|f(x)|^2\,dx}.
\]
Define \(\lambda_1=b_1/\mu\), \(\lambda_2=b_2/\nu\), \(\tau=\nu/\mu=(a+1)/(a+2)\), and let \(\lambda_{\mathrm{rad},\pm}\) be the ordered generalized eigenvalues of
\[
B=\begin{pmatrix}b_0&b_1\\b_1&b_2\end{pmatrix},\qquad
M=\begin{pmatrix}1&\mu\\\mu&\nu\end{pmatrix}.
\]
The **complete spectrum**, with multiplicities before accidental coincidences, is
\[
\lambda_{\mathrm{rad},+},\ \lambda_{\mathrm{rad},-}\quad(1\text{ each}),\qquad
\lambda_1\quad(d),\qquad
\lambda_2\quad\left(\frac{d(d+1)}2-1\right).
\]
In particular \(\Lambda_d(h)=\max\{\lambda_{\mathrm{rad},+},\lambda_1\}\), because \(\lambda_{\mathrm{rad},+}\ge\lambda_2\). **The leading eigenspace consists exclusively of linear polynomials** precisely when both strict inequalities
\[
\boxed{\quad \frac{b_1}{b_0}>\mu\quad\text{and}\quad\frac{b_2}{b_1}<\tau\quad}
\]
hold. The weak inequalities characterize exactly when linear polynomials attain the sharp concentration ratio.

All boundary equality cases are determined: if only the first comparison is equality and the second is strict, the leading space is \(\operatorname{span}\{1,x_1,\ldots,x_d\}\); if the second is equality and the first strict, it is the direct sum of all homogeneous linear and all homogeneous quadratic polynomials. If both are equalities, the concentration operator is **exactly scalar on every polynomial in \(\Pi_2^d\)**, with eigenvalue \(b_0\). Outside the two weak moment inequalities, the maximal eigenvalue is \(\lambda_{\mathrm{rad},+}>\lambda_1\), is simple, and its maximizers are radial polynomials \(c_0+c_1\lVert x\rVert^2\).

For an actual thin spherical shell with squared-radius interval \(E_{z,\varepsilon}=[z-\varepsilon,z+\varepsilon]\subset(0,1)\), there exist, for each fixed \(d\), exactly two transitions \(z_-(\varepsilon)<z_+(\varepsilon)\) for all sufficiently small \(\varepsilon>0\). The maximizing space is linear between the transitions, radial outside, and has the boundary degeneracies above. Writing \(\mu=a/(a+1)\) and \(\tau=(a+1)/(a+2)\), the thresholds satisfy
\[
\boxed{\begin{aligned}
z_-(\varepsilon)&=\mu-\frac{a-1}{3\mu}\varepsilon^2+O_d(\varepsilon^4),\\
z_+(\varepsilon)&=\tau-\frac{a}{3\tau}\varepsilon^2+O_d(\varepsilon^4).
\end{aligned}}
\]
The limiting squared-radius window is \(\tau-\mu=4/((d+2)(d+4))\), shrinking at order \(d^{-2}\).

Finally, in \(d=2\), the **nonconstant sharp radial indicator**
\[
h(t)=\mathbf1_{[0,u]\cup[1/2,v]}(t),\quad
u=\frac{1-1/\sqrt2}{2},\quad v=\frac{1+1/\sqrt2}{2}
\]
(where \(u\) is the lower endpoint just defined) satisfies
\[
\boxed{\int_{\mathbb B^2}h(\lVert x\rVert^2)|f(x)|^2\,dx
=\tfrac12\int_{\mathbb B^2}|f(x)|^2\,dx
\quad\forall f\in\Pi_2^2.}
\]
Thus a nontrivial union of a central disk and an annulus is indistinguishable, at the quadratic concentration-operator level, from the constant half-transmission mask.

## Assumptions and scope
The norm and integrals are over the real unit ball (not the complex ball); polynomial coefficients may be complex. The symbol \(h\) is radial, measurable, satisfies \(0\le h\le1\) almost everywhere and \(b_0>0\). The indicator specialization uses a radial measurable set and normalizes Lebesgue measure by the ball volume. Boundary statements refer to the two comparisons among the three moments \(b_0,b_1,b_2\); the scalar mask case is allowed. Thin-shell thresholds apply for each fixed dimension and sufficiently small strictly positive squared-radius half-width; the error terms do not assert uniformity in growing dimension. Homogeneous degree-two polynomials include \(\lVert x\rVert^2\) as well as traceless quadratic harmonics.

## Proof
**1. Angular decomposition and exact multiplicities.** Put \(t=\lVert x\rVert^2\) and \(x=r\theta\). The pushforward of probability measure on \(\mathbb B^d\) under \(x\mapsto t\) has density \(a t^{a-1}\); \(\theta\) is uniform on the sphere and independent of \(t\). The orthogonal decomposition
\[
\Pi_2^d=\operatorname{span}\{1,t\}
\oplus\operatorname{span}\{x_1,\ldots,x_d\}
\oplus\mathcal H_2(\mathbb R^d)
\]
remains orthogonal after multiplication by a radial weight. Here \(\mathcal H_2\) is the space of homogeneous harmonic quadratics, equivalently traceless symmetric forms. Spherical orthogonality and homogeneity show that the first block has Gram matrices \(M,B\), the linear block is scalar with ratio \(b_1/\mu\), and the traceless quadratic block scalar with ratio \(b_2/\nu\). Its dimension is \(d(d+1)/2-1\). This proves the complete spectrum.

**2. The exact two-moment phase test.** The polynomial \(t\) itself belongs to the radial block and has concentration \(b_2/\nu=\lambda_2\). Hence \(\lambda_{\mathrm{rad},+}\ge\lambda_2\). More decisively, substituting \(\lambda_1=b_1/\mu\) yields the *diagonal identity*
\[
\boxed{\quad B-\lambda_1M=
\begin{pmatrix}b_0-\lambda_1&0\\0&b_2-\nu\lambda_1\end{pmatrix}.\quad}
\]
Since \(M\) is positive definite (\(\nu-\mu^2>0\)), the generalized Rayleigh maximum of the radial block is at most \(\lambda_1\) if and only if both diagonal entries are nonpositive. As \(b_0,b_1>0\), these are exactly \(b_1/b_0\ge\mu\) and \(b_2/b_1\le\nu/\mu\). The latter implies \(\lambda_2\le\lambda_1\), so these conditions are necessary and sufficient for linear maximality. Strict inequalities make \(B-\lambda_1M\) negative definite, so the linear eigenspace is exactly the complete optimizer space.

If only the first entry vanishes, the radial null vector is the constant polynomial \(1\); if only the second vanishes, it is \(t\), while \(\lambda_2=\lambda_1\), so the other degree-two harmonic modes also maximize. If both vanish, \(B=\lambda_1M\), and both remaining angular blocks equal \(\lambda_1\); the whole operator is scalar. Conversely, when the weak conditions fail, \(B-\lambda_1M\) has a strictly positive diagonal entry, so the radial maximum strictly exceeds \(\lambda_1\). Its eigenvalue is then simple: if both generalized radial eigenvalues coincided, \(B=cM\), forcing both phase comparisons to equality, a contradiction. These arguments prove all cases.

For complete computational reproducibility, set \(\Delta=\nu-\mu^2>0\), \(T=(\nu b_0+b_2-2\mu b_1)/\Delta\), and \(D=(b_0b_2-b_1^2)/\Delta\). Then the radial eigenvalues are \((T\pm\sqrt{T^2-4D})/2\), so no implicit spectral operator remains to be evaluated.

**3. Two genuine transitions for finite thin shells.** For \(h=\mathbf1_{E_{z,\varepsilon}}\),
\[
b_j(z,\varepsilon)=\frac{a}{a+j}
\big((z+\varepsilon)^{a+j}-(z-\varepsilon)^{a+j}\big).
\]
The ratios \(F=b_1/b_0\) and \(G=b_2/b_1\) are conditional means of \(t\) on a sliding interval for the positive weights \(a t^{a-1}\) and \(a t^a\), respectively. Each is strictly increasing in \(z\): differentiating a quotient of integrals on \([z-\varepsilon,z+\varepsilon]\), its numerator is the sum of positive terms \(w(z+\varepsilon)(z+\varepsilon-\mathbb E[t])\) and \(w(z-\varepsilon)(\mathbb E[t]-(z-\varepsilon))\). On compact subsets of \((0,1)\), \(F,G\to z\) uniformly as \(\varepsilon\downarrow0\). Since \(0<\mu<\tau<1\), for all sufficiently small \(\varepsilon\), the two equations \(F(z_-,\varepsilon)=\mu\), \(G(z_+,\varepsilon)=\tau\) have unique roots with \(z_-<z_+\). The phase test gives the asserted exact order and eigenspaces. A Taylor expansion of the two weighted conditional means gives
\[
F(z,\varepsilon)=z+\frac{a-1}{3z}\varepsilon^2+O_d(\varepsilon^4),\qquad
G(z,\varepsilon)=z+\frac{a}{3z}\varepsilon^2+O_d(\varepsilon^4),
\]
locally uniformly away from \(z=0\); implicit substitution gives the threshold expansions. Direct algebra gives \(\tau-\mu=4/((d+2)(d+4))\).

**4. Exact masked-disk camouflage.** At \(d=2\), \(a=1\) and \(t\) is uniform on \([0,1]\). Put \(u=(1-1/\sqrt2)/2\) and \(v=(1+1/\sqrt2)/2\). Then \(u+v=1\), \(uv=1/8\); hence \(u^2+v^2=3/4\) and \(u^3+v^3=5/8\). Integrating \(1,t,t^2\) over \([0,u]\cup[1/2,v]\) gives respectively \(1/2,1/4,1/6\), exactly one half of their full-interval moments \(1,1/2,1/3\). Therefore \(B=\frac12M\), \(\lambda_1=\lambda_2=1/2\), and every polynomial has exactly half its energy in the nonconstant masked region.

## Verification
The accompanying standalone `check.py` independently checks the exact sector diagonal identity for hundreds of rational radial unions, reconstructs the full six-dimensional quadratic polynomial Gram spectrum on the disk directly from monomial integrals, checks the nontrivial disk indicator through exact radicals, and solves the two transition equations with high-precision arithmetic in several dimensions. Its output is in `check_output.txt`; these finite tests support arithmetic reliability, while the proof above establishes the universal statements.

## Relationship to prior work
Huang's original arXiv preprint (7 August 2023) introduced multivariate polynomial Slepian concentration on balls and explicitly posed best concentration as a problem distinct from its high-bandwidth eigenvalue-distribution results (version 1, §5.1). The expanded Gerhards–Huang paper studies radial-angular bandwidth geometry, asymptotic eigenvalue distributions, and illustrative tesseroid computations. Its full HTML text, including finite-matrix numerical methods, was compared; it does not supply the present degree-two all-mask moment criterion, exact optimizer multiplicities, two thin-shell crossings, or nonconstant spectral camouflage. The standard spherical-harmonic/Zernike decomposition and the general variational principle are not claimed as new.

Dai–Mahajan's annular-Zernike analysis concerns orthogonal wavefront expansions and turbulence on annular pupils, rather than equality of sharp concentration energies in the fixed full-disk quadratic polynomial band. Earlier Fourier–Bessel/Fourier–Laguerre Slepian concentration on balls uses different spectral spaces. Analogous single-mode Zernike aperture comparisons do not imply a global mixed-degree maximizer classification for arbitrary disconnected radial masks. Priority beyond the inspected sources cannot be certified without independent literature review.

## Limitations
This is a degree-at-most-two theorem, not a classification for arbitrary polynomial degree or nonradial masks. The generic simplicity statement applies only to the winning radial eigenvalue outside the linear-maximizing phase, not to every spectral eigenvalue. The two thin-shell threshold expansions are dimensionwise, not uniform as dimension grows. The exact scalar example is constructed explicitly in dimension two; existence in all dimensions is not asserted. Published literature might contain an equivalent low-degree radial moment classification not located in the searches performed. Scientific review here is self-review only; no independent audit has been performed.

## References
1. X. Huang, *Slepian concentration problem for polynomials on the unit Ball*, arXiv:2308.03543v1, first submitted 7 August 2023, §§2, 5.1. https://arxiv.org/html/2308.03543v1
2. C. Gerhards and X. Huang, *Spatiospectral localization within the ball—studies on the influence of the spectral shape*, arXiv:2308.03543v5, §2 and §§3, 7–8. https://arxiv.org/html/2308.03543v5
3. Z. Khalid, R. A. Kennedy and J. D. McEwen, *Slepian Spatial-Spectral Concentration on the Ball*, Appl. Comput. Harmon. Anal. 40 (2016), 470–504. https://arxiv.org/abs/1403.5553
4. G.-M. Dai and V. N. Mahajan, *Zernike annular polynomials and atmospheric turbulence*, J. Opt. Soc. Am. A 24 (2007), 139–155. https://doi.org/10.1364/JOSAA.24.000139
