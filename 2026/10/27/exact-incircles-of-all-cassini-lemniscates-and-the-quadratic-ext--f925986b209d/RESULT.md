# Exact incircles of all Cassini lemniscates and the quadratic extremal radius

## Finding
For each real \(s\ge0\), define the strict quadratic lemniscate
\[
\Omega_s=\{z\in\mathbb C:|z^2-s^2|<1\},\qquad
\rho(s)=\sup\{r>0:\exists c\in\mathbb C,\ B(c,r)\subset\Omega_s\}.
\]
Then the exact unrestricted inradius for **every** separation is
\[
\boxed{\rho(s)=\begin{cases}
\sqrt{1-s^2},&0\le s\le 1/\sqrt2,\\
1/(2s),&s\ge1/\sqrt2.
\end{cases}}
\]
Every center of a disk of this maximal radius is classified: for \(0\le s\le1/\sqrt2\), the only center is \(0\); for \(s>1/\sqrt2\), the centers are precisely
\[
\boxed{c_\pm(s)=\pm\sqrt{s^2-\frac{1}{4s^2}}.}
\]
Thus the largest inscribed disk undergoes a one-center to two-center bifurcation at \(s=1/\sqrt2\). The displacement has the exact onset law
\[
|c_\pm(s)|=2^{3/4}\sqrt{s-1/\sqrt2}+O((s-1/\sqrt2)^{3/2})
\quad (s\downarrow1/\sqrt2).
\]
The formula covers the convex single-loop, necked single-loop, and disconnected two-loop Cassini regimes without changing its hypotheses.

**Quadratic-polynomial consequence.** Let \(p(z)=(z-a)(z-b)\) be any monic quadratic, and set \(s=|a-b|/2\). Its strict unit lemniscate has inradius \(\rho(s)\) above; its maximal disk centers are obtained by translating the stated centers by \((a+b)/2\) and rotating them in the direction \(a-b\). In particular, among monic quadratics whose zeros both lie in the closed unit disk,
\[
\boxed{\inf_{|a|,|b|\le1}\rho((z-a)(z-b))=\frac12.}
\]
Equality holds **exactly** when \(a\) and \(b\) are antipodal points on the unit circle, equivalently when \(p(z)=z^2-e^{2i\phi}\) for a real angle \(\phi\).

## Assumptions and scope
All disks are open Euclidean disks. The inradius uses the strict sublevel set, permits any center, and means a supremum; the displayed disks attain that radius. No restriction on \(s\) other than \(s\ge0\) is imposed for the geometric theorem. The coefficient of the polynomial is monic and the level is exactly \(1\); other positive levels follow by elementary scaling. The standard primary complex-analytic problem restricts both zeros to \(|z|\le1\), hence \(s\le1\), but the geometric result is valid also for disjoint Cassini lobes.

## Proof
**1. Universal height identity and sharp strips.** Write \(z=x+iy\), where \(x,y\in\mathbb R\). Direct expansion gives the exact identity
\[
|z^2-s^2|^2=(x^2+y^2-s^2)^2+4s^2y^2. \tag{1}
\]
If \(s\ge1/\sqrt2\), (1) implies for every \(z\in\Omega_s\) that
\[
|y|<\frac1{2s}. \tag{2}
\]
If \(0\le s\le1/\sqrt2\) and \(y^2\ge1-s^2\), then \(y^2\ge s^2\); the right side of (1) is at least
\[
(y^2-s^2)^2+4s^2y^2=(y^2+s^2)^2\ge1.
\]
Thus in this range every point of \(\Omega_s\) satisfies
\[
|y|<\sqrt{1-s^2}. \tag{3}
\]
Any open disk of radius \(r\) lying in a horizontal strip \(|y|<H\) has \(r\le H\), regardless of where its center is. Equations (2)–(3) therefore prove the proposed upper bound for the unrestricted inradius.

**2. The centered branch attains the bound.** Suppose \(0\le s\le1/\sqrt2\), and set \(r=\sqrt{1-s^2}\). If \(|z|<r\), then
\[
|z^2-s^2|\le |z|^2+s^2<r^2+s^2=1.
\]
Consequently \(B(0,r)\subset\Omega_s\). Together with (3), this gives \(\rho(s)=r\).

**3. The displaced branch attains the bound.** Suppose \(s>1/\sqrt2\), and put
\[
r=\frac1{2s},\qquad c=\sqrt{s^2-r^2}>0.
\]
On the boundary \(z=c+re^{it}\) of the proposed disk, one has
\[
\begin{aligned}
z^2-s^2&=r^2(e^{2it}-1)+2cre^{it}\\
&=2re^{it}(c+ir\sin t),
\end{aligned}
\]
and hence
\[
|z^2-s^2|^2=4r^2(c^2+r^2\sin^2t)
\le4r^2(c^2+r^2)=4r^2s^2=1. \tag{4}
\]
The nonconstant analytic polynomial \(z^2-s^2\) is therefore strictly bounded by \(1\) throughout the open disk by the maximum-modulus principle. Thus \(B(c,r)\subset\Omega_s\), and (2) gives \(\rho(s)=r\). Replacing \(c\) by \(-c\) gives a second maximizing disk. At the junction \(s=1/\sqrt2\), the centered construction already applies and \(c=0\).

**4. There are no other maximal-disk centers.** Let \(B(c,\rho(s))\subset\Omega_s\), where \(c=u+iv\). Since \(\Omega_s\) lies inside a horizontal strip of half-height exactly \(\rho(s)\), the disk's vertical projection forces \(v=0\). Its top point \(u+i\rho(s)\) belongs to the closure of \(\Omega_s\), so it satisfies \(|(u+i\rho(s))^2-s^2|\le1\). In the centered branch, equality in the inequalities leading to (3), at \(y^2=1-s^2\), is possible only if \(u=0\). In the displaced branch, \(4s^2\rho(s)^2=1\), so (1) implies \(u^2+\rho(s)^2-s^2=0\). Thus \(u=\pm\sqrt{s^2-1/(4s^2)}\), and both signs were constructed in step 3. This exhausts all centers.

**5. Critical law and quadratic rigidity.** Put \(s_0=1/\sqrt2\). For \(s>s_0\), expansion of \(s^2-1/(4s^2)\) around \(s_0\) has first derivative \(2\sqrt2\); taking square roots yields the stated onset law. For a monic quadratic, translate by \((a+b)/2\) and rotate by the argument of \((a-b)/2\) to reduce its modulus to \(|z^2-s^2|\). If \(|a|,|b|\le1\), the triangle inequality gives \(s\le1\). The two branches of \(\rho(s)\) are strictly decreasing for positive \(s\), so \(\rho(s)\ge\rho(1)=1/2\), with equality only at \(s=1\). Equality \(|a-b|=2\) with both points in the closed unit disk forces \(a=-b\) and \(|a|=|b|=1\) by equality in the triangle inequality. This gives the unique extremal polynomial family stated in the finding. \(\square\)

## Verification
The proof depends on the exact quartic identity (1), the exact circle-boundary factorization (4), and a strip extremal argument for *all* potential disk centers. A standalone standard-library checker, `verify.py`, evaluates the quartic identity exactly at 2,025 rational planar configurations and checks the boundary trigonometric polynomials via rational squared-separation parameters on both sides of the transition. It also performs 9,360 supplemental floating-point boundary evaluations. Run `python3 verify.py` beside this file. These finite checks are independent computations of algebraic identities, not a replacement for the continuum proof or a proof of historical originality.

## Relationship to prior work
Geng and Qiu (arXiv:2609.06461v1, 6 September 2026, sections 1–2 and main theorem) established the sharp **asymptotic** universal degree-dependent inradius for polynomial lemniscates, and emphasized the classical model with uniformly spaced unit-circle zeros. They did not state the full two-root separation profile or classify all its maximizing centers.

The published open research note *Exact finite-degree inradius of the roots-of-unity lemniscate* determines the inradius of \(z^n-1\) for every positive integer \(n\), including the special value \(\rho(z^2-1)=1/2\). That model result does not imply a lower bound for *all* monic quadratics, does not calculate the dependence on arbitrary two-root separation, and does not classify the one-to-two transition of inball centers. The overlap at the antipodal model is acknowledged rather than presented as new.

Rabinowitz's 2025 Cassini-oval survey establishes the classical shapes and cites the convexity change at the same normalized focus threshold; its Theorem 33 constructs a doubly tangent auxiliary circle, but neither its stated conclusion nor the surveyed inradius terminology establishes that such a circle is contained, globally maximal, or exhausts all maximal-center configurations. The inspected MathWorld entry gives the equation and topology, not the optimal inballs. Thus the contribution here is the complete sharp **inradius-and-center phase diagram** for all Cassini level sets, with the unit-root quadratic extremal problem as a consequence.

## Limitations
The theorem treats degree-two monic polynomials and classical two-focus Cassini lemniscates, not higher-degree arbitrary polynomials. It does not claim that roots of unity always minimize the inradius at higher finite degrees. The matching geometric transition is elementary once the key quartic identity and maximal circles are found; no broader inverse theorem follows. Classical geometry may contain an equivalent formula under alternative terminology (largest contained circle, maximal inscribed circle, Cassinian oval); the cited bibliographic search and surveyed sources reduce but do not eliminate this historical-priority risk. One potentially related 2024 paper on symmetrical Cassini structures was available by title/abstract but its full article returned an access error, so no noncoverage conclusion is drawn from it. Independent mathematical validation has not been performed.

## References
1. Y. Geng and D. Qiu, *From \(\log 2\) to \(\pi/2\): the sharp asymptotic inradius of polynomial lemniscates*, arXiv:2609.06461v1 (first public 6 September 2026), https://arxiv.org/abs/2609.06461.
2. *Exact finite-degree inradius of the roots-of-unity lemniscate*, published research note (October 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-finite-degree-inradius-of-the-roots-of-unity-lemniscate--c99a919f0262.
3. S. Rabinowitz, *Geometric Properties of a Cassini Oval*, International Journal of Computer Discovered Mathematics **10** (2025), 325–348, https://www.journal-1.eu/2025/65.%20Stanley%20Rabinowitz.%20Geometric%20Properties%20of%20a%20Cassini%20Oval,%20pp.%20325-348..pdf.
4. E. W. Weisstein, *Cassini Ovals*, MathWorld, https://mathworld.wolfram.com/CassiniOvals.html.
5. P. Grabusts, *Applications of the Symmetrical Structures of Cassini Ovals*, Symmetry **16** (2024), article 334, https://doi.org/10.3390/sym16030334 (title and abstract accessible; main text not inspected).
