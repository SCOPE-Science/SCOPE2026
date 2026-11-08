# A dense rational-resonance area spike law for a no-trade center region

## Finding

The area of the **maximal closed all-neutral itinerary region** at the conservative center of the three-partition stock-market map of Gardini, Radi, Schmitt, Sushko, and Westerhoff has an exact arithmetic phase diagram. Fix real \(h>0\), \(d>h\), \(b=1\), and \(0<c<4\). Let
\[
J_c=\begin{pmatrix}2-c&-1\\1&0\end{pmatrix},\qquad
K_{c,h}=\bigcap_{k=0}^{\infty}\{z\in\mathbb R^2: |(1,-1)J_c^kz|\le h\}.
\]
Thus \(K_{c,h}\) is the largest closed set of initial states whose iterates under the central linear branch never leave the closed no-trade strip; for the full piecewise-affine map, it is the maximal closed all-neutral itinerary component. Define
\[
\alpha(c)=\frac1{2\pi}\arccos(1-c/2)\in(0,1/2),\qquad
A_*(c,h)=\frac{\pi h^2}{2}\sqrt{\frac{4-c}{c}}.
\]
If \(\alpha(c)\) is irrational, \(K_{c,h}\) is an ellipse and \(\operatorname{Area}(K_{c,h})=A_*(c,h)\). If \(\alpha(c)=a/n\) in lowest terms, \(0<a/n<1/2\), let \(L=n\) for even \(n\) and \(L=2n\) for odd \(n\). Then \(K_{c,h}\) is an affine image of a regular \(L\)-gon and
\[
\boxed{\operatorname{Area}(K_{c,h})=
\frac{h^2}{2}\sqrt{\frac{4-c}{c}}\,L\tan\!\frac{\pi}{L}.}
\]

Consequently, the area as a function of \(c\) is **continuous exactly at irrational rotation numbers** and has an upward, pointwise spike at every rational rotation number. At each rational point the limit along distinct nearby parameters exists and equals \(A_*(c,h)\). The relative spike height depends only on the number of polygon sides:
\[
\frac{\operatorname{Area}(K_{c,h})-A_*(c,h)}{A_*(c,h)}
=\frac L\pi\tan\!\frac\pi L-1
=\frac{\pi^2}{3L^2}+O(L^{-4})\quad(L\to\infty).
\]
For example, at \(c=2\), \(\alpha=1/4\), \(L=4\), the exact area is \(2h^2\), while its punctured-parameter limit is \(\pi h^2/2\); the ratio is \(4/\pi\). At \(c=3\), the area is \(h^2\) and \(L=6\). At \(c=1\), the area is \(3h^2\) and \(L=6\).

## Assumptions and scope

The source's three-partition map has its central branch \(T_O(x,y)=J_c(x,y)\) when \(|x-y|\le h\), with its outer branches translated by \((\pm d,0)\). Here \(b=1\) and \(d>h>0\) are fixed throughout. The closed weak inequalities in the definition of \(K_{c,h}\) agree with the central-branch convention on the switching lines. Using strict inequalities instead changes at most the boundary and not the area. The result measures **two-dimensional Lebesgue area in the original \((x,y)\) coordinates**, not area in a dynamically normalized coordinate system, not an attraction basin, and not a probability of eventual return after taking an outer branch. The theorem does not classify dynamics outside this all-neutral set.

## Proof

**1. A positive-definite invariant quadratic form.** Put \(t=2-c\). The symmetric matrix
\[
Q_c=\begin{pmatrix}1&-t/2\\-t/2&1\end{pmatrix}
\]
has \(\det Q_c=c(4-c)/4>0\), and direct multiplication gives
\[
J_c^{\mathsf T}Q_cJ_c=Q_c.
\]
Thus, under the invertible linear change \(w=Q_c^{1/2}z\), the matrix \(J_c\) acts as a Euclidean rotation. Its determinant is \(1\) and its trace is \(2-c=2\cos\theta\), so the unsigned rotation angle satisfies \(\theta=\arccos(1-c/2)\in(0,\pi)\). Its orientation sign is immaterial because all iterates are used. Note that \(\alpha=\theta/(2\pi)\).

**2. Exact radius of the transformed strip.** Let \(v=(1,-1)\). The central-branch constraint is \(|vz|\le h\). Its normal in \(w\)-coordinates is \(vQ_c^{-1/2}\). An exact inverse-matrix calculation yields
\[
vQ_c^{-1}v^{\mathsf T}=\frac4{4-c}.
\]
Consequently, the transformed strip is \(|\nu\cdot w|\le r\) for a unit normal \(\nu\) and
\[
r=\frac{h\sqrt{4-c}}2.
\]
Every future no-trade condition is the same strip rotated by an integer multiple of \(\theta\). Therefore \(Q_c^{1/2}K_{c,h}\) is precisely the intersection of strips of inradius \(r\) whose normals have orientations \(k\theta\), interpreted up to the sign of the normal.

**3. Irrational rotation.** If \(\alpha\) is irrational, the normal directions are dense in the unit circle. By continuity of the scalar product, the infinitely many strip inequalities hold if and only if \(|w|\le r\). Thus \(K_{c,h}=\{z:z^{\mathsf T}Q_cz\le r^2\}\). Its area is the disk area \(\pi r^2\) divided by the determinant \(\det(Q_c^{1/2})=\sqrt{\det Q_c}\), giving \(A_*(c,h)\).

**4. Rational rotation.** If \(\alpha=a/n\) is reduced, the cyclic normal directions together with their negatives comprise the vertices of a regular \(L\)-gon on the unit circle, with \(L=n\) if \(n\) is even and \(L=2n\) if \(n\) is odd. The intersection of the corresponding supporting half-planes at distance \(r\) from the origin is a regular \(L\)-gon with inradius \(r\). Its area equals \(Lr^2\tan(\pi/L)\), obtained by decomposing into \(L\) isosceles triangles of base \(2r\tan(\pi/L)\) and height \(r\). Transforming back multiplies area by \(1/\sqrt{\det Q_c}\) and yields the boxed formula. Since \(J_c\) permutes these finitely many constraints, the set is invariant and is the complete closed all-neutral itinerary set, rather than just an invariant subset.

**5. Continuity and the resonant spikes.** For every \(L\ge4\), \(\tan(\pi/L)>\pi/L\). Thus rational rotation produces strictly greater area than the same-parameter ellipse expression. As \(L\to\infty\), \(L\tan(\pi/L)\to\pi\); the Taylor series gives the displayed relative excess. A convergent sequence of distinct reduced rational numbers with bounded denominators is impossible, hence denominators at rational points approaching any fixed parameter must diverge, apart from repetitions of that fixed point. Continuity of \(A_*(c,h)\) therefore proves that the punctured-parameter limit of the full area at every \(c\in(0,4)\) equals \(A_*(c,h)\). At irrational \(\alpha\), actual area equals the limit; at rational \(\alpha\), it exceeds the limit. The rational parameters are dense and countable because \(c=2(1-\cos(2\pi\alpha))\) is a continuous strictly increasing bijection of \((0,1/2)\) onto \((0,4)\).

**6. Boundaries and quantifiers.** Every claim above holds for every real \(d>h>0\) and every \(c\in(0,4)\), with rationality interpreted for the exact real \(\alpha(c)\). No uniform assertion is made at \(c=0\) or \(c=4\), where the quadratic form degenerates. The closed set is bounded because the transformed strips have normals spanning the plane. Its polygonal or elliptical boundary has zero two-dimensional Lebesgue measure, so any boundary convention for switching affects no area conclusion.

## Verification

The included standard-library program `check_area.py` computes the exact rational identity \(J_c^{\mathsf T}Q_cJ_c=Q_c\) for several exact parameter values, checks the exact determinant, independently constructs tangential regular polygons by their vertices for \(134\) reduced rational rotation angles, and compares their shoelace areas with the formula in physical coordinates. It also checks \(\operatorname{Area}=2h^2,h^2,3h^2\) at the three integer benchmark parameters \(c=2,3,1\), respectively. These are finite cross-checks only; the preceding analytic argument proves the universally quantified result.

Run: `python3 check_area.py` from the directory containing this result and the program. Expected terminal marker: `STOCK_CENTER_AREA_EXACT_Q_AND_POLYGON_OK angles=134`.

## Relationship to prior work

Gardini et al. (2023), especially equations (7)--(11) and Section 4.7, introduce the piecewise-affine stock-market map, identify its conservative center at \(b=1\), and establish qualitative invariant ellipses for irrational rotation and polygons with \(n\) or \(2n\) sides for rational rotation. This structural classification is **credited as prior work**. The present result is the **metric refinement**: exact original-coordinate area for all parameters, the denominator-only relative spike, its asymptotic, and the precise pointwise continuity/discontinuity set of that natural area observable. The source's qualitative polygon/ellipse statement does not itself state this area law.

Sushko and Gardini (2008), Section 3 and Propositions 1--2, provide earlier center-bifurcation polygons and ellipses in a related two-piece normal form. That general geometric antecedent does not compute this three-piece stock-market model's exact physical-coordinate area or the everywhere-dense rational spike profile. These works demonstrate that polygon-versus-ellipse geometry alone is not claimed as novel.

## Limitations

This is a theoretical exact center-line statement, not an assertion about real market data or the economic welfare of a particular initial-price distribution. It does not measure an attracting basin or dynamics for \(b\ne1\) or for orbits that visit an outer partition. An equal-width coordinate change alters physical area, so the formula is explicitly tied to the published \((x,y)\) coordinates. The prior-literature search cannot exclude an unindexed derivation of the same area profile. No independent mathematical audit has been performed.

## References

1. L. Gardini, D. Radi, N. Schmitt, I. Sushko, F. Westerhoff, “A 2D piecewise-linear discontinuous map arising in stock market modeling: Two overlapping period-adding bifurcation structures,” *Chaos, Solitons & Fractals* 176 (2023), 114143. First publicly available online 2023-10-12. DOI: 10.1016/j.chaos.2023.114143. Open full text: https://doi.org/10.1016/j.chaos.2023.114143 ; author-hosted full text https://www.researchgate.net/publication/374739774_A_2D_piecewise-linear_discontinuous_map_arising_in_stock_market_modeling_Two_overlapping_period-adding_bifurcation_structures .
2. I. Sushko, L. Gardini, “Center Bifurcation for Two-Dimensional Border-Collision Normal Form,” *International Journal of Bifurcation and Chaos* 18 (2008), 1029--1050. DOI: 10.1142/S0218127408020823. Author-hosted full text: https://www.mdef.it/public/fileadmin/whoiswho/gardini/Publications/Journals/SG_CenterBif_08.pdf .
