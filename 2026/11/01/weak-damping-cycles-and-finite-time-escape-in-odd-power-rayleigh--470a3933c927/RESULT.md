# Weak-damping cycles and finite-time escape in odd-power Rayleigh–Liénard oscillators

## Finding

For each positive odd integer \(m\) consider the planar polynomial system
\[
\dot x=y,\qquad \dot y=-x+\varepsilon(1-x^2)y^m,\qquad \varepsilon>0.
\tag{1}
\]
There is a number \(\varepsilon_m>0\), dependent on the fixed integer \(m\), such that for every \(0<\varepsilon<\varepsilon_m\), (1) has **exactly one nonconstant periodic orbit**, which is hyperbolic and attracting. If \(r_m(\varepsilon)\) is the orbit's largest \(x\)-coordinate, equivalently its intersection \((r,0)\) with \(r>0\), then
\[
 r_m(\varepsilon)=\sqrt{m+3}+O(\varepsilon),\qquad
 \mu_m(\varepsilon)=1-2\varepsilon A_m(m+3)^{(m-1)/2}+O(\varepsilon^2),
\]
where \(\mu_m\) is the nontrivial Floquet multiplier and
\[
 A_m=2\pi\,\frac{\binom{m+1}{(m+1)/2}}{2^{m+1}}>0.
\]
For \(m=1\), every initial condition produces a forward-global solution for **every** \(\varepsilon>0\). In contrast, for every odd \(m\ge3\) and every \(\varepsilon>0\), a nonempty open set of initial data produces finite-time forward escape. On each of the explicitly constructed escaping solutions, the position has a finite limit \(x_\infty\in(-1/8,1/4)\), while the velocity diverges according to
\[
 y(t)\sim [ (m-1)\varepsilon(1-x_\infty^2)(T-t)]^{-1/(m-1)},\quad t\uparrow T<\infty.
\tag{2}
\]
The accompanying positional edge law is
\[
 x_\infty-x(t)\sim\frac{m-1}{m-2}[(m-1)\varepsilon(1-x_\infty^2)]^{-1/(m-1)}(T-t)^{(m-2)/(m-1)}.
\tag{3}
\]
In particular, weak pumping can support a unique stable oscillation while admitting an open set of initial conditions that do not exist for all forward time.

## Assumptions and scope

The phase space is \(\mathbb R^2\); \(m\) is a fixed positive odd integer, and \(\varepsilon\) is positive. The smallness threshold \(\varepsilon_m\) is existential and is not claimed uniform in \(m\). A limit cycle means an isolated periodic orbit of the original physical-time flow. The transverse multiplier is the derivative of the return map to \(\{(r,0):r>0\}\), with crossing from the upper to the lower half-plane. Forward-global means that every maximal solution has endpoint \(+\infty\). Escape means divergence of the velocity at a finite maximal time; the position stays bounded. The original system is polynomial and hence locally well posed.

## Proof

**1. Harmonic return map and cycle existence.** Write \(E=(x^2+y^2)/2\). Along (1),
\[
\dot E=\varepsilon(1-x^2)y^{m+1}.
\tag{4}
\]
At \(\varepsilon=0\), the solution from \((r,0)\) is \(x=r\cos t\), \(y=-r\sin t\), of minimal period \(2\pi\). Fix a compact annulus of section radii about \(\sqrt{m+3}\) away from the origin. Smooth dependence on \(\varepsilon\) gives a well-defined smooth first return and its \(C^1\) perturbation expansion there. Integration of (4) over the unperturbed orbit gives
\[
\begin{aligned}
\Delta E &=\varepsilon r^{m+1}\int_0^{2\pi}(1-r^2\cos^2t)\sin^{m+1}t\,dt+O(\varepsilon^2)\\
&=\varepsilon A_m r^{m+1}\left(1-\frac{r^2}{m+3}\right)+O(\varepsilon^2).
\end{aligned}
\tag{5}
\]
The identity \(\int_0^{2\pi}\cos^2t\sin^{m+1}t\,dt=A_m/(m+3)\) follows from the trigonometric beta-integral recurrence, or by integrating the derivative of \(\sin^{m+2}t\cos t\). Since the energy at a section crossing equals \(r^2/2\), (5) yields
\[
P_\varepsilon(r)-r=\varepsilon A_m r^m\left(1-\frac{r^2}{m+3}\right)+O(\varepsilon^2),
\tag{6}
\]
with the remainder \(C^1\) in \(r\). The coefficient in (6) has a simple positive zero at \(r_0=\sqrt{m+3}\), of derivative \(-2A_m r_0^{m-1}\). Applying the implicit-function theorem to the smoothly extended quotient \((P_\varepsilon(r)-r)/\varepsilon\) gives a periodic orbit at \(r_m(\varepsilon)=r_0+O(\varepsilon)\), with multiplier
\[
P'_\varepsilon(r_m(\varepsilon))=1-2\varepsilon A_m r_0^{m-1}+O(\varepsilon^2)\in(0,1)
\tag{7}
\]
for all sufficiently small positive \(\varepsilon\). This orbit is hyperbolic and attracting.

**2. Global uniqueness for that parameter range.** Theorem 1 of Chen–Xiao–Zhang [1], whose hypothesis and proof are inspected in the cited source, applies to the decomposition \(g(x)=x\), \(f(x)=\varepsilon(x^2-1)\). Both functions are continuously differentiable, \(xg(x)>0\) off zero, the potential \(G(x)=x^2/2\) has equal levels at \(c_1=-1\) and \(c_2=1\), and \(f\) is negative inside the two sign-change points and positive outside. For each positive odd \(m\), the cited theorem says that there is at most one limit cycle in the whole plane and that any such cycle is hyperbolic attracting. Its proof uses the sign of the divergence integral and nesting of planar periodic orbits. The orbit constructed in Step 1 therefore is the sole nonconstant periodic orbit of (1). The external theorem is credited, not claimed anew.

**3. Forward completeness at velocity degree one.** When \(m=1\), equation (4) obeys
\[
\dot E=\varepsilon(1-x^2)y^2\le\varepsilon y^2\le2\varepsilon E.
\]
Gronwall's inequality gives \(E(t)\le E(0)e^{2\varepsilon t}\) on the maximal forward interval. Hence no norm can diverge at a finite time; the polynomial vector field's continuation theorem proves forward globality for every \(\varepsilon>0\).

**4. Open finite-time escape region for all higher odd degrees.** Fix an odd \(m\ge3\) and \(\varepsilon>0\). Choose \(Y>0\) so large that
\[
\varepsilon Y^m\ge1,\qquad \frac{2}{(m-2)\varepsilon Y^{m-2}}<\frac18.
\tag{8}
\]
Take initial conditions in the open set
\[
\mathcal U=\{(x_0,y_0):-1/8<x_0<1/8,\ y_0>Y\}.
\]
As long as \(-1/8\le x\le1/4\) and \(y\ge Y\), we have \(1-x^2\ge15/16\) and \(-x\ge-1/4\), whence
\[
\dot y\ge\frac{15}{16}\varepsilon y^m-\frac14\ge\frac12\varepsilon y^m>0,
\qquad \dot x=y>0.
\tag{9}
\]
Using \(y\) as a parameter and integrating the differential inequality,
\[
\frac{dx}{dy}=\frac{y}{\dot y}\le\frac2{\varepsilon y^{m-1}},\qquad
 x-x_0\le\frac{2}{(m-2)\varepsilon y_0^{m-2}}<\frac18.
\tag{10}
\]
This strict bound prevents exit through \(x=1/4\), and \(x\) cannot exit through \(-1/8\) because it increases. Therefore (9)–(10) hold throughout the maximal forward solution. The comparison \(\dot y\ge\varepsilon y^m/2\) gives a finite maximal time \(T\le2/[(m-1)\varepsilon y_0^{m-1}]\). Continuation of smooth ODEs then forces \(y(t)\to+\infty\), while monotonic bounded \(x(t)\) tends to \(x_\infty\in(-1/8,1/4)\).

**5. Exact escape exponents.** Set \(w(t)=y(t)^{-(m-1)}\). Differentiating and using (1) gives
\[
\dot w=-(m-1)\varepsilon(1-x^2)+(m-1)x\,y^{-m}.
\]
As \(t\uparrow T\), the derivative converges to \(-(m-1)\varepsilon(1-x_\infty^2)<0\), and \(w(T^-)=0\). Integrating over \((t,T)\) proves (2). Integrating \(\dot x=y\) over \((t,T)\) proves (3), because \(1/(m-1)<1\). The coefficient limits are positive and valid for every solution launched in \(\mathcal U\).

## Verification

The standalone script `verify.py` checks the exact trigonometric moment ratios for six odd degrees using rational binomial identities, their sign-changing displacement coefficients, and explicit sufficient escape-cone inequalities. It also performs a deterministic fourth-order Runge–Kutta near-Hamiltonian return-drift comparison for two small-degree examples. The script runs without third-party packages; the executed output is `PASS`. These finite checks support algebraic and numeric reproducibility. The existence, uniqueness, completeness, and escape statements are proved analytically in the preceding steps, not inferred from the finite tests.

## Relationship to prior work

Chen–Xiao–Zhang [1] provide the global uniqueness and hyperbolicity criterion for positive odd velocity powers and explicitly state that it does not prove existence; their three applications concern different polynomial families. The contribution here is the explicit family-wide small-parameter existence law and the sharp contrast between complete and finite-time escaping initial-value problems, with two explicit escape exponents. Villari–Zanolin [2] study superlinear escaping orbits in a different generalized Liénard normal form with a different separation of coordinate variables and damping assumptions; their specific results do not give this polynomial family's threshold or amplitude. Gavrilov–Iliev [3] analyze a six-parameter generalized oscillator whose velocity damping is a polynomial in the separate monomials \(x^2\), \(y^2\), and higher pure powers; it does not include the mixed monomial \(x^2y^3\) required here for \(m=3\). These comparisons identify adjacent techniques and phenomena rather than proving historical uniqueness.

## Limitations

The amplitude/multiplier expansion and existence of the attracting cycle are proved only for sufficiently small \(\varepsilon\), with no uniform threshold in the odd degree. The finite-time escape construction applies to a stated open set, not to every initial condition; no complete basin decomposition is claimed. The blow-up exponents are restricted to the constructed positive-velocity escaping trajectories. The source uniqueness theorem is used as a stated published result with its stated hypotheses; the novelty comparison remains provisional until independent literature review.

## References

1. H. Chen, D. Xiao, R. Zhang, *Some new criteria for the uniqueness of limit cycles in Rayleigh–Liénard systems*, arXiv:2610.33114v1, first publicly posted 23 October 2026. https://arxiv.org/html/2610.33114v1
2. G. Villari and F. Zanolin, *On the Qualitative Behavior of a Class of Generalized Liénard Planar Systems*, Journal of Dynamics and Differential Equations 34 (2022), 179–207. https://doi.org/10.1007/s10884-021-09984-2
3. L. Gavrilov and I. D. Iliev, *The limit cycles in a generalized Rayleigh–Liénard oscillator*, Discrete and Continuous Dynamical Systems 43 (2023), 2381–2400. https://doi.org/10.3934/dcds.2023014
