# Sharp harmonic Hardy–Hilbert Landau radius and co-Lipschitz profile

## Finding
Let \(m(dt)=dt/(2\pi)\) be normalized arc measure on the unit circle, and let \(M\ge1\). Write \(\mathcal H_2(M)\) for all planar complex harmonic Poisson extensions \(f=\mathcal P[F]\) with \(F\in L^2(\mathbb T,m)\), \(\|F\|_2\le M\), and normalized derivatives \(f(0)=0\), \(f_z(0)=1\), \(f_{\bar z}(0)=0\). No global injectivity or sense-preservation is assumed.

Define, for \(0\le r<1\),
\[
S(r)=\sum_{n=2}^{\infty}n^2r^{2n-2}
=\frac{r^2(4-3r^2+r^4)}{(1-r^2)^3}.
\]
For \(M>1\), let \(R_M\) be the unique root in \((0,1)\) of
\[
2(M^2-1)S(R_M)=1;
\]
for \(M=1\), set \(R_1=1\). Then \(R_M\) is **the exact largest universal radius of injectivity**: every \(f\in\mathcal H_2(M)\) is injective and positively oriented in \(|z|<R_M\), and for every \(r>R_M\), some member is not injective on \(|z|<r\).

More precisely, for \(0<r<1\), define the classwise co-Lipschitz constant
\[
L_M(r)=\inf_{f\in\mathcal H_2(M)}\ \inf_{\substack{z,w\in\mathbb D_r\\z\ne w}}
\frac{|f(z)-f(w)|}{|z-w|}.
\]
The **exact complete profile** is
\[
\boxed{L_M(r)=\max\big\{0,\,1-\sqrt{2(M^2-1)S(r)}\big\}.}
\]
For \(M=1\), all maps are the identity. For \(M>1\), the bound is approached by explicit harmonic extremals, and one extremal has zero Jacobian at \(z=R_M\).

## Assumptions and scope
The circle norm is with probability measure \(m\), not unnormalized Lebesgue measure. If \(\|F\|_{L^2(dt)}=B\), then \(M=B/\sqrt{2\pi}\) and the stated normalization forces \(B\ge\sqrt{2\pi}\). The assertion concerns all normalized harmonic Poisson extensions under the given bound, not only mappings globally sense-preserving on \(\mathbb D\). We use the Wirtinger derivatives \(f_z\) and \(f_{\bar z}\). Every radius denotes an open centered disk.

## Proof
**1. Parseval reduction.** The unique normalized harmonic expansion is
\[
f(z)=z+\sum_{n=2}^{\infty}\big(a_nz^n+\overline{b_n z^n}\big).
\]
The analytic and coanalytic Fourier modes are distinct, and hence Parseval yields
\[
\sum_{n=2}^{\infty}(|a_n|^2+|b_n|^2)
=\|F\|_2^2-1\le c^2,
\qquad c^2=M^2-1.
\]
This is an exact equivalence for the boundary \(L^2\) budget; no individual coefficient bound is independently saturated.

**2. Exact chord estimate.** For \(z,w\in\mathbb D_r\), set \(\Delta_n=z^n-w^n\). Cauchy–Schwarz in the two coefficient sequences gives
\[
\begin{aligned}
|f(z)-f(w)-(z-w)|
&\le c\left(2\sum_{n=2}^{\infty}|\Delta_n|^2\right)^{1/2}\\
&\le c\sqrt{2S(r)}\,|z-w|,
\end{aligned}
\]
because \(|\Delta_n|\le nr^{n-1}|z-w|\). Consequently
\[
|f(z)-f(w)|\ge\big(1-c\sqrt{2S(r)}\big)|z-w|.
\]
The same coefficient argument applied to \(f_z-1\) and \(f_{\bar z}\) gives
\[
|f_z(z)|-|f_{\bar z}(z)|
\ge1-c\sqrt{2S(|z|)}.
\]
As \(S\) is strictly increasing on \((0,1)\), diverges at \(1\), and vanishes at \(0\), the root \(R_M\) exists uniquely for \(M>1\). The preceding bounds prove both global injectivity and positive Jacobian throughout every \(\mathbb D_r\) with \(r<R_M\), hence throughout \(\mathbb D_{R_M}\).

**3. Sharp profile below the radius.** For fixed \(0<r<R_M\), put
\[
\gamma_n(r)=\frac{c\,n r^{n-1}}{\sqrt{2S(r)}},
\qquad
f_r(z)=z+\sum_{n=2}^{\infty}\gamma_n(r)
\big(\overline{z}^{\,n}-z^n\big).
\]
These coefficients decay geometrically and the boundary norm is exactly \(M\), since \(2\sum_{n\ge2}\gamma_n(r)^2=c^2\). At the real point \(z=r\),
\[
(f_r)_z(r)=1-c\sqrt{S(r)/2},
\qquad
(f_r)_{\bar z}(r)=c\sqrt{S(r)/2}.
\]
The derivative in the imaginary direction therefore has magnitude exactly \(1-c\sqrt{2S(r)}>0\). Taking difference quotients along imaginary chords whose real parts tend to \(r\) from below shows \(L_M(r)\le1-c\sqrt{2S(r)}\). Together with Step 2 this establishes equality for \(r<R_M\).

**4. Endpoint and optimality.** For \(M>1\), put \(q=R_M\) and
\[
\beta_n=\frac{nq^{n-1}}{2S(q)},
\qquad
f_*(z)=z+\sum_{n=2}^{\infty}\beta_n
\big(\overline{z}^{\,n}-z^n\big).
\]
The identity \(2(M^2-1)S(q)=1\) implies
\[
\|F_*\|_2^2=1+2\sum_{n=2}^{\infty}\beta_n^2
=1+\frac{1}{2S(q)}=M^2.
\]
At \(z=q\), the coefficient sum is \(\sum_{n\ge2}n\beta_nq^{n-1}=1/2\), giving
\[
(f_*)_z(q)=(f_*)_{\bar z}(q)=\frac12,
\qquad J_{f_*}(q)=0.
\]
Lewy's theorem states that a planar harmonic function which is injective on a neighborhood has nonvanishing Jacobian. Hence \(f_*\) cannot be injective on any disk of radius greater than \(q\). For such a disk, its vanishing differential also forces \(L_M(r)=0\), while at \(r=q\) the positive formulas from below tend to zero. Thus the entire profile and the largest radius are sharp.

For \(M=1\), Parseval forces every higher coefficient to vanish, leaving \(f(z)=z\) and \(L_1(r)=1\).

## Verification
The standalone file `check_radius.py` recomputes \(S\) against finite rational power sums, bisects the defining equation for seven values of \(M\), checks the extremal norm and derivative identities using 1500 coefficients, and checks the co-Lipschitz tangential construction at three parameter values. Run `python3 check_radius.py` in the extracted package directory. The checks are finite consistency tests, not proofs of the infinite sums, monotonicity, or Lewy's theorem. Those follow analytically above.

## Relationship to prior work
Ahamed and Hossain, *Bohr Radius and Landau-type Theorems for Harmonic Mappings with Boundary Functions in Lebesgue Spaces*, arXiv:2604.14217v1 (first public April 12, 2026), Theorem 3.1, give sufficient Landau radii from independent coefficient bounds. Their Section 4, problem [A], explicitly asks for absolute sharp constants when \(1<p<\infty\). The present theorem resolves the **univalence-radius component at \(p=2\)** under exactly the same origin and derivative normalization, with normalized-arc-length conversion made explicit. It does not determine their separate schlicht-disk covering-radius problem. Their assertion preceding the conclusion about simultaneous near-saturation of all individual coefficient estimates is not needed here; the extremal saturates the Hilbert-space norm constraint itself.

The same authors' arXiv:2603.28806v1, Sections 2.1–2.3, instead impose specialized differential inequalities defining narrower harmonic subclasses and do not imply the result for all \(L^2\)-boundary extensions. Earlier classical harmonic Landau and Lewy theory supplies background and the necessary local-injectivity criterion.

## Limitations
This is a universal theorem for the unrestricted normalized boundary \(L^2\) ball. It is **not** a statement about normalized harmonic mappings that are already globally sense-preserving or globally univalent, and it does not identify the optimal covered schlicht disk. The exact formula is special to the Hilbert exponent and is not asserted for \(p\ne2\). Although its proof is elementary in Hilbert-space terms, a mathematically equivalent statement could exist in older unindexed literature; the literature comparison is not an independence or exhaustive bibliographic certificate.

## References
1. M. B. Ahamed and R. Hossain, *Bohr Radius and Landau-type Theorems for Harmonic Mappings with Boundary Functions in Lebesgue Spaces*, arXiv:2604.14217v1 (April 12, 2026), especially Theorem 3.1 and Section 4 [A]. https://arxiv.org/html/2604.14217v1
2. M. B. Ahamed and R. Hossain, *Sharp Landau-Type Theorems and Schlicht Disc Radii for certain Subclasses of Harmonic Mappings*, arXiv:2603.28806v1 (March 28, 2026), Sections 2.1–2.3. https://arxiv.org/html/2603.28806v1
3. H. Lewy, *On the non-vanishing of the Jacobian in certain one-to-one mappings*, Bulletin of the American Mathematical Society **42** (1936), 689–692. Classical planar harmonic local-injectivity theorem.
