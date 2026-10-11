# Finite-time escape and universal blow-up scaling in a dissipative hyperbolic-sine jerk flow

## Finding
Consider the autonomous jerk system
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=\varepsilon-a x-b^2y-cz+d\sinh x,
\]
with arbitrary real \(a,\varepsilon\) and \(b,c,d>0\). There are nonempty **open sets** of initial conditions whose maximal forward solutions blow up in finite time, one with \(x\to+\infty\) and another with \(x\to-\infty\). On every solution in the positive set, if \(T<\infty\) denotes the maximal time,
\[
\begin{aligned}
x(t)&=-3\log(T-t)+\log(12/d)+o(1),\\
(T-t)y(t)&\longrightarrow3,\\
(T-t)^2z(t)&\longrightarrow3,
\end{aligned}\qquad t\uparrow T.
\]
On the negative set all three displayed asymptotics have the opposite sign: in particular \(x(t)=3\log(T-t)-\log(12/d)+o(1)\). These conclusions hold despite the constant negative divergence \(\nabla\!\cdot F=-c\).

The open sets and a two-sided blow-up-time estimate are explicit up to a finite large-coordinate cutoff. Let
\[
h=(9d/4)^{1/3},\qquad k=h^2/3,\qquad 0<\eta<1/3.
\]
There is a finite \(X_\eta\), depending on the given parameters and \(\eta\), such that all initial conditions with \(x_0>X_\eta\) and
\[
\begin{split}
h(1-\eta)&<y_0e^{-x_0/3}<h(1+\eta),\\
k(1-3\eta/2)&<z_0e^{-2x_0/3}<k(1+3\eta/2)
\end{split}
\]
blow up positively and satisfy the nonasymptotic bounds
\[
\frac{3e^{-x_0/3}}{h(1+\eta)}
\le T\le
\frac{3e^{-x_0/3}}{h(1-\eta)}.
\]
A corresponding reflected open set produces negative blow-up.

## Assumptions and scope
The vector field is the five-parameter Hu–Sang–Wang system (2.2). The source studies \(0\le\varepsilon\ll1\); the theorem remains true for every fixed real \(\varepsilon\). Only the **destabilizing hyperbolic-sine sign** \(d>0\) is treated, including its damped benchmark case \(b=1,c=0.2,d=1\). The assertion is existence of open basins of finite-time escape with precise asymptotics, not a classification of all initial conditions, bounded or chaotic attractors, or the case \(d<0\). The time origin in the displayed bound is \(t=0\).

## Proof
**1. Exact compactification.** Along a trajectory define a new time \(\tau\) and variables \(Y,Z\) by
\[
\frac{d\tau}{dt}=e^{x/3},\qquad
Y=ye^{-x/3},\qquad Z=ze^{-2x/3}.
\]
Direct differentiation gives the exact transformed equations (a prime denotes \(d/d\tau\))
\[
\begin{aligned}
x'&=Y,\\
Y'&=Z-Y^2/3,\\
Z'&=d/2-2YZ/3+E(x,Y,Z),
\end{aligned}
\]
where
\[
E(x,Y,Z)=-cZe^{-x/3}-b^2Ye^{-2x/3}
 +(\varepsilon-a x)e^{-x}-(d/2)e^{-2x}.
\]
For bounded \(Y,Z\), the remainder converges uniformly to zero as \(x\to+\infty\). The limiting planar subsystem has the positive equilibrium \((Y,Z)=(h,k)\), since \(k=h^2/3\) and \(2hk/3=d/2\).

**2. A forward-invariant escape tube.** Use the closed rectangle
\[
R_\eta=[h(1-\eta),h(1+\eta)]
\times[k(1-3\eta/2),k(1+3\eta/2)].
\]
At its lower and upper \(Y\)-faces the inward-direction expressions for \(Y'\), evaluated at the extremal permitted \(Z\), are respectively
\[
k(\eta/2-\eta^2)>0,
\qquad -k(\eta/2+\eta^2)<0.
\]
For the limiting \(Z\)-equation, the corresponding expressions at its lower and upper faces are
\[
(d/2)(\eta/2+3\eta^2/2)>0,
\qquad (d/2)(-\eta/2+3\eta^2/2)<0.
\]
All inequalities are strict for \(0<\eta<1/3\). Choose \(X_\eta\) so large that on \(x\ge X_\eta\) and \((Y,Z)\in R_\eta\), the absolute error \(|E|\) is smaller than half the smaller \(Z\)-face margin. Then the full transformed vector field points strictly inward on every face. Since \(x'=Y\ge h(1-\eta)>0\), any solution initially in the interior of this tube remains in it and satisfies
\[
x_0+h(1-\eta)\tau\le x(\tau)
\le x_0+h(1+\eta)\tau.
\]
This also proves global existence for \(0\le\tau<\infty\): \(Y,Z\) are bounded and \(x\) grows at most linearly on bounded \(\tau\)-intervals.

**3. Finite physical time.** The original time satisfies \(dt/d\tau=e^{-x/3}\), so
\[
T=\int_0^\infty e^{-x(\tau)/3}\,d\tau.
\]
The preceding two linear bounds on \(x(\tau)\) give exactly the two-sided time estimate in the finding. Thus \(T\) is finite and \(x\to+\infty\) as \(t\uparrow T\); the original solution cannot extend past \(T\). Strict inequalities defining the tube give a nonempty open set of ordinary initial data.

**4. Convergence to a universal scaled profile.** Write \(u=Y-h\), \(v=Z-k\), and \(K=2h^2/9\). Using \(d=4h^3/9\), the transformed equations become
\[
u'=v-2hu/3-u^2/3,
\qquad
v'=-Ku-2hv/3-2uv/3+E.
\]
For the positive definite function \(W=Ku^2+v^2\), direct differentiation yields the exact identity
\[
W'=-\frac{4h}{3}W-\frac{2K}{3}u^3
 -\frac43uv^2+2vE.
\]
On the rectangle \(|u|\le\eta h\), so the cubic terms are bounded above by \((4\eta h/3)W\). Young's inequality then gives, with \(\gamma=2h(1-\eta)/3>0\),
\[
W'\le-\gamma W+\gamma^{-1}E^2.
\]
Because \(x(\tau)\ge x_0+h(1-\eta)\tau\), every term of \(E\) tends to zero exponentially in \(\tau\), including \(xe^{-x}\). Variation of constants implies \(W(\tau)\to0\), so \((Y,Z)\to(h,k)\).

**5. Universal blow-up constants.** Put \(q=e^{-x/3}\). In original time \(\dot q=-Y/3\). Since \(q\to0\) at \(T\) and \(Y\to h\), integration from \(t\) to \(T\) gives
\[
\frac{q(t)}{T-t}\longrightarrow h/3.
\]
Consequently \(x(t)=-3\log(T-t)+\log(27/h^3)+o(1)\), and \(27/h^3=12/d\). Also \(y=Ye^{x/3}=Y/q\) and \(z=Ze^{2x/3}=Z/q^2\), hence their scaled limits are \(3\) and \(9k/h^2=3\).

Finally, replacing \((x,y,z)\) with \((-x,-y,-z)\) changes only \(\varepsilon\) to \(-\varepsilon\) while preserving \(a,b,c,d\). Applying the already proved positive-escape statement to this reflected system yields a negative-escape open set for each fixed original \(\varepsilon\), together with the three sign-reversed limits.

## Verification
The included `verify.py` (Python with SymPy 1.14.0) checks the exact compactification residuals, the limiting equilibrium identity, the four signed rectangle-face margins, the polynomial identity for \(W'\), and the constant \(27/h^3=12/d\). These are algebraic checks; the global invariant-region, convergence, and finite-time conclusions use the analytic arguments above rather than finite numerical simulation.

For a numerical sanity check only, the published benchmark \(b=d=1,c=0.2\) with \(a=2\), \(\varepsilon=0.01\), \(x_0=20\), \(Y_0=h\), \(Z_0=k\) was integrated in stretched time to \(\tau=28\), giving approximately \(Y=1.310370696\), \(Z=0.572357121\) and \(T\approx0.002913682\). This experiment is not a proof and the nonasymptotic tube cutoff was not certified numerically.

## Relationship to prior work
Hu, Sang, and Wang (2022), equations (2.2)–(2.8), analyze local pitchfork/Hopf bifurcations, period-doubling routes, chaotic attractors, and circuitry. Their page 15719 infers confinement of all orbits from the constant divergence \(-c\). A negative divergence contracts the volume of a flow where defined but does not imply forward completeness or boundedness; the present open sets exhibit precisely that missing qualification without questioning the existence of any bounded attractor.

The separately published result “A sharp compact-recurrence threshold for a hyperbolic-sine jerk flow” concerns bounded forward/complete orbits and compact invariant measures in the symmetric case; it explicitly does not determine the fate of unbounded trajectories. It neither asserts nor implies finite-time escape or the logarithmic rate here. Earlier periodic-orbit energy balances for the same system likewise concern bounded recurrence and cannot imply these claims. Hoang's general finite-time blow-up analysis for systems with positively homogeneous dominant terms concerns a different class of vector fields; the exponential-in-position jerk forcing does not meet that stated hypothesis directly.

## Limitations
The explicit open tubes can start only beyond a parameter-dependent large \(X_\eta\); the theorem does not determine sharp escape boundaries or the fate of all other initial data. It does not claim that trajectories displayed as bounded chaotic attractors in the motivating article escape, and it does not cover the restoring sign \(d<0\). More general blow-up and compactification theory may supply alternative proofs; novelty here concerns this specific damped hyperbolic-sine jerk family and its universal physical-time rate, subject to ordinary literature-indexing limits.

## References
1. X. Hu, B. Sang and N. Wang, “The chaotic mechanisms in some jerk systems,” *AIMS Mathematics* **7** (2022), 15714–15740, DOI: 10.3934/math.2022861. The publicly indexed October 6, 2021 preprint predates the June 24, 2022 journal article; equation and arguments checked against the journal full text: https://www.aimspress.com/aimspress-data/math/2022/9/PDF/math-07-09-861.pdf.
2. “A sharp compact-recurrence threshold for a hyperbolic-sine jerk flow,” public mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-sharp-compact-recurrence-threshold-for-a-hyperbolic-sine-jerk--e3c8f2764332 (full result inspected).
3. L. Hoang, “On the finite time blow-ups for solutions of nonlinear differential equations,” arXiv:2303.10153, initial preprint March 2023, https://arxiv.org/abs/2303.10153.
