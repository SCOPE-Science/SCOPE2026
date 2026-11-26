# A sharp duration–amplitude tipping boundary for temporary habitat shocks in a strong-Allee predator–prey system

## Finding

A predator–prey community can recover from a temporary reduction in habitat capacity or collapse permanently **after the habitat is restored**. For the slow–fast strong-Allee model in [1], the fast-pulse limit has a complete, explicit survival–extinction classification. The shock must first exceed a sharp amplitude threshold; above it, the duration needed to cause irreversible extinction is an exact integral, strictly decreasing with shock amplitude and diverging with a universal inverse-square-root law at its lower endpoint. There is also a nontrivial baseline parameter region in which *no admissible positive shock of any finite fast-scaled duration* can induce collapse in this limit.

**Theorem.** Fix \(0<a<1\) and \((2-a)^{-1}<\phi_0<1\). Put
\[
v_0=(1-\phi_0)(1-a),\qquad w=a+\frac1{\phi_0}-1,\qquad
\phi_c=\frac1{(\sqrt{a+v_0}+\sqrt{v_0})^2}.
\]
For \(\varepsilon>0\), start at \((u(0),v(0))=(1,v_0)\), and solve the piecewise-autonomous system
\[
\varepsilon \frac{du}{dt}=u[(1-\phi(t)u)(u-a)-v],\qquad
\frac{dv}{dt}=v(u-1),
\]
where, for an amplitude \(\phi_1\in(\phi_0,1)\) and scaled duration \(s>0\),
\[
\phi(t)=\begin{cases}\phi_1,&0\le t<\varepsilon s,\\ \phi_0,&t\ge\varepsilon s.\end{cases}
\]
Here \(t\) is the original slow time, while \(s\) is the shock duration measured in fast prey-time units. The shock duration \(\varepsilon s\) tends to zero as \(\varepsilon\to0^+\); \(a,\phi_0,\phi_1,s\) remain fixed.

1. If \(\phi_0\ge(3+a)/4\), then for every admissible \(\phi_1\) and every fixed finite \(s>0\), the restored system converges to \((1,v_0)\) for all sufficiently small positive \(\varepsilon\).
2. If \((2-a)^{-1}<\phi_0<(3+a)/4\), then \(\phi_0<\phi_c<1\). For every \(\phi_1\le\phi_c\) and fixed finite \(s>0\), the restored system converges to \((1,v_0)\) for all sufficiently small positive \(\varepsilon\). For \(\phi_1>\phi_c\), define
\[
 s_c(\phi_1)=\int_w^1 \frac{d\xi}{\xi\left[\phi_1\xi^2-(1+a\phi_1)\xi+(a+v_0)\right]}.
\]
This is finite and strictly positive. For fixed \(0<s<s_c(\phi_1)\), the restored solution converges to \((1,v_0)\) for all sufficiently small \(\varepsilon>0\). For fixed \(s>s_c(\phi_1)\), it converges instead to the extinction equilibrium \((0,0)\) for all sufficiently small \(\varepsilon>0\). No conclusion is claimed at the singular boundary \(s=s_c(\phi_1)\).
3. On \((\phi_c,1)\), \(s_c\) is continuously differentiable and strictly decreasing; \(\lim_{\phi_1\uparrow1}s_c(\phi_1)\in(0,\infty)\). As \(\phi_1\downarrow\phi_c\),
\[
 s_c(\phi_1)\sim \frac{C(a,\phi_0)}{\sqrt{\phi_1-\phi_c}},\qquad
 C(a,\phi_0)=\frac{4\pi\phi_c^{3/2}}{(1+a\phi_c)\sqrt{1-a^2\phi_c^2}}.
\]
All of these assertions concern fixed finite \(s\) followed by the limit \(\varepsilon\to0^+\), not an exact finite-\(\varepsilon\) threshold or a uniform assertion as \(s\to\infty\).

**Exact example.** For \(a=1/2\), \(\phi_0=4/5\), \(v_0=1/10\), and \(w=3/4\), the shock fold occurs at \(\phi_c=(14-4\sqrt6)/5\). At \(\phi_1=9/10\),
\[
 s_c=20\int_{3/4}^{1}\frac{d\xi}{\xi(18\xi^2-29\xi+12)}
 =\frac56\log\frac23+\frac{145\sqrt{23}}{69}\arctan\sqrt{23}
 =13.421142615246071\ldots.
\]
Thus a pulse lasting \(12\varepsilon\) yields long-term recovery, whereas one lasting \(15\varepsilon\) yields long-term extinction, for all sufficiently small positive \(\varepsilon\), despite the same restored habitat.

## Assumptions and scope

The model is deterministic, nonnegative, continuous across the two parameter switches and otherwise governed by the displayed differential equations. Both environmental values lie strictly below \(1\), and the original inverse capacity \(\phi_0\) lies above \((2-a)^{-1}\) so its coexistence point is a hyperbolic sink. No additional mortality impulse is applied at switching. The initial condition is precisely that baseline coexistence point; arbitrary starts are not classified. The study concerns rapid fixed-scaled-duration deterioration and recovery, not the prolonged linear environmental ramps examined in [1].

The value \(\phi_c\) is a shock-amplitude fold threshold depending on the *baseline predator population* \(v_0\). It is not the folded-saddle threshold for a linearly ramped three-dimensional system considered in [1].

## Proof

**Baseline dynamics and post-restoration basin test.** Define \(q_\phi(u)=(1-\phi u)(u-a)\). The equilibrium \(S=(1,v_0)\) has Jacobian
\[
 \begin{pmatrix}\big(1-(2-a)\phi_0\big)/\varepsilon&-1/\varepsilon\\v_0&0\end{pmatrix}.
\]
Its trace is strictly negative and determinant \(v_0/\varepsilon>0\), hence it is a hyperbolic sink for every positive \(\varepsilon\). The origin is likewise a sink, with eigenvalues \(-a/\varepsilon\) and \(-1\). The baseline factorization is \(q_{\phi_0}(u)-v_0=-\phi_0(u-1)(u-w)\), with \(a<w<(1+a\phi_0)/(2\phi_0)<1\). The scalar fast flow with \(v=v_0\) approaches \(1\) from any \(u>w\), and \(0\) from \(0<u<w\).

Consider restored initial states with prey tending to a fixed \(U_s>0\), \(U_s\ne w\), and predator equal to \(v_0+O(\varepsilon)\). On any bounded additional interval of fast time, continuous dependence gives convergence to the scalar flow from \(U_s\), with predator still \(v_0+O(\varepsilon)\). For \(U_s>w\), choose such an interval long enough that the limiting scalar prey value lies near \(1\) with \(h(u)<h(w)/2\), where \(h(u)=u-1-\log u\). Define the autonomous relative-entropy function (cf. [4])
\[
 E(u,v)=\varepsilon h(u)+v-v_0-v_0\log(v/v_0).
\]
The predator part is \(O(\varepsilon^2)\) at the end of this fast interval, so \(E<\varepsilon h(w)\) for sufficiently small \(\varepsilon\). For each such fixed \(\varepsilon\), the sublevel with bound equal to this entry value is compact in the positive quadrant and lies in \(u>w\): if \(u\le w\), then \(h(u)\ge h(w)\). In original time,
\[
 \dot E=(u-1)[q_{\phi_0}(u)-v_0]=-\phi_0(u-1)^2(u-w).
\]
The sublevel is forward invariant and the only invariant subset of \(\dot E=0\) within it is \(S\), since \(u=1\) can persist only when \(v=v_0\). It follows that the restored solution converges to \(S\).

For \(U_s<w\), choose the additional fast interval so that its limiting scalar endpoint has prey strictly below \(a/2\). The full system enters \(0<u<a/2\) for sufficiently small \(\varepsilon\). There the fast-time derivative satisfies \(u'\le -(a/2)(1-\phi_0 a/2)u\), because \(v\ge0\), \(a-u\ge a/2\) and \(1-\phi_0u\ge 1-\phi_0 a/2>0\). This region is forward invariant in the nonnegative quadrant and \(\dot v\le-(1-a/2)v\) in original time. Thus both populations tend to zero. Neither argument assigns a basin when \(U_s=w\).

**Fast pulse.** In fast time \(\theta=t/\varepsilon\), while the shock is active,
\[
 u'=u[q_{\phi_1}(u)-v],\qquad v'=\varepsilon v(u-1).
\]
On each fixed interval \(0\le\theta\le s\), ordinary continuous dependence and Gronwall estimates give \(v(\theta)=v_0+O(\varepsilon)\) and \(u(\theta)=U(\theta)+O(\varepsilon)\), where \(U(0)=1\) solves the scalar layer equation
\[
 U'=U[q_{\phi_1}(U)-v_0].
\]
The bounds are uniform on each fixed finite \(0\le\theta\le s\). The full solution stays nonnegative with \(u\le1/\phi_1\), since at that level the prey derivative is nonpositive. This bounds \(v'\) by \(O(\varepsilon)\) on the fast interval. The scalar solution stays positive for finite time and satisfies \(U\le1\), since \(q_{\phi_1}(1)<v_0\). Thus the restored initial values satisfy precisely the hypotheses of the basin test with \(U_s=U(s)\) whenever \(U(s)\ne w\).

**Amplitude threshold and finite-duration classification.** The parabola \(q_\phi\) has its maximum at
\[
 f(\phi)=\frac{1+a\phi}{2\phi},\qquad
 F(\phi)=\frac{(1-a\phi)^2}{4\phi}.
\]
On \((0,1/a)\), \(F'(\phi)=(a^2-\phi^{-2})/4<0\), and \(F(1/a)=0\). At baseline \(\phi_0\), the maximum is strictly larger than \(v_0\) because \(q_{\phi_0}(1)=v_0\) and \(1>f(\phi_0)\). Consequently there is a unique \(\phi_c\in(\phi_0,1/a)\) solving \(F(\phi_c)=v_0\), with the stated radical expression. It belongs to the admissible interval \((\phi_0,1)\) precisely when
\[
 v_0>F(1)=\frac{(1-a)^2}{4}\quad\Longleftrightarrow\quad \phi_0<\frac{3+a}{4}.
\]
For \(\phi_0<\phi\le\phi_c\), \(f(\phi)<1\) and \(f(\phi)>w\): if the continuous vertex first reached \(w\), then \(F(\phi)=q_\phi(w)<q_{\phi_0}(w)=v_0\) because \(w>a\), contradicting \(F(\phi)\ge v_0\). Also \(q_\phi(1)<v_0\). For \(\phi_1<\phi_c\), the stable upper root therefore lies in \((w,1)\). At \(\phi_1=\phi_c\), the two roots merge at \(f(\phi_c)\in(w,1)\). Scalar uniqueness prevents \(U\) from crossing either equilibrium in finite time. Thus the restored solution recovers for any fixed finite \(s\) whenever the shock does not exceed the admissible fold, including throughout the baseline immunity region.

For \(\phi_1>\phi_c\), \(q_{\phi_1}(u)<v_0\) at every \(u\), so the layer prey trajectory decreases strictly from \(1\), crosses \(w\) exactly once, and separation of variables gives the stated positive integral \(s_c\). It is the unique crossing time; the post-switch basin assignment above proves the two long-term outcomes whenever \(s\ne s_c\).

**Monotonicity and singular bottleneck.** On the integration interval \([w,1]\), \(\xi>a\). Differentiating the integrand with respect to \(\phi_1\), the denominator's derivative is \(\xi^2(\xi-a)>0\); therefore \(s_c\) strictly decreases and is smooth above \(\phi_c\). Its limit as \(\phi_1\uparrow1\) is finite and positive because the denominator stays uniformly positive there when \(\phi_c<1\). Completing the square,
\[
 v_0-q_\phi(u)=\phi\big(u-f(\phi)\big)^2+v_0-F(\phi).
\]
Since \(f(\phi_c)\in(w,1)\), only an interior quadratic bottleneck contributes the singular part of the integral. Write \(\delta=\phi-\phi_c\) and \(\kappa=-F'(\phi_c)=(1-a^2\phi_c^2)/(4\phi_c^2)>0\). Localizing the integral to a fixed small neighborhood of \(f(\phi_c)\) and rescaling \(u-f(\phi)\) by \(\sqrt\delta\) yields
\[
 s_c(\phi)\sim\frac{\pi}{f(\phi_c)\sqrt{\phi_c\kappa}}\delta^{-1/2}
 =\frac{4\pi\phi_c^{3/2}}{(1+a\phi_c)\sqrt{1-a^2\phi_c^2}}\delta^{-1/2}.
\]
The complement is bounded; the equality uses the explicit formula for \(f(\phi_c)\). This proves the claim.

**Exact example.** Substituting \(a=1/2\), \(\phi_0=4/5\), \(\phi_1=9/10\) into the integral gives the quadratic denominator \((18\xi^2-29\xi+12)/20\). Rational partial fractions and completion of the square yield the displayed logarithm/arctangent expression. Its value lies strictly between \(12\) and \(15\), establishing the two opposite outcomes without numerical integration of the biological ODE.

## Verification

Run the self-contained `verify.py` with Python 3 and SymPy/mpmath installed. It checks the fold and denominator identities symbolically in the example, compares the closed expression to quadrature at high precision, tests the two duration inequalities, and illustrates the bottleneck prefactor numerically at a sequence of amplitudes approaching the fold. Optional SciPy integration illustrates finite positive \(\varepsilon\) outcomes. The basin conclusions and the singular asymptotic are established by the analysis above, not by finite tests.

## Relationship to prior work

Hennessy, Popović, and Sattar [1] introduced and analysed the same strong-Allee two-species system under a **linear ramp** in inverse carrying capacity; its preprint provides the frozen critical manifold, fold geometry, bistability, and a ramp-rate tipping threshold. None of those established foundations is claimed here as new. The novel investigated input is instead a **finite rapid rectangular deterioration with full restoration**, where the predator remains quasi-frozen during the pulse. The above result supplies a complete sharp fast-pulse amplitude/duration diagram, an explicit baseline immunity region, and the exact fold-divergence constant.

Ratajczak and collaborators [2] showed qualitatively and computationally that ecological regime shifts under press/pulse disturbances depend jointly on intensity and duration. Karakoç and collaborators [3] investigated recovery under pulse and press perturbations in a different predator–prey/resource model. These general phenomena motivate the question; neither supplies the displayed exact limit classification for the model [1]. Standard scalar separatrix, singular perturbation, and quadratic bottleneck techniques are acknowledged as underlying methods.

For the same autonomous system, [4] gives the relative-entropy sublevel used here and a separate high-predator extinction certificate. The pulse classification does not require locating the full autonomous basin boundary: a bounded layer transient suffices to reach either the entropy sublevel or the low-prey region.

## Limitations

The duration boundary is exact only for the limiting fast-pulse problem, for each fixed shock amplitude and scaled duration separated from its critical value. In particular, **the outcome exactly at \(s=s_c\) is not determined** for small positive \(\varepsilon\); the theorem supplies neither a finite-\(\varepsilon\) exact critical duration nor uniform estimates as the parameters jointly approach the fold. The admissible deterioration is restricted to \(\phi_1<1\); no claim is made for more severe shocks, slowly varying forcing or arbitrary initial populations. The analysis is deterministic, spatially homogeneous, and excludes demographic noise. The literature comparison is not a mathematical proof of uniqueness or novelty; general fast–slow separatrix theory may already imply parts of the result as a corollary.

## References

[1] B. Hennessy, N. Popović, and Z. Sattar, *A minimal model for rate-induced tipping to extinction*, arXiv:2610.12319v1 (first public version, 8 October 2026), https://arxiv.org/abs/2610.12319 ; open HTML https://arxiv.t3mt.com/html/2610.12319v1 .

[2] Z. Ratajczak, P. D'Odorico, S. L. Collins, B. T. Bestelmeyer, F. I. Isbell, and J. B. Nippert, *The interactive effects of press/pulse intensity and duration on regime shifts at multiple scales*, Ecological Monographs 87 (2017), 198–218, https://doi.org/10.1002/ecm.1249 .

[3] C. Karakoç, A. Singer, K. Johst, H. Harms, and A. Chatzinotas, *Transient recovery dynamics of a predator–prey system under press and pulse disturbances*, BMC Ecology 17 (2017), 13, https://doi.org/10.1186/s12898-017-0123-2 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC5381073/ .

[4] *Two explicit, opposing basin certificates in a strong-Allee tipping model*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-two-explicit-opposing-basin-certificates-in-a-strong-allee-tippi--f7e958313282 .
