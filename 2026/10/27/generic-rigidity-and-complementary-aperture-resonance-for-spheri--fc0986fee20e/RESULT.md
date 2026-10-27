# Generic rigidity and complementary-aperture resonance for spherical-cap covariance mixtures

## Finding

Let \(d\ge2\), and let \(\sigma\) be normalized surface measure on the unit sphere \(\mathbb S^d\). Given two angular radii \(0<r,s<\pi\), write
\[
B_{r,s}(x,y)=\int_{\mathbb S^d}\mathbf1_{\{\theta(x,z)\le r\}}\mathbf1_{\{\theta(y,z)\le s\}}\,d\sigma(z).
\]
For real \(a,b,c\), consider the symmetric two-aperture covariance candidate
\[
K_{a,b,c}^{r,s}(x,y)=aB_{r,r}(x,y)+2cB_{r,s}(x,y)+bB_{s,s}(x,y),
\qquad M=\begin{pmatrix}a&c\\c&b\end{pmatrix}.
\]
Here positive definite means positive semidefinite on every finite point set; *strictly* positive definite means all Gram matrices on distinct finite points are positive definite.

**Generic aperture rigidity.** If \(1,r/\pi,s/\pi\) are linearly independent over \(\mathbb Q\), then
\[
K_{a,b,c}^{r,s}\text{ is positive definite}\quad\Longleftrightarrow\quad M\succeq0,
\]
that is, \(a,b\ge0\) and \(ab\ge c^2\). Every nonzero admissible kernel is strictly positive definite. If \(M\not\succeq0\), strictly negative spherical-harmonic eigenvalues occur with the same positive natural density along the even degrees and along the odd degrees. This density has the exact formula in the proof below.

**Complementary-aperture resonance.** If \(s=\pi-r\), with \(0<r<\pi\) and \(r\ne\pi/2\), and \(v=\sigma\{z:\theta(x,z)\le r\}\), then
\[
K_{a,b,c}^{r,\pi-r}\text{ is positive definite}\quad\Longleftrightarrow\quad
 a+b\ge2|c|\quad\text{and}\quad av^2+2cv(1-v)+b(1-v)^2\ge0.
\]
It is strictly positive definite precisely when both weak inequalities hold and \(a+b>2|c|\). Thus the complementary aperture cone can properly contain indefinite mixing matrices: for instance, \(r=\pi/3\), \(s=2\pi/3\), and \((a,b,c)=(-1,2,0)\) give a strictly positive definite kernel on every \(\mathbb S^d\), \(d\ge2\), even though \(M\) is indefinite.

## Assumptions and scope

The sphere is embedded in \(\mathbb R^{d+1}\), \(\theta(x,y)=\arccos(x\cdot y)\), and all integrals use probability-normalized surface measure. The integer \(d\ge2\) is arbitrary but fixed for asymptotic and density statements. Cap boundaries have surface measure zero. All three mixing parameters are arbitrary real numbers, and no normalization of \(K(x,x)\) is imposed. In the generic theorem rational independence is an explicit hypothesis; complementary radii are treated separately. No conclusion is asserted for other arithmetically dependent pairs of radii, nor for \(d=1\).

## Proof

### Zonal cap multipliers

Set \(\lambda=(d-1)/2\) and \(\kappa_d=\Gamma((d+1)/2)/(\sqrt\pi\,\Gamma(d/2))\). The zonal operator \(T_r f(x)=\int\mathbf1_{\{\theta(x,z)\le r\}}f(z)\,d\sigma(z)\) is scalar on spherical harmonics of degree \(\ell\). By the Funk--Hecke formula its multiplier is
\[
m_\ell(r)=\frac{\kappa_d}{C_\ell^\lambda(1)}\int_0^r
 C_\ell^\lambda(\cos t)\sin^{2\lambda}t\,dt.
\]
For \(\ell=0\) this is the cap volume \(v_d(r)=\kappa_d\int_0^r\sin^{d-1}t\,dt\). For every integer \(\ell\ge1\), differentiating the Gegenbauer identity in the cited cap-convolution literature gives
\[
m_\ell(r)=\frac{\kappa_d}{C_\ell^\lambda(1)}
\frac{2\lambda}{\ell(\ell+2\lambda)}
(\sin r)^{2\lambda+1}C_{\ell-1}^{\lambda+1}(\cos r). \tag{1}
\]
This is also verified by differentiation and its vanishing at \(r=0\). In particular,
\[
m_1(r)=\frac{\kappa_d}{d}\sin^d r>0,
\qquad m_2(r)=\frac{\kappa_d}{d}\sin^d r\cos r.\tag{2}
\]
The kernel \(B_{r,s}\) is the kernel of \(T_rT_s\), by Fubini and symmetry. Consequently its degree-\(\ell\) eigenvalue is \(m_\ell(r)m_\ell(s)\), and the degree-\(\ell\) eigenvalue of the displayed mixture is
\[
\Lambda_\ell=a m_\ell(r)^2+2c m_\ell(r)m_\ell(s)+b m_\ell(s)^2
=Q_M(m_\ell(r),m_\ell(s)).\tag{3}
\]
The kernels are continuous (rotating a cap changes its indicator continuously in \(L^1\)). Spherical harmonic decomposition shows that every finite Gram matrix is positive semidefinite exactly when \(\Lambda_\ell\ge0\) for every \(\ell\ge0\). For the converse direction, a negative harmonic eigenvalue gives a negative integrated quadratic form, which is approximated by finite weighted point sums. As each cap indicator is in \(L^2\), \(\sum_\ell(\dim\mathcal H_\ell)m_\ell(r)^2<\infty\), so the expansions cause no convergence ambiguity.

### Oscillating multipliers and generic-radii density

A Darboux estimate for the Gegenbauer generating function
\[
\sum_{j\ge0}C_j^\mu(\cos r)z^j=(1-2z\cos r+z^2)^{-\mu}
\]
gives, for fixed \(\mu>1\) and \(0<r<\pi\),
\[
C_j^\mu(\cos r)=\frac{2^{1-\mu}}{\Gamma(\mu)}
 j^{\mu-1}(\sin r)^{-\mu}
\cos\!\left((j+\mu)r-\frac{\mu\pi}{2}\right)
+O_{\mu,r}(j^{\mu-2}).\tag{4}
\]
For completeness, factor the generating function as
\((1-ze^{ir})^{-\mu}(1-ze^{-ir})^{-\mu}\); singularity transfer at the two conjugate points contributes the conjugate leading terms in (4), while the first subleading transfers give the stated remainder. Substituting \(\mu=\lambda+1\), \(j=\ell-1\), and \(C_\ell^\lambda(1)=\Gamma(\ell+2\lambda)/(\Gamma(2\lambda)\Gamma(\ell+1))\) into (1) yields
\[
m_\ell(r)=A_d(r)\ell^{-\lambda-1}
\cos\!\left((\ell+\lambda)r-\frac{(\lambda+1)\pi}{2}\right)
+O_{d,r}(\ell^{-\lambda-2}),\tag{5}
\]
where the strictly positive amplitude is
\[
A_d(r)=\kappa_d\frac{2^{1-\lambda}\Gamma(2\lambda)}{\Gamma(\lambda)}
(\sin r)^\lambda.\tag{6}
\]
For a fixed nonzero matrix \(M\), define the explicit phase-area fraction
\[
\rho_d(M;r,s)=\frac{1}{4\pi^2}\int_0^{2\pi}\!\int_0^{2\pi}
\mathbf1_{\{Q_M(A_d(r)\cos u,A_d(s)\cos v)<0\}}\,du\,dv.\tag{7}
\]
Rational independence of \(1,r/\pi,s/\pi\) implies, by Weyl equidistribution, that the pair of phases in (5) is uniformly distributed on the two-torus even after restricting \(\ell\) to either parity. The zero locus of the nonzero trigonometric polynomial inside the indicator in (7) has area zero. Therefore the \(O(1/\ell)\) normalized remainder from (5) does not change the limiting fraction of negative \(\Lambda_\ell\). The exact limiting fraction equals (7), separately among even and odd indices.

If \(M\not\succeq0\), its quadratic form is strictly negative on an open cone. The rectangle attained by the two independent cosine coordinates contains points in that cone, so \(\rho_d(M;r,s)>0\). This forces infinitely many negative eigenvalues, establishing generic necessity. If \(M\succeq0\), (3) is nonnegative for all degrees, establishing sufficiency. Moreover when \(M\succeq0\) and \(M\ne0\), the positive set of \(Q_M\) has positive phase area, yielding infinitely many positive \(\Lambda_\ell\) of both parities. The classical strict-positivity criterion for zonal kernels on \(\mathbb S^d\), \(d\ge2\), then gives strict positive definiteness.

### Complementary apertures

For \(s=\pi-r\), the geometric cap identity, holding for almost every \(z\), is
\[
\mathbf1_{\{\theta(x,z)\le\pi-r\}}=1-\mathbf1_{\{\theta(-x,z)\le r\}}.
\]
Antipodal spherical harmonics have parity \((-1)^\ell\). Thus
\[
m_0(\pi-r)=1-v_d(r),\qquad m_\ell(\pi-r)=(-1)^{\ell+1}m_\ell(r)
\quad(\ell\ge1).\tag{8}
\]
Equation (3) becomes
\[
\Lambda_0=av^2+2cv(1-v)+b(1-v)^2,\qquad
\Lambda_\ell=(a+b+2(-1)^{\ell+1}c)m_\ell(r)^2 \quad(\ell\ge1).\tag{9}
\]
The first two positive-frequency multipliers are nonzero when \(r\ne\pi/2\), by (2), so their necessary restrictions are \(a+b+2c\ge0\) and \(a+b-2c\ge0\), equivalent to \(a+b\ge2|c|\). Together with \(\Lambda_0\ge0\), these are sufficient for all degrees. The three inequalities are therefore sharp and complete.

For strictness, if \(a+b>2|c|\), every nonzero \(m_\ell(r)\) yields a positive \(\Lambda_\ell\). The recurrence
\[
(j+1)C_{j+1}^{\lambda+1}(x)=2(j+\lambda+1)xC_j^{\lambda+1}(x)
 -(j+2\lambda+1)C_{j-1}^{\lambda+1}(x)
\]
shows that for \(x=\cos r\ne0\), two successive polynomials of the same parity cannot both vanish at \(x\): otherwise the intermediate polynomial also vanishes, contradicting the recurrence and \(C_0^{\lambda+1}(x)=1\). Hence each parity has infinitely many nonzero cap multipliers, and the spherical strict-positivity criterion applies. Conversely if \(a+b=2|c|\), one entire positive-degree parity of (9) vanishes, so strict positive definiteness fails. (The conclusion includes the case \(a+b=c=0\).)

Finally for \(r=\pi/3\), \(v_d(r)<1/2\) for every \(d\ge2\), since a cap of radius strictly less than a hemisphere has normalized area less than \(1/2\). For \((a,b,c)=(-1,2,0)\), equations (9) yield \(a+b=1>0\), and \(\Lambda_0=-v^2+2(1-v)^2>0\). This proves the stated indefinite-mixing example and completes the proof.

## Verification

The included standalone `CHECK.py` uses Python 3 with SciPy. Run `python CHECK.py` to compare (1) with independent numerical Funk--Hecke integrals, verify (8) across several dimensions and radii, inspect generic indefinite examples, and check the complementary negative-weight example for the first 99 positive degrees. The recorded tests comprise 128 integral comparisons and 1,050 antipodal-complement comparisons; their maximum observed absolute errors were approximately \(5.6\times10^{-17}\) each. They additionally inspect oscillatory multiplier asymptotics. These finite tests do not establish the theorem or prove infinite-degree positivity; the proof rests on (1), (4), Weyl equidistribution, and the parity argument.

## Relationship to prior work

Ziegel's convolution-root analysis gives spherical cap self-convolutions and regularity constraints. Beatson and zu Castell establish the exact cap Gegenbauer coefficient identity and positive-definite self-convolution constructions, with their Section 5 addressing a single aperture. Gneiting surveys the Schoenberg positivity and strict-positivity criteria. Gribov and Krivoruchko describe practical two-scale step-filter covariance mixtures, but their displayed coefficients are products of feature weights and hence impose a positive-semidefinite mixing matrix. These results motivate the present object but do not provide the generic *necessity* of matrix positivity, its negative spectral density, or the expanded complementary-radius cone for arbitrary signed mixing matrices. The conclusions concern the precise implication gap rather than a claim that unrelated cap-covariance models are novel.

## Limitations

The theorem is confined to integer dimensions at least two, generic pairs with a specified rational-independence hypothesis, and distinct complementary radii. It does not classify other arithmetically resonant pairs of radii. Formula (7) gives an exact integral for spectral density, not a generally elementary closed form. Literature coverage is bounded; equivalent claims under alternative terminology or unpublished derivations remain possible. The checks supplied with the result are finite numerical corroborations, not an independent audit.

## References

1. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077v1 (first posted 2011-11-30), https://arxiv.org/abs/1111.7077.
2. J. Ziegel, *Convolution roots and differentiability of isotropic positive definite functions on spheres*, arXiv:1201.5833v1 (first posted 2012-01-27), https://arxiv.org/abs/1201.5833.
3. R. K. Beatson and W. zu Castell, *Dimension hopping and families of strictly positive definite zonal basis functions on spheres*, arXiv:1510.08658v1 (first posted 2015-10-29), https://arxiv.org/abs/1510.08658.
4. A. Gribov and K. Krivoruchko, *New Flexible Compact Covariance Model on a Sphere*, arXiv:1701.03405v1 (first posted 2017-01-12), https://arxiv.org/abs/1701.03405.
5. G. Szegő, *Orthogonal Polynomials*, 4th ed., American Mathematical Society (1975), classical Darboux expansions for Gegenbauer polynomials.
