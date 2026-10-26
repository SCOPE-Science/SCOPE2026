# Two exact dipole–quadrupole transitions for antipodal hyperspherical concentration

## Finding

For every integer \(d\ge3\), let \(\sigma_d\) be probability surface measure on \(S^{d-1}\subset\mathbb R^d\). Fix an axis \(u\in S^{d-1}\) and \(0<c<1\). Write \(t=u\cdot x\), \(E_c=\{x:|u\cdot x|\ge c\}\), and let \(\mathcal H_j\) be the complex restrictions of harmonic homogeneous polynomials of degree \(j\) to \(S^{d-1}\). On the natural mean-zero band \(\mathcal B=\mathcal H_1\oplus\mathcal H_2\), define \(T_c=P_{\mathcal B}M_{\mathbf1_{E_c}}|_{\mathcal B}\).

The complete spectrum consists of five explicitly integrable eigenvalue types \(A,B,C,D,E\) with multiplicities \(1,d-1,1,d-1,(d-2)(d+1)/2\), respectively. Let
\[
k_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)},\qquad
\rho_d(t)=k_d(1-t^2)^{(d-3)/2},
\]
and set \(\Lambda[f](c)=2\int_c^1 f(t^2)\rho_d(t)\,dt\). Then
\[
\begin{aligned}
A&=\Lambda[dX],&
B&=\Lambda[\tfrac d{d-1}(1-X)],\\
C&=\Lambda[\tfrac{d+2}{2(d-1)}(dX-1)^2],&
D&=\Lambda[\tfrac{d(d+2)}{d-1}X(1-X)],\\
E&=\Lambda[\tfrac{d(d+2)}{(d-1)(d+1)}(1-X)^2],
\end{aligned}
\]
where \(X\) is the integration variable \(t^2\), not an additional random variable. The exact strict comparisons \(A>D>B\) and \(D>E\) hold at every \(0<c<1\).

Define the **two distinct universal thresholds**
\[
c_1=d^{-1/2},\qquad c_2=\frac{\sqrt{d+2}}d.
\]
They obey \(0<c_1<c_2<1\). Below \(c_1\), the leading and runner-up eigenvalue types are \(A,D\). At \(c_1\), \(A\) remains the unique leading eigenvalue and the runner-up type is tied between \(C\) and \(D\). For \(c_1<c<c_2\), the leading and runner-up types are \(A,C\). At \(c_2\), \(A=C\) is the top eigenvalue with multiplicity two, and \(D\) is the largest strictly smaller type. For \(c_2<c<1\), the leading and runner-up types are \(C,A\). This gives the complete maximizing eigenspace classification, including every transition degeneracy.

The gap to the nearest **distinct lower** eigenvalue is sharp and equals
\[
\Delta_d(c)=\begin{cases}
A-D,&0<c<c_1,\\
A-C,&c_1\le c<c_2,\\
A-D,&c=c_2,\\
C-A,&c_2<c<1.
\end{cases}
\]
Thus, for the orthogonal projection \(\Pi_c\) onto the entire top eigenspace and every \(f\in\mathcal B\),
\[
\int_{E_c}|f|^2\,d\sigma_d\le\lambda_*(c)\|f\|_2^2-\Delta_d(c)\|f-\Pi_cf\|_2^2,
\]
with equality for each \(c\) for some \(f\notin\operatorname{Ran}\Pi_c\). The coefficient cannot be increased. In particular, the dimension of the maximizing space jumps from one to two at \(c_2\), then returns to one. The transition interval shrinks sharply as \(d\to\infty\):
\[
c_2-c_1=d^{-3/2}+O(d^{-5/2}).
\]

## Assumptions and scope

All inner products and energies use probability-normalized surface measure. The dimension is any integer \(d\ge3\); the band excludes constants and includes **all** complex degree-one and degree-two spherical harmonics, with no zonality or reality assumption on \(f\). The cap is the union of two antipodal closed polar caps. Their boundary has zero surface measure. The thresholds refer to \(c=\cos\Theta\), not the angular radius \(\Theta\). Equalities and multiplicities count over complex scalars.

## Proof

**1. Orthogonal reducing subspaces.** Rotate \(u\) to the first coordinate and write \(x=(t,y)\) with \(y\in\mathbb R^{d-1}\) and \(t^2+|y|^2=1\). The orthogonal stabilizer of \(u\) and the reflection \((t,y)\mapsto(-t,y)\) preserve the cap. The band decomposes as five pairwise orthogonal reducing spaces: axial dipoles \(\operatorname{span}\{t\}\); transverse dipoles \(\operatorname{span}\{y_j\}\); axial quadrupoles \(\operatorname{span}\{dt^2-1\}\); mixed quadrupoles \(\operatorname{span}\{ty_j\}\); and transverse quadrupoles \(Q(y)\) where \(Q\) ranges over traceless homogeneous quadratic polynomials on \(\mathbb R^{d-1}\). Their complex dimensions are exactly \(1,d-1,1,d-1,(d-2)(d+1)/2\). Conditional rotational symmetry in \(y\), parity in \(t\), and the vanishing mean of traceless quadratics show that the multiplication compression is scalar on each space. There is no hidden coupling between the degree-one and degree-two sectors because the cap is antipodally invariant.

**2. Five exact eigenvalue formulas.** The marginal density of \(t\) is \(\rho_d(t)\). Uniform-sphere moments give
\[
\mathbb E[t^2]=1/d,\quad \mathbb E[t^4]=3/[d(d+2)],\quad
\mathbb E[t^2(1-t^2)]=(d-1)/[d(d+2)],
\]
\[
\mathbb E[(1-t^2)^2]=(d-1)(d+1)/[d(d+2)].
\]
Conditional squared amplitudes of each reducing space, normalized to have expectation one, are precisely the five densities displayed under Finding. Hence they yield every eigenvalue and multiplicity. Their total trace equals \(\dim(\mathcal B)\sigma_d(E_c)\), another normalization check.

**3. Strict order outside the axial quadrupole.** Each pair among the normalized densities \((A,D)\), \((D,B)\), and \((D,E)\) has a strictly increasing density ratio as a function of \(X=t^2\): respectively a positive multiple of \((1-X)^{-1}\), of \(X\), and of \(X/(1-X)\). The elementary monotone-likelihood-ratio lemma follows by integrating \((f(x)-g(x))\) from a threshold to one: because the densities both integrate to one, the difference changes sign only once from negative to positive, so every nontrivial upper-tail mass is strictly larger for the increasing-ratio density. This proves \(A>D>B\) and \(D>E\) for all \(0<c<1\).

**4. Exact boundary factorizations.** Set \(m=(d-1)/2\). Direct differentiation of \(c(1-c^2)^m(a+bc^2)\), using the density \(\rho_d\), and the fact that this boundary expression vanishes at \(c=1\), gives
\[
\boxed{\ C-A=\frac{k_d}{d-1}c(1-c^2)^m\big(d^2c^2-d-2\big)\ },
\]
\[
\boxed{\ C-D=\frac{k_d(d+2)}{d-1}c(1-c^2)^m\big(dc^2-1\big)\ },
\]
and subtraction yields
\[
\boxed{\ A-D=\frac{2k_dd}{d-1}c^3(1-c^2)^m>0\ }.
\]
These identities prove that \(C\) crosses \(D\) **only** at \(c_1=1/\sqrt d\) and crosses \(A\) **only** at \(c_2=\sqrt{d+2}/d\), with strict reversal at each crossing. Together with Step 3, they establish the entire top-two spectral phase diagram and the asserted maximizing eigenspaces. Since \(d^2>d+2\) when \(d\ge3\), both thresholds lie strictly inside the admissible cap range.

**5. Sharp stability and high-dimensional pinching.** Decompose \(f\) spectrally. The top eigenspace contribution has concentration exactly \(\lambda_*\|\Pi_cf\|_2^2\), and every orthogonal spectral component has concentration at most \((\lambda_*-\Delta_d(c))\) times its squared norm. This yields the displayed deficit with the listed piecewise exact constant. A vector in the next distinct eigenspace attains equality; if \(f\) has components in both top and next spaces, equality is again attained. The tie at \(c_2\) is handled by including **both** axial components in \(\Pi_c\); in particular, the gap to the next *distinct* eigenvalue is then \(A-D>0\), not zero. Finally
\[
\frac{\sqrt{d+2}}d-\frac1{\sqrt d}=d^{-1/2}\Big(\sqrt{1+2/d}-1\Big)=d^{-3/2}+O(d^{-5/2}),
\]
proving the pinching law.

## Verification

The standalone \(checker.py\) independently integrates the five normalized angular densities at six dimensions \(d=3,4,5,7,10,25\), and tests values below, at, between, and above both transitions. It checks all three exact boundary factorizations, eigenvalue ordering, degeneracies, and the full trace identity against the cap area. Its finite checks corroborate the formulas but are **not** the proof for infinitely many dimensions or all cap radii. The latter is supplied analytically in the five steps above.

## Relationship to prior work

The scalar spherical Slepian concentration framework and double-polar-cap parity decomposition on the ordinary two-sphere are classical; see Simons and Dahlen (2006), especially their Section 4.2 and accompanying matrix problem. Michel, Plattner, and Seibert (first public arXiv version March 26, 2021) give a unified scalar/vector/tensor Slepian framework on the two-sphere, with a general commuting-operator construction for spherical caps. Neither source asserts the all-dimensional, **mean-zero dipole-plus-quadrupole** two-transition classification or the present exact sharp stability coefficient. The theorem does not claim the general spherical Slepian framework, bandlimited matrix construction, or two-sphere symmetry reduction as new.

## Limitations

This result concerns only the complete mean-zero degree-at-most-two band, equal antipodal caps, and ordinary (spin-zero) spherical harmonics. It does not classify higher bandwidths, unequal caps, or tensor-valued fields. The all-dimensional threshold and stability laws are proved analytically, but priority relative to any unlocated low-degree special-function tables remains subject to independent verification. The previous literature gives a strong method for deriving such finite-band spectra; the identified contribution is the explicit uniform-in-dimension ordering, crossings, degeneracies, and sharp gap, not a new diagonalization method.

## References

1. V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first public version March 26, 2021), https://arxiv.org/abs/2103.14650.
2. F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, Geophysical Journal International 166 (2006), 1039–1061, https://doi.org/10.1111/j.1365-246X.2006.03065.x.
3. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral Concentration on a Sphere*, SIAM Review 48 (2006), 504–536, arXiv:math/0408424, https://arxiv.org/abs/math/0408424.
