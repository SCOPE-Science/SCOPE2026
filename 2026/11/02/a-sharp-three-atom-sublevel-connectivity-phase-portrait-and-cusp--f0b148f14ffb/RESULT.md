# A sharp three-atom sublevel connectivity phase portrait and cusp law

## Finding
Let \(\omega=e^{2\pi i/3}\), let \(a>0\), and define the singular inner function
\[
\Theta_a(z)=\exp[-F_a(z)],\qquad
F_a(z)=a\frac{1+z}{1-z}+\frac{\omega+z}{\omega-z}+\frac{\omega^2+z}{\omega^2-z},\quad z\in\mathbb D.
\]
For \(c>0\), write \(\Omega_{a,c}=\{z\in\mathbb D:|\Theta_a(z)|<e^{-c}\}=\{\operatorname{Re}F_a(z)>c\}\), and let \(N_a(c)\) be its number of connected components. Every component is simply connected. The **exact complete phase diagram**, including transition levels, is as follows.

For \(0<a<1\), put
\[
h_{\pm}(a)=\sqrt{\frac{20a+8-a^2\pm8(1-a)^{3/2}}3},\qquad 0<h_-(a)<h_+(a).
\]
Then
\[
N_a(c)=\begin{cases}3,&c\ge h_+(a),\\2,&h_-(a)\le c<h_+(a),\\1,&0<c<h_-(a).\end{cases}
\]
For \(a=1\), \(N_1(c)=3\) if \(c\ge3\), and \(N_1(c)=1\) if \(0<c<3\).

For \(a>1\), set
\[
h_0(a)=\sqrt{\frac{\sqrt{a(a+8)^3}+20a+8-a^2}{6}}.
\]
Then \(N_a(c)=3\) for \(c\ge h_0(a)\) and \(N_a(c)=1\) for \(0<c<h_0(a)\). In particular a two-component phase exists **if and only if** \(0<a<1\). At the symmetric collision of the two critical heights,
\[
\lim_{a\uparrow1}\frac{h_+(a)-h_-(a)}{(1-a)^{3/2}}=\frac89.
\]
The exponent \(3/2\) and coefficient \(8/9\) are sharp.

## Assumptions and scope
The three atoms lie at the cube roots of unity, with masses \(a,1,1\), and \(a>0\). The number \(N_a(c)\) counts open connected components at the **strict** sublevel threshold \(e^{-c}\), so the equality cases in the formulas above are part of the claim. This is a one-parameter geometric classification for singular inner functions; it does not classify arbitrary three-support atomic measures.

## Proof

**1. Rational covering and the component-count principle.** The root-of-unity identity gives
\[
F_a(z)=3\frac{1+z^3}{1-z^3}+(a-1)\frac{1+z}{1-z}.
\]
Since all three masses are strictly positive, \(\operatorname{Re}F_a>0\) on \(\mathbb D\), and the boundary values of \(F_a\) away from the atoms are purely imaginary. Consequently the Cayley transform \((F_a-1)/(F_a+1)\) is a finite Blaschke product of degree three: there is no pole cancellation because all three boundary residues are nonzero. Thus \(F_a:\mathbb D\to\{\operatorname{Re}w>0\}\) is a proper holomorphic map of degree three.

For each \(c>0\), its restriction \(F_a:\Omega_{a,c}\to\{\operatorname{Re}w>c\}\) is proper with total degree three. Each component of \(\Omega_{a,c}\) is simply connected: any simple closed curve in one component bounds a disk on which \(\operatorname{Re}F_a>c\), by the harmonic minimum principle; hence the bounded interior cannot contain a hole. A proper map of degree \(d\) from a simply connected planar component onto a half-plane has exactly \(d-1\) critical points counted with multiplicity, by the planar Riemann–Hurwitz formula (equivalently conjugate to a degree-\(d\) finite Blaschke product). Summing over components yields
\[
N_a(c)=3-\sum_{\substack{z\in\mathbb D,\ F'_a(z)=0\\\operatorname{Re}F_a(z)>c}}\operatorname{mult}_z(F'_a).
\tag{1}
\]
The inequality in (1) is strict. Thus a critical point lying **on** the level \(\operatorname{Re}F_a=c\) does not yet merge components, which determines the endpoint conventions.

**2. Critical points.** Differentiating the rational form gives
\[
F_a'(z)=\frac{2}{(1-z)^2}\left[a-1+\frac{9z^2}{(1+z+z^2)^2}\right].
\tag{2}
\]
Degree three entails exactly two interior critical points counted with multiplicity. For \(0<a<1\), solving \(3z/(1+z+z^2)=\pm\sqrt{1-a}\) shows that these two interior critical points are distinct and real: the function on the left increases strictly on \((-1,1)\), from \(-3\) to \(1\), and each target lies in \((-1,1)\). More directly its derivative is \(3(1-z^2)/(1+z+z^2)^2>0\) there. For \(a=1\), the only interior critical point is \(z=0\) of multiplicity two. For \(a>1\), no critical point is real and the two interior critical points form a conjugate pair.

**3. Exact critical heights.** Let \(w=F_a(z)\). Using the numerator–denominator representation
\[
F_a(z)=\frac{-(z+1)[a(z^2+z+1)+2z^2-4z+2]}{(z-1)(z^2+z+1)},
\]
the discriminant in \(z\) of the cubic equation \(F_a(z)=w\) is
\[
-3\left[9w^4+6(a^2-20a-8)w^2+a(a+8)^3\right].
\tag{3}
\]
The two possible squared critical values are therefore
\[
w^2=\frac{20a+8-a^2\pm8(1-a)^{3/2}}3,
\tag{4}
\]
where for \(a>1\), the last factor is interpreted as \(\pm i(a-1)^{3/2}\). For \(0<a<1\), both interior critical values are positive real numbers because the critical points lie in \((-1,1)\) and \(\operatorname{Re}F_a>0\). They have distinct heights \(h_-(a)\) and \(h_+(a)\). For \(a=1\), the unique interior critical value is \(F_1(0)=3\), counted twice. For \(a>1\), the interior critical values are a complex-conjugate pair, with equal positive real part. Taking the positive square root of \(w^2\) in (4) gives its real part as \(h_0(a)\), since
\[
\left|\frac{20a+8-a^2+8i(a-1)^{3/2}}3\right|=\frac{\sqrt{a(a+8)^3}}3.
\]
The component counts now follow immediately from (1).

**4. The cusp.** The squared heights satisfy \(h_+^2-h_-^2=16(1-a)^{3/2}/3\), while \(h_+(a)+h_-(a)\to6\) as \(a\uparrow1\). Hence \(h_+-h_-=(8/9)(1-a)^{3/2}+o((1-a)^{3/2})\), as claimed.

## Verification
The standalone `check.py` symbolically verifies identities (2)–(4), the discriminant and the squared-height gap, and numerically tests interior critical-point locations and height formulas at representative rational masses on both sides of \(a=1\). It separately checks the cusp coefficient. Run `python check.py` after installing the exact dependency in `requirements.txt`. These finite tests do not replace the analytic proof or establish global component counts by enumeration.

## Relationship to prior work
Looi's 2026 theorem characterizes when all bounded truncated Toeplitz operators admit bounded symbols by **existence** of a connected inner-function sublevel; it includes elementary degree-two Blaschke examples but not this exact three-atom phase portrait [1]. Nicolau–Reijonen already record the one-component property for any finite collection of positive atomic singular masses; that qualitative statement is strictly weaker than the present complete threshold classification [2]. Bickel–Gorkin's Lemma 2.1 establishes the analogous critical-point count for centered sublevels of finite Blaschke products, and its argument supplies an important precedent for step 1; neither the general count idea nor the one-component property is claimed as original here [3]. The assessed contribution is the explicit asymmetric three-atom threshold structure, the disappearance of its intermediate phase at the symmetric mass, and the exact \(3/2\) cusp law. Searches of the named sources and relevant mathematics records did not identify the complete formulas, although implicit coverage in older rational-map lemniscate literature remains a priority risk.

## Limitations
This theorem is restricted to three equispaced boundary masses \((a,1,1)\), with \(a>0\). It gives component counts, critical heights and the cusp, not a conformal parametrization of all components. No new qualitative one-component theorem is asserted; no independent audit has been performed. The self-review documents the scientific checks separately.

## References
[1] Sam Looi, *Bounded symbols and one-component geometry*, publicly available 2026-10-07; arXiv:2610.31382v1, https://arxiv.org/html/2610.31382v1.

[2] Artur Nicolau and Atte Reijonen, *A characterization of one-component inner functions*, Bulletin of the London Mathematical Society **53** (2021), 42–52, first published 2020-07-27, https://doi.org/10.1112/blms.12395.

[3] Kelly Bickel and Pamela Gorkin, *Blaschke Products, Level Sets, and Crouzeix's Conjecture*, arXiv:2112.06321v1 (2021), Lemma 2.1, https://arxiv.org/pdf/2112.06321.
