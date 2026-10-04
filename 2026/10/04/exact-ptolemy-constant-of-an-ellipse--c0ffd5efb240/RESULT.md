# Exact Ptolemy constant of an ellipse
## Finding
For an ellipse
\[
E_{a,b}=\{(a\cos t,b\sin t):0\le t<2\pi\},\qquad a\ge b>0,
\]
define the Ptolemy constant by
\[
P(E_{a,b})=\sup \frac{|A_1A_2|\,|A_3A_4|+|A_1A_4|\,|A_2A_3|}{|A_1A_3|\,|A_2A_4|},
\]
where the four distinct boundary points occur in cyclic order. Then
\[
P(E_{a,b})=\frac12\left(\frac{a}{b}+\frac{b}{a}\right)=\frac{a^2+b^2}{2ab}.
\]
The value is attained by the four axis endpoints \((a,0),(0,b),(-a,0),(0,-b)\).

## Assumptions and scope
The statement is for nondegenerate Euclidean ellipses in the plane. The semiaxes satisfy \(a\ge b>0\). The Ptolemy ratio uses Euclidean chord lengths and four distinct points in their cyclic boundary order. No uniqueness classification of maximizing quadruples is asserted.

The motivating 2016 work of Harmaala and Klén proved the bounds
\[
\frac12\left(\frac{a}{b}+\frac{b}{a}\right)\le P(E_{a,b})\le \frac1{\sin(\pi b/(2a))},
\]
and proved the angular-domain comparison used below. Finch subsequently reported symbolic and numerical evidence that the lower bound should be exact, while explicitly stating that a rigorous global verification was missing.

## Proof
Write
\[
r(t)=(a\cos t,b\sin t).
\]
Choose parameters
\[
t_1<t_2<t_3<t_4<t_1+2\pi,
\]
set \(t_5=t_1+2\pi\), and put \(g_i=t_{i+1}-t_i\) for \(1\le i\le4\). Thus every \(g_i>0\) and \(\sum_i g_i=2\pi\). Define side-midpoint parameters
\[
m_i=\frac{t_i+t_{i+1}}2,
\]
with \(m_5=m_1+2\pi\). The chord identity
\[
r(t_{i+1})-r(t_i)=2\sin\!\left(\frac{g_i}2\right)
\bigl(-a\sin m_i,b\cos m_i\bigr)
\]
shows that the oriented side direction is the angle of \((-a\sin m,b\cos m)\).

Let \(\psi\) be a continuous lift of that angle. Direct differentiation gives
\[
\psi'(m)=f(m):=\frac{ab}{a^2\sin^2m+b^2\cos^2m}>0,
\qquad \psi(m+\pi)=\psi(m)+\pi.
\]
The exterior turning angle from side \(i\) to side \(i+1\) is therefore
\[
\tau_i=\int_{m_i}^{m_{i+1}}f(m)\,dm.
\]
If the interior angles of the quadrilateral are \(\alpha_1,\ldots,\alpha_4\), then \(\alpha_{i+1}=\pi-\tau_i\) and \(\sum_i\tau_i=2\pi\). Hence
\[
\alpha_1+\alpha_3=\tau_1+\tau_3,
\qquad
\alpha_2+\alpha_4=\tau_2+\tau_4.
\]
Moreover,
\[
(m_2-m_1)+(m_4-m_3)=\frac12\sum_{i=1}^4g_i=\pi,
\]
and the same identity holds for the complementary pair of midpoint intervals. Thus each sum of opposite interior angles is the integral of \(f\) over a subset of a \(2\pi\)-period having total length \(\pi\).

We now prove the sharp integral bound. On one \(2\pi\)-period let
\[
H=\left[\frac\pi4,\frac{3\pi}4\right]\cup
\left[\frac{5\pi}4,\frac{7\pi}4\right].
\]
It has length \(\pi\). With
\[
T=\frac{2ab}{a^2+b^2},
\]
one has \(f\le T\) on \(H\) and \(f\ge T\) on its complement, because \(a\ge b\) and \(H\) is exactly the set where \(\sin^2m\ge\cos^2m\). For any measurable set \(S\) of length \(\pi\), the sets \(S\setminus H\) and \(H\setminus S\) have equal length, so
\[
\int_S f-\int_H f
=\int_{S\setminus H}(f-T)\,dm-
\int_{H\setminus S}(f-T)\,dm\ge0.
\]
A continuous antiderivative of \(f\) on an interval avoiding its branch cut is obtained from \(\arctan((a/b)\tan m)\). Accounting for the continuous branch across \(\pi/2\),
\[
\int_{\pi/4}^{3\pi/4}f(m)\,dm
=\pi-2\arctan(a/b)=2\arctan(b/a).
\]
Therefore
\[
\int_H f(m)\,dm=4\arctan(b/a).
\]
It follows that both opposite-angle sums satisfy
\[
\alpha_1+\alpha_3\ge4\arctan(b/a),
\qquad
\alpha_2+\alpha_4\ge4\arctan(b/a).
\]

For any convex quadrilateral, Harmaala and Klén's Proposition 4.1 gives the angular Ptolemy bound
\[
p\le\frac1{\sin((\alpha_1+\alpha_3)/2)}.
\]
Because the two opposite-angle sums add to \(2\pi\), this denominator depends only on their smaller sum. Let
\[
s=\min\{\alpha_1+\alpha_3,\alpha_2+\alpha_4\}\le\pi.
\]
The preceding estimate gives \(s\ge4\arctan(b/a)\). Since \(1/\sin(x/2)\) decreases on \((0,\pi]\),
\[
p\le\frac1{\sin(s/2)}
\le\frac1{\sin(2\arctan(b/a))}
=\frac{a^2+b^2}{2ab}.
\]
This proves the global upper bound.

For the four axis endpoints, all four side lengths equal \(\sqrt{a^2+b^2}\), while the diagonals have lengths \(2a\) and \(2b\). Their Ptolemy ratio is therefore
\[
\frac{2(a^2+b^2)}{4ab}=\frac{a^2+b^2}{2ab},
\]
so the upper bound is attained and the formula is exact.

## Verification
The proof is analytic and covers every cyclically ordered boundary quadruple. The key new ingredient is the sharp opposite-angle lower bound obtained from the side-direction derivative \(f\) and the length-\(\pi\) threshold-set argument. The published angular Ptolemy comparison was checked in the full text of Harmaala and Klén.

The bundled script `verify.py` checks the exact axis-endpoint value and the identity
\[
\frac1{\sin(2\arctan(b/a))}=\frac{a^2+b^2}{2ab},
\]
and performs deterministic random stress tests of both the opposite-angle lower bound and the final Ptolemy bound for several aspect ratios. These finite tests are diagnostic only and are not used as an infinite proof.

## Relationship to prior work
Harmaala and Klén introduced the relevant explicit ellipse bounds and proved the general angular Ptolemy estimate. Their Theorem 4.11 leaves a nonzero gap for every nonspherical ellipse. The first public version is dated 2016-04-18 and lists MSC 51M05 first.

Finch studied exactly the same ellipse optimization later in 2016. He reported symbolic Hessian calculations and numerical optimization suggesting that the four axis endpoints give the global maximum, but stated that he did not see how to verify global maximality rigorously. The formula above is exactly the lower-bound value that Finch identified conjecturally. The present argument supplies the missing global proof by converting the problem to a sharp rearrangement bound for opposite-angle turning.

## Limitations
The theorem is specific to planar Euclidean ellipses. It does not determine Ptolemy constants of rectangles, regular hexagons, Reuleaux triangles, arbitrary convex quadrilaterals, or higher-dimensional analogues. It also does not classify every maximizing quadruple. Unindexed or differently phrased prior work remains a residual originality risk; in particular, the older unpublished Seittenranta thesis cited by Harmaala and Klén was not independently inspected here, although the later full paper that builds on it still states only bounds for ellipses.

## References
1. E. Harmaala and R. Klén, “Ptolemy constant and uniformity,” arXiv:1604.05367v1, first submitted 2016-04-18; revised arXiv version 2020; later published in *Publicationes Mathematicae Debrecen* 98 (2021), 15–42, DOI 10.5486/PMD.2021.8746.
2. S. Finch, “Ptolemy Constants as Described by Eccentricity,” arXiv:1608.04299v1, submitted 2016-08-12.
