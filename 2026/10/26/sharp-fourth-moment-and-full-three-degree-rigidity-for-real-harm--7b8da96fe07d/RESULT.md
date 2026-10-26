# Sharp fourth moment and full three-degree rigidity for real harmonic quadratics on the disk

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) have probability area measure \(d\mu=dx\,dy/\pi\). For every nonzero **real-valued** harmonic polynomial \(h\) of total degree at most two,
\[
\frac{\|h\|_{L^4(\mu)}^4}{\|h\|_{L^2(\mu)}^4}\leq K_*,\qquad
K_*=\frac{9(33q_*^4+240q_*^3+520q_*^2+960q_*+560)}{2(43q_*^4+240q_*^3+300q_*^2+1440q_*+1080)}
=4.330553360251238\ldots,
\]
where \(q_*=3.640733644769532\ldots\) is the unique positive zero of
\[
12q^4+67q^3-180q^2-680q-480=0.
\]
Let
\[
s_*=\frac{3q_*^4+20q_*^3+15q_*^2+120q_*+120}{5(5q_*^2+24q_*+12)}
=2.714054203859350\ldots.
\]
**All** equality cases, and no others, are
\[
h(z)=\lambda\left[1+2\sqrt{s_*}\,\operatorname{Re}(e^{-i\theta}z)+q_*\operatorname{Re}(e^{-2i\theta}z^2)\right],
\quad\lambda\in\mathbb R\setminus\{0\},\quad\theta\in\mathbb R.
\]
Moreover, if at most two of the homogeneous harmonic degrees \(0,1,2\) are present, the exact sharp fourth-power quotient is \(297/86=3.453488372093\ldots<K_*\). Consequently every global maximizer requires all three degrees, with a strict quantified gap \(K_*-297/86=0.877064988158\ldots\).

## Assumptions and scope

The polynomial has real values on \(\mathbb D\), is harmonic for the Euclidean Laplacian, and has total degree at most two. Its \(L^p\) norms are taken with respect to the **same probability-normalized area measure**, not boundary arc length. Coefficients, extrema and equality cases are unrestricted apart from real-valuedness and nonvanishing. The theorem does not assert the sharp constant for complex-valued harmonic polynomials or for higher degree.

Any real harmonic quadratic is uniquely a sum of a constant, a linear harmonic polynomial and a homogeneous quadratic harmonic polynomial. By rotating the disk, reversing the overall sign if needed, and representing the quadratic term in polar coordinates, one may write
\[
h(re^{i\varphi})=a+br\cos\varphi+Cr^2\cos(2\varphi-\psi),\qquad a,b,C\geq0,
\]
with an arbitrary phase \(\psi\). If \(a=0\) or \(b=0\), the same formula holds by continuity and a choice of axes.

## Proof

**1. Exact moments and phase alignment.** Polar integration gives, for the above normal form,
\[
\begin{aligned}
\|h\|_2^2&=a^2+\frac{b^2}{4}+\frac{C^2}{6},\\
\|h\|_4^4&=a^4+\frac32a^2b^2+a^2C^2+ab^2C\cos\psi
+\frac18b^4+\frac38b^2C^2+\frac3{40}C^4.
\end{aligned}
\]
The only phase-dependent term is \(ab^2C\cos\psi\). Hence alignment \(\psi=0\) maximizes the fourth moment for fixed magnitudes; if all three degrees are nonzero, alignment is necessary for equality.

**2. Eliminate the linear amplitude.** For \(a>0\) set \(q=C/a\) and \(s=b^2/(4a^2)\). The quotient becomes
\[
R_q(s)=\frac{C(q)+B(q)s+2s^2}{[A(q)+s]^2},\quad
A(q)=1+\frac{q^2}{6},\quad
B(q)=6+4q+\frac{3q^2}{2},\quad
C(q)=1+q^2+\frac{3q^4}{40}.
\]
Its derivative with respect to \(s\) has numerator
\[
B(q)A(q)-2C(q)+[4A(q)-B(q)]s.
\]
For every \(q\geq0\), both \(B(q)-4A(q)>0\) and \(B(q)A(q)-2C(q)>0\); these follow by expansion into polynomials with strictly positive coefficients. Thus \(R_q\) strictly increases until its unique maximum and strictly decreases afterward. That maximum is at
\[
s(q)=\frac{3q^4+20q^3+15q^2+120q+120}{5(5q^2+24q+12)}>0.
\]
Substitution simplifies the optimized quotient exactly to
\[
F(q)=\frac{9(33q^4+240q^3+520q^2+960q+560)}{2(43q^4+240q^3+300q^2+1440q+1080)}.
\]

**3. Unique global radius ratio.** Direct differentiation yields
\[
F'(q)=-\frac{180(5q^2+24q+12)\bigl(12q^4+67q^3-180q^2-680q-480\bigr)}{(43q^4+240q^3+300q^2+1440q+1080)^2}.
\]
The displayed quartic has exactly one sign change in descending coefficient order, hence exactly one positive root by Descartes' rule (existence follows from its negative value at zero and positive leading coefficient). Therefore \(F\) strictly increases then strictly decreases on \([0,\infty)\), attaining its sole maximum at \(q_*\). At the endpoints \(F(0)=7/3\) and \(\lim_{q\to\infty}F(q)=297/86\), both strictly smaller than \(F(q_*)\). The case \(a=0\), obtained directly by maximizing the corresponding quadratic quotient in \(b^2\) and \(C^2\), has maximum \(297/86\). Consequently the global maximum has \(a,b,C>0\), forcing the unique relative phase alignment and the stated complete equality family.

**4. Exact two-degree benchmark.** Normalize the squared \(L^2\) energies of the two present homogeneous degrees to sum to one, and let \(t\in[0,1]\) denote the second energy fraction. For pairs \((0,1)\), \((0,2)\) and \((1,2)\), the fourth-power quotients are respectively
\[
(1-t)^2+6t(1-t)+2t^2,\qquad
(1-t)^2+6t(1-t)+\frac{27}{10}t^2,\qquad
2t^2+9t(1-t)+\frac{27}{10}(1-t)^2.
\]
Their unique maxima are \(7/3\), \(63/23\) and \(297/86\), attained at \(t=2/3\), \(20/23\) and \(18/43\), respectively. This proves the sharp gap and the necessity of all three homogeneous degrees.

## Verification

The accompanying standalone `check_harmonic_quadratic.py` evaluates disk moments independently by exact monomial integration, reconstructs all fourth-power coefficients, verifies the reduced rational optimization and its derivative symbolically, checks the unique positive quartic root, proves the three pair-degree constants symbolically, and compares 100 randomly chosen quadratics against high-order independent polar quadrature. The checker ran successfully. Computed sample values are \(q_*=3.64073364476953\), \(s_*=2.71405420385935\), and \(K_*=4.33055336025124\). The infinite-domain sharpness and equality classification follow from the analytical sign arguments above, **not** from finite sampling.

## Relationship to prior work

Dai, Gorbachev and Tikhonov (arXiv:1905.00323, first public 2019-05-01) study orders of Nikolskii inequalities for **lacunary spherical polynomials**, not exact fourth-power norms of all real harmonic polynomials of disk degree two. The disk problem is related to spherical analysis because uniform disk area is the marginal of uniform surface measure on the unit three-sphere in four dimensions, but the three-degree non-lacunary subspace and its extremizers are not resolved by their bounds.

Melentijević and Božin (arXiv:1911.06429, first public 2019-11-15) prove a sharp **boundary-to-diameter harmonic Hardy trace inequality**, whose functionals and measures differ from the present disk-area \(L^4/L^2\) quotient. Melentijević (arXiv:2211.03655, first public 2022-11-07) proves hypercontractive inequalities for **analytic** weighted Bergman functions under a dilation, not the full real harmonic quadratic subspace. Üreyen (arXiv:2207.13140, first public 2022-07-26) studies harmonic Bergman projection on hyperbolic balls in dimension at least three. Nearby published claims concerning degree-two **homogeneous spherical harmonics** do not imply this three-degree disk result: they omit both the constant and the degree-one interaction, and the measures/ambient spaces differ.

## Limitations

The result is for real-valued planar harmonic degree-at-most-two polynomials and normalized Euclidean disk area only; it does not cover complex-valued maps, other weights, higher degrees, or all finite-dimensional spherical polynomial subspaces. No independent audit or historical-priority certification has been performed. Although targeted published-literature and mathematical-record comparisons found no covering statement, an equivalent treatment under Zernike-polynomial, spherical-marginal or finite-band Nikolskii terminology remains possible.

## References

1. F. Dai, D. Gorbachev and S. Tikhonov, *Nikolskii inequality for lacunary spherical polynomials*, arXiv:1905.00323 (2019), https://arxiv.org/abs/1905.00323.
2. P. Melentijević and V. Božin, *Sharp Riesz–Fejér inequality for harmonic Hardy spaces*, arXiv:1911.06429 (2019), https://arxiv.org/abs/1911.06429.
3. P. Melentijević, *Hypercontractive inequalities for weighted Bergman spaces*, arXiv:2211.03655 (2022), https://arxiv.org/abs/2211.03655.
4. A. E. Üreyen, *H-harmonic Bergman projection on the hyperbolic ball*, arXiv:2207.13140 (2022), https://arxiv.org/abs/2207.13140.
