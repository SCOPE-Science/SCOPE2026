# Two detuning scales and a universal slow flow near rational sigmoid rotations

## Finding

Fix coprime integers \(1\le p<q\), with \(q\ge2\), and let
\[
F_{a,b}(x)=x+b-\frac{1}{1+e^{-ax}},\qquad
\epsilon=e^{-a/(2q)},\qquad b_0=p/q.
\]
For every fixed compact set of \((\xi,y)\in\mathbb R^2\), the period-\(q\) return map \(P_{a,b}=F_{a,b}^{q}\), under the **critical detuning** \(b=b_0+2\epsilon\xi/q\), obeys uniformly as \(a\to\infty\)
\[
\frac{P_{a,b}(1/(2q)+y/a)-(1/(2q)+y/a)}{2\epsilon}
=\xi-\sinh y+O(a\epsilon),
\quad
(P_{a,b})'(1/(2q)+y/a)=1-2a\epsilon\cosh y+O(a^2\epsilon^2).
\tag{1}
\]
Consequently, for every fixed \(\xi\), there is a locally attracting primitive period-\(q\) orbit whose point near \(1/(2q)\) and full-return multiplier satisfy
\[
x_{a,\xi}=\frac1{2q}+\frac{\operatorname{arsinh}\xi}{a}+O(\epsilon),
\qquad
\Lambda_{a,\xi}=1-2a\epsilon\sqrt{1+\xi^2}+O(a^2\epsilon^2).
\tag{2}
\]
Writing \(h_a=2a\epsilon\) and \(y_m=a(P_{a,b}^{m}(1/(2q)+y_0/a)-1/(2q))\), the interpolated discrete trajectory converges uniformly over each bounded slow-time interval, with \(m=\lfloor t/h_a\rfloor\), to the unique solution of
\[
\dot y=\xi-\sinh y,\qquad y(0)=y_0.
\tag{3}
\]
This is the universal, nonlinear dynamical crossover behind the exponentially weak period-\(q\) attraction.

The critical scale connects to a distinct **outer detuning** regime. Fix \(0<\tau<1/(2q)\), \(d>0\), and a sign \(s\in\{-1,+1\}\); put \(b=b_0+s(d/q)e^{-a\tau}\). There is a locally attracting primitive period-\(q\) orbit, with the point in \((0,1/q)\) located at
\[
x_{a,+}=\frac1q-\tau+\frac{\log d}{a}+o(a^{-1}),\quad
x_{a,-}=\tau-\frac{\log d}{a}+o(a^{-1}),
\quad
\Lambda_{a,s}=1-ad e^{-a\tau}(1+o(1)).
\tag{4}
\]
Thus exponentially small detuning can move the selected cycle by an order-one distance, and the sign of detuning selects opposite sides of a rational grid cell. Assertions (1)–(4) comprise one two-scale perturbation theorem; no claim of global uniqueness away from the exhibited local orbit is made.

## Assumptions and scope

All limits take \(a\to+\infty\), with \(p,q\) fixed. The central estimates are uniform when \((\xi,y)\) ranges in a fixed compact set. Slow-flow convergence is for any fixed bounded initial \(y_0\), fixed \(\xi\), and finite observation time. Outer estimates hold for fixed positive \(\tau,d\), with \(\tau<1/(2q)\). The phase point chosen for each cycle is the unique one in the indicated grid cell; the other \(q-1\) points are its iterates. A periodic orbit is *locally attracting* when the full-period derivative has modulus less than one.

## Proof

**Cyclic grid and uniform return identity.** Write \(g_a(x)=(1+e^{-ax})^{-1}\), \(J=\{p-q,\dots,p-1\}\), \(z_j=(j+1/2)/q\), and let \(\sigma(j)=j+p\) when \(j<0\), or \(j+p-q\) otherwise. Because \(p,q\) are coprime, \(\sigma\) traverses all \(q\) distinct grid sites. The discontinuous rotation \(G(x)=x+p/q-\mathbf 1_{x>0}\) sends \(z_j\) to \(z_{\sigma(j)}\). On any compact range that stays away from zero, the difference \(F_{a,b}(x)-G(x)\) is
\[
(b-b_0)+r_a(x),\qquad r_a(x)=\begin{cases}-g_a(x),&x<0,\\1-g_a(x),&x>0.\end{cases}
\]
Its derivative is \(r_a'(x)=-g_a'(x)\). In the critical regime, an orbit initiated at \(1/(2q)+y/a\) follows the grid itinerary with position at site \(j\) equal to \(z_j+y/a+O_{p,q}(\epsilon)\), uniformly for bounded \(\xi,y\): this follows by induction over the fixed \(q\) steps, using \(q|b-b_0|=O(\epsilon)\) and \(|r_a(x)|\le e^{-a|x|}\). Its distance from the discontinuity is at least \(1/(2q)-O(a^{-1})\). All accumulated switching integers sum to \(p\), hence the exact telescoping return identity is
\[
P_{a,b}(x)-x=q(b-b_0)+\sum_{i=0}^{q-1}r_a(F_{a,b}^{i}(x)).
\tag{5}
\]
The unique closest negative and positive grid sites are \(z_{-1}=-1/(2q)\) and \(z_0=1/(2q)\), visited once each. Their contributions are respectively \(-\epsilon e^{y}(1+O(a\epsilon))\) and \(+\epsilon e^{-y}(1+O(a\epsilon))\); every other site is at distance at least \(3/(2q)\) and contributes \(O(\epsilon^3)\). Equation (5) gives the first formula of (1), including its compact uniform remainder.

For the derivative, the exact chain rule yields
\[
(P_{a,b})'(x)=\prod_{i=0}^{q-1}\left(1-a g_a(F_{a,b}^{i}(x))(1-g_a(F_{a,b}^{i}(x)))\right).
\tag{6}
\]
At the two closest sites the derivative losses are \(a\epsilon e^{y}+O(a^2\epsilon^2)\) and \(a\epsilon e^{-y}+O(a^2\epsilon^2)\); elsewhere they are \(O(a\epsilon^3)\). Expanding the finite product proves the second formula in (1), uniformly on each bounded \((\xi,y)\) set.

**Central orbit and multiplier.** Fix \(\xi\), choose constants \(L<\operatorname{arsinh}\xi<R\). For sufficiently large \(a\), equation (1) shows \(P_{a,b}(1/(2q)+L/a)>1/(2q)+L/a\) and the opposite strict inequality at \(R\). By continuity there is a return fixed point between them. On this interval, equation (1) gives \(0<P_{a,b}'<1\), hence uniqueness within the interval and local attraction. By the mean value theorem and the nonzero derivative of \(\xi-\sinh y\) at its sole zero, the scaled fixed-point location differs from \(\operatorname{arsinh}\xi\) by \(O(a\epsilon)\), yielding the phase claim in (2). Substitution in (6) gives its multiplier with error \(O(a^2\epsilon^2)\). The visited sites are distinct, so the primitive period is exactly \(q\).

**Slow flow.** In the variable \(y=a(x-1/(2q))\), equation (1) becomes uniformly over compact \(y\) intervals
\[
y_{m+1}=y_m+h_a(\xi-\sinh y_m)+O(h_a^2),\qquad h_a=2a\epsilon\to0.
\tag{7}
\]
The vector field is locally Lipschitz and points inward outside any sufficiently large compact interval containing the initial value and its equilibrium. Pick such an interval containing the continuous solution over the desired finite time. The discrete evolution remains in a slightly larger interval for all \(m h_a\le T\) by the standard first-exit and Euler stability argument. The discrete Grönwall inequality applied to (7) and the corresponding integral equation gives \(\sup_{m h_a\le T}|y_m-y(mh_a)|=O_T(h_a)\); the time rounding contributes another \(O_T(h_a)\). This proves (3).

**Outer detuning.** Set \(v=e^{-a\tau}\). For the positive sign, center the phase at \(X_+=1/q-\tau\) and examine \(x=X_++(\log d+z)/a\), \(z\) in a fixed bounded interval. All \(q\) sites remain separated from the discontinuity by at least \(\tau-O(a^{-1})\), and the orbit follows the same grid permutation. Induction over \(q\) steps gives itinerary errors \(O(v)\). In (5) only the negative site at distance \(1/q-x=\tau-(\log d+z)/a\) contributes at the leading scale. The positive site is at distance \(1/q-\tau+O(a^{-1})>\tau\), so its contribution is \(o(v)\). The leading return displacement is therefore
\[
P_{a,b}(x)-x=d v(1-e^z)+o(v),
\tag{8}
\]
uniformly for bounded \(z\). The derivative formula (6) similarly gives
\[
(P_{a,b})'(x)=1-ad v e^z(1+o(1)).
\tag{9}
\]
For the negative sign, center at \(X_-=\tau\) and put \(x=X_-+(-\log d+z)/a\). Only the closest positive site contributes, and the corresponding expressions are
\[
P_{a,b}(x)-x=d v(e^{-z}-1)+o(v),\qquad
(P_{a,b})'(x)=1-ad v e^{-z}(1+o(1)).
\tag{10}
\]
Both limiting drift functions are strictly decreasing, positive at \(z=-1\), and negative at \(z=1\). Existence of a unique return fixed point in the corresponding interval follows by the intermediate value theorem and strict derivative contraction. Its \(z\)-coordinate tends to zero, yielding both phase asymptotics in (4). The derivative estimate yields the multiplier asymptotic; because \(a e^{-a\tau}\to0\), it lies strictly between zero and one for large \(a\). Again the orbit traverses all \(q\) grid labels and has primitive period \(q\). No singular branch is crossed.

## Verification

The standalone Python 3 script `check_detuning.py` evaluates both return asymptotics, the central equilibrium displacement and multiplier, the time-rescaled nonlinear flow, and the outer phase/multiplier laws. Its accompanying `CHECKS.txt` documents 12 central tests and 16 outer tests, with the final marker `CHECKS_PASS`. All uses of floating-point arithmetic are finite consistency checks; identities and limits follow from the analytic estimates above, independently of the script.

## Relationship to prior work

Bielawski and coauthors established rational period-\(q\) attraction for the unperturbed ratio \(b=p/q\) and qualitatively described rotation mimicking; their later study of strange bifurcation diagrams motivates the parameter sensitivity investigated here. The previously published result “Singular half-grid selection and exponentially weak attraction in rational EOS maps” proves the selected half-grid and multiplier at **exact** \(b=p/q\); its parameter remains fixed, so it does not give the nonlinear scaled **detuning flow** (3), the shift \(a^{-1}\operatorname{arsinh}\xi\) for variable \(b\), or the macroscopic selection laws (4). For \(\xi=0\) the central multiplier reduces to that known special case; the nonzero-detuning and outer-regime conclusions are the added content. Searches for logistic rational resonances, Arnold tongues, interval-map smoothing and exponential detuning found no directly covering statement, but priority cannot be established by search alone.

## Limitations

The result is local to the exhibited cycles, not a claim about the complete bifurcation diagram, global basins, or all periodic points. It does not identify a uniform threshold in \(q\), allow \(p,q\) to vary with \(a\), or treat the transition where \(\tau\uparrow1/(2q)\) without the critical scaling. All error estimates use fixed compact parameters; neither the same scaling nor the single-cycle local uniqueness is claimed globally. 

## References

[1] J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, “Strange bifurcation diagrams,” arXiv:2605.19756v1 (first public May 19, 2026), https://arxiv.org/abs/2605.19756.

[2] J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, “Interval maps mimicking circle rotations,” arXiv:2411.01495v1 (first public November 3, 2024), https://arxiv.org/abs/2411.01495.

[3] “Singular half-grid selection and exponentially weak attraction in rational EOS maps,” public mathematical record (October 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-singular-half-grid-selection-and-exponentially-weak-attraction-i--b03eb35b1a55.
