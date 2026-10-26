# Gaussian harmonic trinomials: a one-crossing valence law and its logarithmic large-degree correction

## Finding
Fix an integer \(n\ge2\) and independent standard circular complex Gaussians \(A,B\), normalized by \(\mathbb E|A|^2=\mathbb E|B|^2=1\). For \(s>0\) let
\[
H_{n,s}(z)=z^n+sA\overline z+B,
\qquad N_{n,s}=\#\{z\in\mathbb C:H_{n,s}(z)=0\}.
\]
Put \(q_n=n/(n-1)\), \(r_n=n^{-1/(n-1)}\), and let \(D_n\) be the bounded domain enclosed by the clockwise hypocycloid
\[
\gamma_n(t)=r_n\left(e^{-it}+n^{-1}e^{int}\right),\qquad 0\le t\le2\pi.
\]
Write \(\rho_n(\theta)>0\) for its radial function. Let \(R=|B|\), \(X=|A|^2\), and let \(\Theta\) be a uniform angle independent of \(R,X\). Define
\[
T_n=\frac{(R/\rho_n(\Theta))^{1/q_n}}{\sqrt X}.
\]
There is a coupling with these distributions under which, almost surely and simultaneously for all \(s\ne T_n\),
\[
N_{n,s}=n+2\mathbf1_{\{s>T_n\}}.
\]
Consequently the maximal-valence probability is exactly
\[
p_n(s):=\mathbb P(N_{n,s}=n+2)
=\frac1{2\pi}\int_0^{2\pi}\int_0^\infty
\exp\!\left[-x-\frac{x^{1/q_n}}{s^2\rho_n(\theta)^{2/q_n}}\right]dx\,d\theta.
\tag{1}
\]
It is strictly increasing from zero to one; \(\mathbb E N_{n,s}=n+2p_n(s)\) and \(\operatorname{Var}(N_{n,s})=4p_n(s)(1-p_n(s))\). Its transition threshold has the exact Mellin-moment law
\[
\mathbb E T_n^p=\Gamma\left(1+\frac{p}{2q_n}\right)
\Gamma\left(1-\frac p2\right)
\frac1{2\pi}\int_0^{2\pi}\rho_n(\theta)^{-p/q_n}\,d\theta,
\qquad -2q_n<p<2,\tag{2}
\]
with infinite moments beyond those strict endpoints. In particular, \(\mathbb ET_n<\infty\) but \(\mathbb ET_n^2=\infty\).

For fixed \(n\), the weak-coupling law has two explicit nonzero coefficients:
\[
p_n(s)=a_ns^{2q_n}-b_ns^{4q_n}+O_n(s^{6q_n})\quad(s\downarrow0),\tag{3}
\]
\[
a_n=\left(1-\frac1n\right)r_n^2\Gamma(1+q_n),\qquad
b_n=\frac{r_n^4}2\left(1-\frac{2(n-1)}{n^2}-\frac1{n^3}\right)\Gamma(1+2q_n).
\]
The strong-coupling law is
\[
p_n(s)=1-\frac{c_n}{s^2}+\frac{d_n}{2s^4}+O_n(s^{-6})\quad(s\to\infty),\tag{4}
\]
where \(c_n=\Gamma(1+1/q_n)\langle\rho_n^{-2/q_n}\rangle\), \(d_n=\Gamma(1+2/q_n)\langle\rho_n^{-4/q_n}\rangle\), and \(\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f(\theta)d\theta\).

Most notably, **for fixed positive coupling \(s\)** the maximal-valence probability has the refined high-degree expansion
\[
\boxed{\displaystyle
p_n(s)=\frac{s^2}{1+s^2}
-\frac{s^2}{n(1+s^2)^2}
\left[2\log n+\gamma+\log(1+s^{-2})\right]
+O_{\delta,\Delta}\!\left(\frac{(\log n)^2}{n^2}\right),}\tag{5}
\]
uniformly for \(\delta\le s\le\Delta\), for every fixed \(0<\delta<\Delta<\infty\). Here \(\gamma\) is Euler's constant. Hence \(p_n(s)\to s^2/(1+s^2)\), with an explicit negative logarithmic finite-degree correction.

## Assumptions and scope
The random coefficients are independent, centered, isotropic complex Gaussian variables of unit second moment; the leading analytic coefficient is deterministic and equal to one. All counts concern distinct complex zeros and all stated zero counts hold away from critical target values, an almost-sure event at each fixed \(s\). The transition is asserted jointly in \(s\) away from the single random critical parameter; no count is specified at \(s=T_n\). Degrees are integers \(n\ge2\). All implicit constants in (3) and (4) may depend on the fixed degree; in (5) they may depend on the compact coupling interval but not on \(n\).

The radial function and all coefficients are computable by a single smooth periodic integral. For \(u\in[0,2\pi]\) define
\[
\rho_{n,u}=\frac{r_n}{n}\sqrt{n^2+2n\cos u+1},\qquad
W_n(u)=\frac{n(n-1)(1-\cos u)}{n^2+2n\cos u+1}.
\tag{6}
\]
Then, for every continuous function \(F\),
\[
\langle F(\rho_n)\rangle=\frac1{2\pi}\int_0^{2\pi}W_n(u)F(\rho_{n,u})\,du.
\tag{7}
\]
In particular, no numerical inversion of a cusped curve is needed to reproduce the stated formulae.

## Proof
**1. One reversing preimage and the hypocycloid.** For \(f_n(z)=z^n+\overline z\), the Jacobian equals \(J_{f_n}(z)=n^2|z|^{2n-2}-1\), so the reversing locus is the open disk \(|z|<r_n\). If \(|z|,|w|\le r_n\) and \(z\ne w\), the factorization of \(z^n-w^n\) gives
\[
|z^n-w^n|\le\sum_{j=0}^{n-1}|z|^{n-1-j}|w|^j|z-w|\le|z-w|.
\]
The inequality is strict unless both points lie on the critical circle. For boundary points, direct examination of the parametrization below supplies injectivity. Thus \(f_n\) is injective on the closed reversing disk.

Parameterize that critical circle by \(z=r_ne^{it}\); its image is exactly \(\gamma_n(t)\). With \(u=(n+1)t\), the polar-angle derivative satisfies
\[
-\frac{d}{dt}\arg\gamma_n(t)=W_n(u)
=\frac{n(n-1)(1-\cos u)}{n^2+2n\cos u+1}\ge0.
\]
The angular derivative is strictly negative away from finitely many cusp parameters and the curve never reaches zero, since \(|\gamma_n(t)|\ge r_n(1-1/n)>0\). It completes one clockwise turn, hence traces a simple star-shaped Jordan curve and establishes (6)–(7). The reversing disk is mapped homeomorphically onto \(\overline D_n\), with exactly one reversing preimage for each target in \(D_n\) and none outside \(\overline D_n\). The planar topological degree at infinity is \(n\): on sufficiently large circles the leading analytic term \(z^n\) dominates the conjugate term. At every regular target, the number of preserving preimages minus the number of reversing preimages is therefore \(n\). It follows that the full number of preimages is \(n+2\) inside \(D_n\), and \(n\) outside \(\overline D_n\). This deterministic count is a specialized instance of existing harmonic argument-principle and caustic results [1,2,3], **not** an assertion of a new deterministic valence theorem.

**2. Gaussian transition and moment law.** For \(A=|A|e^{i\psi}\ne0\), substitute
\[
z=(s|A|)^{1/(n-1)}e^{i\psi/(n+1)}\zeta.
\]
Then \(z^n+sA\overline z=(s|A|)^{q_n}e^{in\psi/(n+1)}(\zeta^n+\overline\zeta)\). Because \(-B\) is isotropic and independent, its effective target has an independent uniform angle \(\Theta\) and radius \(R/(s|A|)^{q_n}\). By star-shapedness, it belongs to \(D_n\) precisely when \(R<s^{q_n}X^{q_n/2}\rho_n(\Theta)\). This is equivalent to \(s>T_n\). A single threshold works jointly over positive \(s\) for every realization except the null event \(A=0\) or \(B=0\). The independent variables \(R^2,X\) are unit-rate exponentials. Conditioning on \(R,\Theta\) gives (1), and independence gives (2), since \(\mathbb E R^t=\Gamma(1+t/2)\) for \(t>-2\) and \(\mathbb E X^v=\Gamma(1+v)\) for \(v>-1\). The bounded positive radial function does not change these sharp moment cutoffs. Strict monotonicity is immediate from (1).

**3. Exact area and inertia; two coupling regimes.** Let \(a=r_n\), \(b=r_n/n\), and set \(w(z)=az^{-1}+bz^n\) on \(|z|=1\). The oriented curve is clockwise; the residue form of Green's theorem gives
\[
|D_n|=-\pi\operatorname{Res}_{z=0}(\overline{w(z)}w'(z))
=\pi(a^2-nb^2)
=\pi r_n^2(1-1/n),
\]
where on the unit circle \(\overline{w(z)}=az+bz^{-n}\). Similarly,
\[
\int_{D_n}|w|^2\,dA(w)
=-\frac\pi2\operatorname{Res}_{z=0}(w(z)\overline{w(z)}^2w'(z))
=\frac\pi2\left(a^4-2(n-1)a^2b^2-nb^4\right).
\]
For a fixed scale \(t>0\), the Gaussian area mass of \(tD_n\) is \(\pi^{-1}\int_{tD_n}e^{-|w|^2}dA(w)\). Taylor's formula, the two geometric identities, and the integrable third residual term, averaged with \(t=(s|A|)^{q_n}\), yield (3) with its stated \(O_n(s^{6q_n})\) bound. For (4), use the equivalent conditional expectation \(p_n(s)=\mathbb E\exp[-(R/\rho_n(\Theta))^{2/q_n}/s^2]\) and Taylor's formula with a bounded third-moment remainder for \((R/\rho_n(\Theta))^{2/q_n}\). All **nonnegative moments of this latter variable** exist, because \(R\) has Rayleigh tails and \(\rho_n\) is bounded away from zero. This is compatible with the divergent second moment of the *different* variable \(T_n\) in (2).

**4. The logarithmic finite-degree correction.** With \(X=|A|^2\), a second form of the exact probability is
\[
p_n(s)=1-\frac1{2\pi}\int_0^{2\pi}W_n(u)
\int_0^\infty\exp[-x-s^{2q_n}x^{q_n}\rho_{n,u}^2]dx\,du.
\tag{8}
\]
Uniformly in \(u\),
\[
q_n=1+\frac1n+O(n^{-2}),\quad
\log\rho_{n,u}^2=\frac{-2\log n+2\cos u}{n}
+O\!\left(\frac{\log n+1}{n^2}\right),\quad
W_n(u)=(1-\cos u)+O(n^{-1}).
\]
For fixed \(s\) in a compact subset of \((0,\infty)\), Taylor-expand the inner exponential at \(e^{-s^2x}\). The first variation of its negative exponent is
\[
\frac{s^2x}{n}\left(2\log s+\log x-2\log n+2\cos u\right).
\]
Integration against \(e^{-(1+s^2)x}\) is justified uniformly by the integrability of \(x^v(1+|\log x|)^2e^{-x}\) for \(v\) in a neighborhood of one; the second-order integrated remainder is bounded by \(C_{\delta,\Delta}(\log n)^2/n^2\). Use the exact identities
\[
\frac1{2\pi}\int_0^{2\pi}(1-\cos u)\cos u\,du=-\frac12,
\qquad
\int_0^\infty xe^{-kx}\log x\,dx=\frac{1-\gamma-\log k}{k^2}.
\]
The zeroth-order integral is \(1/(1+s^2)\); the displayed variation is
\[
\frac{s^2}{n(1+s^2)^2}\left(2\log s-2\log n-\gamma-\log(1+s^2)\right).
\]
Rearrangement gives (5), including the compact-uniform remainder.

## Verification
The attached standalone checker `CHECKER.py` (Python 3, NumPy and SciPy) evaluates (1) independently by conditioning on \(A\) and on \(B\), confirms (7) and the residue-derived geometric moments, checks the exact quadratic coefficients \(a_2=1/4\), \(b_2=9/32\), and compares the finite-degree asymptotic with direct quadrature for degrees up to \(250\), and numerically enumerates zeros for degrees \(2,3,4\) at interior and exterior regular targets. It completed 64 numerical consistency assertions. Its numerical tests are corroboration; the proof of the all-degree and asymptotic statements is analytical and appears above.

## Relationship to prior work
The deterministic preimage-count method and geometry are standard in the cited harmonic-map literature. Brilleslyper et al. [2] prove zero-count transitions for harmonic trinomials with real coefficients; Brooks et al. [3] extend them to complex coefficients. Sète and Zur [1] develop a general caustic-based count. Consequently **neither the hypocycloid representation nor the bare \(n\) versus \(n+2\) alternative is claimed as new**. The contribution here is the explicit Gaussian-random transition law with its complete moment spectrum, two-sided coupling asymptotics and particularly the universal rational high-degree crossover with its explicit negative \((\log n)/n\) correction. Lundberg [4] and Lundberg–Thomack [5] address harmonic polynomial zero counts through different probabilistic constructions and Gaussian ensembles; they do not state this sparse-coefficient distribution. These comparisons do not establish absolute historical priority.

## Limitations
Only a monic leading analytic term and one anti-analytic linear random term are covered; arbitrary random leading coefficients and higher coanalytic degrees are not covered. The zero count is not assigned at the singular transition, and no claim is made about the spatial distribution of individual roots or the joint law for distinct degrees. Formula (5) is uniform only on compact positive coupling intervals, not through \(s=0\) or \(s=\infty\). Novelty is provisional pending independent literature review, especially for equivalent probabilistic formulations of deterministic caustic geometry.

## References
[1] O. Sète and J. Zur, *Number and location of pre-images under harmonic mappings in the plane*, arXiv:1908.08759 (first public 2019-08-23), https://arxiv.org/abs/1908.08759.

[2] M. Brilleslyper, J. Brooks, M. Dorff, R. Howell and L. Schaubroeck, *Zeros of a one-parameter family of harmonic trinomials*, Proc. Amer. Math. Soc. Ser. B **7** (2020), 82–90, doi:10.1090/bproc/51 (2020-06-17), https://doi.org/10.1090/bproc/51.

[3] J. Brooks, M. Dorff, A. Hudson, E. Pitts, C. Whiffen and A. Woodall, *Zeros of a family of complex-valued harmonic trinomials*, Bull. Malays. Math. Sci. Soc. **45** (2022), 1079–1091, doi:10.1007/s40840-021-01230-8, https://doi.org/10.1007/s40840-021-01230-8.

[4] E. Lundberg, *The valence of harmonic polynomials viewed through the probabilistic lens*, arXiv:2201.00788 (first public 2022-01-03), https://arxiv.org/abs/2201.00788.

[5] E. Lundberg and A. Thomack, *On the average number of zeros of random harmonic polynomials with i.i.d. coefficients: precise asymptotics*, arXiv:2308.10333 (first public 2023-08-20), https://arxiv.org/abs/2308.10333.
