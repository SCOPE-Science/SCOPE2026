# Exact phase locking excludes hyperchaos in a five-dimensional complex flow
## Finding
For the integer-order complex system reproduced by Lin, Hou, Al-Towailb, and Saberi-Nik, write \(u=x_1+i x_2\), \(v=x_3+i x_4\), and \(z=x_5\). With \(\sigma>0\), \(\beta>0\), and \(r\in\mathbb R\), define
\[
J=\operatorname{{Im}}(\overline u v)=x_1x_4-x_2x_3.
\]
Then
\[
\dot J=-(\sigma+1)J.
\]
It follows that every bounded complete trajectory lies in \(J=0\). Every nontrivial such trajectory has a fixed common complex phase and is a rotation of a trajectory of
\[
\dot X=(\sigma+z)Y-\sigma X,\qquad
\dot Y=(r-z)X-Y,\qquad
\dot z=XY-\beta z.
\]
For every non-equilibrium compact ergodic invariant probability measure, the full five-dimensional Lyapunov spectrum is
\[
\left\{{\lambda,0,-(\sigma+1+\beta)-\lambda,0,-(\sigma+1)}\right\}
\]
for one real exponent \(\lambda\). Hence there is at most one positive exponent, and compact hyperchaos in the usual two-positive-exponent sense is impossible for this integer-order system.

## Assumptions and scope
The system is
\[
\dot x_1=\sigma(x_3-x_1)+x_3x_5,\quad
\dot x_2=\sigma(x_4-x_2)+x_4x_5,
\]
\[
\dot x_3=rx_1-x_3-x_1x_5,\quad
\dot x_4=rx_2-x_4-x_2x_5,\quad
\dot x_5=x_1x_3+x_2x_4-\beta x_5,
\]
with \(\sigma>0\), \(\beta>0\), and arbitrary real \(r\). “Bounded complete” means defined and bounded for all \(t\in\mathbb R\). The Lyapunov-spectrum statement is for non-equilibrium compact ergodic invariant probability measures for which Oseledets exponents are defined; compact support and the smooth polynomial vector field give the usual integrability conditions. The result is not claimed for the Caputo fractional-order model studied later in the source.

## Proof
Differentiate \(J=x_1x_4-x_2x_3\). Direct substitution gives
\[
\begin{{aligned}}
\dot J
&=x_4\dot x_1+x_1\dot x_4-x_3\dot x_2-x_2\dot x_3\\
&=-(\sigma+1)(x_1x_4-x_2x_3)=-(\sigma+1)J.
\end{{aligned}}
\]
Therefore
\[
J(t)=e^{-(\sigma+1)(t-t_0)}J(t_0).
\]
If a complete trajectory were bounded and \(J(t_0)\ne0\), then \(|J(t)|\) would diverge as \(t\to-\infty\), a contradiction. Thus every bounded complete trajectory has \(J\equiv0\).

On \(J=0\), the real two-vectors \((x_1,x_2)\) and \((x_3,x_4)\) are collinear. A nontrivial bounded complete trajectory never meets the axis \(u=v=0\): if it did, uniqueness would keep it on that axis, where \(\dot z=-\beta z\), and bounded completeness would force \(z=0\), giving the origin. Hence at any time there are a phase \(\theta\) and real \(X,Y\), not both zero, such that
\[
u=e^{i\theta}X,\qquad v=e^{i\theta}Y.
\]
The plane with this fixed \(\theta\) is invariant because all coefficients in the \((u,v)\) equations are real. Uniqueness therefore keeps \(\theta\) constant and gives the displayed three-dimensional real flow.

Rotate a non-equilibrium recurrent trajectory so that its fixed phase is \(\theta=0\). The variational equation splits into a real \((\delta x_1,\delta x_3,\delta x_5)\) block, equal to the variational equation of the three-dimensional base, and an imaginary \((\delta x_2,\delta x_4)\) block
\[
\frac d{{dt}}
\begin{{pmatrix}}\delta x_2\\\delta x_4\end{{pmatrix}}
=
\begin{{pmatrix}}-\sigma&\sigma+z\\r-z&-1\end{{pmatrix}}
\begin{{pmatrix}}\delta x_2\\\delta x_4\end{{pmatrix}}.
\]
The vector \((X,Y)\) is a solution of this imaginary block: it is the infinitesimal common-phase rotation. Along an ergodic non-equilibrium recurrent trajectory its exponent is \(0\), because recurrence returns its nonzero norm arbitrarily close to its initial value. The block trace is the constant \(-\sigma-1\), so Liouville's formula gives its other exponent as \(-\sigma-1\).

The base-flow divergence is the constant
\[
-\sigma-1-\beta.
\]
Its flow direction supplies one zero exponent on a non-equilibrium recurrent trajectory, and Liouville's formula makes the other two sum to \(-\sigma-1-\beta\). Writing one of them as \(\lambda\) gives the claimed spectrum. Since their sum is negative, at most one of those two can be positive, while the two additional exponents are \(0\) and \(-\sigma-1<0\).

## Verification
The bundled `verify.py` implements exact multivariate-polynomial arithmetic using only the Python standard library. It verifies the identity \(\dot J+(\sigma+1)J=0\), the full divergence \(-2\sigma-2-\beta\), the base divergence \(-\sigma-1-\beta\), invariance of the fixed-phase real leaf, and the trace \(-\sigma-1\) of the imaginary variational block. These algebraic checks complement, but do not replace, the analytic bounded-completeness and recurrence arguments above.

## Relationship to prior work
Lin et al. reproduce the integer-order system in their Section 2.1 and state that earlier work studied its Lyapunov exponents, chaotic attractors, and ultimate bounds. Their paper then develops a Caputo fractional-order version and boundedness/synchronization theory. Chien et al. explicitly describe hyperchaotic, chaotic, and periodic cases for the nonlinear complex system, and Mahmoud, Al-Kashif, and Farghaly introduced a five-dimensional complex nonlinear system as chaotic and hyperchaotic. The exact relative-phase decay and resulting no-hyperchaos theorem for compact recurrent dynamics were not located in the inspected sources.

A close structural analogue is an exact phase-locking result for the complex Rikitake dynamo, where a different relative-phase defect also decays exponentially. That result concerns a different vector field and does not imply the present coefficient \(-\sigma-1\), the present three-dimensional quotient, or the present Lyapunov split.

## Limitations
The theorem is restricted to the ordinary integer-order differential equation. It does not transfer automatically to Caputo derivatives, where the ordinary product rule used for \(J\) is unavailable. It excludes compact non-equilibrium ergodic states with two positive asymptotic Lyapunov exponents; it does not rule out finite-time intervals with two positive numerical growth rates, nor does it determine whether particular chaotic invariant sets exist. The full 2008 article could not be lawfully obtained during the literature check; its abstract and the accessible 2022 article's explicit attribution were inspected, leaving a residual risk that an unindexed equivalent phase reduction appears in inaccessible material.

## References
1. M. Lin, Y. Hou, M. A. Al-Towailb, H. Saberi-Nik, “The global attractive sets and synchronization of a fractional-order complex dynamical system,” *AIMS Mathematics* 8 (2023), 3523–3541. DOI: 10.3934/math.2023179. Published 22 November 2022.
2. F. Chien, M. Inc, H. R. Yosefzade, H. Saberi Nik, “Predicting the chaos and solution bounds in a complex dynamical system,” *Chaos, Solitons & Fractals* 153 (2021), 111474. DOI: 10.1016/j.chaos.2021.111474.
3. G. M. Mahmoud, M. A. Al-Kashif, A. A. Farghaly, “Chaotic and hyperchaotic attractors of a complex nonlinear system,” *Journal of Physics A: Mathematical and Theoretical* 41 (2008), 055104. DOI: 10.1088/1751-8113/41/5/055104.
