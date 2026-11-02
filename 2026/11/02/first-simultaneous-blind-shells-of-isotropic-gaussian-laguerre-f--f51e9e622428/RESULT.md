# First simultaneous blind shells of isotropic Gaussian–Laguerre filters and the sharp integrability threshold

## Finding
Fix an integer \(d\geq1\) and put \(N=2d\). For \(n\in\{0,1,2,3,4\}\), consider the Schwartz convolution operator \(G_{d,n}\) on \(L^p(\mathbb R^N)\), \(1\leq p\leq\infty\), with Euclidean Fourier multiplier
\[
 m_{d,n}(\xi)=\binom{n+d-1}{n}^{-1}e^{-|\xi|^2/4}L_n^{(d-1)}(|\xi|^2/2).
\]
For distinct \(i,j\in\{0,1,2,3,4\}\), the joint map \(f\mapsto(G_{d,i}f,G_{d,j}f)\) is injective on every \(L^p\), except possibly for precisely these two triples:
\[
 (d,i,j)=(6,1,4)\quad\text{or}\quad(24,2,4).
\]
For either exceptional triple, its entire joint kernel on every \(L^p\) is, respectively,
\[
 \{f\in L^p(\mathbb R^{12}):(-\Delta-12)f=0\},\qquad
 \{f\in L^p(\mathbb R^{48}):(-\Delta-60)f=0\},
\]
with the differential equations understood distributionally. The joint map in the two exceptional cases is injective exactly for
\[
 1\leq p\leq\frac{4d}{2d-1};
\]
for larger \(p\), including \(p=\infty\), the joint kernel is nonzero. The endpoints are \(24/11\) for \(d=6\) and \(96/47\) for \(d=24\).

In particular, every pair among levels \(0,1,2,3\) is jointly injective on all \(L^p\) in every dimension, whereas level \(4\) is the first level that can produce a simultaneous blind frequency sphere with a lower level. The exceptional Euclidean frequency spheres are \(|\xi|=\sqrt{12}\) and \(|\xi|=\sqrt{60}\), respectively.

## Assumptions and scope
The generalized Laguerre polynomials use the normalization
\[
 L_n^{(\alpha)}(s)=\sum_{k=0}^n(-1)^k\binom{n+\alpha}{n-k}\frac{s^k}{k!},\qquad\alpha=d-1\in\mathbb Z_{\geq0}.
\]
The Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R^N}f(x)e^{-ix\cdot\xi}\,dx\), extended to tempered distributions. A Schwartz inverse transform of \(m_{d,n}\) defines \(G_{d,n}\) by convolution for every \(p\in[1,\infty]\). Equality of outputs means equality of the resulting functions almost everywhere. No positivity of the convolution kernel is required.

These multipliers are not an arbitrarily selected polynomial test: their radial Laguerre structure is the normalized Weyl characteristic function of the isotropic \(n\)-excitation shell of a \(d\)-mode oscillator, after the standard identification of phase space with \(\mathbb R^{2d}\). More explicitly, the product of one-mode Laguerre generating functions gives
\[
 \sum_{|\boldsymbol\nu|=n}\prod_{h=1}^d L_{\nu_h}^{(0)}(s_h)
 =L_n^{(d-1)}\!\left(\sum_{h=1}^d s_h\right).
\]
The scalar normalization is the shell multiplicity \(\binom{n+d-1}{n}\). The assertion is about the explicitly defined classical convolution maps, **not** about higher-dimensional polyanalytic Toeplitz operators or arbitrary quantum observables.

## Proof
**1. Joint kernels reduce to a polynomial greatest common divisor.** Let \(s=|\xi|^2/2\) and \(P_n(s)=L_n^{(d-1)}(s)\). The Gaussian factor and the normalization in each multiplier are smooth and everywhere nonzero. If both convolutions vanish for \(f\in L^p\), Fourier transformation gives \(P_i(s)\widehat f=P_j(s)\widehat f=0\) in \(\mathcal D'(\mathbb R^N)\). The removal of the Gaussian is justified by local multiplication by its smooth reciprocal; no globally tempered reciprocal is invoked. Because polynomial multiplication of a tempered distribution is tempered, the resulting identities also hold in \(\mathcal S'\). Bézout's identity in the single variable \(s\) shows that the joint kernel equals the kernel of \(\gcd(P_i,P_j)(|\xi|^2/2)\) acting on \(\widehat f\). Conversely, such a greatest-common-divisor equation implies both multiplier equations, so this equivalence is exact.

**2. All ten polynomial pairs are classified for every dimension.** Set \(a=d-1\). Direct exact polynomial elimination gives the following resultants; each line refers to \(\operatorname{Res}_s(L_i^{(a)},L_j^{(a)})\):
\[
\begin{aligned}
 R_{0,1}=R_{0,2}=R_{0,3}=R_{0,4}&=1,\\
 R_{1,2}&=-(a+1)/2,\\
 R_{1,3}&=-2(a+1)/3,\\
 R_{1,4}&=(a-5)(a+1)/8,\\
 R_{2,3}&=-(a+1)(a+2)^2/72,\\
 R_{2,4}&=(a-23)(a+1)(a+2)^2/2304,\\
 R_{3,4}&=(a+1)(a+2)^2(a+3)^3/165888.
\end{aligned}
\]
They follow by substituting the displayed degree-at-most-four coefficient formula into the Sylvester determinants. The standalone exact-arithmetic script independently recomputes each determinant, not just its zeros. Because \(a\) is an integer at least zero, the only vanishing resultants are \((a,i,j)=(5,1,4)\) and \((23,2,4)\). The corresponding factors are
\[
\begin{aligned}
 L_1^{(5)}(s)&=6-s,\\
 L_4^{(5)}(s)&=(s-6)(s^3-30s^2+252s-504)/24,\\
 L_2^{(23)}(s)&=(s-20)(s-30)/2,\\
 L_4^{(23)}(s)&=(s-30)(s^3-78s^2+1872s-14040)/24.
\end{aligned}
\]
Euclidean polynomial division yields a monic greatest common divisor equal to \(s-6\) in the first case and \(s-30\) in the second. All other pairs have greatest common divisor \(1\).

**3. The exact blind spaces are Helmholtz eigenspaces.** In the first exceptional case, \((|\xi|^2/2-6)\widehat f=0\) is equivalent to \(( -\Delta-12)f=0\), and in the second \((|\xi|^2/2-30)\widehat f=0\) is equivalent to \((-\Delta-60)f=0\). The factors are simple, so the Fourier equations involve the first power of the Helmholtz polynomial, not its higher powers. For instance \(f(x)=e^{i\sqrt{12}x_1}\) and \(f(x)=e^{i\sqrt{60}x_1}\), respectively, give bounded nonzero joint-kernel elements.

**4. The sharp \(L^p\) threshold.** Consider a nonzero distributional solution of \(( -\Delta-\kappa^2)f=0\) in \(L^p(\mathbb R^N)\), where \(N\geq2\) and \(\kappa>0\). Elliptic regularity makes \(f\) smooth. At least one spherical harmonic coefficient is nonzero and, by separation of variables and regularity at the origin, must equal a nonzero constant times
\[
 r^{-(N-2)/2}J_{\ell+(N-2)/2}(\kappa r).
\]
Hölder's inequality on the unit sphere bounds the angular \(L^p\) norm below by a positive constant times the absolute value of that coefficient. The fixed-order Bessel asymptotic is a nonzero cosine times \(r^{-(N-1)/2}\), up to \(O(r^{-(N+1)/2})\). On a positive fraction of every sufficiently distant oscillation period, its magnitude is bounded below by a constant multiple of \(r^{-(N-1)/2}\). Consequently, the radial \(L^p\) integral diverges if
\[
 N-1-\frac{p(N-1)}{2}\geq-1,
 \quad\text{equivalently}\quad p\leq\frac{2N}{N-1}.
\]
The endpoint diverges logarithmically. This proves the zero-kernel assertion for these finite exponents.

For the converse let \(d\sigma\) be normalized surface measure on \(S^{N-1}\) and set
\[
 H_\kappa(x)=\int_{S^{N-1}}e^{i\kappa x\cdot\omega}\,d\sigma(\omega)
 =\Gamma(N/2)\left(\frac{2}{\kappa|x|}\right)^{N/2-1}J_{N/2-1}(\kappa|x|),
\]
where the continuous value at the origin is \(1\). It is a nonzero Helmholtz solution, is bounded, and has decay \(O((1+|x|)^{-(N-1)/2})\). Therefore it belongs to \(L^p\) for every finite \(p>2N/(N-1)\) and also to \(L^\infty\). With \(N=2d\), the critical exponent is \(4d/(2d-1)\), proving the assertion for the two exceptional dimensions and completing the proof.

## Verification
Run `python checks/check_claim.py` after installing the single dependency in `checks/requirements.txt`. Its exact rational computations check every resultant, the two exceptional monic polynomial greatest common divisors, simplicity at the common roots, the shell-multiplicity normalization, and the stated rational exponents. The code does not claim to check the analytical Fourier-distribution argument or the Bessel/Helmholtz integrability theorem; those steps are proved above using standard Fourier calculus, separation of variables, and fixed-order Bessel asymptotics. The full theorem quantifies over every integer \(d\geq1\), every listed level pair, and every \(1\leq p\leq\infty\), not merely sampled dimensions.

## Relationship to prior work
Hanin and Zelditch (2019), Proposition 1.2, write isotropic oscillator eigenspace Wigner distributions in terms of \(L_n^{(d-1)}\); their results concern Wigner-function and interface asymptotics, not exact two-filter injectivity. Fulsche and Hagger (2023 preprint), Section 3, especially Theorem 3.4, characterize the kernel of a single true-polyanalytic Toeplitz quantization in one complex variable using ordinary Laguerre zero circles. The present scalar convolution problem instead combines distinct isotropic oscillator shells, varies the oscillator dimension, and identifies the first pairs with a common spherical zero together with their exact \(L^p\) nullspaces. Arvesú, Driver and Littlejohn (2020), Sections 1–3, analyze interlacing with different Laguerre parameters; the same-parameter, low-level resonance classification above is not asserted in those sections. Driver and Muldoon (2015) study common Laguerre zeros and may contain related algebraic identities; its full article was not inspected, so indirect priority coverage of the resultant identities remains a limitation. The proof relies on standard Laguerre algebra and classical Bessel asymptotics and makes no claim that either ingredient itself is new.

## Limitations
The finite-degree cutoff is \(n\leq4\); nothing here classifies all higher oscillator levels, other radial families, or Toeplitz compression in several complex variables. The exceptional joint kernels are identified as **all** \(L^p\) distributional solutions of the stated Helmholtz equations, not as finite plane-wave spans. Uniqueness of a scientific result cannot be established by failure of an indexed search; the algebraic coincidences may have been recorded in older polynomial-zero literature, and the exact synthesis of the two-filter and \(L^p\) statements merits independent historical and mathematical review. Finite symbolic calculations are auxiliary exact certificates, not substitutes for the infinite-dimensional proof.

## References
- R. Fulsche and R. Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces*, arXiv:2308.11292 (first submitted 2023-08-22), Section 3, Theorem 3.4. https://arxiv.org/abs/2308.11292
- B. Hanin and S. Zelditch, *Interface Asymptotics of Eigenspace Wigner distributions for the Harmonic Oscillator*, arXiv:1901.06438 (2019), Proposition 1.2. https://arxiv.org/abs/1901.06438
- J. Arvesú, K. Driver and L. Littlejohn, *Interlacing of zeros of Laguerre polynomials of equal and consecutive degree*, arXiv:2009.10206 (2020), Sections 1–3. https://arxiv.org/abs/2009.10206
- K. Driver and M. E. Muldoon, *Common and interlacing zeros of families of Laguerre polynomials*, Journal of Approximation Theory 193 (2015), 89–98, DOI:10.1016/j.jat.2013.11.013 (abstract checked; full text not inspected).
- NIST Digital Library of Mathematical Functions, chapters on Bessel functions and their large-argument asymptotics. https://dlmf.nist.gov/10.17
