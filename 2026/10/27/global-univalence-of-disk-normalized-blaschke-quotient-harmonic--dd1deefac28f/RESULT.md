# Global univalence of disk-normalized Blaschke-quotient harmonic convolution squares

## Finding

For every real pair \(0<x<1\) and \(0\le y<(1-x)/(3+x)\), define the real Blaschke factors \(B_t(z)=(z-t)/(1-tz)\), the circle map
\[
\Gamma_{x,y}(z)=z\frac{B_{-x}(z)}{B_y(z)},\qquad |z|=1,
\]
and its harmonic Poisson extension \(U_{x,y}\). Let \(c_n\) be its real Fourier coefficients, and set
\[
f_{x,y}(z)=\frac{U_{x,y}(z)-c_0}{c_1}.
\]
Then \(c_1>0\), \(f_{x,y}(0)=0\), its analytic derivative at the origin is \(1\), and \(f_{x,y}\) is an orientation-preserving harmonic diffeomorphism onto a translated-and-rescaled Euclidean disk.

Its harmonic Hadamard self-convolution \(F_{x,y}=f_{x,y}\widetilde *f_{x,y}\) is **globally one-to-one, sense-preserving and quantitatively co-Lipschitz** on the unit disk. In particular, for all \(z,w\in\mathbb D\),
\[
|F_{x,y}(z)-F_{x,y}(w)|\ge\Lambda(x,y)|z-w|,
\]
where
\[
\begin{aligned}
D&=1-x^2-xy-y^2,\\
\mu&=\frac{(1-x^2)(x+y)}{D},\\
\nu&=\frac{y(x+y)(1-y^2)}{D},\\
\Lambda(x,y)&=1-\frac{\mu^2(2+x^2)}{(1+x^2)^2}-\frac{\nu^2}{(1-y^2)^2}\\
&=\frac{(1-x^2)[1+x+(x^2-x+2)y][1-x-(x^2+x+2)y]}{(1+x^2)^2D^2}>0.
\end{aligned}
\]
This is a positive stability theorem throughout the **entire strictly orientation-preserving two-parameter sector** of this circle-map family. It concerns complex-linear normalization to a disk and does *not* assert that the real-affine, coanalytic-derivative-killing normalization to an ellipse has univalent self-convolution.

## Assumptions and scope

The unit disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). A planar harmonic map has unique representation \(f=h+\overline g\) after imposing \(g(0)=0\). For \(f=h+\overline g\) and \(F=H+\overline G\), their harmonic Hadamard convolution is \((h*H)+\overline{(g*G)}\), where \(*\) multiplies equal-degree Taylor coefficients. The normalization here fixes \(h'(0)=1\) but permits \(g'(0)=\nu\ne0\). In particular, this family belongs to the normalized convex harmonic class \(\mathcal K_H\), generally **not** its smaller subclass \(\mathcal K_H^0\).

The angular derivative of \(\Gamma_{x,y}\), with \(t=\arg z\) and \(u=\cos t\), is
\[
1+\frac{1-x^2}{1+2xu+x^2}-\frac{1-y^2}{1-2yu+y^2}.
\]
It is strictly decreasing in \(u\in[-1,1]\); its minimum, at \(u=1\), is \(\bigl[1-x-(3+x)y\bigr]/\bigl[(1+x)(1-y)\bigr]\). Therefore the stated strict parameter region is exactly the region where \(\Gamma_{x,y}\) has positive angular derivative everywhere. Because its topological degree is one, it is a circle diffeomorphism; the Radó–Kneser–Choquet theorem gives the claimed disk-valued harmonic diffeomorphism \(U_{x,y}\).

## Proof

**1. Fourier coefficients and nondegenerate normalization.** The rational boundary function is
\[
\Gamma_{x,y}(z)=\frac{z(z+x)(1-yz)}{(1+xz)(z-y)}.
\]
Its Laurent expansion converges on an annulus containing the unit circle. Subtraction of the simple pole at \(z=y\) and expansion of the outside pole at \(z=-1/x\) give
\[
\begin{aligned}
c_1&=\frac{D}{1+xy},\\
c_2&=-\frac{(1-x^2)(x+y)}{1+xy},\\
c_{-1}&=\frac{y(x+y)(1-y^2)}{1+xy},\\
c_n&=c_2(-x)^{n-2}\quad(n\ge2),\\
c_{-n}&=c_{-1}y^{n-1}\quad(n\ge1).
\end{aligned}
\]
The function \(D=1-x^2-xy-y^2\) decreases with \(y\ge0\). At the upper permitted endpoint its value is
\[
D\left(x,\frac{1-x}{3+x}\right)=\frac{(1-x)(1+x)(x^2+5x+8)}{(3+x)^2}>0.
\]
Thus \(c_1>0\), and the normalization is legitimate. Splitting positive and negative modes yields
\[
f_{x,y}=h+\overline g,\qquad
h(z)=z-\frac{\mu z^2}{1+xz},\qquad
g(z)=\frac{\nu z}{1-yz}.
\]
Its image is the disk \(\{(w-c_0)/c_1:|w|<1\}\).

**2. Exact convolution and divided differences.** Coefficientwise squaring of the two geometric Taylor tails yields
\[
F_{x,y}=H+\overline G,\qquad
H(z)=z+\frac{\mu^2z^2}{1-x^2z},\qquad
G(z)=\frac{\nu^2z}{1-y^2z}.
\]
Put \(r=x^2\), \(s=y^2\), and \(d=\mu^2-r\). The identity
\[
\mu-x=\frac{y(1+xy)}{D}\ge0
\]
implies \(d\ge0\). For distinct \(z,w\in\mathbb D\), exact subtraction gives
\[
\frac{H(z)-H(w)}{z-w}
=\frac{1+d(z+w)-rdzw}{(1-rz)(1-rw)},\qquad
\frac{G(z)-G(w)}{z-w}=\frac{\nu^2}{(1-sz)(1-sw)}.
\]
Since \(|z|,|w|<1\), the reverse triangle inequality yields
\[
|H(z)-H(w)|\ge
\frac{1-d(2+r)}{(1+r)^2}|z-w|
=\left(1-\frac{\mu^2(2+r)}{(1+r)^2}\right)|z-w|,
\]
and
\[
|G(z)-G(w)|\le \frac{\nu^2}{(1-s)^2}|z-w|.
\]
No positivity of the intermediate numerator was assumed: the next step verifies that its resulting difference is strictly positive on the parameter domain.

**3. A global positive algebraic margin.** Combining the preceding estimates gives
\[
|F_{x,y}(z)-F_{x,y}(w)|\ge
\left(1-\frac{\mu^2(2+r)}{(1+r)^2}-\frac{\nu^2}{(1-s)^2}\right)|z-w|.
\]
Substituting the rational formulas for \(\mu,\nu\), and clearing denominators, factors the coefficient **exactly** as the displayed \(\Lambda(x,y)\). The first numerator factor is positive because \(0<x<1\); the middle factor \(1+x+(x^2-x+2)y\) is positive because \(x^2-x+2>0\). For the last factor, observe that \(x^2+x+2<x+3\), so
\[
(x^2+x+2)y<(3+x)y<1-x,
\]
which gives \(1-x-(x^2+x+2)y>0\). Consequently \(\Lambda>0\).

This proves the global co-Lipschitz inequality and injectivity. Taking a directional difference quotient in the **separate** bounds for \(H\) and \(G\) yields \(|H'(z)|-|G'(z)|\ge\Lambda>0\) for every \(z\in\mathbb D\); hence the Jacobian \(|H'|^2-|G'|^2\) is strictly positive. The inverse function theorem gives a sense-preserving harmonic diffeomorphism onto the open image. No finite sampling or numerical continuation is needed. \(\square\)

## Verification

The standalone `verification.py` uses exact SymPy rational-function arithmetic. It reconstructs the Laurent coefficients from \(\Gamma_{x,y}\), checks the rational closed forms for \(H,G\) and their two-point divided differences, verifies \(\mu-x\), the factorization for \(\Lambda\), and the endpoint formula for \(D\). Representative rational parameter substitutions provide independent sanity checks. Running `python3 verification.py` printed `PASS: exact Laurent coefficients, convolution divided differences, parameter positivity and gap factorization`. The proof of inequalities for *all* admissible real parameters is analytic and is not inferred from finitely many tests.

## Relationship to prior work

Wang and Zhong (2026, arXiv:2609.11556, Sections 3–8) introduce the underlying rational circle map, prove the Poisson disk-diffeomorphism property for one parameter pair, and apply an additional **real-affine** normalization to obtain \(g'(0)=0\) and an **ellipse** image. The ellipse-normalized map has a non-locally-univalent self-convolution. Their findings do not assert that the **complex-linearly** normalized disk-target map or its full two-parameter sector has a globally one-to-one Hadamard square. Here the new proof uses the disk target, a different prescribed normalization, and an explicit two-point positive lower bound across the whole parameter region.

The published notes *Unique real-axis fold point in the Dorff ellipse counterexample* (2026), *Sharp disk-wide local-univalence radius for the Dorff ellipse self-convolution* (2026), *Exact parameter threshold for the Dorff counterexample’s rational witness* (2026), and *Every higher convolution power of the Dorff ellipse map loses local univalence* (2026) all concern the **real-affine ellipse normalization**, not the disk-normalized positive result. The 2001 Dorff and 2014 Boyd–Dorff–Nowak–Romney–Wołoszkiewicz positive results concern specific half-plane/strip and shear families, respectively, not this Blaschke-quotient disk-normalized family. Merely matching the initial boundary rational function is insufficient to imply the new global inequality, because harmonic coefficientwise squaring does not commute with non-complex-linear affine postcomposition.

## Limitations

The theorem is restricted to the explicitly given two-real-parameter Blaschke-quotient Poisson family, strict positive-angular-derivative sector, and complex-linear normalization. It makes no claim about general harmonic disk diffeomorphisms, harmonic convex mappings with \(g'(0)=0\), or all outside-sector parameters. The positive constant \(\Lambda\) is a proven uniform co-Lipschitz lower bound; it is not asserted optimal for general \(y>0\). Unknown or unindexed more general harmonic convolution preservation theorems remain a priority risk. The output image of the convolution is not claimed convex.

## References

1. Z.-G. Wang and D. Zhong, *A counterexample to an open problem of Dorff*, arXiv:2609.11556v1 (first publicly posted 2026-09-10), Sections 3–8, https://arxiv.org/abs/2609.11556.
2. M. Dorff, *Convolutions of planar harmonic convex mappings*, Complex Variables 45 (2001), 263–271, DOI:10.1080/17476930108815381.
3. Z. Boyd, M. Dorff, M. Nowak, M. Romney and M. Wołoszkiewicz, *Univalency of convolutions of harmonic mappings*, Applied Mathematics and Computation 234 (2014), 326–332, DOI:10.1016/j.amc.2014.01.162.
4. L. Li and S. Ponnusamy, *Injectivity of sections of convex harmonic mappings and convolution theorems*, Czechoslovak Mathematical Journal 66 (2016), 331–350, DOI:10.1007/s10587-016-0259-9.
5. *Sharp disk-wide local-univalence radius for the Dorff ellipse self-convolution* (2026), public mathematical record `a0b680fc0771`.
6. *Exact parameter threshold for the Dorff counterexample’s rational witness* (2026), public mathematical record `e20d7884e72b`.
7. *Every higher convolution power of the Dorff ellipse map loses local univalence* (2026), public mathematical record `486895b5c6f3`.
8. *Unique real-axis fold point in the Dorff ellipse counterexample* (2026), public mathematical record `8f1ef438e553`.
