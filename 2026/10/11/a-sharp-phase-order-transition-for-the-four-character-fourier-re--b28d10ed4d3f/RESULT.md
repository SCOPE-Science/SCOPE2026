# A sharp phase-order transition for the four-character Fourier rectangle

## Finding
Let \(z,w\) be independent Haar-uniform points of the unit circle and let
\[
P(z,w)=a+bz+cw+dzw,\qquad a,b,c,d\in\mathbb C.
\]
Put \(A=|a|\), \(B=|b|\), \(C=|c|\), \(D=|d|\). For positive \(A,B,C,D\), every coefficient vector is, up to multiplication by a common unimodular scalar and independent rotations of \(z,w\), equivalent to
\[
P_\theta(z,w)=A+Bz+Cw+De^{i\theta}zw,\qquad
\theta=\arg\!\left(\frac{ad}{bc}\right).
\]
Define its normalized moment for \(p>0\) by
\[
M_p(\theta)=\int_{\mathbb T^2}|P_\theta(z,w)|^p\,dm(z)\,dm(w).
\]
**Theorem.** For every fixed quadruple of strictly positive amplitudes and every real \(p>0\):

* If \(p>2\), \(M_p(\theta)\) is **strictly decreasing** as the circular distance of \(\theta\) from \(0\) increases from \(0\) to \(\pi\). Its unique maximizing cross phase is \(\theta=0\) and its unique minimizing cross phase is \(\theta=\pi\), modulo \(2\pi\).
* If \(0<p<2\), the phase ordering is **strictly reversed**: the unique maximizing cross phase is \(\theta=\pi\), and the unique minimizing cross phase is \(\theta=0\).
* At \(p=2\), every phase has the same moment \(M_2=A^2+B^2+C^2+D^2\).

Consequently, for every \(p>2\) the precise sharp fixed-modulus phase majorant is
\[
\int_{\mathbb T^2}|a+bz+cw+dzw|^p\,dm^2
\leq\int_{\mathbb T^2}(\,|A+Bz+Cw+Dzw|\,)^p\,dm^2,
\]
with equality for nonzero coefficients if and only if \(ad/(bc)\) is positive real. For \(0<p<2\) the analogous sharp upper bound instead uses \(A+Bz+Cw-Dzw\), with equality if and only if \(ad/(bc)\) is negative real. If at least one coefficient vanishes, the moment is independent of all remaining coefficient phases. Both bounds are attained for every prescribed quadruple of amplitudes.

For instance, at unit amplitudes the two fourth moments are exactly \(36\) (aligned) and \(20\) (opposed); the sixth moments are \(400\) and \(112\). The transition exponent is exactly \(p=2\), independent of the four amplitudes.

## Assumptions and scope
The ambient group is \(\mathbb T^2\) with probability Haar measure in both variables. The four Fourier frequencies are exactly \((0,0),(1,0),(0,1),(1,1)\). The theorem concerns **fixed coefficient magnitudes and optimization over their phases**, not a comparison allowing independent increases of the four magnitudes. The exponent \(p\) is any finite positive real number. Strictness requires all four magnitudes to be positive; the zero-amplitude case has no nontrivial cross phase.

## Proof
**1. Phase reduction.** Factor out the phase of \(a\) and rotate \(z\) and \(w\) so the first three coefficients become \(A,B,C\). The remaining phase is \(\arg(ad/(bc))\); the Haar moment depends on no other phase invariant.

**2. A signed mixed derivative.** For \(s=p/2>0\), define the circular average
\[
\Phi_s(X,Y)=\frac1{2\pi}\int_0^{2\pi}
(X+Y+2\sqrt{XY}\cos t)^s\,dt,\qquad X,Y\ge0.
\]
For \(0<X<Y\), set \(r=X/Y\). The absolutely convergent binomial expansion gives
\[
\Phi_s(X,Y)=Y^s F_s(r),\qquad
F_s(r)=\sum_{k=0}^{\infty}\binom{s}{k}^{\!2}r^k.
\]
The coefficient recurrence \(k^2\binom{s}{k}^2=(s-k+1)^2\binom{s}{k-1}^2\) yields, directly by termwise differentiation,
\[
r(1-r)F_s''+[1+(2s-1)r]F_s'-s^2 F_s=0.
\]
Differentiating \(Y^sF_s(X/Y)\) and using that identity gives
\[
\begin{aligned}
\partial_X\partial_Y\Phi_s(X,Y)
&=Y^{s-2}\bigl[(s-1)F_s'(r)-rF_s''(r)\bigr]\\
&=\frac{s^2}{\sqrt{XY}}\frac1{2\pi}
\int_0^{2\pi}\cos t\,
(X+Y+2\sqrt{XY}\cos t)^{s-1}\,dt.
\end{aligned}
\]
Indeed, the last identity follows upon differentiating the circular-average expression for \(F_s\), or by the displayed differential equation. Because the cosine has mean zero and the remaining factor is strictly increasing in \(\cos t\) for \(s>1\), strictly decreasing for \(0<s<1\), and constant for \(s=1\), this mixed derivative has the **strict sign of \(s-1\)** when \(X,Y>0\) and \(X\ne Y\). The same sign holds with \(X>Y\) by symmetry. Continuity of \(\Phi_s\) extends the corresponding strictly supermodular/submodular four-corner inequality across the diagonal \(X=Y\), where classical second derivatives need not be finite at small exponents.

**3. Coupling of two cosine marginals.** Integrate first in \(z\) and let \(w=e^{it}\). Then
\[
M_p(\theta)=\frac1{2\pi}\int_0^{2\pi}
\Phi_s(X(t),Y_\theta(t))\,dt,
\]
with
\[
X(t)=A^2+C^2+2AC\cos t,\qquad
Y_\theta(t)=B^2+D^2+2BD\cos(t+\theta).
\]
Their separate distributions are independent of \(\theta\). Only the coupling changes. To compare couplings, first note the elementary circular-arc intersection formula: if \(I_\alpha\) is the arc \(\{|t|<\alpha\}\) and \(I_\beta\) is the analogous arc shifted through an angular distance \(u\in[0,\pi]\), with \(0<\alpha,\beta<\pi\), then its overlap length is
\[
L_{\alpha,\beta}(u)
=(\alpha+\beta-u)_+-(|\alpha-\beta|-u)_+
 +(\alpha+\beta+u-2\pi)_+,
\]
where \(x_+=\max(x,0)\). This expression is nonincreasing in \(u\). For \(\alpha=\beta=\pi/2\), it equals \(\pi-u\), so the decrease is strict throughout the interval. In particular, for any interior thresholds \(x,y\), the joint survival probability
\[
\Pr\{X(t)>x,\;Y_\theta(t)>y\}
\]
is nonincreasing as \(|\theta|\) moves from \(0\) to \(\pi\), and for thresholds near the two cosine midpoints its decrease is strict.

For a smooth bivariate function, expanding by its signed mixed derivative expresses its expectation under a coupling as a phase-independent marginal contribution plus the integral of its mixed derivative against these joint survival probabilities. Applying this formula to \(\Phi_s\) on positive compact subrectangles and passing to the boundaries by continuity is legitimate; equivalently, approximate \(\Phi_s\) uniformly by its rectangular grid values and use the strict signs of all mixed four-corner differences. The sign proved in Step 2 and the arc-overlap ordering now show that \(M_p(\theta)\) decreases strictly with \(|\theta|\) for \(s>1\), and increases strictly for \(0<s<1\). Strictness follows by integrating over a neighborhood of the midpoint thresholds, where the mixed derivative has a fixed nonzero sign and the arc overlap strictly changes. At \(s=1\), \(\Phi_1(X,Y)=X+Y\), so the coupling disappears.

**4. Equality and boundaries.** The strict phase ordering gives the unique extremizing cross phases in each nontrivial exponent regime, up to the harmless common scalar and torus rotations. If any one of \(A,B,C,D\) is zero, one cosine marginal above is constant, proving phase independence. The stated \(p=2\) value follows also directly from orthogonality of the four distinct characters. This completes the proof for every finite \(p>0\), without discretizing the torus.

## Verification
The standalone `checker.py` reproduces exactly, by integer convolution, the unit-amplitude fourth and sixth moments \((36,20)\) and \((400,112)\) for aligned/opposed phases. It then checks strict sampled phase ordering for \(21\) amplitude quadruples at \(11\) exponents on a \(64\times64\) torus mesh, including exponents on either side of \(2\), and checks phase independence when one coefficient vanishes. Its output is `FINITE_CHECK_PASS 944 supplementary assertions`. A separate high-resolution test confirmed the circular-arc overlap formula at \(100\) nondegenerate parameter triples. These finite checks support implementation and special cases; the proof of all exponents and amplitudes is the analytic mixed-derivative and arc-rearrangement argument above.

## Relationship to prior work
Gressman, Guo, Pierce, Roos, and Yung (2021) characterize frequency sets enjoying the strict majorant property for **every** exponent and construct intervals of failure for affinely dependent sets. Their Theorem 1 and Proposition 10 allow a failure below exponent \(2\) for the four-point rectangular relation, and their Lemma 12 covers even exponents, but do not provide the complete exact phase ordering for this fixed rectangle for **all** positive real exponents, arbitrary positive amplitudes, and all equality cases. Their affine-independent theorem also does not apply to this affinely dependent four-point configuration. Rains (1978) studies global upper-majorant properties of entire locally compact Abelian groups and gives a group-level failure theorem, not this fixed-support phase optimization. The publicly available four-point rectangle Fourier-zero classification works on finite cyclic product groups with unimodular coefficients and counts zeros rather than continuous \(L^p\) moments; the four-point cyclic-prime fourth-moment work instead addresses a different support geometry and a minimum in one variable. None of those inspected statements implies the present exponent-wide fixed-modulus phase monotonicity. An equivalent earlier application of circular rearrangement to exactly this polynomial cannot be ruled out solely from the inspected literature.

## Limitations
This is a fixed-modulus phase theorem, not a theorem about unrestricted coefficientwise domination, arbitrary four-point supports, finite cyclic sampling, or the endpoint \(p=\infty\). Equivalent earlier formulations in classical rearrangement or majorant literature cannot be completely excluded. At the degenerate zero-amplitude boundary the phase characterization becomes vacuous, as required by the theorem. The elementary proof does not provide a closed form for the optimal \(p\)-moments at every real exponent; it identifies their exact maximizing and minimizing phase configurations for all magnitudes.

## References
1. P. T. Gressman, S. Guo, L. B. Pierce, J. Roos, and P.-L. Yung, *On the strict majorant property in arbitrary dimensions*, arXiv:2106.12538v1 (first posted 2021-06-23), *Quarterly Journal of Mathematics* **74** (2023), 139–161. Full text: https://arxiv.org/html/2106.12538v2.
2. M. Rains, *On the upper majorant property for locally compact Abelian groups*, *Canadian Journal of Mathematics* **30** (1978), 915–925. DOI: 10.4153/CJM-1978-079-3.
3. *Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups*, publicly available research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-phase-only-fourier-zero-spectrum-of-a-four-point-rectangle-on-cy--b51ecb1779fe.
4. *Four-point support geometry quantizes the phase-only fourth Fourier moment*, publicly available research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-point-support-geometry-quantizes-the-phase-only-fourth-four--2b7f859e0b5c.
