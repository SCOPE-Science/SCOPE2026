# A likelihood-ordered matched crossover and period overshoot at a quintic global center

## Finding
Consider the reversible polynomial flow
\[
\dot x=y,\qquad \dot y=-x-\alpha x^3y^2-\beta x^5,\qquad \beta>0,\quad\alpha\ge0.
\]
For every amplitude \(A>0\), the origin is surrounded by a unique periodic energy oval with positive turning coordinate \(A\); let \(T_{\alpha,\beta}(A)\) be its **minimal original-time period**. Uniformly sample an original physical time over this period, and let \(X_A=|x|/A\in[0,1]\) be the normalized absolute position.

For \(q\ge0\) and \(0\le t<1\), set
\[
J_q(t)=2\int_t^1 e^{qs^4/2}s^5\,ds,\quad
w_q(t)=\frac{e^{qt^4/4}}{\sqrt{J_q(t)}},\quad
C(q)=4\int_0^1w_q(t)\,dt,
\quad \rho_q(t)=\frac{4w_q(t)}{C(q)}.
\]
All these integrals are finite, and \(\rho_q\) is a probability density on \((0,1)\). For any sequence \(A\to\infty\), \(\alpha=\alpha_A\ge0\) with \(\alpha_A A^4\to q<\infty\), and any fixed \(\beta>0\),
\[
\boxed{\sqrt\beta A^2T_{\alpha_A,\beta}(A)\longrightarrow C(q),\qquad
\mathcal L(X_A)\xrightarrow{\mathrm{TV}}\rho_q(t)\,dt.}
\]
For each finite \(Q\), the relative period error and the total-variation error are \(O_Q(|\alpha_A A^4-q|+(\beta A^4)^{-1})\), whenever the scaling parameters lie in \([0,Q]\).

**Strict ordering:** \(C(q)\) decreases strictly in \(q\); if \(q_2>q_1\), the likelihood ratio \(\rho_{q_2}(t)/\rho_{q_1}(t)\) is strictly increasing for \(0<t<1\). Thus every nontrivial normalized near-turning-point occupation probability \(\int_r^1\rho_q(t)\,dt\), \(0<r<1\), strictly increases with \(q\).

**Nonmonotone rescaled period:** despite the monotone \(C(q)\), the natural amplitude-velocity normalization \(S(q)=\sqrt q\,C(q)\) has an interior global maximum **strictly larger than \(2\pi\)**. Specifically,
\[
S(2)>\frac{1575543}{247000}>\frac{44}{7}>2\pi,
\qquad \lim_{q\downarrow0}S(q)=0,\quad
\lim_{q\to\infty}S(q)=2\pi.
\]
No uniqueness of the maximizer is asserted.

The crossover joins two sharply different position laws. At \(q=0\),
\[
C(0)=\frac{2\sqrt3}{3}B\!\left(\frac16,\frac12\right),\qquad
\rho_0(t)=\frac{6}{B(1/6,1/2)\sqrt{1-t^6}}.
\]
As \(q\to\infty\), the time-position law concentrates at the turning points: \(\rho_q(t)dt\Rightarrow\delta_1\). More precisely, if \(U_q=q(1-t)\) under \(\rho_q\), its law converges in total variation to
\[
\boxed{f(u)\,du=\frac2\pi\frac{e^{-u}}{\sqrt{1-e^{-2u}}}\,du,\quad u>0,}
\]
whose cumulative distribution is \((2/\pi)\arccos(e^{-u})\) and whose median is \((\log2)/2\). This last step is the *successive limit* after first taking the finite-\(q\) matched high-amplitude limit; it does not assert a uniform law for arbitrary simultaneously diverging \(q\).

## Assumptions and scope
Here \(\beta>0\) is fixed, \(A\) labels the maximum positive coordinate of an energy oval, and all periods, orbit positions, and time averages use the original differential-equation time. The scale \(q=\alpha A^4\) is nonnegative and may vary with \(A\); every stated quantitative finite-\(q\) error is for \(q\) restricted to a compact interval. Total-variation distance uses \(\sup_E|P(E)-Q(E)|\), not twice this quantity. The preceding central result is a joint, matched asymptotic across \(\alpha\downarrow0\), not a claim that \(\alpha\) is fixed and positive during the first limit. All finite-q results hold at the endpoint \(q=0\). The original global-center classification and each fixed-parameter high-amplitude period law are prior results [1,3], not new claims.

## Proof
**Energy and exact time quadrature.** Set \(p(x)=\exp(\alpha x^4/4)\) and \(V(x)=\int_0^x\exp(\alpha s^4/2)(s+\beta s^5)\,ds\). The function \(H(x,y)=\frac12p(x)^2y^2+V(x)\) obeys \(\dot H=0\), because \(p'/p=\alpha x^3\). As \(V\) is even, strictly increasing for positive \(x\) and unbounded, every positive energy level is a simple smooth periodic oval with turning points \(\pm A\). On its positive ascending/descending quarter-orbits,
\[
T_{\alpha,\beta}(A)=4\int_0^A\frac{e^{\alpha x^4/4}}{\sqrt{2[V(A)-V(x)]}}\,dx.
\tag{1}
\]
The Jacobian-energy construction itself is standard [2], and the global-center domain was identified in [1].

**Exact matched rescaling.** Write \(q_A=\alpha A^4\), \(\delta_A=(\beta A^4)^{-1}\), and \(x=At\). Then (1) becomes the exact identity
\[
\sqrt\beta A^2 T_{\alpha,\beta}(A)
=4\int_0^1 w_{q_A,\delta_A}(t)\,dt,
\quad w_{q,\delta}(t)=\frac{e^{qt^4/4}}{\sqrt{J_{q,\delta}(t)}},
\quad J_{q,\delta}(t)=2\int_t^1 e^{qs^4/2}(s^5+\delta s)\,ds.
\tag{2}
\]
The density of \(X_A\) is exactly \(w_{q_A,\delta_A}/\int_0^1w_{q_A,\delta_A}\), because the four quarter-traversals have equal original-time contributions. The ratio between the extra \(\delta\)-integral and \(J_q\) is
\[
0\le R_q(t)=\frac{2\int_t^1 e^{qs^4/2}s\,ds}{J_q(t)}\le 3e^{Q/2}\quad(0\le q\le Q,\ 0\le t<1),
\]
using \(e^{qs^4/2}\in[1,e^{Q/2}]\) and \((1-t^2)/(1-t^6)\le1\). Therefore \(w_{q,\delta}/w_q=(1+\delta R_q)^{-1/2}=1+O_Q(\delta)\) uniformly in \(t\). Furthermore \(-1/4\le\partial_q\log w_q(t)\le0\), as established below, so a change \(q_A-q\) changes each \(w\) by at most a uniform relative factor \(\exp(|q_A-q|/4)\). This proves both the limit and the error for the period and the total-variation convergence of the time-position densities; the singularity at \(t=1\) is integrable and the relative estimates remain uniform there.

**Strict monotone likelihood ratio.** Write \(z=t^4\) and change variables \(v=s^4\) inside \(J_q\). Apart from a positive factor, the measure in its integral has density \(g_q(v)=v^{1/2}e^{qv/2}\), \(z<v<1\). Differentiating the logarithm gives
\[
\partial_q\log w_q(t)=-\frac14d_q(z),\qquad
 d_q(z)=\frac{\int_z^1(v-z)g_q(v)\,dv}{\int_z^1g_q(v)\,dv}>0.
\tag{3}
\]
For completeness, \(d_q\) strictly decreases in \(z\). Define \(G_q(z)=\int_z^1g_q(v)\,dv\) and hazard \(h_q(z)=g_q(z)/G_q(z)\). Then
\[
\frac{G_q(z)}{g_q(z)}=\int_0^{1-z}\left(1+\frac{u}{z}\right)^{1/2}e^{qu/2}\,du
\]
is strictly decreasing for \(0<z<1\), hence \(h_q\) strictly increases. The tail representation
\[
d_q(z)=\int_0^{1-z}\frac{G_q(z+u)}{G_q(z)}\,du
=\int_0^{1-z}\exp\left(-\int_z^{z+u}h_q(v)\,dv\right)du
\]
then strictly decreases in \(z\): both the domain and integrand decrease as the lower endpoint moves right. Thus \(\partial_q\log w_q(t)\) is strictly increasing in \(t\) by (3), proving that \(\rho_{q_2}/\rho_{q_1}\) is strictly increasing for \(q_2>q_1\). Since (3) is strictly negative, \(C(q)\) decreases. The likelihood-ratio property entails strictly larger upper tails, because the two normalized densities cross exactly once.

**Pure-quintic endpoint.** At \(q=0\), \(J_0(t)=(1-t^6)/3\); the beta substitution \(v=t^6\) yields the stated exact \(C(0)\) and \(\rho_0\).

**Large-\(q\) concentration and boundary layer.** Substitute \(u=q(1-t)\) in \(C(q)\):
\[
\frac{\sqrt q}{4}C(q)=\int_0^q
\frac{\exp\{\frac q4[(1-u/q)^4-1]\}}{\sqrt{F_q(u)}}du,
\quad F_q(u)=2\int_0^u\exp\{\frac q2[(1-v/q)^4-1]\}(1-v/q)^5\,dv.
\tag{4}
\]
For fixed \(u>0\), the integrand tends to \(e^{-u}/\sqrt{1-e^{-2u}}\). If \(q\ge2\), its numerator is at most \(e^{-u/4}\). For \(0\le v\le\min\{u,1\}\), we have \(1-v/q\ge1/2\) and \(\frac q2[(1-v/q)^4-1]\ge-2v\), so \(F_q(u)\ge(e^{-2}/16)\min\{u,1\}\). Hence the integrand is bounded by \(4e e^{-u/4}/\sqrt{\min\{u,1\}}\), uniformly integrable over the half-line. Dominated convergence yields \(\sqrt q C(q)/4\to\pi/2\). The normalized transformed densities then converge in \(L^1\) to the stated \(f\) by dominated convergence, which proves total variation, concentration at \(t=1\), and the claimed cumulative distribution and median. The fixed-positive-\(\alpha\) analog of this endpoint period limit and its quadrature are included in [3]; the new claim is the full finite-\(q\) matched family and its strict likelihood ordering and overshoot.

**Rigorous overshoot.** Since \(J_2(t)\le eJ_0(t)\) and \(e^{2t^4/4}\ge1\), \(C(2)\ge e^{-1/2}C(0)\). Using the binomial expansion of \((1-t^6)^{-1/2}\) and the first four strictly positive terms gives
\[
C(0)>4\sqrt3\left(1+\frac1{14}+\frac3{104}+\frac5{304}\right).
\]
With elementary bounds \(\sqrt2>7/5\), \(\sqrt3>17/10\), \(\sqrt e<5/3\), \(\pi<22/7\), we obtain
\[
S(2)=\sqrt2 C(2)>\frac{1575543}{247000}>\frac{44}{7}>2\pi.
\]
Since \(C\) is positive, continuous and bounded at \(q=0\), \(S(q)\to0\) at zero, whereas (4) gives \(S(q)\to2\pi\) at infinity. The strict overshoot and compactness therefore force at least one finite positive global maximizer, with maximum strictly exceeding \(2\pi\).

## Verification
The standalone script `verify_crossover.py` checks the conserved-energy identity symbolically, the matched integral numerically at finite amplitudes, the beta-function endpoint, strict sample inequalities for the normalized density ratios, and the global period overshoot certificate. The mathematical proof of the infinite-dimensional parameter and asymptotic statements is the argument above, not finite experimental enumeration. The script depends on ordinary Python with SymPy and SciPy and has no hidden input file.

## Relationship to prior work
Da Cruz and Llibre [1], first public December 9, 2023, classify a broader class of quintic global centers and encompass the nonnegative coefficient regime above. The Jacobi-multiplier energy and time-conserving transformation are established tools [2]. The published result [3] already proves strict decrease of \(T(A)\) and its **separate** high-amplitude limits for fixed \(\alpha>0\) and for \(\alpha=0\), using a related boundary-layer integral; neither fact is presented as new. Neither the separate endpoints nor the general period criteria [4] imply a uniform matched \(\alpha A^4\to q\) law, total-variation spatial distributions ordered by likelihood ratio, or an interior overshoot for \(\sqrt q C(q)\). These distinct comparisons are the asserted contribution, conditional on the presently inspected literature; absence from a search index is not proof of priority.

## Limitations
The theorem requires fixed \(\beta>0\), finite matched \(q\) in its first limit, and nonnegative \(\alpha\); no result is claimed for the entire six-parameter quintic family, \(\beta=0\), or arbitrary jointly unbounded \(q\). The global maximizer of \(S\) is proved to exist but is not claimed unique or explicitly located. The large-\(q\) layer is a successive limit, and an equivalent unindexed general singular-perturbation theorem remains possible. Numerical checks support but cannot certify the analytic theorem. No independent mathematical audit has been performed.

## References
1. L. P. C. da Cruz and J. Llibre, *Global Centers in a Class of Quintic Polynomial Differential System*, arXiv:2312.05709v1 (first public 2023-12-09), https://arxiv.org/abs/2312.05709 ; journal version doi:10.1017/prm.2024.43.
2. S. Chanda, A. Ghose-Choudhury and P. Guha, *Jacobi-Maupertuis metric of Liénard type equations and Jacobi Last Multiplier*, Electronic Journal of Differential Equations **2018** (120), 1–9, https://ejde.math.txstate.edu/Volumes/2018/120/chanda.pdf .
3. *Strict period decrease and sharp large-amplitude laws for quintic global centers*, public mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-strict-period-decrease-and-sharp-large-amplitude-laws-for-quinti--ffe383da977f (its RESULT.md inspected in full).
4. L.-J. Yang and X.-W. Zeng, *The period function of Liénard systems*, Proc. Royal Soc. Edinburgh A **143** (2013), 205–221, doi:10.1017/S0308210511000096 (abstract and metadata inspected; full text not obtained).
