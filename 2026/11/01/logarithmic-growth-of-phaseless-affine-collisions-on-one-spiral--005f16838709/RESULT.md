# Logarithmic growth of phaseless affine collisions on one spiral

## Finding

Fix a real number \(\alpha\ne0\) and the outward logarithmic spiral
\[
\Gamma_\alpha^+=\{z(t)=e^{(1+i\alpha)t}:t\ge0\}.
\]
For every \(s>0\), set \(\kappa=\sinh(2s)\) and consider the distinct degree-one polynomials
\[
P_s(z)=\cosh(s)z+\sinh(s),\qquad
Q_s(z)=\sinh(s)z-\cosh(s).
\]
They have equal magnitudes at exactly \(N_\alpha(\kappa)\) points of the spiral with strictly positive parameter, where \(N_\alpha(\kappa)\) is finite and
\[
\boxed{N_\alpha(\kappa)=\frac{|\alpha|}{\pi}\operatorname{arsinh}\kappa+O_\alpha(1)
=\frac{|\alpha|}{\pi}\log(2\kappa)+O_\alpha(1).}
\]
Here the constant in \(O_\alpha(1)\) may depend on fixed \(\alpha\), but not on \(\kappa\). Consequently, **there is no universal finite number of arbitrarily placed phaseless samples** on this spiral that recovers all complex polynomials of degree at most one up to global phase. This remains true although every polynomial is determined up to global phase by its magnitude on the entire spiral.

## Assumptions and scope

The exponent \(\alpha\) is an arbitrary fixed nonzero real number, the polynomial coefficients are arbitrary complex numbers, and measurements are exact and individually labelled. Coincidence points are distinct values of \(t>0\), not zeros counted with multiplicity. The collision asymptotic uses the one-parameter family above; it does not assert that this family maximizes the number of collisions among all affine polynomial pairs. The impossibility statement quantifies over every integer sample budget and **some adversarial choice** of that many distinct spiral points, not over every choice of sites.

## Proof

**1. Exact coincidence identity.** Put \(a=\cosh s\), \(b=\sinh s\). As \(a^2-b^2=1\), direct expansion gives, for every complex \(z\),
\[
|az+b|^2-|bz-a|^2=|z|^2-1+4ab\operatorname{Re}z
=|z|^2-1+2\kappa\operatorname{Re}z.
\]
Thus the equality locus is precisely the Euclidean circle
\[
|z+\kappa|^2=\kappa^2+1.
\]
On \(z=e^{(1+i\alpha)t}\), the magnitude-square difference is
\[
2e^t\bigl(\sinh t+\kappa\cos(\alpha t)\bigr).
\]
The two polynomials are not constant multiples: the determinant of their coefficient vectors, ordered as linear and constant, is \(-\cosh^2s-\sinh^2s\ne0\).

**2. Exact localization of the coincidence points.** Set \(\beta=|\alpha|>0\), \(L=\operatorname{arsinh}\kappa\), and
\[
F_\kappa(t)=\sinh t+\kappa\cos(\beta t).
\]
Since \(\sinh t>0\) for \(t>0\), every positive root lies in a negative-cosine lobe
\[
I_j=\left(\frac{(4j+1)\pi}{2\beta},\frac{(4j+3)\pi}{2\beta}\right),\qquad j=0,1,2,\ldots.
\]
Moreover no root lies beyond \(L\), because \(\sinh t>\kappa\) there. Hence the root set is finite: on the compact interval \([0,L]\), the real-analytic function \(F_\kappa\), nonzero at zero, has finitely many zeros.

**3. A lower bound with the sharp coefficient.** Each lobe has center
\[
c_j=\frac{(2j+1)\pi}{\beta}.
\]
If \(c_j<L\), then \(F_\kappa(c_j)=\sinh c_j-\kappa<0\), whereas \(F_\kappa\) is strictly positive at both lobe endpoints. The intermediate value theorem therefore gives at least two distinct zeros in this lobe. The number of such centers is \(\beta L/(2\pi)+O_\beta(1)\), so
\[
N_\alpha(\kappa)\ge\frac{\beta L}{\pi}-O_\beta(1).
\]

**4. A matching upper bound.** On a negative-cosine lobe, the root equation is \(R(t)=\kappa\) for
\[
R(t)=\frac{\sinh t}{-\cos(\beta t)}>0.
\]
Direct differentiation gives
\[
\frac{d^2}{dt^2}\log R(t)=\beta^2\sec^2(\beta t)-\operatorname{csch}^2t.
\]
For every \(t>\operatorname{arsinh}(1/\beta)\), this quantity is strictly positive. Thus, on each lobe lying entirely beyond this fixed threshold, \(\log R\) is strictly convex and the horizontal line \(\log\kappa\) intersects its graph at most twice. Only a number of lobes bounded in terms of \(\beta\) meet the initial compact interval. On each of those finitely many lobes, \(R\) is real analytic with finitely many critical points, because \(R'/R=\coth t+\beta\tan(\beta t)\) is meromorphic across each finite closed lobe except for finitely many endpoint poles, so it cannot have infinitely many zeros unless identically zero, which it is not. Hence each initial lobe also admits a fixed uniform-in-\(\kappa\) root-count bound. Every remaining lobe with a root has its left endpoint at most \(L\), and there are at most \(\beta L/(2\pi)+O_\beta(1)\) such lobes. Therefore
\[
N_\alpha(\kappa)\le\frac{\beta L}{\pi}+O_\beta(1).
\]
Combining both inequalities gives the asserted asymptotic. Since \(\operatorname{arsinh}\kappa=\log(2\kappa)+O(\kappa^{-2})\), the logarithmic version follows.

**5. No finite universal arbitrary-site budget.** Fix any positive integer \(M\), put \(t_j=j\pi/\beta\) for \(j=0,\ldots,M\), and choose \(\kappa>\sinh(M\pi/\beta)\). Then \(F_\kappa(t_j)=\sinh t_j+(-1)^j\kappa\) alternates strictly in sign. Therefore every open interval \((t_{j-1},t_j)\) contains a distinct positive root, giving \(M\) sites where the two polynomials agree in modulus but are not phase equivalent. Thus no \(M\) works for **all** sets of \(M\) spiral sites.

**6. Continuous uniqueness, included for comparison.** For any two complex polynomials \(P(z)=\sum_{j=0}^n a_jz^j\) and \(Q(z)=\sum_{j=0}^n b_jz^j\), equality of magnitudes for every \(t\ge0\) implies
\[
\sum_{j,k=0}^n(a_j\overline{a_k}-b_j\overline{b_k})
 e^{(j+k+i\alpha(j-k))t}=0.
\]
All exponents are distinct because equality of their real and imaginary parts forces the same \((j,k)\) when \(\alpha\ne0\). The linear independence of finitely many complex exponentials on a real interval implies \(a_j\overline{a_k}=b_j\overline{b_k}\) for all \(j,k\). Two coefficient vectors with the same rank-one Hermitian Gram matrix differ by one unimodular constant (including the zero case). This establishes the stated contrast but is not asserted as the novel part.

## Verification

A Python-standard-library checker named `spiral_crossing_check.py` is included. Run it with `python3 spiral_crossing_check.py`. It independently checks the magnitude-square identity at representative parameters, signs yielding arbitrary finite collision sets, and numerical root-count values against the asymptotic. It also tests examples of regular nonresonant phaseless sampling to illustrate the distinction between selected and arbitrary sites. Its reported `CHECKS_PASS 190` is **supplementary finite evidence only**; it is not an exhaustive test of all real \(\alpha\) or all \(\kappa\). The all-parameter assertions follow from the proof above.

## Relationship to prior work

Holomorphic phase retrieval from prescribed lines and line grids is studied by Wellershoff [1] and Liehr [2]. Chalendar and Partington [3] consider intersecting curves and pairs of circles. Those theorems do not directly count intersections of one spiral with an affine-polynomial magnitude-equality circle. On the other hand, structured geometric meshes admit simple finite-dimensional exponential-Vandermonde interpolation in nonresonant situations; this finding **does not claim** a new bound for such selected meshes. Its separate contribution is the logarithmic growth law for collisions on the outward spiral and the absence of a finite **universal arbitrary-position** sampling budget, which is compatible with the existence of efficient designed sampling sets.

## Limitations

The asymptotic constant is proved for a particular family of affine-polynomial pairs, not as a maximum over all pairs. The error term may depend on the spiral pitch; it is not claimed uniform as \(\alpha\to0\). The arbitrary-node impossibility does not rule out deterministic or random carefully designed stable reconstruction. All measurements are idealized exact magnitudes; no noise or conditioning bound is proved. Historical priority has not been independently established, and a more general curve-intersection theorem could subsume this special growth law.

## References

[1] M. Wellershoff, *Phase retrieval of entire functions and its implications for Gabor phase retrieval*, arXiv:2202.03733 (first public version 2022-02-08), https://arxiv.org/abs/2202.03733.

[2] L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, arXiv:2308.05722 (first public version 2023-08-10), https://arxiv.org/abs/2308.05722.

[3] I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first public version 2024-03-24), https://arxiv.org/abs/2403.16255.
