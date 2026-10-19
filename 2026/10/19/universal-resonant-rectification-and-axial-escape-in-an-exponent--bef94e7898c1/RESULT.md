# Universal resonant rectification and axial escape in an exponential Duffing lift

## Finding

Consider the periodically forced real three-dimensional differential equation
\[
\dot x=y,\qquad \dot y=-y-x-Bx^3+\varepsilon\cos t,\qquad
\dot z=\alpha x\exp(\beta x).
\]
For every \(B\ge0\), \(\varepsilon>0\) satisfying \(B\varepsilon^2\le1/256\), every nonzero real \(\alpha\), every real \(\beta\), and **every** initial \((x(0),y(0),z(0))\in\mathbb R^3\), there is a unique \(2\pi\)-periodic solution \((X_\varepsilon(t),Y_\varepsilon(t))\) of the first two equations and constants \(L\in\mathbb R\), \(C>0\) (the latter two may depend on the initial condition) such that
\[
\begin{aligned}
(x(t),y(t))&=(X_\varepsilon(t),Y_\varepsilon(t))+O(e^{-t/8}),\\
z(t)&=J_{B,\varepsilon}(\alpha,\beta)t+P(t)+L+O(e^{-t/8}),
\end{aligned}
\]
where \(P\) is \(2\pi\)-periodic, \(P(0)=0\), and
\[
J_{B,\varepsilon}(\alpha,\beta)
=\frac{\alpha}{2\pi}\int_0^{2\pi}X_\varepsilon(t)e^{\beta X_\varepsilon(t)}\,dt
=\frac{\alpha}{\pi}\int_0^\pi X_\varepsilon(t)\sinh(\beta X_\varepsilon(t))\,dt.
\]
This drift is strictly positive if \(\alpha\beta>0\), strictly negative if \(\alpha\beta<0\), and zero **exactly** if \(\beta=0\). Thus every real trajectory escapes linearly in the axial coordinate for \(\beta\ne0\), while every axial coordinate stays bounded and becomes asymptotically periodic for \(\beta=0\). In particular, for \(\beta\ne0\) the phase-extended flow on \(\mathbb R^3\times(\mathbb R/2\pi\mathbb Z)\) has no nonempty compact forward-invariant set.

There is also a two-term **nonlinear resonance law**. For each fixed \(B\ge0\), \(\alpha\ne0\), and real \(\beta\), as \(\varepsilon\to0^+\),
\[
\boxed{\ J_{B,\varepsilon}(\alpha,\beta)
=\frac{\alpha\beta}{2}\varepsilon^2
+\frac{\alpha\beta^3}{16}\varepsilon^4
+O_{B,\alpha,\beta}(\varepsilon^6).\ }
\]
The entire quartic-order coefficient is independent of the cubic stiffness \(B\); the first possible stiffness dependence in the transport speed occurs at sixth order.

## Assumptions and scope

This is the single-well, positively damped, exactly linearly resonant slice of the exponential lift of a periodically forced Duffing equation: the source equation uses parameters \(a=-1\), \(\zeta=-1\), \(b=B\), \(c=\varepsilon\), \(d=1\), and phase \(g=0\). The source's axial function is retained without approximation. The inequality \(B\varepsilon^2\le1/256\) is an explicit **sufficient** weak-drive domain, not asserted to be the optimal dynamical threshold. The phase of the forcing is fixed at time zero. The result neither describes the source's distinct large-amplitude chaotic parameter choices nor classifies all trajectories at larger drive.

For the proof, put \(V(x,y)=\tfrac12(y+x/2)^2+\tfrac58x^2+\tfrac B4x^4\), \(T=2\pi\), and \(D=\{(x,y):V(x,y)\le8\varepsilon^2\}\). Both the initial condition and the axial offset are unrestricted real numbers.

## Proof

**1. Coercive forced-energy inequality.** Along a base trajectory,
\[
\dot V=-\frac12(y^2+x^2+Bx^4)+\varepsilon(y+x/2)\cos t.
\]
By Cauchy--Schwarz and Young's inequality,
\[
\varepsilon|y+x/2|
\le\frac18(x^2+y^2)+\frac52\varepsilon^2.
\]
Since \(V\le x^2+y^2+Bx^4\), it follows that
\[
\dot V\le-\frac38 V+\frac52\varepsilon^2.
\]
The base solution is forward complete because \(V\) is coercive and the right side bounds \(V\) on every finite interval. Every base solution enters \(D\) in finite time because its energy is eventually below \((20/3)\varepsilon^2<8\varepsilon^2\). Moreover, \(D\) is forward invariant: on its boundary the displayed derivative is at most \(-\varepsilon^2/2<0\). It is a nonempty compact convex set (the defining function is convex).

**2. An explicit global contraction.** Let \((x_i,y_i)\), \(i=1,2\), be any two base trajectories lying in \(D\). Their difference \(w=x_1-x_2\), \(v=y_1-y_2\) obeys
\[
\dot w=v,\qquad \dot v=-v-(1+r)w,
\quad r=B(x_1^2+x_1x_2+x_2^2).
\]
Because \(V(x_i,y_i)\ge5x_i^2/8\), the hypotheses give
\[
0\le r\le\frac{192}{5}B\varepsilon^2\le\frac3{20}.
\]
The positive definite difference energy
\[
W=\frac12(v+w/2)^2+\frac58w^2
\]
satisfies the exact identity
\[
\dot W=-\frac12(v^2+w^2)-rw(v+w/2).
\]
Using \(|vw|\le(v^2+w^2)/2\),
\[
\dot W\le-\left(\frac12-\frac r2\right)v^2
-\left(\frac12-r\right)w^2
\le-\frac14(v^2+w^2)\le-\frac14 W.
\]
Thus differences decay in energy at least as \(e^{-t/4}\), and in Euclidean norm as \(e^{-t/8}\), whenever both trajectories are in \(D\).

**3. Unique globally attracting periodic base.** The time-\(T\) map of the base sends compact convex \(D\) continuously into itself, so Brouwer's fixed-point theorem supplies a \(T\)-periodic base solution. The difference estimate proves this solution is unique and is exponentially attracting to every base trajectory, since every solution eventually enters \(D\). The forcing and restoring terms have the symmetry \((x(t),y(t))\mapsto(-x(t+\pi),-y(t+\pi))\), which preserves the \(T\)-periodic equation. Uniqueness therefore gives
\[
X_\varepsilon(t+\pi)=-X_\varepsilon(t),\qquad
Y_\varepsilon(t+\pi)=-Y_\varepsilon(t).
\]
Since \(\varepsilon>0\), \(X_\varepsilon\) is not identically zero.

**4. Exact drift, its sign, and axial asymptotics.** Pairing the half-periods in the integral for \(J\) gives the second formula in the finding. For every real \(u\ne0\), the quantity \(u\sinh(\beta u)\) has the strict sign of \(\beta\). Its integral is nonzero because \(X_\varepsilon\not\equiv0\). Put
\[
P(t)=\int_0^t\bigl(\alpha X_\varepsilon(s)e^{\beta X_\varepsilon(s)}-J\bigr)\,ds.
\]
The integrand has mean zero over \(T\), hence \(P\) is \(T\)-periodic. By the exponential base convergence and smoothness of \(u\mapsto ue^{\beta u}\) on the ultimately bounded base range, the difference
\[\alpha\bigl(x(t)e^{\beta x(t)}-X_\varepsilon(t)e^{\beta X_\varepsilon(t)}\bigr)\]
is absolutely integrable on \([0,\infty)\) and is \(O(e^{-t/8})\). Its integral from time zero to \(t\) therefore equals a finite constant plus \(O(e^{-t/8})\). This proves the full axial asymptotic, including the bounded \(\beta=0\) case. If \(\beta\ne0\), every axial component diverges with nonzero linear rate, excluding a nonempty compact forward-invariant set in the phase extension.

**5. Fourth-order resonance cancellation.** Define the periodic differential operator \(\mathcal L=\partial_t^2+\partial_t+1\). It is invertible on \(2\pi\)-periodic functions, because its Fourier multipliers \(1-n^2+in\) never vanish for integer \(n\). Analytic implicit-function theory at zero forcing and the exact oddness in \(\varepsilon\) give the periodic expansion
\[
X_\varepsilon(t)=\varepsilon\sin t+B\varepsilon^3U(t)+O_B(\varepsilon^5),
\quad
U(t)=\frac34\cos t-\frac2{73}\sin3t-\frac3{292}\cos3t,
\]
with \(\mathcal L U=-\sin^3t\). By Fourier orthogonality, \(\langle\sin t\,U(t)\rangle=0\), where \(\langle f\rangle=T^{-1}\int_0^Tf(t)\,dt\). Consequently,
\[
\langle X_\varepsilon^2\rangle=\frac12\varepsilon^2+O_B(\varepsilon^6),
\qquad
\langle X_\varepsilon^4\rangle=\frac38\varepsilon^4+O_B(\varepsilon^6).
\]
Anti-periodicity makes all odd moments of \(X_\varepsilon\) vanish. Expanding the entire exponential on the uniformly small periodic orbit therefore yields
\[
\langle X_\varepsilon e^{\beta X_\varepsilon}\rangle
=\beta\langle X_\varepsilon^2\rangle
+\frac{\beta^3}{6}\langle X_\varepsilon^4\rangle+O_{B,\beta}(\varepsilon^6),
\]
which is the claimed quadratic-plus-quartic law. Its stiffness independence through fourth order is caused by the exactly resonant \(90^\circ\) phase of the cubic fundamental correction, not by an assumption that the cubic term vanishes.

## Verification

Run `python verify.py` in an environment with `sympy`, `numpy`, and `scipy`. The program checks the exact forced-energy identity, exact contraction identity, cubic response equation and orthogonality, and trigonometric moments. It then shoots for nine representative periodic responses and numerically checks half-period antisymmetry, drift sign and consistency with the fourth-order formula. Exact symbolic assertions passed, and all numerical checks passed during preparation. Finite tests provide reproducibility evidence, not proof of the global existence, uniqueness, or asymptotics; those follow from Steps 1--5.

## Relationship to prior work

Liu, Wang, Liu, Sun and He (2023) introduce the three-coordinate natural-exponential extension and numerically examine its three-dimensional outputs, bifurcations and Poincaré projections. Their published equation explicitly has a forced Duffing base independent of the axial coordinate. The present result isolates an analytically controlled resonant weak-forcing regime of that exact equation, establishes a common **all-initial-condition** axial speed, identifies the precise zero-drift boundary, and computes the leading two nonzero transport coefficients. It does not claim priority for elementary Duffing existence theory, Lyapunov estimates, or positivity of covariance for a monotone exponential observable taken separately.

Chen and Li (2008) investigate multiplicity/stability of periodic solutions of Duffing equations; this is relevant to the base oscillator, not in itself a covering result for the exponential axial coordinate. Lin (2014) considers numerical postverification of forced Duffing periodic solutions; the source does not provide the present axial transport theorem. A related established covariance/monotonicity principle supplies the sign once zero-mean forcing response is known, but cannot by itself provide the global response, exact forcing domain, or resonant quartic coefficient. No equivalent complete statement was found in the searched literature and mathematical-result records; unidentified or unindexed equivalent derivations remain possible.

## Limitations

This is an explicit sufficient weak-drive domain, not a sharp parameter boundary for uniqueness. The result makes no assertion about large forcing or about parameter sets used to demonstrate chaotic behavior in the originating study. It proves no independent review or external mathematical certification. The coefficient \(O_{B,\alpha,\beta}(\varepsilon^6)\) is asymptotic for fixed coefficients and is not a uniform error bound as \(B\), \(\alpha\), or \(\beta\) vary with the forcing. The complete text of every potentially related historical Duffing paper was not available; novelty is assessed against the specific reviewed statements and sources rather than claimed as exhaustive.

## References

1. S. Liu, Q. Wang, C. Liu, Y. Sun, and L. He, *Natural Exponential and Three-Dimensional Chaotic System*, Advanced Science **10** (2023), 2204269. DOI: https://doi.org/10.1002/advs.202204269. First publicly dated article: 2023-03-28. The original three equations, numerical scope and discussion were read in the lawful open-access HTML full text.
2. H. Chen and Y. Li, *Bifurcation and stability of periodic solutions of Duffing equations*, Nonlinearity **21** (2008), 2485--2505. DOI: https://doi.org/10.1088/0951-7715/21/11/001. Comparison from accessible abstract; complete text not verified.
3. Y.-P. Lin, *A Postverification Method for Solving Forced Duffing Oscillator Problems without Prescribed Periods*, Journal of Applied Mathematics (2014), Article 317460. DOI: https://doi.org/10.1155/2014/317460. Accessible open full text inspected.
4. Mathematical Reviews and zbMATH, *MSC2020 Classification System*, code 34C11: growth and boundedness of solutions to ordinary differential equations, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=34C11 (34Cxx classification list).
