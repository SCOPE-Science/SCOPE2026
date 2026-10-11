# Critical quintic logarithm and finite-part energy in exponential-memory blow-up

## Finding

Consider the positive exponential-memory system
\[
\dot u=v^p,\qquad \dot v=\alpha u-\beta v,
\qquad \alpha,\beta>0,\quad p>3,\quad u(0),v(0)>0.
\]
Every solution blows up at some finite time \(T\), with \(v(t)\to\infty\) and eventually \(\dot v(t)>0\). On its final increasing branch, let \(t=t(v)\) be the inverse of \(v(t)\) and write \(Y(v)=\dot v(t(v))\). Define
\[
q=\frac{p+1}{2}>2,\quad c=\sqrt{\frac{\alpha}{q}},\quad
 d=-\frac{\beta}{q+1},\quad
 e=\frac{\beta^2 q}{2c(q+1)^2},
\qquad J_q(v)=\begin{cases}
\dfrac{v^{3-q}}{3-q},&q\ne3,\\[2pt]
\log v,&q=3.
\end{cases}
\]
Then the following limit exists and is finite for every initial condition:
\[
\boxed{\displaystyle K=\lim_{v\to\infty}\left[Y(v)^2-c^2v^{2q}
+\frac{2\beta c}{q+1}v^{q+1}
-\frac{\beta^2}{q+1}v^2+2\beta e J_q(v)\right]\in\mathbb R.}
\]
The error in the expression within the limit is \(O(v^{4-2q})\) for \(2<q<3\), \(O(v^{-2}\log v)\) for \(q=3\), and \(O(v^{1-q})\) for \(q>3\). In particular the natural energy after subtracting its first three polynomial terms diverges as a power for \(3<p<5\), diverges logarithmically for \(p=5\), and converges for \(p>5\).

At the critical quintic nonlinearity \(p=5\), let \(c=\sqrt{\alpha/3}\). The expansion becomes
\[
\boxed{Y(v)^2=\frac\alpha3 v^6-\frac{\beta c}{2}v^4
+\frac{\beta^2}{4}v^2-\frac{3\beta^3}{16c}\log v+K+o(1).}
\]
Equivalently, for some finite trajectory-dependent constant \(C\),
\[
\boxed{Y(v)=cv^3-\frac\beta4v+\frac{3\beta^2}{32c}v^{-1}
-\frac{9\beta^3}{32\alpha}\,v^{-3}\log v+C v^{-3}+o(v^{-3}).}
\]
The logarithmic coefficients are nonzero for all \(\alpha,\beta>0\) and depend only on these two parameters.

The finite-part constant also **strictly orders orbits** at any fixed initial memory level. Fix \(v_0>0\) and let two solutions have positive initial phase velocities \(0<Y_1(v_0)<Y_2(v_0)\), so that \(u_i(0)=[Y_i(v_0)+\beta v_0]/\alpha>0\). Their finite parts satisfy the exact difference formula
\[
\boxed{K_2-K_1=\bigl(Y_2(v_0)^2-Y_1(v_0)^2\bigr)
\exp\!\left[-2\beta\int_{v_0}^{\infty}\frac{ds}{Y_1(s)+Y_2(s)}\right]>0.}
\]
Thus \(K\) is an injective order parameter on this one-dimensional family of positive trajectories, not merely a subtraction-dependent finite number.

## Assumptions and scope

All functions are classical real solutions of the specified autonomous system on their maximal interval \([0,T)\). Only the positive quadrant and \(p>3\) are asserted; \(p\le3\), signed states, non-exponential kernels and general nonautonomous forcing are not covered. The inverse \(t(v)\) is used only beyond a point where \(\dot v>0\), so none of the statements requires initial monotonicity. The exponent \(p\) may be nonintegral. The constant \(K\) depends on the orbit, while the divergent counterterm coefficients are universal.

## Proof

**Positivity, eventual growth, finite-time blow-up.** For as long as the solution exists, \(u\) increases since \(\dot u=v^p>0\); the variation-of-constants formula for \(v\) keeps \(v>0\). Differentiation yields
\[
\ddot v+\beta\dot v=\alpha v^p>0.
\]
Whenever \(\dot v=0\), its derivative \(\ddot v=\alpha v^p>0\). Thus \(\dot v\) can cross zero only from negative to positive. If it were negative forever on a global solution, \(v\) would have a finite limit. If that limit were positive, \(u(t)\) would grow without bound, forcing \(\dot v=\alpha u-\beta v>0\); if it were zero, \(u\ge u(0)>0\) would give the same contradiction. A finite maximal interval cannot terminate while \(v\) decreases, since then \(v\) and \(\dot u=v^p\), and hence \(u\), stay bounded. Consequently \(\dot v>0\) eventually.

If a global positive solution had \(v\) bounded thereafter, then \(v\) would converge to a positive limit, forcing \(u\to\infty\) and hence \(\dot v>0\) without bound, impossible. Therefore \(v\to\infty\) either at a finite maximal time or at infinity. On the increasing branch, \(Y>0\) and
\[
\frac{d}{dv}Y(v)^2=2\alpha v^p-2\beta Y(v).
\tag{1}
\]
Fix \(v_0\) on that branch. Integrating (1) and writing \(q=(p+1)/2\) gives
\[
Y(v)^2=c^2v^{2q}+C_0-2\beta\int_{v_0}^vY(s)\,ds,
\qquad c^2=\frac\alpha q.
\tag{2}
\]
Since \(Y>0\), (2) implies \(Y=O(v^q)\). Thus the integral is \(O(v^{q+1})=o(v^{2q})\) (because \(q>1\)), and \(Y(v)\sim cv^q\). Inverting the increasing branch gives \(dt/dv=1/Y(v)\sim c^{-1}v^{-q}\). This is integrable at infinity; hence the maximal time \(T\) is finite and \(v(t)\to\infty\) as \(t\uparrow T\).

**Three controlled iterations.** Equation (2) first yields \(Y=cv^q+O(v)\). Substitution back into (2), then taking the positive square root, gives
\[
Y=cv^q+d v+O(v^{2-q}),\qquad d=-\frac\beta{q+1}.
\tag{3}
\]
The integral of the last error in (3) is \(O(v^{3-q})\) if \(2<q<3\), \(O(\log v)\) if \(q=3\), and \(O(1)\) if \(q>3\). Equation (2) therefore also gives
\[
Y^2=c^2v^{2q}+2cd\,v^{q+1}-\beta d\,v^2+
\begin{cases}O(v^{3-q}),&2<q<3,\\O(\log v),&q=3,\\O(1),&q>3.
\end{cases}
\tag{4}
\]
Comparing the coefficient of \(v^2\) in the square of \(cv^q+d v+e v^{2-q}\) with \(-\beta d=\beta^2/(q+1)\) fixes
\[
e=\frac{-\beta d-d^2}{2c}=\frac{\beta^2q}{2c(q+1)^2}.
\]
The square-root remainder in (4) consequently yields the genuinely integrable error
\[
R(v):=Y(v)-cv^q-dv-e v^{2-q}
=\begin{cases}O(v^{3-2q}),&2<q<3,\\
O(v^{-3}\log v),&q=3,\\
O(v^{-q}),&q>3.
\end{cases}
\tag{5}
\]
Each power in (5) is integrable over the positive tail because \(q>2\).

**Renormalized energy and sharp remainder.** Define
\[
\mathcal K_q(v)=Y(v)^2-c^2v^{2q}
+\frac{2\beta c}{q+1}v^{q+1}-\frac{\beta^2}{q+1}v^2
+2\beta e J_q(v).
\]
Using (1), \(d=-\beta/(q+1)\), and \(J_q'(v)=v^{2-q}\), direct differentiation gives the exact identity
\[
\mathcal K_q'(v)=-2\beta R(v).
\tag{6}
\]
The integrable bounds (5) prove convergence to \(K\), and integrating them from \(v\) to infinity establishes all three stated error estimates. Since \(e>0\), the unrenormalized fourth term \(-2\beta eJ_q(v)\) diverges as a power for \(2<q<3\), is logarithmic for \(q=3\), and vanishes for \(q>3\). Thus the boundary is exactly \(q=3\), or \(p=5\).

Finally, set \(q=3\) in the limit formula. Then \(d=-\beta/4\) and \(e=3\beta^2/(32c)\). Taking the positive square root through order \(v^{-3}\) gives the displayed quintic expansion, with
\[
C=\frac{K-2de}{2c}=\frac{K}{2c}+\frac{9\beta^3}{128\alpha}.
\]
The square-root remainder is \(o(v^{-3})\) because the squared expansion has remainder \(o(1)\). This completes the asymptotic part. To compare two solutions with the same \(v_0\) and increasing initial velocities, subtract their two exact equations (1). The strictly positive difference \(D(v)=Y_2(v)^2-Y_1(v)^2\) obeys
\[
D'(v)=-2\beta\frac{D(v)}{Y_1(v)+Y_2(v)}.
\]
Integration yields the asserted formula for \(K_2-K_1=\lim_{v\to\infty}D(v)\). The integral converges because both phase velocities satisfy \(Y_i(v)\sim cv^q\) and \(q>2\), so the exponential factor is strictly positive. This finishes the proof of the order property.

## Verification

The exact phase identity (1) is obtained by differentiating the original two-dimensional ODE and changing variable to \(v\), not by assuming a formal series. The algebraic consistency conditions are \(2cd=-2\beta c/(q+1)\), \(d^2+2ce=\beta^2/(q+1)\), and \(2\beta e=3\beta^3/(16c)\) when \(q=3\). Each is an exact identity. The proof's third error term (5) is integrable on all stated parameter ranges, making the finite-part limit rigorous. The zero-forgetting check \(\beta=0\) formally removes every correction and restores the conservative energy \(Y^2-c^2v^{2q}=\mathrm{constant}\).

For a reproducible symbolic spot-check using an independent algebra path, run the optional accompanying script `verify_algebra.py` with Python and SymPy. It checks all universal coefficient identities symbolically, but neither the symbolic check nor a finite numerical calculation substitutes for the analytic convergence proof.

## Relationship to prior work

Yu Ichida, *Memory-induced blow-up solutions and their dynamical transitions in distributed delay differential equations*, arXiv:2609.15470v1 (first public 14 September 2026), Section 3 and Theorem 1, analyzes precisely this exponential-memory power system and establishes finite blow-up with leading temporal rates, but does not state the phase-space finite-part invariant or the quintic logarithmic coefficient. Asai–Kodani–Matsue–Ochiai–Sasaki, arXiv:2211.06865v2, develop general multi-order blow-up asymptotic methods and discuss resonances; the inspected examples do not supply this specific model, counterterm, or limit. Hoang, arXiv:2303.10153v2, proves general leading blow-up and error estimates rather than this explicit power-to-logarithm threshold. A publicly indexed analysis of the different reciprocal-memory nonlinearity concerns a distinct vector field, not the power model.

## Limitations

This is a phase-space asymptotic along the final monotone orbit, not an explicit formula for the blow-up time or a result for arbitrary delay kernels. The orbit-dependent finite part \(K\) is defined by a convergent limit, not evaluated in closed form in terms of the initial data. No claim is made for \(p\le3\), for \(\beta<0\), or for unbounded sign-changing histories. General asymptotic-expansion techniques may independently reproduce the calculation; an equivalent explicit coefficient under older terminology remains a literature risk.

## References

1. Y. Ichida, *Memory-induced blow-up solutions and their dynamical transitions in distributed delay differential equations*, arXiv:2609.15470v1, 2026. https://arxiv.org/html/2609.15470v1 .
2. T. Asai, H. Kodani, K. Matsue, H. Ochiai, T. Sasaki, *Multi-order asymptotic expansion of blow-up solutions for autonomous ODEs. I — Method and Justification*, arXiv:2211.06865v2, 2022. https://arxiv.org/html/2211.06865v2 .
3. L. T. Hoang, *On the finite time blow-ups for solutions of nonlinear differential equations*, arXiv:2303.10153v2, 2023. https://arxiv.org/html/2303.10153v2 .
