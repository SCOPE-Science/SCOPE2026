# A unique inverse-power two-cycle and its sharp stability boundary

## Finding

Consider the positive scalar discrete-time map
\[
F_{a,b,p}(x)=a x+\frac{b}{x^p},\qquad x>0,
\]
with \(0<a<1\), \(b>0\), and \(p>1\). A *primitive two-cycle* is an unordered pair of distinct positive numbers \(\{x,y\}\) such that \(F_{a,b,p}(x)=y\) and \(F_{a,b,p}(y)=x\).

**Theorem (complete primitive two-cycle classification and quadratic-inverse stability).** For every \(p>1\), \(a\in(0,1)\), and \(b>0\), a primitive two-cycle exists **if and only if**
\[
0<a<\frac{p-1}{p+1}.
\]
When it exists, the unordered cycle is **unique**. Its ratio \(r=y/x>1\) is the unique solution of
\[
a=\frac{r^p-r}{r^{p+1}-1},\qquad r>1,
\]
and its coordinates are
\[
x=\left(\frac{b}{r-a}\right)^{1/(p+1)},\qquad y=rx.
\]

For \(p=2\), let \(0<a<1/3\), and define
\[
S=\left(\frac{b(1+a)}{a^2}\right)^{1/3},\qquad
\eta=\sqrt{\frac{1-3a}{1+a}},\qquad x_\pm=\frac S2(1\pm\eta).
\]
The **only** primitive two-cycle is \(\{x_-,x_+\}\), with exact two-step derivative
\[
\boxed{(F_{a,b,2}^2)'(x_-)=9a^2+6a-2.}
\]
Writing \(a_{\mathrm{crit}}=(\sqrt 2-1)/3\), this two-cycle is locally asymptotically attracting when \(a_{\mathrm{crit}}<a<1/3\), is repelling when \(0<a<a_{\mathrm{crit}}\), and has multiplier \(-1\) at \(a=a_{\mathrm{crit}}\). The last assertion is a neutral *linearization statement only*, not a nonlinear stability classification. At \(a=1/3\), the two-cycle coalesces with the unique fixed point and no longer is primitive. The transition locations and two-cycle multiplier are independent of \(b\).

## Assumptions and scope

All variables and parameters are real. The phase space is \((0,\infty)\), the map is iterated discretely, \(0<a<1\) and \(b>0\), and the general classification assumes \(p>1\). The sole stability assertion concerns \(p=2\). Local asymptotic attraction means attraction for every sufficiently near starting point to the two-cycle under the second iterate; repelling means the corresponding multiplier has modulus larger than one. No assertion is made for global attraction, other periods, invariant probabilities, or the neutral nonlinear behavior at either boundary.

A separate fixed point exists for all these parameters:
\[
x_*=(b/(1-a))^{1/(p+1)},\qquad F'_{a,b,p}(x_*)=(p+1)a-p.
\]
For the quadratic-inverse case it is locally attracting when \(1/3<a<1\) and repelling when \(0<a<1/3\); its derivative is \(-1\) at the common cycle-creation boundary \(a=1/3\).

## Proof

**1. Two-cycle ratio identity.** Suppose \(x<y\) is a primitive two-cycle and write \(r=y/x>1\). The equations \(y=a x+b/x^p\) and \(x=a y+b/y^p\) are exactly equivalent to
\[
b=x^{p+1}(r-a)=x^{p+1}r^p(1-ar).
\]
Eliminating the positive scalar \(b/x^{p+1}\) gives
\[
a(r^{p+1}-1)=r^p-r.
\]
Conversely, any \(r>1\) satisfying this identity yields \(r-a>0\) because \(0<a<1\). Taking \(x=(b/(r-a))^{1/(p+1)}\) and \(y=rx\) satisfies both cycle equations, so the ratio equation is also sufficient. As the pair is unordered, restricting to \(r>1\) loses no cycles.

**2. Exact existence and uniqueness for all \(p>1\).** Put \(r=e^{2t}\), with \(t>0\). Cancellation of positive exponentials rewrites the ratio equation as
\[
a=R_p(t):=\frac{\sinh((p-1)t)}{\sinh((p+1)t)}.
\]
Set \(H(u)=u\coth u\) for \(u>0\). Then
\[
H'(u)=\frac{\sinh u\cosh u-u}{\sinh^2u}>0,
\]
since the numerator vanishes at zero and has derivative \(2\sinh^2u>0\). Therefore
\[
\frac{R_p'(t)}{R_p(t)}=
\frac{H((p-1)t)-H((p+1)t)}t<0.
\]
Moreover \(\lim_{t\downarrow0}R_p(t)=(p-1)/(p+1)\) and \(\lim_{t\to\infty}R_p(t)=0\). Continuity and strict decrease prove that the equation \(a=R_p(t)\) has one solution exactly for \(0<a<(p-1)/(p+1)\), and none at or above that threshold. Step 1 now proves existence and uniqueness of the positive primitive two-cycle with its stated coordinates.

**3. Explicit cycle for \(p=2\).** For a primitive pair set \(S=x+y\) and \(P=xy\). The ratio identity simplifies to \(a=xy/(x^2+xy+y^2)\), hence
\[
P=\frac{aS^2}{1+a}.
\]
Adding \(b=x^2(y-ax)\) and \(b=y^2(x-ay)\) yields
\[
2b=PS-a(S^3-3PS)=\frac{2a^2S^3}{1+a}.
\]
Thus \(S=(b(1+a)/a^2)^{1/3}\), and the two roots of \(z^2-Sz+P=0\) are precisely \(x_-\) and \(x_+\). The discriminant is \(S^2(1-3a)/(1+a)\), positive exactly for \(0<a<1/3\). This also checks positivity and excludes an extraneous root.

**4. Two-step multiplier and its strict regimes.** At each point of this cycle, \(b=x^2(y-ax)\) gives
\[
F'_{a,b,2}(x)=a-\frac{2b}{x^3}=3a-2\frac yx.
\]
Similarly \(F'_{a,b,2}(y)=3a-2x/y\). The cycle identity gives \(r+r^{-1}=a^{-1}-1\), so
\[
F'_{a,b,2}(x)F'_{a,b,2}(y)
=9a^2-6a(r+r^{-1})+4=9a^2+6a-2.
\]
This increasing polynomial has value \(-2\) as \(a\downarrow0\), equals \(-1\) exactly at \(a=(\sqrt2-1)/3\), and tends to \(1\) as \(a\uparrow1/3\). Consequently the multiplier has modulus less than one precisely in \(((\sqrt2-1)/3,1/3)\), and is smaller than \(-1\) below this interval. The one-dimensional contraction/expansion criterion for the second iterate proves the stated hyperbolic local stability and repulsion. The neutral boundary is expressly excluded from a nonlinear conclusion.

## Verification

`checker.py` uses only Python's standard library. Run it with `python3 checker.py` in the directory containing this document. It checks exactly, using rational arithmetic, that for 1,771 rational parameterizations of primitive cycles with integer powers \(2\) through \(8\), the two equations hold, the existence inequality is strict, and (for \(p=2\)) the multiplier equals the quadratic polynomial. It additionally checks 28 numerical instances of the explicit square-root formula and 5 finite grids for monotonicity. On the packaged run it reported **PASS: 1804 exact-rational/float finite diagnostics.** These are finite checks only. The exact continuum classifications, uniqueness, and sharp thresholds are proved in the preceding four steps.

## Relationship to prior work

Le Van, Nguyen-Trong, Pham, and Pham study a semi-endogenous innovation model and, for zero direct R&D influence on the innovation law, arrive at the scalar map \(x\mapsto ax+b x^{\gamma_a}\). Their Proposition 5 and Appendix A.2 prove a *sufficient* condition for existence of a two-period innovation cycle when \(\gamma_a<-1\), namely \(a<(p-1)/(p+1)\) after the substitution \(p=-\gamma_a\); they neither claim this condition is necessary nor classify the number or stability of such cycles. The present finding retains that threshold as prior knowledge and adds the converse, uniqueness, coordinates, and a second exact local-stability transition in the quadratic-inverse case. The same source explicitly notes that existence of cycles does not establish attraction.

Abdelrahman, Chatzarakis, Li, and Moaaz analyze delayed recurrences with a nonlinear term homogeneous of degree **zero** in two lagged variables. Their period-two theorems concern different delay parities and cannot cover the inverse-power term of degree \(-p\) in this single-state recurrence. Classical one-dimensional multiplier tests are standard and are used here, not presented as a novel principle. The claimed new content is the *specific exact classification and boundary*, not the general test for local stability.

## Limitations

This theorem classifies only positive primitive two-cycles, not all periodic orbits; smaller persistence parameters may permit higher periods or chaotic behavior. The stability partition is explicit only for exponent \(p=2\), and at multiplier \(-1\) no nonlinear attraction, repulsion, or period-doubling direction is asserted. The conclusions hold for the standalone one-dimensional reduced map and are not automatically a classification of the full two-state economic model when the scalar reduction does not apply. Equivalent exact statements in older difference-equation literature cannot be excluded by database search alone.

## References

1. C. Le Van, T. Nguyen-Trong, N.-S. Pham, and T. K. C. Pham, *From Balanced Growth to Innovation Cycles: A Solow-Type Semi-Endogenous Growth Model*, arXiv:2610.01610v1 (first posted 2026-10-01), Proposition 5 and Appendix A.2. https://arxiv.org/pdf/2610.01610
2. M. A. E. Abdelrahman, G. E. Chatzarakis, T. Li, and O. Moaaz, *On the difference equation \(x_{n+1}=a x_{n-l}+b x_{n-k}+f(x_{n-l},x_{n-k})\)*, *Advances in Difference Equations* **2018**, article 431, especially Sections 1, 3, and 4. https://doi.org/10.1186/s13662-018-1880-8
3. S. Elaydi, *Discrete Chaos: With Applications in Science and Engineering*, second edition, CRC Press (2007). Cited for standard local multiplier stability principles only.
