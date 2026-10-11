# Exact fold threshold and square-root splitting for symmetric forced absolute-value equations

## Finding
Let \(L>0\), \(b>0\), and let \(h\in C^3(\mathbb R)\) be \(2L\)-periodic, even, half-wave antisymmetric, and strictly decreasing on \([0,L]\):
\[
h(-t)=h(t),\qquad h(t+L)=-h(t),\qquad h'(t)<0\quad(0<t<L).
\]
Write \(H=h(0)>0\). Consider the scalar nonautonomous equation
\[
\dot x=b|x|+h(t)-c,\qquad c\in\mathbb R.
\]
Define the **weighted half-wave threshold**
\[
c_*:=\frac{b}{1-e^{-bL}}\int_0^L e^{-bt}h(t)\,dt,
\qquad 0<c_*<H.
\]
The number of distinct \(2L\)-periodic solutions is **zero** for \(c<c_*\), **one** for \(c=c_*\), and **two** for \(c>c_*\). At equality, the unique periodic solution has \(x_*(0)=x_*(L)=0\), \(x_*(t)>0\) for \(0<t<L\), and \(x_*(t)<0\) for \(L<t<2L\); it is a nondegenerate semistable fold. For \(c>c_*\), the two periodic solutions have initial values \(x_\pm(0;c)=\pm u(c)\) with \(u(c)>0\), the lower one attracting and the upper one repelling. Their Floquet multipliers have exact product \(1\).

The fold separation is sharp. Put
\[
Q=\frac1{H-c_*}+\frac{e^{bL}}{H+c_*},\qquad
K=\sqrt{\frac{2(1-e^{-bL})}{b^2 Q}}.
\]
Then
\[
u(c)=K\sqrt{c-c_*}+o(\sqrt{c-c_*})\qquad(c\downarrow c_*),
\]
and the two Floquet multipliers obey
\[
\rho_\pm(c)=1\pm 2bQK\sqrt{c-c_*}
+o(\sqrt{c-c_*}).
\]
These formulas are in the original forcing time, with no averaging or small-forcing approximation.

As a two-frequency explicit consequence, if \(\omega>0\), \(A>0\), \(0\le B<A/3\), \(L=\pi/\omega\), and
\[
h(t)=A\cos(\omega t)+B\cos(3\omega t),
\]
then the hypotheses hold and
\[
c_*=b^2\coth\left(\frac{\pi b}{2\omega}\right)
\left(\frac{A}{b^2+\omega^2}+\frac{B}{b^2+9\omega^2}\right).
\]
This example shows that the fold bias depends on the waveform's weighted harmonic content, whereas the leading separation also depends on its peak \(H=A+B\).

## Assumptions and scope
Solutions are classical \(C^1\) functions on the real line. The time-dependent vector field is globally Lipschitz in \(x\), hence every initial value gives a unique global solution. A periodic solution means a function with period \(2L\) under the specified forcing, equivalently a fixed point of the time-\(2L\) map \(P_c(u)=x(2L;0,u,c)\). The strict monotonicity assumption implies that \(h\) has fundamental period \(2L\), so every such solution has minimal period \(2L\). The assertion concerns positive \(b\) and strictly monotone half-wave waveforms; no claim is made for arbitrary periodic forcing or time-varying \(b\).

## Proof
**1. Construct the balanced crossing solution.** Evenness and half-wave antisymmetry imply \(h(L-t)=-h(t)\) and \(h(L)=-H\). The function \(h\) is positive before \(L/2\), negative after \(L/2\), and the weighted integral is positive by pairing \(t\) and \(L-t\):
\[
\int_0^L e^{-bt}h(t)dt
=\int_0^{L/2}\big(e^{-bt}-e^{-b(L-t)}\big)h(t)dt>0.
\]
The formula for \(c_*\) is a positive weighted average of \(h\) on \([0,L]\), hence \(0<c_*<H\). Set \(F(t)=h(t)-c_*\), which decreases strictly on \([0,L]\) from a positive to a negative value. On the first half construct
\[
x_*(t)=e^{bt}\int_0^t e^{-bs}F(s)ds\qquad(0\le t\le L).
\]
By the definition of \(c_*\), the integral vanishes at \(L\). It grows then decreases, so it is strictly positive on \((0,L)\). On \([L,2L]\) construct
\[
x_*(t)=e^{-b(t-L)}\int_L^t e^{b(s-L)}F(s)ds.
\]
The identity \(\int_0^L e^{bs}h(s)ds=-e^{bL}\int_0^L e^{-bs}h(s)ds\), obtained by reflection, implies \(x_*(2L)=0\). Since \(F\) increases from \(-H-c_*\) to \(H-c_*\) on this half, the weighted integral is strictly negative between its two zeros. Both pieces therefore solve the stated absolute-value equation and meet continuously with matching first derivatives at the crossings.

**2. Convexity and global count.** For any parameter \(c\), the time map \(P_c\) is strictly increasing in its initial value by order preservation. It is convex: if \(x_1,x_2\) solve the equation and \(0<\theta<1\), their convex combination \(z\) satisfies \(z'\ge b|z|+h-c\), so scalar comparison gives \(P_c(\theta u_1+(1-\theta)u_2)\le\theta P_c(u_1)+(1-\theta)P_c(u_2)\). For very negative and very positive initial values the entire finite-time trajectory keeps its sign, so
\[
P_c(u)-u\sim(e^{-2bL}-1)u\quad(u\to-\infty),\qquad
P_c(u)-u\sim(e^{2bL}-1)u\quad(u\to+\infty).
\]
Thus displacement tends to \(+\infty\) at both ends. The derivative of the time map along a trajectory having only transverse zeros is
\[
P_c'(u)=\exp\left(b\int_0^{2L}\operatorname{sgn}(x(t;u,c))dt\right).
\]
At \((u,c)=(0,c_*)\), the positive and negative residence times both equal \(L\), so \(P_{c_*}'(0)=1\). By convexity, \(P_{c_*}(u)-u\ge0\), and the strict second derivative computed below makes the contact isolated. As \(c\) increases, solutions and \(P_c(u)\) decrease strictly at every fixed \(u\). Therefore no fixed point exists for \(c<c_*\). For \(c>c_*\), the displacement at \(u=0\) is negative and it tends to \(+\infty\) at both ends; convexity, together with strict monotonicity of the time-map derivative wherever trajectories straddle \(x=0\), yields precisely two simple fixed points. Their derivatives lie, respectively, below and above \(1\). At the threshold there is precisely one fixed point.

**3. Reversible pairing.** Because \(h(-t)=h(t)\), the transformation \(x(t)\mapsto -x(-t)\) preserves the differential equation. It takes a periodic solution with initial value \(u\) to one with initial value \(-u\). Since there are precisely two fixed points above threshold, their initial values are exactly \(\pm u(c)\). Time reversal changes the period-integral of \(\operatorname{sgn}(x)\) to its negative, hence the two positive multipliers are exact reciprocals. The lower initial point is attracting; the upper is repelling.

**4. Exact fold derivatives.** At the threshold, the only zeros of the periodic orbit in one period are at \(0,L,2L\), with transverse velocities \(H-c_*>0\) and \(-H-c_*<0\). Varying the initial value \(u\), the linear sensitivity of the solution at \(L\) is \(e^{bL}\), while at the periodic time boundary it is \(1\). Implicit differentiation of the two crossing times, counting the periodic boundary crossing once, gives
\[
\left.\frac{d}{du}\operatorname{Leb}\{t\in[0,2L]:x(t;u,c_*)>0\}\right|_{u=0}
=\frac1{H-c_*}+\frac{e^{bL}}{H+c_*}=Q.
\]
Consequently, differentiating the time-map multiplier at the balanced cycle yields
\[
\partial_{uu}(P_c(u)-u)|_{(0,c_*)}=2bQ>0.
\]
Differentiating the ODE with respect to \(c\), using the two signs on the critical orbit, gives the exact sensitivity
\[
\partial_c(P_c(u)-u)|_{(0,c_*)}
=-\int_0^{2L}\exp\left(\int_s^{2L}b\operatorname{sgn}(x_*(r))dr\right)ds
=-\frac{2(1-e^{-bL})}{b}<0.
\]
The crossings are transverse, so the time map is twice differentiable in a neighborhood of \((0,c_*)\) by the smooth implicit crossing-time equations, despite the absolute-value kink. Its Taylor expansion is therefore
\[
P_c(u)-u=bQ u^2-\frac{2(1-e^{-bL})}{b}(c-c_*)
+o\big(u^2+|c-c_*|\big).
\]
Solving the fixed-point equation and using the exact reversible pairing gives the claimed \(u(c)\sim K\sqrt{c-c_*}\). Differentiating the local expansion in \(u\) gives the two multiplier expansions. These steps provide an analytic, not numerical, proof of the square-root coefficient.

**5. Explicit harmonic evaluation.** For odd integers \(n\), direct integration gives
\[
\int_0^L e^{-bt}\cos(n\omega t)dt
=\frac{b(1+e^{-bL})}{b^2+n^2\omega^2}
\qquad(L=\pi/\omega).
\]
When \(0\le B<A/3\), the identity \(\sin(3z)=\sin z(3-4\sin^2 z)\) implies \(A\sin z+3B\sin3z>0\) for \(0<z<\pi\); thus \(h\) is strictly decreasing on its first half. Substitution into the general threshold finishes the two-frequency formula.

## Verification
The argument directly checks the two transverse junctions, exact periodicity, time-map convexity, and the local fold derivatives. The supplementary script uses a two-frequency waveform with \(A=1\), \(B=1/8\), \(b=1\), and \(L=\pi\). It reproduces the analytical threshold, confirms the sign of the return displacement on either side of the threshold, and checks the leading square-root coefficient at decreasing offsets. Execute `python3 verification.py` with the Python standard library. The script checks finite computations, not the complete class of smooth waveforms; the infinite-dimensional claim rests on the proof above.

## Relationship to prior work
Gasull and Zhao (2023) prove a sharp general two-cycle upper bound for scalar periodic equations with a constant-sign coefficient multiplying an absolute value, and analyze possible cycle configurations and abstract fold perturbations. The present theorem does not claim that upper bound: it identifies an exact bias threshold as a weighted functional of an **arbitrary strictly monotone even half-wave waveform**, and computes its local square-root splitting constant and reciprocal multipliers. Bravo, Fernández, and Ojeda (2024) study trigonometric-coefficient equations, with finiteness and uniform bounds, but do not state this half-wave functional threshold. Earlier work of Carmona, Freire, Ponce, and Torres (2004) treats a sinusoidally forced piecewise-linear reduction; that special-harmonic literature is a material priority risk, particularly for the single-frequency specialization, but its described forcing class does not cover the general half-wave class asserted here.

## Limitations
The conclusion needs strict first-half monotonicity and reflection symmetries; it is not a universal criterion for arbitrary periodic forcing. The double solution is semistable, not independently validated. The resulting local coefficient does not predict finite-distance branch shapes. Earlier equivalent formulations under different forcing coordinates, particularly in inaccessible older piecewise-linear work, have not been definitively excluded. Numerical checks have only illustrative scope.

## References
1. A. Gasull and Y. Zhao, “Existence of at most two limit cycles for some non-autonomous differential equations,” *Communications on Pure and Applied Analysis* 22 (2023), 970–982. DOI: 10.3934/cpaa.2023016. Public access January 10, 2023.
2. J. L. Bravo, M. Fernández, and I. Ojeda, “Hilbert Number for a Family of Piecewise Nonautonomous Equations,” *Qualitative Theory of Dynamical Systems* (2024). DOI: 10.1007/s12346-023-00922-9.
3. V. Carmona, E. Freire, E. Ponce, and F. Torres, “Invariant manifolds of periodic orbits for piecewise linear three-dimensional systems,” *IMA Journal of Applied Mathematics* 69 (2004), 71–91. DOI: 10.1093/imamat/69.1.71.
4. J. L. Bravo, M. Fernández, and A. Tineo, “Periodic solutions of a periodic scalar piecewise ODE,” *Communications on Pure and Applied Analysis* 6 (2007), 213–228. DOI: 10.3934/cpaa.2007.6.213.
