# Bessel-weighted caustic asymptotic for a phase-modulated vacuum plane wave

## Finding

Let \(\Omega>0\), fix \(\epsilon\in\mathbb R\) with \(J_2(2\epsilon)\ne0\), and put
\[
\theta(u)=\Omega u+\epsilon\sin(\Omega u),\qquad
R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},\qquad
D=\operatorname{diag}(1,-1).
\]
For each amplitude \(a>0\), consider the four-dimensional plane-wave metric
\[
ds^2=2\,du\,dv+dx_1^2+dx_2^2+x^{\mathsf T}A_a(u)x\,du^2,
\qquad A_a(u)=aR(\theta(u))DR(\theta(u))^{\mathsf T}.
\]
The profile is trace-free, so this is a vacuum plane wave. Let \(B_a\) solve the transverse Jacobi matrix equation
\[
B_a''(u)=A_a(u)B_a(u),\qquad B_a(0)=0,\qquad B_a'(0)=I_2,
\]
and define the first positive conjugate time by
\[
T_c(a)=\inf\{u>0:\det B_a(u)=0\}.
\]
Then the first positive conjugate time exists for all sufficiently small \(a>0\), and
\[
\boxed{\lim_{a\downarrow0}\sqrt a\,T_c(a)=\frac{\pi}{\sqrt{|J_2(2\epsilon)|}}.}
\]
Here \(J_2\) is the Bessel function of the first kind of order two. The rotation frequency \(\Omega\) is held fixed in the limit.

## Assumptions and scope

The profile is smooth and periodic, the null coordinate \(u\) is the affine parameter, and the initial Jacobi data are exactly \(B_a(0)=0\), \(B_a'(0)=I_2\). The limit is taken as \(a\downarrow0\) with fixed \(\Omega>0\) and fixed \(\epsilon\) such that \(J_2(2\epsilon)\ne0\). The result does not cover a joint limit in which \(\epsilon\) approaches a zero of \(J_2(2\epsilon)\); in particular, the unmodulated case \(\epsilon=0\) is excluded.

## Proof

Write \(Q(u)=R(\theta(u))DR(\theta(u))^{\mathsf T}\), so \(A_a=aQ\). Its entries satisfy
\[
Q_{11}(u)+iQ_{12}(u)=e^{2i\theta(u)}.
\]
With \(z=\Omega u\), the Jacobi--Anger expansion gives
\[
e^{2iz+2i\epsilon\sin z}=\sum_{n\in\mathbb Z}J_n(2\epsilon)e^{i(n+2)z}.
\]
The constant Fourier coefficient is \(J_{-2}(2\epsilon)=J_2(2\epsilon)\). Therefore the mean of the periodic matrix \(Q\) over one period is
\[
\overline Q=J_2(2\epsilon)D=:cD,\qquad c\ne0.
\]

Rescale time and the Jacobi matrix by
\[
\tau=\sqrt a\,u,\qquad Y_a(\tau)=\sqrt a\,B_a(\tau/\sqrt a).
\]
Then
\[
Y_a''(\tau)=Q(\tau/\sqrt a)Y_a(\tau),\qquad Y_a(0)=0,\qquad Y_a'(0)=I_2.
\]
The coefficient is bounded and periodic with period \(2\pi\sqrt a/\Omega\) in the \(\tau\)-variable. To justify averaging on each fixed compact \(\tau\)-interval, write the associated first-order system as \(Z_a'=M(\tau/\sqrt a)Z_a\), where
\[
M(s)=\begin{pmatrix}0&I_2\\Q(s)&0\end{pmatrix},\qquad
\overline M=\begin{pmatrix}0&I_2\\cD&0\end{pmatrix}.
\]
The periodic matrix \(M-\overline M\) has mean zero and hence a bounded periodic primitive \(P\). The near-identity change \(Z_a=(I_4+\sqrt a\,P(\tau/\sqrt a))W_a\) cancels the mean-zero term and yields \(W_a'=\overline M W_a+O(\sqrt a)W_a\), uniformly on compact intervals. Grönwall's inequality then gives convergence of the rescaled Jacobi matrices in \(C^1\) on compact intervals to the solution \(Y_0\) of
\[
Y_0''=cDY_0,\qquad Y_0(0)=0,\qquad Y_0'(0)=I_2.
\]

Solving the two scalar equations shows that, for \(\tau>0\),
\[
\det Y_0(\tau)=\frac{\sinh(\sqrt{|c|}\,\tau)\sin(\sqrt{|c|}\,\tau)}{|c|}.
\]
This determinant is strictly positive for \(0<\tau<\tau_0\), where \(\tau_0=\pi/\sqrt{|c|}\), and has a simple zero at \(\tau_0\). Uniform convergence therefore excludes zeros on any compact subinterval of \((0,\tau_0)\) bounded away from zero and places a zero near \(\tau_0\). Near zero, the integral equation and boundedness of \(Q\) give \(Y_a(\tau)=\tau I_2+O(\tau^3)\), with a bound uniform in \(a\); thus \(\det Y_a(\tau)>0\) on a sufficiently small common interval \((0,\delta]\). It follows that the first positive zero \(\tau_c(a)=\sqrt a\,T_c(a)\) converges to \(\tau_0\), proving the stated limit.

## Verification

The trace identity \(\operatorname{tr}A_a=0\) verifies the vacuum condition for the stated plane-wave metric. The Bessel coefficient is obtained from the convergent Jacobi--Anger Fourier expansion, not from finite sampling. The averaging step is justified by a bounded primitive of the zero-mean periodic part and a near-identity transformation; the limiting determinant has a simple first positive zero, and the uniform small-time expansion rules out spurious earlier zeros. No finite numerical experiment is used as proof.

## Relationship to prior work

Flores and Sánchez formulate conjugate points for general plane-fronted waves through a Jacobi equation and a variational problem, but do not state the phase-modulated profile or the Bessel-weighted weak-amplitude asymptotic proved here. Shore derives exact oscillator and van Vleck--Morette formulas for homogeneous plane waves with constant-rate rotating profiles and studies the anti-Mach example; the present profile has nonconstant angular rate \(\theta'(u)=\Omega(1+\epsilon\cos\Omega u)\), so it is outside that homogeneous class. The contribution here is the specific mean-curvature coefficient \(J_2(2\epsilon)\) and the resulting first-caustic scaling law, not a new general averaging theorem.

## Limitations

The result is asymptotic as \(a\downarrow0\) for fixed nonzero \(J_2(2\epsilon)\). It does not give higher-order corrections, the full set of later conjugate times, or a uniform estimate as \(J_2(2\epsilon)\to0\). The primary literature search was bounded; the priority of this particular asymptotic is not independently certified. The exact homogeneous-plane-wave formulas in the literature do not directly cover the phase-modulated profile, but broader work on periodic Jacobi equations remains a residual priority risk.

## References

1. J. L. Flores and M. Sánchez, “Causality and Conjugate Points in General Plane Waves,” *Classical and Quantum Gravity* 20 (2003), 2275–2291; first public preprint arXiv:gr-qc/0211086 (26 November 2002), especially §6.
2. G. M. Shore, “A New Twist on the Geometry of Gravitational Plane Waves,” *Journal of High Energy Physics* 09 (2017), 039; arXiv:1705.09533, especially §§3, 6 and Appendix A.
