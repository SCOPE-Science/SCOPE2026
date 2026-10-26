# Microscopic Bessel zero law and universal drift for Euclidean-distance Bergman kernels

## Finding
For an integer \(d\ge2\), let \(B_d=\{z\in\mathbb C^d:\|z\|<1\}\). Write \(K_{d,t}(s)\) for the weighted Bergman kernel of \((1-\|z\|)^t\) with respect to ordinary Lebesgue volume, where \(t>0\) is any **real** number and \(s=\langle z,w\rangle\). Put \(F_{d,t}(u)=t^{-2d}K_{d,t}(u/t^2)\), initially for \(|u|<t^2\). Let \(D=u\,d/du\). Then, locally uniformly on the entire complex plane as \(t\to+\infty\),
\[
F_{d,t}(u)=F_d(u)+t^{-1}(D+d)(2D+2d+1)F_d(u)+O_{d,R}(t^{-2}),\qquad |u|\le R,
\]
where
\[
F_d(u)=\frac{\sqrt\pi}{2^{2d}\pi^d\Gamma(d+\frac12)}\,{}_0F_1\!\left(;d+\frac12;\frac u4\right).
\]
Write \(j_{\nu,k}\) for the \(k\)-th positive zero of the standard Bessel function \(J_\nu\) and \(\nu=d-1/2\). For every fixed positive integer \(k\), all sufficiently large real \(t\) admit a unique simple negative scalar zero \(u_{k,t}\) in a fixed small neighborhood of \(-j_{\nu,k}^2\), and
\[
u_{k,t}=-j_{\nu,k}^2\left(1-\frac{2(d+1)}t\right)+O_{d,k}(t^{-2}).
\]
In physical kernel coordinates, the corresponding scalar zero is \(u_{k,t}/t^2\in(-1,0)\) for large \(t\). On every bounded region whose boundary avoids limiting zeros, the complete scalar-zero count (with multiplicity) eventually agrees with that of \(F_d\). In particular, for any fixed \(N\), all sufficiently large **real**, including noninteger, exponents produce at least \(N\) distinct scalar zeros in the ball kernel.

## Assumptions and scope
The exponent \(t\to+\infty\) varies over every real value, not just integers. The complex dimension \(d\ge2\) is fixed, and the zero index \(k\ge1\) is fixed before taking the limit. The function \(K_{d,t}(s)\) is the scalar analytic kernel associated to \(s=\sum_{a=1}^{d}z_a\overline w_a\) for \(|s|<1\); the rescaled function is holomorphic for \(|u|<t^2\). The weight is the actual Euclidean boundary distance \(1-\|z\|\), not \(1-\|z\|^2\). The limiting entire kernel corresponds, after scaling, to the radial exponential weight \(e^{-\|z\|}\) in \(\mathbb C^d\). Zeros are in the scalar product coordinate, not isolated points of a several-variable hypersurface.

## Proof
**1. Exact moments for every real exponent.** Let \(d\sigma\) be ordinary surface measure on the unit sphere. The spherical monomial identity gives \(\int_{S^{2d-1}}|\zeta^\alpha|^2\,d\sigma=2\pi^d\alpha!/\Gamma(|\alpha|+d)\). Polar integration of \((1-r)^t\) gives the beta factor \(B(2m+2d,t+1)\) for homogeneous degree \(m\). Orthogonal completeness of the monomials and the multinomial theorem therefore yield the exact series
\[
K_{d,t}(s)=\frac{1}{2\pi^d}\sum_{m=0}^{\infty}\frac{\Gamma(m+d)\Gamma(t+2m+2d+1)}{m!\,\Gamma(2m+2d)\Gamma(t+1)}s^m,
\qquad |s|<1.
\]
No integer assumption on \(t\) was used. For \(q=2m+2d\), the integer-step gamma quotient equals \(\Gamma(t+q+1)/\Gamma(t+1)=\prod_{j=1}^{q}(t+j)\). Thus
\[
F_{d,t}(u)=\sum_{m\ge0}a_{d,m}u^m\prod_{j=1}^{2m+2d}\left(1+\frac jt\right),\qquad
 a_{d,m}=\frac{\Gamma(m+d)}{2\pi^d m!\Gamma(2m+2d)}.
\]

**2. A genuine locally uniform two-term expansion.** Treat \(h=1/t\) as a complex variable and define \(G_d(h,u)\) by the last series with \(1+j/t\) replaced by \(1+jh\). Successive absolute summands have ratio tending to \(|u h^2|\) as \(m\to\infty\). More precisely, their coefficient ratio is
\[
\frac{a_{d,m+1}}{a_{d,m}}=\frac{m+d}{(m+1)(2m+2d)(2m+2d+1)},
\]
and the remaining factor is \((1+(2m+2d+1)h)(1+(2m+2d+2)h)\). Consequently the series converges normally on every compact polydisk \(|u|\le R, |h|\le h_0\) for \(Rh_0^2<1\). Cauchy's estimates give a uniform \(O_R(h^2)\) remainder about \(h=0\). Since \(\sum_{j=1}^{q}j=q(q+1)/2=(m+d)(2m+2d+1)\), termwise differentiation in \(h\) proves
\[
G_d(h,u)=F_d(u)+h(D+d)(2D+2d+1)F_d(u)+O_R(h^2).
\]
The duplication formula gives the displayed \({}_0F_1\) expression for \(F_d\). This also proves local uniform convergence with derivatives on every compact disk, rather than formal coefficient convergence alone.

**3. Complete limiting zero geometry and first drift.** With \(\nu=d-1/2\), the standard identity \({}_0F_1(;\nu+1;-x^2/4)=\Gamma(\nu+1)(x/2)^{-\nu}J_\nu(x)\) shows that the zeros of \(F_d\) are exactly \(u_k=-j_{\nu,k}^2\) for \(k\ge1\), all simple because \(\nu>-1\). The differential equation for the limit is
\[
u F_d''(u)+(d+\tfrac12)F_d'(u)-\tfrac14F_d(u)=0.
\]
At each zero \(u_k\), it implies \(D^2F_d(u_k)=(\tfrac12-d)u_kF'_d(u_k)\). Expanding the correction operator as \(2D^2+(4d+1)D+d(2d+1)\), we therefore get
\[
\big[(D+d)(2D+2d+1)F_d\big](u_k)=2(d+1)u_kF_d'(u_k).
\]
Rouché's theorem on disjoint small circles around finitely many simple limiting zeros, together with the analytic implicit-function theorem, gives exactly one zero near each \(u_k\) and yields
\[
u_{k,t}=u_k-t^{-1}\frac{2(d+1)u_kF'_d(u_k)}{F'_d(u_k)}+O_{d,k}(t^{-2})=u_k\big[1-2(d+1)/t\big]+O_{d,k}(t^{-2}).
\]
All Taylor coefficients are real for real \(t\), so complex conjugation preserves these zeros; local uniqueness forces each to be real. Since \(u_k<0\), they are negative for large \(t\). For any fixed number of roots, their locations divided by \(t^2\) eventually lie in \((-1,0)\) and are realized by \(z=\sqrt{|s|}e_1\), \(w=-\sqrt{|s|}e_1\). Rouché's theorem on the boundary of any compact zero-avoiding region also gives the asserted complete local count.

## Verification
The exact monomial moment formula, the integer-step gamma quotient and the hypergeometric differential equation independently determine every constant in the theorem. As an additional numerical stress test, a high-precision recurrence evaluator for the scalar kernel was applied in dimensions \(d=2,3\) at \(t=100,200,400\) and Bessel-zero indices \(k=1,2\). In each case \(t^2\) times the difference between the computed zero and the stated two-term approximation remained bounded and tended toward a finite value. For instance for \(d=2,k=1\), those residuals were approximately \(-777.8563,-803.2738,-816.6082\); for \(d=3,k=1\), approximately \(-2200.3962,-2294.2941,-2344.2820\). These finite evaluations are consistency checks, not the proof of the asymptotic statement. The proof itself is the normally convergent two-variable series and implicit-function argument.

## Relationship to prior work
Marinescu and Xing (2026, arXiv:2609.24258v1) prove real-analytic dependence of Euclidean boundary-distance weighted Bergman kernels for **finite** parameter values on smooth bounded pseudoconvex domains; their introduction explicitly distinguishes their work from large-parameter asymptotics. A publicly available later exact ball calculation, *Negative-real scalar zeros of Euclidean-distance Bergman kernels in every complex-ball dimension* (published-finding corpus, October 2026), supplies a Jacobi-polynomial zero classification for **integer** exponents \(t\ge0\). Its complete statement and proof were compared: it does not assert this locally uniform all-real-parameter high-power limit or the universal first-order displacement. Its exact integer formulas, together with classical Mehler–Heine Jacobi asymptotics, strongly anticipate the leading behavior on the integer subsequence; no novelty is claimed for the integer-only zero-count geometry or the underlying classical Bessel identities. A separate published disk result, *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels* (published-finding corpus, October 2026), gives explicit zeros for all real exponents in complex dimension one; the present theorem is explicitly restricted to dimension at least two. Engliš (2016, arXiv:1601.03716) studies high powers in the **harmonic**, not holomorphic, Bergman setting; its accessible abstract does not establish this holomorphic scalar-zero law. The new claim is the real-exponent complex-ball microscopic zero limit with its explicit common first-order relative drift, not an exact enumeration of existing integer-Jacobi roots.

## Limitations
The dimension, limiting zero index and compact regions are each fixed as \(t\to\infty\). This result does not classify all zeros for a fixed exponent or provide error bounds uniform for zero indices growing with \(t\). The leading integer-subsequence limit can be derived from classical Jacobi asymptotics combined with the known exact integer ball formula, limiting any priority claim for that special case. An unlocated general holomorphic high-power theorem or a published higher-order Jacobi expansion might already cover some or all of the first correction; a historical-priority risk remains. This is not an independently audited mathematical result.

## References
1. G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258v1, first public September 21, 2026, https://arxiv.org/abs/2609.24258.
2. *Negative-real scalar zeros of Euclidean-distance Bergman kernels in every complex-ball dimension*, published-finding corpus (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-negative-real-scalar-zeros-of-euclidean-distance-bergman-kernels--996941b74aa3/RESULT.md.
3. *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels*, published-finding corpus (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-lu-qi-keng-transitions-for-euclidean-boundary-distance-wei--b68d363f03d0/RESULT.md.
4. M. Engliš, *High-power asymptotics of some weighted harmonic Bergman kernels*, arXiv:1601.03716v1 (2016), https://arxiv.org/abs/1601.03716.
5. NIST Digital Library of Mathematical Functions, Bessel functions §10.21 and hypergeometric functions §16.2, https://dlmf.nist.gov/10.21 and https://dlmf.nist.gov/16.2.