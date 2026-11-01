# Exact thin-ellipse cusp and the sharp inclusion-monotonicity threshold for radial weighted perimeter

## Finding
For \(0<a\le1\), let
\[
K_a=\{(x,y)\in\mathbb R^2:x^2/a^2+y^2\le1\},\qquad
F_p(a)=\int_{\partial K_a}|(x,y)|^p\,d\mathcal H^1(x,y),\quad p>-1.
\]
These are smooth, strictly convex, centrally symmetric nested bodies with the same vertical semiaxis. The function \(F_p\) is strictly increasing in \(a\) on \((0,1]\) **if and only if** \(p\ge0\). For every \(-1<p<0\), it is instead strictly decreasing for all sufficiently small positive \(a\), strictly increasing for \(a\) sufficiently close to one, and has a minimizer at an interior value \(a\in(0,1)\).

More precisely, for every fixed \(-1<p<0\),
\[
F_p(a)=\frac4{p+1}+C_pa^{p+1}+o(a^{p+1}),\qquad
F_p'(a)=(p+1)C_pa^p+o(a^p),\quad a\downarrow0,
\]
where the explicit nonzero **negative** cusp coefficient is
\[
\boxed{C_p=\frac{2p\sqrt\pi}{p+1}\,
 \frac{\Gamma((1-p)/2)}{\Gamma(1-p/2)}<0.}
\]
Thus inclusion monotonicity fails for **every** negative integrable power even when restricted to nested, smooth, origin-centered ellipses. The exponent \(p+1\) is optimal even for pairs of strictly convex ellipses with a fixed unit major semiaxis: with \(0<a\ll1\),
\[
 d_H(K_{a/2},K_a)=\frac a2,\qquad
\lim_{a\downarrow0}\frac{F_p(a/2)-F_p(a)}{d_H(K_{a/2},K_a)^{p+1}}
 =-C_p(2^{p+1}-1)>0.
\]
The coefficient \(C_p\) is an exact asymptotic, not a proposed globally optimal Hölder constant.

## Assumptions and scope
The Euclidean norm and one-dimensional Hausdorff measure are used. For \(a>0\) the ordinary boundary integral is finite for every real \(p\), but \(p>-1\) is necessary for finite passage to the degenerate centered unit segment. A degenerate segment is assigned boundary multiplicity two only when discussing its limit: \(\lim_{a\downarrow0}F_p(a)=4/(p+1)\). No statement is asserted about arbitrary nonsymmetric convex bodies, higher-dimensional ellipsoids, or uniqueness of the interior minimizer.

## Proof
**1. Exact one-variable formula and positive powers.** Parameterize the ellipse by \((a\cos t,\sin t)\). Fourfold symmetry gives
\[
F_p(a)=4\int_0^{\pi/2}
 (a^2\cos^2t+\sin^2t)^{p/2}
 \sqrt{a^2\sin^2t+\cos^2t}\,dt.\tag{1}
\]
When \(p\ge0\), both factors are nondecreasing in \(a\) at every fixed \(t\), and the arc-length factor is strictly increasing for \(0<t<\pi/2\). This proves strict monotonicity on the entire interval \((0,1]\).

**2. Derivative decomposition for negative powers.** Fix \(-1<p<0\). Differentiation under the integral is legitimate on every compact positive subinterval of \(a\). Writing \(s=\sin t\), \(c=\cos t\), one obtains \(F'_p(a)=N_p(a)+T_p(a)\) with
\[
N_p(a)=4pa\int_0^{\pi/2}c^2(a^2c^2+s^2)^{(p-2)/2}
   \sqrt{a^2s^2+c^2}\,dt,\tag{2}
\]
\[
T_p(a)=4a\int_0^{\pi/2}
\frac{s^2(a^2c^2+s^2)^{p/2}}{\sqrt{a^2s^2+c^2}}\,dt.\tag{3}
\]
Clearly \(N_p(a)<0<T_p(a)\). We show that the negative term dominates when \(a\downarrow0\).

For \(0<a\le\tfrac12\), split (3) at \(t=\pi/4\). On \([0,\pi/4]\), use \(a^2c^2+s^2\ge s^2\), \(\sqrt{a^2s^2+c^2}\ge c\ge 1/\sqrt2\), and \(p<0\) to bound the integrand by a constant times \(a\sin^{p+2}t\), which is integrable. On \([\pi/4,\pi/2]\), the first radial factor is uniformly bounded and the denominator is bounded below by a constant times \(\sqrt{a^2+(\pi/2-t)^2}\). Consequently
\[
0<T_p(a)=O_p(a\log(1/a))=o(a^p).\tag{4}
\]

In (2), substitute \(t=az\). After division by \(a^p\), the integrand (omitting its factor \(4p\)) is
\[
I_a(z)=\mathbf1_{0\le z\le\pi/(2a)}\cos^2(az)
\left(\cos^2(az)+\frac{\sin^2(az)}{a^2}\right)^{(p-2)/2}
\sqrt{a^2\sin^2(az)+\cos^2(az)}.
\]
For each \(z\ge0\), this tends to \((1+z^2)^{(p-2)/2}\). For \(0\le az\le\pi/2\), the inequalities \(\sin(az)\ge2az/\pi\) and \(\cos^2(az)+\sin^2(az)/a^2\ge1\) give a uniform majorant \(C_p(1+z^2)^{(p-2)/2}\). This is integrable on \([0,\infty)\) because \(p<1\). Dominated convergence and the beta integral yield
\[
\lim_{a\downarrow0}\frac{N_p(a)}{a^p}
=4p\int_0^\infty(1+z^2)^{(p-2)/2}\,dz
=2p\sqrt\pi\frac{\Gamma((1-p)/2)}{\Gamma(1-p/2)}<0.\tag{5}
\]
By (4), equation (5) is also the limit of \(F'_p(a)/a^p\), establishing its eventual strict negativity.

**3. Cusp and recovery of the endpoint.** For \(p>-1\), dominated convergence in (1) as \(a\downarrow0\) gives
\[
F_p(0+)=4\int_0^{\pi/2}\sin^p t\cos t\,dt=\frac4{p+1}.
\]
For negative \(p\), integrate (5) from \(0\) to \(a\) (or use the mean-value integral and its uniform small-\(a\) error) to obtain \(F_p(a)-F_p(0+)=C_pa^{p+1}+o(a^{p+1})\). The displayed expression for \(C_p\) follows by division by \(p+1\), which is positive.

**4. Interior turn and sharpness for full-dimensional pairs.** Evaluation of the exact derivative (2)--(3) at \(a=1\) gives
\[
F'_p(1)=4\int_0^{\pi/2}(p\cos^2t+\sin^2t)\,dt=\pi(p+1)>0.
\]
Continuity on the closed extension \([0,1]\), strict decrease near zero, and strict increase near one force a global minimizer inside \((0,1)\) (not necessarily unique). Finally, \(K_{a/2}\subset K_a\), and the support point \((a,0)\) has distance \(a/2\) from \(K_{a/2}\), whereas applying the diagonal map between the two ellipses displaces every point by at most \(a/2\); hence \(d_H(K_{a/2},K_a)=a/2\). Subtracting the two cusp expansions proves the positive limiting quotient in the finding and rules out a Hölder exponent larger than \(p+1\) even on this restricted smooth class.

## Verification
The standalone Python program `verify.py` (dependency in `requirements.txt`) numerically evaluates the exact boundary integral and its differentiated form using high-precision adaptive quadrature. It tests three negative powers, the predicted gamma-function coefficients and slopes at aspect ratio \(10^{-4}\), decreasing nested pairs, and the positive-power and circular-endpoint identities. It reports `NESTED_ELLIPSE_FINITE_CHECKS_OK`. These finite tests do not establish asymptotics for arbitrary real \(p\); the proof above rests on the explicit integrals, an integrable majorant, and dominated convergence.

## Relationship to prior work
Csató, Giovagnoli, and Roy (arXiv:2608.19851v1, 2026-08-20) obtain optimal fixed-*perimeter* weighted moment inequalities for symmetric plane curves, including a needle upper extremizer for negative powers; their theorem does not compare ellipses at fixed major semiaxis, determine the signed thin-ellipse cusp coefficient, or classify inclusion monotonicity of this nested family. Csató and Giovagnoli (arXiv:2610.11677v1, 2026-10-08), Theorem 1.3, establish inclusion monotonicity for nondecreasing radial weights and construct negative-weight failures in a different setting; their general continuity theorem does not provide the present coefficient or all-negative-exponent smooth-ellipse counterfamily. Saracco and Stefani (arXiv:2306.07770v1) prove global inclusion-monotonicity rigidity without requiring origin-centered or origin-containing bodies; this does not imply failure on the much narrower centered-ellipse family. A separately published planar weighted-perimeter Hausdorff modulus theorem determines the optimal exponent \(p+1\) by disk scaling, without determining this nonpoint, fixed-major-axis elliptic cusp or its sign. The optimal Hölder exponent itself is therefore credited as known.

## Limitations
The negative-power conclusion holds for sufficiently thin ellipses; it does not assert decreasing behavior for every \(a\in(0,1)\), nor a unique interior minimizer. The \(p+1\) cusp is specific to the thin-ellipse path. The result neither improves the already-known universal Hölder exponent nor establishes a sharp universal Hölder coefficient. No exhaustive historical-priority guarantee or independent scientific audit is claimed.

## References
1. G. Csató, D. Giovagnoli, P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1, first public 2026-08-20, https://arxiv.org/html/2608.19851v1 .
2. G. Csató, D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1, first public 2026-10-08, https://arxiv.org/pdf/2610.11677 .
3. G. Saracco, G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, arXiv:2306.07770v1, first public 2023-06-13, https://arxiv.org/abs/2306.07770 .
4. *Sharp Hausdorff regularity exponents of planar radial weighted perimeters*, publicly available mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-hausdorff-regularity-exponents-of-planar-radial-weighted-p--840cdd1da1ee .
