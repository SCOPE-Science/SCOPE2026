# Trimodal stationary states and the exact fold boundary for saturating run-and-tumble motion

## Finding

A two-state, one-dimensional run-and-tumble particle with bounded hyperbolic-tangent speed and reversal rates can have **three**, not merely one or two, strict local maxima in its normalized stationary positional density. On the natural commensurate slice \(g=3u\), the number and type of all critical points are classified exactly by two parameter boundaries. In addition, a sixth-order flat central peak occurs at their merger.

Specifically, let
\[
A=uv_1^2,\qquad B=\gamma_0v_1,\qquad C=\gamma_1v_0,\qquad A_c=B+3C.
\]
If \(B<5C\), put
\[
A_f=\frac{3B+5C+2\sqrt{6C(B+C)}}4.
\]
Then \(0<A_f<A_c\), and the stationary density has:

- exactly one strict local maximum, at the origin, when \(0<A<A_f\);
- one central strict maximum and two nonextremal stationary shoulders when \(A=A_f\);
- exactly three strict maxima and two strict minima when \(A_f<A<A_c\);
- exactly two strict off-center maxima and a flat central minimum when \(A=A_c\);
- exactly two strict off-center maxima and a strict central minimum when \(A>A_c\).

For \(B\geq5C\), there are no three-peak states: one strict central maximum for \(A<A_c\) and two strict off-center maxima for \(A>A_c\). At equality \(A=A_c\), the origin remains the only maximum, flat of fourth order if \(B>5C\) and of sixth order if \(B=5C\).

An exact admissible example is
\[
(v_0,v_1,\gamma_0,\gamma_1,u,g)=\left(3,1,1,\frac{13}{15},8,24\right),
\]
whose five stationary-density critical points are \(0\), the local-minimum pair
\[
\pm\frac18\operatorname{arctanh}\left(\frac1{\sqrt{10}}\right),
\]
and the off-center local-maximum pair
\[
\pm\frac18\operatorname{arctanh}\left(\frac1{\sqrt3}\right).
\]
The three maxima are structurally stable under sufficiently small independent variations of **all** six parameters, not only variations preserving \(g=3u\).

## Assumptions and scope

At position \(x\in\mathbb R\), an internal state \(\sigma\in\{+,-\}\) moves at signed velocity \(+v_+(x)\) or \(-v_-(x)\), respectively. The rates of switching away from the corresponding states are \(\gamma_+(x)\) and \(\gamma_-(x)\), where
\[
v_\pm(x)=v_0\mp v_1\tanh(ux),\qquad
\gamma_\pm(x)=\gamma_0\pm\gamma_1\tanh(gx).
\]
Assume \(v_0>v_1>0\), \(\gamma_0\geq\gamma_1>0\), \(u>0\), and \(g=3u\). These conditions ensure positive velocities and nonnegative switching rates for all finite positions. The normalizable, positive, even stationary position density from [1] is
\[
p(x)=\frac1Z\left(\frac1{v_+(x)}+\frac1{v_-(x)}\right)
\exp\!\left[\int_0^x\left(\frac{\gamma_-(y)}{v_-(y)}-\frac{\gamma_+(y)}{v_+(y)}\right)dy\right],
\]
where \(Z\in(0,\infty)\) is the normalization. As \(x\to+\infty\), the logarithmic derivative tends to the strictly negative value \(-2(B+C)/(v_0^2-v_1^2)\); this gives exponential integrability.

Here **mode** means strict local maximum. A stationary shoulder has zero derivative but is neither a local maximum nor a local minimum. The stated phase diagram holds on \(g=3u\); the openness assertion for the exact witness holds in the full parameter space.

## Proof

**1. Exact derivative reduction.** The stationary density above has a positive even prefactor \(H(x)=2v_0/(v_0^2-v_1^2\tanh^2(ux))\). Its exponential integral has derivative
\[
I'(x)=-2\frac{B\tanh(ux)+C\tanh(3ux)}{v_0^2-v_1^2\tanh^2(ux)}.
\]
Writing \(t=\tanh(ux)\), \(s=t^2\) and using \(\tanh(3ux)=t(3+s)/(1+3s)\), direct differentiation gives the **exact identity**
\[
\frac{p'(x)}{p(x)}=\frac{2t\,\Phi(s)}{(v_0^2-v_1^2s)(1+3s)},
\qquad
\Phi(s)=-3As^2+(2A-3B-C)s+(A-B-3C).
\]
For \(x>0\), \(t>0\) and \(s\in(0,1)\), while every factor outside \(\Phi(s)\) is strictly positive. Thus the **entire** positive-half-line critical-point problem is equivalent to signs and roots of this one quadratic polynomial. Also
\[
\Phi(0)=A-A_c,\qquad\Phi(1)=-4(B+C)<0,
\]
and its discriminant is
\[
\Delta=16A^2-8(3B+5C)A+(3B+C)^2.
\]

**2. Complete root counting.** For \(A>A_c\), the signs \(\Phi(0)>0>\Phi(1)\), the negative leading coefficient and the negative constant term imply precisely one simple root in \((0,1)\); its positive-position critical point is a strict maximum and the origin is a strict minimum. For \(A=A_c\),
\[
\Phi(s)=s\big[(5C-B)-3(B+3C)s\big].
\]
When \(B<5C\), this has one simple interior root and \(\Phi(s)>0\) for small \(s>0\), making the origin a flat minimum and the off-center pair strict maxima. When \(B\geq5C\), \(\Phi(s)<0\) throughout \((0,1)\), so the origin is the sole maximum.

For \(A<A_c\), the constant term is negative. If \(B\geq5C\), the linear coefficient is \(2A-3B-C<5C-B\leq0\); hence \(\Phi(s)<0\) on \((0,1)\) and the origin alone is a maximum. If \(B<5C\), the larger positive \(A\)-root of \(\Delta=0\) is exactly \(A_f\); the double \(s\)-root at \(A=A_f\) is interior because its vertex \((2A_f-3B-C)/(6A_f)\) is positive and smaller than one (the first inequality is equivalent, after squaring where needed, to \(B<5C\), and \(\Phi(1)<0\) gives the second). For \(A\) just below \(A_c\), the two roots are positive and interior: one approaches zero from above, the other approaches \((5C-B)/(3A_c)\in(0,1)\). By continuity, their number can change in \((0,A_c)\) only when two roots coalesce, a root crosses \(s=0\), or a root crosses \(s=1\). The last two are excluded below \(A_c\), and the only relevant double positive root occurs at \(A_f\). Consequently there are two simple interior roots for \(A_f<A<A_c\), a double interior root at \(A_f\), and none for \(0<A<A_f\). The quadratic is negative / positive / negative across the two distinct roots, proving the sequence central maximum, inner minima and outer maxima. At the fold the derivative has a same-sign double zero, yielding two stationary inflection shoulders.

**3. Flat-order merger.** At \(A=A_c\), \(\Phi(s)=(5C-B)s-3A_cs^2\). If \(B>5C\), the first term is negative and the origin is a fourth-order flat maximum; if \(B<5C\), it is a fourth-order flat minimum. At \(B=5C\) and \(A=8C\), \(\Phi(s)=-24Cs^2\); since \(\tanh(ux)=ux+O(x^3)\),
\[
\log\frac{p(x)}{p(0)}=-\frac{8Cu^5}{v_0^2}x^6+O(x^8),
\]
which proves a sixth-order flat maximum.

**4. Exact example and robustness.** The parameters displayed in the Finding give \(A=8\), \(B=1\), \(C=13/5\), and
\[
\Phi(s)=-\frac45(3s-1)(10s-1).
\]
There are therefore two simple roots at \(s=1/10\) and \(s=1/3\), and the origin is a strict maximum because \(\Phi(0)=-4/5<0\). At all five critical points the required nondegeneracies hold (at zero, \(p''(0)<0\); at the four others, \(\Phi'(s)\ne0\)). Smooth dependence of the stationary logarithmic derivative on the six model parameters, together with the implicit-function theorem, preserves these five critical points and their types for every sufficiently small six-parameter perturbation. Since the original five critical points are all the critical points, the nearby density has at least three maxima; global completeness off the commensurate slice is not asserted.

## Verification

Run the accompanying exact-symbolic and diagnostic checker with `python verify.py` (requires SymPy and mpmath). It independently reconstructs the stationary logarithmic derivative, verifies the discriminant, threshold identity, exact witness factorization and sixth-order polynomial, and checks the direct integral of the source stationary formula at a three-peak parameter set. It also performs 100 deterministic random rational-parameter root-count diagnostics. The verifier reports **115 passed checks**. A finite parameter sample is **not** used to prove the classification; the exhaustive argument is the preceding quadratic root-count proof.

Numerical integration of the **unnormalized** stationary law gives \(p(x_1)/p(0)\approx0.999525403218692\) and \(p(x_2)/p(0)\approx1.000088781593336\), in agreement with the three-peak sign pattern; normalizing the density does not change these ratios.

## Relationship to prior work

Jain and Chatterjee [1] introduced exactly these bounded speed and switching-rate functions and derived the stationary law (their Eq. 7) and the implicit extremum condition (their Eq. 15). They observed a central unimodal/bimodal criterion but explicitly conditioned a complete two-phase classification on an assumption of **at most two maxima** (their discussion surrounding Eqs. 15–17). The present explicit five-critical-point witness disproves that extra assumption for the full parameter range in the same model. Their studied special case \(g=u\) is distinct from the present \(g=3u\) slice; no claim is made about invalidating that special case.

Monthus [2] developed general stationary-density and large-deviation formulas for spatially dependent two-state run-and-tumble processes. The present theorem uses the known zero-current stationary density rather than claiming this formula as new. The new elements are the exact fold, the open trimodal wedge, the complete critical-point diagram on \(g=3u\), and the sixth-order meeting point. Active-particle models with more states, thermal fluctuations or external harmonic confinement can have distinct multi-peak behavior [3]; that general phenomenon is not claimed as new.

## Limitations

This is a theorem about the **stationary positional density** of a two-state continuous-time process, not a claim of dynamical phase-transition singularity, metastability or observational mode resolution. The complete classification is restricted to \(g=3u\), \(v_0>v_1>0\), \(\gamma_0\ge\gamma_1>0\), and \(u>0\). When \(g/u\) is arbitrary, a higher number of maxima is neither proved nor ruled out. The full six-parameter openness statement asserts persistence of at least the three known peaks, not an exhaustive count off the slice. A global literature novelty claim or independent validation has not been established.

## References

[1] K. Jain and S. Chatterjee, *Run-and-tumble particle with saturating rates*, arXiv:2405.13521 (first publicly posted 2024-05-22); Phys. Rev. E **110**, 064110 (2024), https://arxiv.org/html/2405.13521v2 , https://doi.org/10.1103/PhysRevE.110.064110 . The original preprint is arXiv:2405.13521v1.

[2] C. Monthus, *Large deviations at various levels for run-and-tumble processes with space-dependent velocities and space-dependent switching rates*, arXiv:2103.08885 (2021), https://arxiv.org/abs/2103.08885 .

[3] D. Wexler, N. S. Gov, K. Ø. Rasmussen and G. Bel, *Dynamics and escape of active particles in a harmonic trap*, arXiv:1909.02938 (2019), https://arxiv.org/abs/1909.02938 .
