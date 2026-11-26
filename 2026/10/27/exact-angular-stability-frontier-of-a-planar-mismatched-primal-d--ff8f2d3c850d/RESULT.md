# Exact angular stability frontier of a planar mismatched primal–dual iteration

## Finding

Consider the constant equal-step, primal-first Chambolle–Pock iteration on isotropic strongly convex quadratics in the plane, with an exact forward operator and a rotated adjoint. For step size \(t>0\) and angle \(\theta\) modulo \(2\pi\), put
\[
H(t)=\frac{2t^4-6t^2-8t-3}{(2t+1)^2},\quad \varphi=\frac{1+\sqrt5}{2},\quad T=1+\sqrt3.
\]
Every initial state converges geometrically to the origin precisely when \(0<t\le\varphi\) and \(\theta\not\equiv\pi\), or when \(\varphi<t<T\) and \(\cos\theta>H(t)\). No rotation yields convergence from every state for \(t\ge T\). At the antipodal rotation the spectral radius is one for every \(t\). For \(\cos\theta>-1\), it is one at \(\cos\theta=H(t)\) and exceeds one at \(\cos\theta<H(t)\).

The frontier is strictly increasing, crossing \(-1\) at \(\varphi\) and \(+1\) at \(T\). For this orthogonal family the angle gives no additional norm-independent information at fixed \(t\): the operator-norm mismatch \(d=\|I_2-R_{-\theta}\|_2=\sqrt{2-2\cos\theta}\) determines \(\cos\theta\). Equivalently the two strict-stability regimes are \(d<2\) for \(0<t\le\varphi\) and \(d<\sqrt{2(1-H(t))}\) for \(\varphi<t<T\). This describes the exact joint step-size and mismatch dependence, rather than a step-size-independent mismatch tolerance. For example, \(H(2)=-11/25\): a right-angle mismatch at step size two is stable, whereas a \(120^\circ\) mismatch admits diverging initial states.

## Assumptions and scope

The primal and dual spaces are both \(\mathbb R^2\), with \(G(x)=\|x\|_2^2/2\), \(F^*(y)=\|y\|_2^2/2\), \(A=I_2\), and implemented adjoint \(R_{-\theta}\). The exact proximal steps with extrapolation one give
\[
x_{n+1}=\frac{x_n-tR_{-\theta}y_n}{1+t},\qquad y_{n+1}=\frac{y_n+t(2x_{n+1}-x_n)}{1+t}.
\]
There is no forcing, noise, restart, roundoff, or parameter variation. All-state convergence refers to this fixed linear update, equivalently to strict spectral radius less than one. The unique saddle of the matched objective is the origin; at the antipodal rotation there are additional fixed states of the mismatched iteration.

## Proof

Let \(u=(1+t)^{-1}\) and identify each planar space with \(\mathbb C\), so that \(R_{-\theta}\) acts by multiplication by \(z=e^{-i\theta}\). The update is the complex matrix
\[
B_z=\begin{pmatrix}u&-utz\\ut(2u-1)&u-2u^2t^2z\end{pmatrix}.
\]
The real update has the spectrum of \(B_z\) and its conjugate. Write its complex characteristic polynomial as \(\lambda^2-P\lambda+Q\), where \(P=2u-2u^2t^2z\) and \(Q=u^2(1-t^2z)\). With \(c=\cos\theta\),
\[
1-|Q|^2=\frac{2t(2+(3+c)t+2t^2)}{(1+t)^4}>0,
\]
\[
(1-|Q|^2)^2-|P-\overline P Q|^2
=\frac{4t^4(1+c)}{(1+t)^8}\left((2t+1)^2c-2t^4+6t^2+8t+3\right).
\]
For example, these expansions use \(z+\bar z=2c\) and \(z\bar z=1\). To see why the sign of the second expression is decisive, let \(a,b\) be the two roots. Substituting \(P=a+b\) and \(Q=ab\) into that expression gives
\[
(1-|a|^2)(1-|b|^2)|1-a\overline b|^2.
\]
Since \(|ab|<1\), the last factor is positive and at least one root is strictly inside the unit disk. Thus the positive, zero and negative signs give spectral radius below, equal to and above one, respectively. At \(c=-1\) one can also read off the roots \(1\) and \((1+t^2)/(1+t)^2\). At \(c>-1\) the sign is precisely the sign of \(c-H(t)\).

Finally,
\[
H'(t)=\frac{4(t+1)(2t^3+1)}{(2t+1)^3},\quad
H(t)+1=\frac{2(t^2-t-1)(t^2+t+1)}{(2t+1)^2},\quad
H(t)-1=\frac{2(t+1)^2(t^2-2t-2)}{(2t+1)^2}.
\]
These identities prove the monotonicity, parameter regimes and endpoint statements. The norm formula follows from \((I_2-R_{-\theta})^T(I_2-R_{-\theta})=2(1-c)I_2\).

## Verification

The supplementary `verify.py` checks the trace and determinant, both margin expansions, the frontier derivative and endpoint identities, along with a finite grid of real-matrix eigenvalues and direct recurrences. The grid is a corroboration; the classification, including the exact equality cases, follows from the root-product argument.

## Relationship to prior work and limitations

The mismatched-adjoint iteration and general sufficient conditions for it are established. Matched scalar results describe the case \(\theta=0\), not the full rotational frontier. The specific claim here is the necessary-and-sufficient joint frontier for the equal-step planar quadratic model, not novelty of the splitting scheme or of polynomial root tests. It does not automatically extend to other mismatch matrices, nonlinear proximal maps, unequal steps, different extrapolation, forcing or finite precision. Historical priority remains subject to equivalent specialized stability calculations.

## References

1. D. A. Lorenz and F. Schneppe, *Chambolle–Pock's Primal-Dual Method with Mismatched Adjoint*, arXiv:2201.04928; *Applied Mathematics & Optimization* **87** (2023), article 22.
2. E. Chouzenoux, A. Contreras, J.-C. Pesquet and M. Savanier, *Convergence Results for Primal-Dual Algorithms in the Presence of Adjoint Mismatch*, *SIAM Journal on Imaging Sciences* **16** (2023), 1–34.
3. E. Chouzenoux, J.-C. Pesquet and F. Roldán, *Solution of Mismatched Monotone+Lipschitz Inclusion Problems*, arXiv:2310.06402.
