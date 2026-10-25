# A sharp continuous commutator band for two Hermite-window half-plane concentrators

## Finding

Let \(h_0(v)=\pi^{-1/4}e^{-v^2/2}\) and \(h_1(v)=\sqrt2\,v h_0(v)\). On \(\mathcal H=L^2(\mathbb R;\mathbb C^2)\), introduce the two-window time-frequency isometry
\[
 (\mathcal V f)(y,\xi)=\sum_{j=0}^1\int_{\mathbb R}f_j(u)h_j(y-u)e^{-2\pi i\xi u}\,du.
\]
For each real threshold \(s\), define the compressed half-plane concentration \(T_s=\mathcal V^*M_{\mathbf1_{\{y\le s\}}}\mathcal V\). These are positive selfadjoint contractions.

For every \(s\ne t\), putting \(d=|s-t|\),
\[
\boxed{\sigma([T_s,T_t])=i[-\kappa_d,\kappa_d],\qquad
 \|[T_s,T_t]\|=\|[T_s,T_t]\|_{\mathrm{ess}}
 =\kappa_d=\frac{d}{\sqrt2\,\pi}e^{-d^2/2}.}
\]
The entire spectrum is essential and purely absolutely continuous; there are no eigenvalues. For each sign of the imaginary spectral parameter, the absolutely continuous spectral multiplicity is two almost everywhere in the open half-band. No nonzero commutator is compact or belongs to a finite Schatten class, and its operator norm is not attained by a nonzero vector.

The exact sharp pairwise incompatibility is
\[
\boxed{\sup_{s,t\in\mathbb R}\|[T_s,T_t]\|=\frac1{\pi\sqrt{2e}}.}
\]
The maximizing threshold pairs are exactly those satisfying \(|s-t|=1\). For \(s=t\), the commutator vanishes.

## Assumptions and scope

All measures are Lebesgue measures, the Fourier convention has kernel \(e^{-2\pi i\xi u}\), and \(M_b\) denotes multiplication by the bounded symbol \(b\) on \(L^2(\mathbb R^2)\). The order of the Hermite windows and their Gaussian scale are part of the normalization; the numerical optimal threshold separation changes under a rescaling of the spatial coordinate. No compact support, smoothness, or finite-dimensional truncation of the input \(f\) is assumed. All assertions apply to the complete infinite-dimensional vector-valued signal space.

This is a simultaneous first-two-Hermite-window, or order-two polyanalytic, horizontal spectral model; it is not a claim about two independently compressed single-window operators, which are scalar in each fixed translation fiber.

## Proof

**1. Isometry and exact fibers.** Orthogonality \(\int h_j(v)h_k(v)\,dv=\delta_{jk}\) and Plancherel in \(\xi\) give
\[
\|\mathcal V f\|_{L^2(\mathbb R^2)}^2
=\int_{\mathbb R}\sum_{j,k}f_j(u)\overline{f_k(u)}\int_{\mathbb R}h_j(v)h_k(v)\,dv\,du
=\|f\|_{\mathcal H}^2.
\]
Plancherel applied to the compressed quadratic form, now integrating \(y\le s\), shows that \(T_s\) is multiplication on \(\mathcal H\) by
\[
G(s-u),\qquad G(a)=\int_{-\infty}^{a}
\begin{pmatrix}h_0(v)^2&h_0(v)h_1(v)\\h_0(v)h_1(v)&h_1(v)^2\end{pmatrix}dv.
\]
Set \(\phi(a)=\pi^{-1/2}e^{-a^2}\) and \(F(a)=\int_{-\infty}^{a}\phi(v)\,dv\). The Gaussian identities \(\phi'=-2a\phi\) and \(\int_{-\infty}^{a}2v^2\phi(v)\,dv=F(a)-a\phi(a)\) give
\[
G(a)=\begin{pmatrix}F(a)&-\phi(a)/\sqrt2\\-\phi(a)/\sqrt2&F(a)-a\phi(a)\end{pmatrix}.
\]

**2. Exact commutator.** Direct multiplication of these real symmetric matrices gives
\[
[G(a),G(b)]=\frac{a-b}{\sqrt2}\phi(a)\phi(b)
\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Thus \([T_s,T_t]\) is a matrix multiplier of the displayed fixed skew-symmetric matrix, with real scalar factor
\[
 k_{s,t}(u)=\frac{s-t}{\sqrt2\pi}
\exp\bigl(-(s-u)^2-(t-u)^2\bigr).
\]
For \(m=(s+t)/2\) and \(d=|s-t|\), completing the square yields
\[
|k_{s,t}(u)|=\kappa_d e^{-2(u-m)^2},\qquad
\kappa_d=\frac{d}{\sqrt2\pi}e^{-d^2/2}.
\]

**3. Spectrum and spectral type.** A fixed complex unitary diagonalizes the skew matrix with eigenvalues \(i\) and \(-i\). Therefore the commutator is unitarily equivalent to multiplication by \(ik_{s,t}(u)\) and \(-ik_{s,t}(u)\). The essential range of \(|k_{s,t}|\) is the closed interval \([0,\kappa_d]\), giving precisely the stated imaginary spectrum and equality of operator and essential norms. Each level set of \(k_{s,t}\) has measure zero: positive interior levels have two points, the peak has one, and zero has none. Thus there are no eigenvalues, including at zero and the spectral endpoints.

On the two monotone branches \(u<m\) and \(u>m\), the mapping \(u\mapsto \kappa_de^{-2(u-m)^2}\) is a smooth bijection onto \((0,\kappa_d)\), with nonzero derivative away from the single peak. Change of variables makes the spectral measures absolutely continuous; the two branches yield multiplicity two for each sign almost everywhere. The unique peak has Lebesgue measure zero, so no nonzero vector attains the operator norm. A nonzero multiplication operator on the nonatomic measure space \(\mathbb R\) is not compact (choose infinitely many disjoint positive-measure subsets where its modulus is bounded below); consequently it lies in no finite Schatten class.

**4. Sharp optimization.** The derivative of \(d\exp(-d^2/2)\) is \((1-d^2)\exp(-d^2/2)\) for \(d>0\). It is positive for \(0<d<1\) and negative for \(d>1\), vanishing only at \(d=1\). Hence the unique positive maximizing separation is \(1\) and the sharp value is \(1/(\pi\sqrt{2e})\). Translation of both thresholds changes only \(m\) and does not change the norm.

## Verification

The standalone `check.py` uses only the Python standard library. It independently integrates the Hermite Gram-matrix entries, multiplies the resulting \(2\times2\) matrices, checks the closed commutator fiber formula for multiple thresholds and locations, and probes the Gaussian spectral-edge identity and sharp scalar bound. The accompanying `verification_output.txt` records 714 successful assertions. These are finite sanity checks; the infinite-dimensional spectral classification and global optimization follow analytically from the preceding steps.

## Relationship to prior work

Jaming and Speckbacher (arXiv:1906.02964, 2019) develop quantitative Hermite-window short-time Fourier concentration and polyanalytic sampling inequalities. Keller and Luef (arXiv:1905.07741, 2019; journal 2021) derive symbolic calculus and semiclassical commutator expansions for polyanalytic Toeplitz operators with smooth symbols. Arroyo Neri and collaborators (DOI:10.1155/2021/9919243, 2021, Section 3) establish the general Hermite-fiber matrix representation for horizontal poly-Fock Toeplitz operators. The present result uses the canonical first-two-window realization and adds the exact paired *discontinuous half-plane* commutator, entire absolutely continuous spectrum, sharp globally optimized norm, and nonattainment/essential-norm properties; those quantitative conclusions are not asserted in the inspected source statements.

## Limitations

The exact constant depends on the stipulated Hermite scale. The finding does not treat higher-order multiwindow packets, arbitrary nonparallel half-planes, or general measurable concentration masks. The relevant general horizontal matrix representation is established prior work and is not claimed as new. Exhaustive priority across older or unindexed operator literature is not established; in particular, special cases might be implicit in that general representation.

## References

1. P. Jaming and M. Speckbacher, *Planar sampling sets for the short-time Fourier transform*, arXiv:1906.02964 (first posted 2019-06-07), primary MSC2010 42C40.
2. J. Keller and F. Luef, *Polyanalytic Toeplitz operators: isomorphisms, symbolic calculus and approximation of Weyl operators*, arXiv:1905.07741 (first posted 2019-05-19), Journal of Fourier Analysis and Applications 27 (2021), article 47.
3. J. L. Arroyo Neri, A. Sánchez-Nungaray, M. Hernández Marroquin, and R. R. López-Martínez, *Toeplitz Operators with Lagrangian Invariant Symbols Acting on the Poly-Fock Space of* \(\mathbb C^n\), Journal of Function Spaces (2021), article 9919243, DOI:10.1155/2021/9919243.
