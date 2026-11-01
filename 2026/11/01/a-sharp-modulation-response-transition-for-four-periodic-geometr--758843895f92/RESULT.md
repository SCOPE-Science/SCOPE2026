# A sharp modulation-response transition for four-periodic geometric weighted-shift tests

## Finding
Let \(0<q<1\), \(s,t>0\), and let \(T_{q,s,t}\) be the unilateral weighted shift on \(\ell^2(\mathbb N_0)\) with weights
\[
w_{4k+j}=q^{4k+j}\sigma_j,\qquad (\sigma_0,\sigma_1,\sigma_2,\sigma_3)=(1,s,1,t),\qquad k\ge0.
\]
Its normalized geometric vectors \(v_z=\sqrt{1-z}(1,\sqrt z,z,z^{3/2},\ldots)\) yield the lower-bound functional
\[
F_{q,s,t}(z)=\langle T_{q,s,t}v_z,v_z\rangle
=\frac{\sqrt z(1-z)(1+sqz+q^2z^2+tq^3z^3)}{1-q^4z^4},\quad 0<z<1.
\]
Let \(z_*(q,s,t)\) be its unique maximizer. Define \(\rho(q)\) as the unique zero in \((0,1)\) of
\[
3-5\rho+q^4\rho^4(5-3\rho)=0,
\]
and define the positive transition parameter
\[
\tau(q)=\frac{1-q^2\rho(q)^2}{2q^3\rho(q)^3}.
\]
**Sharp response phase diagram.** At every permissible parameter triple,
\[
\frac{\partial z_*}{\partial t}>0,\qquad
\operatorname{sgn}\!\left(\frac{\partial z_*}{\partial s}\right)
=\operatorname{sgn}(\tau(q)-t).
\]
On the **entire neutral surface** \(t=\tau(q)\), the maximizer is exactly \(\rho(q)\) for every \(s>0\), independently of the first modulation. The transition \(\tau:(0,1)\to(0,\infty)\) is strictly decreasing and onto, with sharp endpoint laws
\[
\tau(q)=\frac{125}{54}q^{-3}-\frac56q^{-1}+O(q)\quad(q\downarrow0),
\]
\[
\tau(q)=\left(\frac45\right)^{1/3}(1-q)^{1/3}
+O\bigl((1-q)^{2/3}\bigr)\quad(q\uparrow1).
\]
Consequently, for each fixed \(t>0\) there is exactly one \(q_c(t)\in(0,1)\) where the response to \(s\) reverses; its endpoint laws are
\[
1-q_c(t)\sim\frac54t^3\quad(t\downarrow0),\qquad
q_c(t)\sim\left(\frac{125}{54t}\right)^{1/3}\quad(t\to\infty).
\]
These are statements about the optimizing **geometric test vector**, not the maximizing vector over the whole Hilbert space or the exact numerical radius.

## Assumptions and scope
All parameters \(q,s,t\) are real and positive, with \(q<1\). The inner product is linear in the first argument, but the displayed Rayleigh quotient is positive real regardless of convention. The operator is compact because its weights decay geometrically. Its numerical radius \(w(T_{q,s,t})\) satisfies \(w(T_{q,s,t})\ge \max_{0<z<1}F_{q,s,t}(z)\). No differentiability or monotonicity assertion here concerns \(w(T_{q,s,t})\) itself. Every parameter derivative is taken with the other two parameters fixed.

## Proof
**Step 1: algebraic stationarity and uniqueness.** Put \(P(z)=1+sqz+q^2z^2+tq^3z^3\) and
\[
h_j(z)=(2j+1)-(2j+3)z+q^4z^4[(7-2j)+(2j-5)z],\quad j=0,1,2,3.
\]
Direct differentiation gives
\[
F_{q,s,t}'(z)=\frac{G(z)}{2\sqrt z(1-q^4z^4)^2},\qquad
G(z)=h_0(z)+sqz\,h_1(z)+q^2z^2h_2(z)+tq^3z^3h_3(z).
\]
One has \(G(0)=1\) and \(G(1)=-2(1-q^4)P(1)<0\). We give a self-contained algebraic uniqueness certificate, while not claiming uniqueness itself as new. Let \(y=z/(1-z)\), \(x=qs\), \(u=q^2\), and \(v=q^3t\). The polynomial \(H(y)=(1+y)^8G(y/(1+y))=\sum_{j=0}^8c_jy^j\) has coefficients
\[
\begin{aligned}
c_0&=1, & c_1&=5+3x,&c_2&=7+16x+5u,\\
c_3&=-7+33x+23u+7v,\\
c_4&=-35+30x+40u+26v+7u^2,\\
c_5&=-49+(5+5u^2)x+30u+34v+23u^2,\\
c_6&=-35+(12u^2-12)x+5u+16v+27u^2+3u^3,\\
c_7&=-(1-u^2)(13+9x+5u+v),\\
c_8&=-2(1-u^2)(1+x+u+v).
\end{aligned}
\]
For \(x,v>0\), \(0<u<1\), the coefficients \(c_0,c_1,c_2\) are positive and \(c_7,c_8\) negative. The exact inequalities
\[
\begin{aligned}
c_4-4c_3&=7u^2-52u-2v-102x-7<0,\\
5c_5-7c_4&=66u^2-130u-12v+(25u^2-185)x<0,\\
2c_6-c_5&=6u^3+31u^2-20u-2v+(19u^2-29)x-21<0
\end{aligned}
\]
show that once any of \(c_3,c_4,c_5\) is nonpositive, all subsequent middle coefficients are negative. The last inequality follows from \(6u^3+31u^2\le37u\), hence the parameter-free part is at most \(17u-21<0\); the other two are immediate for \(0<u<1\). Thus \(H\) has exactly one sign change. Descartes' rule and the opposite endpoint signs give a **single positive zero counted with multiplicity**, hence one simple zero of \(G\) on \((0,1)\), at which \(G_z<0\). This is the global maximum \(z_*\), and the implicit-function theorem gives analytic parameter dependence.

**Step 2: a distinguished single-mode marker.** The polynomial
\[
h_1(z)=3-5z+q^4z^4(5-3z)
\]
is strictly decreasing on \((0,1)\), since
\[
\partial_z h_1=5[q^4z^3(4-3z)-1]<0.
\]
It starts at \(3\) and ends at \(-2(1-q^4)\), so its unique zero \(\rho(q)\) is well-defined. Moreover
\[
h_j(z)-h_1(z)=2(j-1)(1-z)(1-q^4z^4).
\]
At \(z=\rho\) put \(B=(1-\rho)(1-q^4\rho^4)>0\). Then \(h_0=-2B\), \(h_1=0\), \(h_2=2B\), \(h_3=4B\), so
\[
G(\rho)=2B[-1+q^2\rho^2+2tq^3\rho^3]
=4Bq^3\rho^3[t-\tau(q)].
\]
Since \(G\) changes from positive to negative at \(z_*\), this identity gives
\[
\operatorname{sgn}(z_*-\rho)=\operatorname{sgn}(t-\tau(q)).
\]
In particular \(z_*=\rho\) identically in \(s\) along the neutral surface.

**Step 3: derivative signs.** Differentiation of \(G(z_*(q,s,t),q,s,t)=0\), using \(G_z(z_*)<0\), yields
\[
\partial_s z_*=-\frac{qz_*h_1(z_*)}{G_z(z_*)},\qquad
\partial_t z_*=-\frac{q^3z_*^3h_3(z_*)}{G_z(z_*)}.
\]
The strict decrease of \(h_1\) and Step 2 give the stated sign of \(\partial_s z_*\). To establish \(\partial_t z_*>0\), note that \(h_3(z)=7-9z+q^4z^4(1+z)\) decreases strictly from \(7\) to \(-2(1-q^4)\) because \(h_3'=-9+q^4(4z^3+5z^4)<0\). At its unique zero \(\zeta_3\), all \(h_j(\zeta_3)<0\) for \(j<3\), by the displayed affine difference formula. Hence \(G(\zeta_3)<0\), so \(z_*<\zeta_3\) and \(h_3(z_*)>0\), proving the strict positive derivative.

**Step 4: the global critical curve and endpoint exponents.** Implicit differentiation of \(h_1(\rho(q),q)=0\) gives \(\rho'(q)>0\), since \(\partial_qh_1=4q^3\rho^4(5-3\rho)>0\) and \(\partial_zh_1<0\). Writing \(v(q)=q\rho(q)\), we have \(v'(q)>0\) and
\[
\tau(q)=\frac{1-v(q)^2}{2v(q)^3},\qquad
\frac{d}{dv}\frac{1-v^2}{2v^3}=\frac{v^2-3}{2v^4}<0.
\]
The endpoint limits of \(\rho\) are \(3/5\) at \(q=0\) and \(1\) at \(q=1\), proving that \(\tau\) decreases bijectively from infinity to zero. Near zero, \(\rho(q)=3/5+O(q^4)\), which produces the claimed two-term Laurent expansion. Near one, write \(\delta=1-\rho\), \(\eta=1-q^4\). The defining equation is exactly
\[
\delta^3(10-10\delta+3\delta^2)=\eta(1-\delta)^4(2+3\delta).
\]
Thus \(\delta=(\eta/5)^{1/3}+O(\eta^{2/3})=(4/5)^{1/3}(1-q)^{1/3}+O((1-q)^{2/3})\), and \(\tau(q)=\delta+O(\delta^2+1-q)\). Inverting this strictly monotone relation gives the two stated laws for \(q_c(t)\). All asymptotics use ordinary real positive limits.

## Verification
Run `python verify.py` using Python 3 with SymPy, NumPy and SciPy. The standalone checker reconstructs the stationarity polynomial, its Möbius-transformed coefficients, each sign-chain identity, the exact neutral-surface formula, and the parameter-response signs at 90 parameter configurations. It also tests low- and high-\(q\) endpoint constants. The analytic proof establishes the continuum claims; the finite tests are supplementary and cannot certify publication priority or universal uniqueness on their own. For example at \(q=1/2\), one gets \(\rho\approx0.605344269354\) and \(\tau\approx16.38041228249\). At \(t=1\), increasing \(s\) moves \(z_*\) right, while at \(t=40\), increasing \(s\) moves it left; at \(t=\tau\), \(z_*\) is exactly independent of \(s\).

## Relationship to prior work
Ghosh, Birbonshi and Ojha (2026), arXiv:2608.17486, introduced the four-periodic geometric weighted shift and its geometric-vector lower bound; they analyzed the eighth-degree critical equation and a restricted uniqueness regime. A separate prior uniqueness result for this exact test profile has already established one simple optimizer for all positive modulations. **Neither optimizer uniqueness nor the numerical-radius lower-bound formula is claimed as new.** The present statement isolates the exact *directional parameter-response transition*, the entire first-modulation-neutral surface, its strict monotone global phase curve, and its cubic-root boundary law. A previously published allocation transition for the actual numerical radius under a fixed modulation budget concerns a different constrained optimization problem; it does not give derivatives of the geometric-vector maximizer at fixed modulations. Classical weighted-shift numerical-range papers provide background, not a covering response classification.

## Limitations
The distinguished variable is the geometric-vector Rayleigh optimizer, **not** a norming vector for the actual numerical radius. No statement is made at \(q=1\), for nonpositive parameters, or about higher-period patterns. The uniqueness lemma is prior mathematical coverage and the new phase diagram is a sharpened consequence requiring additional analysis, not a claim of an independent numerical-radius formula. Publication priority for equivalent sensitivity formulas in unindexed or incompletely accessible literature remains unresolved; no independent audit has been performed.

## References
1. A. Ghosh, R. Birbonshi and S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486, first public version 18 August 2026, https://arxiv.org/abs/2608.17486.
2. B. Chakraborty and S. Ojha, *On the numerical radius of weighted shift operators with generalized geometric weights*, Journal of Mathematical Analysis and Applications 543 (2025), 129021, https://doi.org/10.1016/j.jmaa.2024.129021.
3. Prior mathematical record, *Unique geometric test-vector optimizer for four-periodic weighted shifts*, claim identifier cafdbb59-8ee0-46de-b4ba-c105db682bc7 (unpublished; cited solely to credit the already-established full-parameter uniqueness step).
