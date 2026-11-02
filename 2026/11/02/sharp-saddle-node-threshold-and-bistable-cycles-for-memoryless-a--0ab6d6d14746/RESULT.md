# Sharp saddle-node threshold and bistable cycles for memoryless Adam on superquadratic losses

## Finding

Fix a real exponent \(p>2\), positive denominator shift \(\varepsilon>0\), and constant step \(\eta>0\). Consider deterministic Adam with bias-corrected first- and second-moment coefficients both set to zero, applied to the strictly convex scalar loss
\[
f_p(x)=\frac{|x|^p}{p}.
\]
Its precise iteration is
\[
x_{k+1}=T(x_k),\qquad
T(x)=x-\eta\frac{|x|^{p-2}x}{|x|^{p-1}+\varepsilon},\qquad x\in\mathbb R.
\]
This is the memoryless, denominator-smoothed normalized-gradient update, not the two-memory Adam iteration.

Define
\[
r_*=((p-2)\varepsilon)^{1/(p-1)},\qquad
\eta_c=\frac{2(p-1)}{p-2}\,r_*.
\]
Then the following threshold is **sharp**.

1. **Universal convergence below the threshold.** If \(0<\eta<\eta_c\), every real initial point converges to the unique minimizer \(0\); indeed \(|T(x)|<|x|\) for every \(x\ne0\).
2. **A critical two-cycle.** At \(\eta=\eta_c\), \(\{r_*,-r_*\}\) is a nonzero symmetric period-two orbit. Its two-step derivative is \(1\). Thus universal convergence to the minimizer fails at equality.
3. **Bistability above the threshold.** If \(\eta>\eta_c\), there are exactly two distinct positive solutions \(r_-<r_*<r_+\) of
   \[
   r+\frac{\varepsilon}{r^{p-2}}=\frac\eta2.
   \]
   They give exactly two symmetric nonzero sign-alternating period-two orbits \(\{r_-,-r_-\}\) and \(\{r_+,-r_+\}\). The first is locally repelling and the second locally asymptotically attracting. The minimizer \(0\) also remains locally asymptotically attracting **for every** \(\eta>0\). Thus two distinct attracting invariant sets coexist above the sharp threshold.

At either symmetric two-cycle of radius \(r\), the exact two-step derivative is
\[
\mu_2(r)=\left(1-\frac{2(p-1)\varepsilon}{r^{p-1}+\varepsilon}\right)^2.
\]
As \(\eta\downarrow\eta_c\) from above, its two radii coalesce with the square-root law
\[
r_\pm=r_*\pm\sqrt{\frac{r_*}{p-1}}\sqrt{\eta-\eta_c}
+O(\eta-\eta_c).
\]
Moreover, any nonterminating trajectory converging to \(0\) has the exact algebraic asymptotic
\[
\lim_{k\to\infty}k|x_k|^{p-2}
=\frac{\varepsilon}{(p-2)\eta}.
\]
Here *nonterminating* means \(x_k\ne0\) for every finite index; some initial points reach the minimizer exactly in one or more steps.

For the explicit cubic loss \(f_3(x)=|x|^3/3\), take \(\varepsilon=1\), \(\eta=5\). Then \(\eta_c=4\), and the two nonzero cycles have radii \(1/2\) and \(2\). Their exact two-step multipliers are respectively \(121/25\) (repelling) and \(1/25\) (attracting), even though \(0\) is also locally attracting. The attracting nonzero orbit has constant positive objective \(8/3\).

## Assumptions and scope

The exponent \(p\) is any real number strictly greater than \(2\), with no upper bound. The loss and gradient are deterministic, the step and denominator shift are constant and strictly positive, and all operations are in exact real arithmetic. The Adam specialization has \(\beta_1=\beta_2=0\), and the denominator is \(\sqrt{\widehat v_k}+\varepsilon\); consequently the denominator becomes \(|f_p'(x_k)|+\varepsilon\). There is no weight decay, projection, gradient noise, or numerical clipping.

“Symmetric cycle” means precisely the pair \(\{r,-r\}\) with \(r>0\) and \(T(r)=-r\). The theorem classifies these symmetric cycles, not all possible nonsymmetric periodic orbits. “Universal convergence” means every real initial point converges to the minimizer under repeated application of this one-step map; it is not a statement about full Adam with positive memory coefficients.

## Proof

**Reduction to a scalar radial multiplier.** For \(r>0\), set
\[
h(r)=r+\varepsilon r^{-(p-2)},\qquad
u(r)=\frac\eta{h(r)}
=\frac{\eta r^{p-2}}{r^{p-1}+\varepsilon}.
\]
The map is odd and satisfies
\[
T(x)=x(1-\nu(|x|)),\qquad |T(x)|=|x|\,|1-\nu(|x|)|.
\]
One has
\[
h'(r)=1-(p-2)\varepsilon r^{-(p-1)},\qquad
h''(r)=(p-2)(p-1)\varepsilon r^{-p}>0.
\]
Also \(h(r)\to\infty\) both as \(r\downarrow0\) and as \(r\to\infty\). Therefore its unique global minimum occurs at the point satisfying \(r_*^{p-1}=(p-2)\varepsilon\), and
\[
h(r_*)=\frac{p-1}{p-2}r_*,\qquad
\max_{r>0}\nu(r)=\frac\eta{h(r_*)}=\frac{2\eta}{\eta_c}.
\]

**Global threshold.** For \(0<\eta<\eta_c\), we have \(0<\nu(r)<2\) for every positive radius, whence \(|T(x)|<|x|\) whenever \(x\ne0\). Along any orbit, its nonnegative radii therefore decrease until a possible finite hit at zero or otherwise approach a limit \(a\ge0\). If \(a>0\), continuity of \(\nu\) gives \(|1-\nu(a)|<1\), contradicting convergence of the positive radii to \(a\). Thus \(a=0\) and universal convergence follows.

At \(\eta=\eta_c\), the radial multiplier at \(r_*\) is \(\nu(r_*)=2\); consequently \(T(r_*)=-r_*\), and oddness gives \(T(-r_*)=r_*\). Hence universal convergence fails at equality. For every \(\eta>\eta_c\), the cycles below also prevent universal convergence. This proves the exact if-and-only-if universal convergence boundary.

**Number and stability of symmetric cycles.** The condition \(T(r)=-r\) is equivalent to \(\nu(r)=2\), or \(h(r)=\eta/2\). Strict decrease of \(h\) on \((0,r_*)\), strict increase on \((r_*,\infty)\), and its two infinite endpoint limits give no positive solution below the threshold, exactly one double solution at the threshold, and precisely two solutions above it.

For \(r>0\), direct differentiation of the original map gives
\[
T'(r)=1-\frac{\eta(p-1)\varepsilon r^{p-2}}{(r^{p-1}+\varepsilon)^2}.
\]
At a cycle \(\eta=2(r^{p-1}+\varepsilon)/r^{p-2}\), so
\[
T'(r)=1-\frac{2(p-1)\varepsilon}{r^{p-1}+\varepsilon}.
\]
Since \(T\) is odd, its derivative is even at nonzero points; thus the multiplier of \(T\circ T\) at the symmetric cycle is precisely \(\mu_2(r)=(T'(r))^2\). For \(r<r_*\), the denominator is less than \((p-1)\varepsilon\), so \(T'(r)<-1\) and \(\mu_2(r)>1\). For \(r>r_*\), \(-1<T'(r)<1\), so \(\mu_2(r)<1\) and the orbit attracts an open neighborhood. At \(r=r_*\), \(T'(r_*)=-1\), proving the stated unit multiplier without asserting hyperbolic stability at the collision.

**Minimizer stability for all steps.** As \(r\downarrow0\), \(\nu(r)=\eta r^{p-2}/\varepsilon+o(r^{p-2})\to0\). For some sufficiently small \(\delta>0\), therefore, \(0<\nu(r)<1\) for all \(0<r<\delta\). On that neighborhood the map is sign-preserving and strictly reduces radius. The preceding limit argument again shows all its orbits tend to zero and remain in the same neighborhood. This establishes local asymptotic stability of zero regardless of \(\eta\); the derivative at zero is \(1\), so this conclusion is nonlinear rather than exponential linear stability.

**Square-root coalescence.** At its critical point,
\[
h''(r_*)=\frac{p-1}{r_*}>0.
\]
Taylor expansion there gives
\[
h(r_*+s)=h(r_*)+\frac{p-1}{2r_*}s^2+O(s^3).
\]
Using \(h(r_\pm)=\eta/2\) and \(h(r_*)=\eta_c/2\), inversion on the two monotone sides gives
\[
s_\pm=\pm\sqrt{\frac{r_*}{p-1}}\sqrt{\eta-\eta_c}+O(\eta-\eta_c).
\]
This is a nondegenerate saddle-node collision of the *symmetric period-two radii*.

**Exact tail rate.** Suppose an orbit converges to zero but never lands exactly at zero. Since \(\nu(r)\to0\), for all sufficiently large \(k\) its radius \(r_k=|x_k|\) satisfies \(r_{k+1}=r_k(1-\nu(r_k))\). Put \(a=p-2>0\) and \(z_k=r_k^{-a}\). The binomial expansion at zero gives
\[
\begin{aligned}
z_{k+1}-z_k
&=z_k\left[(1-\nu(r_k))^{-a}-1\right]\\
&=a z_k\nu(r_k)(1+o(1))\\
&=\frac{a\eta}{\varepsilon+r_k^{p-1}}(1+o(1))
\longrightarrow\frac{a\eta}{\varepsilon}.
\end{aligned}
\]
Averaging these increments yields \(z_k/k\to a\eta/\varepsilon\), equivalently \(k r_k^a\to\varepsilon/(a\eta)\).

**Exact cubic witness.** For \(p=3\), \(\varepsilon=1\), the symmetric-cycle equation is \(r+1/r=\eta/2\). At \(\eta=5\) it factors to give \(r=1/2\) and \(r=2\). The derivative formula becomes \(T'(r)=1-4/(r^2+1)\), giving \(T'(1/2)=-11/5\) and \(T'(2)=1/5\). Their squared two-step derivatives and objective values are as stated.

## Verification

The self-contained Python standard-library script `artifacts/verify.py` checks the exact rational cubic example, directly evaluates the original update and analytic minimizer, numerically locates both roots for randomized real exponents and shifts, checks cycle identities and stability types, samples strict global contraction, and verifies the asymptotic coefficient along nonterminating trajectories. It reports 3,970 passing finite arithmetic and numerical assertions.

These finite checks support the algebra but do not prove the universal quantifiers, uniqueness, stability, or infinite-time rate. Those assertions follow from the preceding derivative, convexity, continuity, Taylor, and summation arguments. The finite precision tests do not address the boundary in arbitrary precision or floating-point implementations.

## Relationship to prior work

Tang, Chen, and Liu (2026), *Beyond Quadratic Loss: The Stability Phase Diagram of Adam*, investigate optimizer loss spikes and superquadratic geometry as two momentum coefficients vary. Their publicly accessible abstract and detailed summaries do not state a global convergence threshold, saddle-node creation of two distinct symmetric cycles, or coexistence with an attracting minimizer in the \(\beta_1=\beta_2=0\) specialization. Their full primary manuscript could not be inspected, leaving an explicit priority uncertainty; the present result should not be described as an improvement over their analysis of full Adam.

The published note *Decoupled weight decay lowers the exact chattering threshold in AdamW* analyzes a denominator-smoothed **quadratic** normalized-gradient map, where the origin loses local stability at a flip threshold. This does not imply the present result for superquadratic losses: here the normalization factor vanishes at zero, the origin stays attracting, and two distinct cycles emerge away from the origin. *A sharp flip frontier for the Polar-Express surrogate on scalar quadratics* likewise has a finite nonzero normalized gain at zero and a single cycle created by a flip. The published *Sharp partial-adaptivity phase transition in scalar Padam* uses a historical maximum of second moments and a different memory recurrence, not this memoryless smoothed-gradient map.

The saddle-node and period-two multiplier tools themselves are standard one-dimensional dynamical-systems methods. No novelty is claimed for those general techniques. The specific sharp universal-convergence boundary, two-cycle classification, square-root coalescence and nonlinear bistability for the stated optimization update are the scientific claims assessed here.

## Limitations

The result concerns a scalar strictly convex power loss with exponent strictly greater than two and the special memoryless Adam update. The analytic map has no stochastic gradients, first- or second-moment memory, bias-correction transients, weight decay, coupling between coordinates, or finite-precision arithmetic. The theorem classifies symmetric sign-alternating two-cycles, not all periodic orbits or global basins above the threshold. A numerical plot cannot establish any of the exact thresholds; the proof is elementary but complete for its stated domain. Historical-priority uncertainty remains because the full 2026 motivating paper was inaccessible and no exhaustive literature search is possible.

## References

1. G. Tang, H. Chen, Z. Liu, *Beyond Quadratic Loss: The Stability Phase Diagram of Adam*, arXiv:2609.18314v1, first public September 16, 2026. https://arxiv.org/abs/2609.18314
2. *Decoupled weight decay lowers the exact chattering threshold in AdamW*, publicly accessible mathematical note. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-decoupled-weight-decay-lowers-the-exact-chattering-threshold-in--1457b4d13f59
3. *A sharp flip frontier for the Polar-Express surrogate on scalar quadratics*, publicly accessible mathematical note. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-sharp-flip-frontier-for-the-polar-express-surrogate-on-scalar--5f6e926df82f
4. *Sharp partial-adaptivity phase transition in scalar Padam*, publicly accessible mathematical note. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-partial-adaptivity-phase-transition-in-scalar-padam--64bfa7f15a9c
