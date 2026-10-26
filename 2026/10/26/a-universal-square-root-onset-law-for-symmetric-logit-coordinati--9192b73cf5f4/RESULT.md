# A universal square-root onset law for symmetric logit coordination feedback

## Finding

For the **balanced environmental target** \(k=1/2\) in the two-speed coordination game of Loginov [1], the logit-flow threshold \(\lambda=4\) is globally sharp, including equality. Above it there is precisely one periodic state, and its **payoff-gap amplitude** obeys an explicit, feedback-rate-independent square-root law:
\[
\max_{0\le t<T_\lambda}(x(t)-y(t))
=\frac12\sqrt{\lambda-4}+O_\alpha((\lambda-4)^{3/2}),
\qquad T_\lambda\longrightarrow\frac{2\pi}{\sqrt\alpha}.
\]
The leading \(1/2\) is universal over \(\alpha>0\). On the cycle, exactly \(\overline x=\overline y=1/2\). The corresponding leading amplitudes of the centered cooperation and payoff coordinates are, respectively,
\[
\max_t\left|x(t)-\tfrac12\right|
=\frac{\sqrt{\lambda-4}}{2\sqrt{1+\alpha}}+O_\alpha((\lambda-4)^{3/2}),
\quad
\max_t\left|y(t)-\tfrac12\right|
=\frac{\sqrt\alpha\,\sqrt{\lambda-4}}{2\sqrt{1+\alpha}}+O_\alpha((\lambda-4)^{3/2}).
\]
The sharp threshold and qualitative unique-cycle conclusion follow by reducing the model to a classical Liénard oscillator; the additional explicit three-coordinate onset coefficients resolve the oscillation size in the original model.

## Assumptions and scope

Fix arbitrary \(\alpha>0\), \(\lambda>0\). Consider the autonomous equations
\[
\dot x=S_\lambda(x-y)-x,\qquad
\dot y=\alpha(x-\tfrac12),\qquad
S_\lambda(z)=\frac{1}{1+e^{-\lambda z}}.
\]
Here \(x\in[0,1]\) is a population share and \(y\in\mathbb R\) is the moving payoff-comparison state. The strip \([0,1]\times\mathbb R\) is forward invariant because \(\dot x>0\) at \(x=0\) and \(\dot x<0\) at \(x=1\). In the original notation [1], \(\alpha=r/s>0\), \(\lambda=s/\eta>0\), and the environmental balance point is \(k=1/2\). Every assertion concerns forward solutions of these exact continuous-time equations, not a discrete imitation map or arbitrary asymmetric \(k\).

There is precisely one equilibrium, \(x=y=1/2\). For \(\lambda\le4\), it attracts every point of the strip, including the critical equality \(\lambda=4\). For \(\lambda>4\), it is unstable, and there is exactly one nonconstant periodic orbit, asymptotically orbitally attracting every other forward trajectory from the strip. There is no assertion of a uniform convergence rate near the threshold.

## Proof

**1. Exact oscillator reduction.** Put \(z=x-y\) and \(v=\dot z\). Directly,
\[
 v=S_\lambda(z)+\alpha/2-(1+\alpha)x,
\quad x=\frac{S_\lambda(z)+\alpha/2-v}{1+\alpha},\quad y=x-z.
\]
Consequently the full planar flow is conjugate to the second-order equation
\[
\ddot z+f_\lambda(z)\dot z+g_{\lambda,\alpha}(z)=0,
\quad f_\lambda(z)=1-\frac\lambda4\operatorname{sech}^2(\lambda z/2),
\quad g_{\lambda,\alpha}(z)=\frac\alpha2\tanh(\lambda z/2).
\]
The primitive \(F_\lambda(z)=\int_0^z f_\lambda(w)\,dw\) and the potential \(G_{\lambda,\alpha}=\int_0^z g_{\lambda,\alpha}(w)dw\) are
\[
F_\lambda(z)=z-\frac12\tanh(\lambda z/2),\qquad
G_{\lambda,\alpha}(z)=\frac\alpha\lambda\log\cosh(\lambda z/2).
\]
Both are even or odd as appropriate, and \(G\to\infty\) as \(|z|\to\infty\).

**2. Damped and critical regimes.** For \(\lambda\le4\), \(f_\lambda(z)\ge0\), and its zero set is empty if \(\lambda<4\) and only \(z=0\) if \(\lambda=4\). The proper energy \(E=v^2/2+G(z)\) satisfies \(\dot E=-f_\lambda(z)v^2\le0\). No nonstationary full trajectory can remain inside \(\{\dot E=0\}\): a nonconstant solution would need \(z=0\) or \(v=0\) continuously, incompatible with the oscillator equations. LaSalle's principle gives convergence to the equilibrium for every initial point (indeed for the full \((z,v)\)-plane). Equality at \(\lambda=4\) is included; linearization alone would not suffice there.

**3. Unique attracting cycle for \(\lambda>4\).** For positive \(z\),
\[
f_\lambda'(z)=\frac{\lambda^2}{4}\operatorname{sech}^2(\lambda z/2)\tanh(\lambda z/2)>0.
\]
Thus \(f\) increases from a strictly negative value \(1-\lambda/4\) to \(1\), changing sign once on each half-line. The odd function \(F\) therefore has one positive zero \(a>0\), is strictly negative on \((0,a)\), strictly positive and increasing on \((a,\infty)\), and tends to \(+\infty\). The odd restoring force obeys \(g(z)>0\) for \(z>0\), and its primitive \(G\) is radially unbounded. These are precisely the classical Liénard unique stable-cycle existence conditions [2,3], so there is exactly one nonconstant periodic orbit and it is attracting. Its equilibrium has trace \(\lambda/4-1>0\) and determinant \(\alpha\lambda/4>0\), hence is a source. All other physical trajectories are bounded and enter the unique cycle's basin, using the Liénard trapping conclusion (alternatively the convergence-to-a-periodic-orbit theorem in [1] and uniqueness).

**4. Exact half-period symmetry and averages.** Because \(S_\lambda(-z)=1-S_\lambda(z)\), the original vector field commutes with the involution \((x,y)\mapsto(1-x,1-y)\). It preserves the unique periodic orbit. Its action on the orbit is a nontrivial time translation of order two: it cannot be the identity because only the excluded equilibrium is fixed. Therefore it equals a shift of \(T/2\), so \(x(t+T/2)=1-x(t)\), \(y(t+T/2)=1-y(t)\), and both time means equal \(1/2\) exactly.

**5. Sharp oscillation-size coefficient.** Write \(\delta=\lambda-4>0\), and consider the branch as \(\delta\downarrow0\). Taylor expansion about the equilibrium yields
\[
f_\lambda(z)=-\frac\delta4+4z^2+O(\delta z^2+z^4),
\quad g_{\lambda,\alpha}(z)=\alpha z+O(\delta z+z^3).
\]
The unperturbed angular frequency is \(\omega=\sqrt\alpha\). For a small sinusoidal oscillation \(z=A\cos(\omega t)\), the exact energy derivative has one-cycle mean
\[
\left\langle\dot E\right\rangle
=\frac{\delta\alpha A^2}{8}-\frac{\alpha A^4}{2}
+O_\alpha(\delta^2 A^2+\delta A^4+A^6).
\]
This follows from \(\langle\sin^2\rangle=1/2\) and \(\langle\sin^2\cos^2\rangle=1/8\); corrections to the leading harmonic do not alter the displayed terms. Dividing by the derivative \(d(\alpha A^2/2)/dA=\alpha A\) gives the local radial return-flow normal form
\[
\dot A=\frac\delta8 A-\frac12 A^3
+O_\alpha(\delta^2 A+\delta A^3+A^5).
\]
The coefficient of \(A^3\) is strictly negative. The nondegenerate supercritical Hopf theorem, or the implicit-function theorem for the analytic radial Poincaré displacement after \(A=\sqrt\delta\,a\), gives \(A^2=\delta/4+O_\alpha(\delta^2)\). The cycle's positive maximum of \(z\) therefore satisfies \(A=\tfrac12\sqrt\delta+O_\alpha(\delta^{3/2})\). Its period tends to \(2\pi/\sqrt\alpha\). The inverse transformation in step 1 sends its leading sinusoidal \(z\) and quadrature derivative \(v\) to the stated leading amplitudes of \(x\) and \(y\), with no quadratic waveform correction because the vector field is odd about its equilibrium. The inverse map also verifies that the small cycle lies strictly in the physical strip.

## Verification

Run the included standalone Python file `verify.py` after installing the dependencies in `requirements.txt`. The program checks the exact coordinate reduction and derivative coefficients, numerically confirms the stable-cycle asymptotic at several positive feedback rates, and checks the half-wave shift and periodic means. It also checks energy monotonicity when \(\lambda\le4\). Exact symbolic calculations and the stated Liénard/Hopf arguments, not finite simulations, establish the infinite-dimensional parameter assertions.

## Relationship to prior work

Loginov [1] introduces the logit feedback system, identifies the local noise stability boundary, and proves convergence to closed orbits in the oscillatory regime. The paper does not provide uniqueness of the selected orbit; the uniqueness question is explicitly raised there. The qualitative symmetric-case uniqueness is a direct specialization, under the exact oscillator reduction above, of classical Liénard existence/uniqueness theorems [2,3]. It is **not asserted as a newly invented general Liénard theorem**. The additional contribution here is the combined model-specific global critical classification and the exact rate-independent \(1/2\) leading amplitude coefficient for the payoff gap, with translated cooperation and payoff amplitudes and exact half-wave symmetry. No matching explicit quantitative statement was identified in the inspected primary literature or bibliographic searches. Broad Hopf theory predicts square-root order but does not itself specify the coefficient for these game coordinates.

## Limitations

Only \(k=1/2\) is classified. The leading asymptotic is as \(\lambda\downarrow4\) from above and its higher-order constants can depend on \(\alpha\). No convergence rates or amplitude formulas for arbitrary \(\lambda>4\) are asserted. The result is deterministic, with homogeneous behavior and exactly logistic revision; it does not classify stochastic finite-population systems or asymmetric environmental targets. An equivalent game-specific quantitative expansion in other sources remains a bibliographic risk. No independent audit or validation has been performed.

## References

[1] George Loginov, *Cyclical behavior of evolutionary dynamics in coordination games with changing payoffs*, International Journal of Game Theory **51** (2022), 1–27. First made public online 2021-06-14. DOI:10.1007/s00182-021-00783-z. Full preprint: arXiv:2106.08224.

[2] Classical Liénard existence and uniqueness criterion; see A. Liénard (1928), *Étude des oscillations entretenues*, Revue générale de l'électricité **23**, 901–912, 946–954, and standard Levinson–Smith refinements.

[3] L. Rosati and G. Villari, *On Massera's theorem concerning the uniqueness of a periodic solution for the Liénard equation. When does such a periodic solution actually exist?*, Boundary Value Problems **2013**, article 144. DOI:10.1186/1687-2770-2013-144.
