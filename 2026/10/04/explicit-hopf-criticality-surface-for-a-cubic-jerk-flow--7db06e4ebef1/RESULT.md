# Explicit Hopf criticality surface for a cubic jerk flow
## Finding
Consider the three-dimensional jerk flow
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=-x-y-z-\alpha z^2+xy-\beta+\gamma z^3,
\]
with real parameters \(\alpha,\beta,\gamma\). Its unique equilibrium is \(E_\beta=(-\beta,0,0)\). The equilibrium is asymptotically stable for every \(\beta>0\) and has unstable dimension two for every \(\beta<0\). At the exact boundary \(\beta=0\), a conjugate pair crosses the imaginary axis transversally and the first Lyapunov coefficient in the normalization stated below is
\[
l_1=\frac{8\alpha^2-13\alpha+15\gamma-1}{20}.
\]
Consequently, whenever \(l_1\ne0\), the boundary is a nondegenerate Hopf bifurcation. If \(l_1>0\), the small periodic branch lies on the stable-equilibrium side \(\beta>0\) and is radially unstable. If \(l_1<0\), it lies on the unstable-equilibrium side \(\beta<0\) and is radially stable. For the article's Case A nonlinearities \(\alpha=23/10\) and \(\gamma=1/20\), \(l_1=1217/2000>0\).

## Assumptions and scope
The claim concerns the printed smooth polynomial ODE and real \(\alpha,\gamma\), with \(\beta\) restricted to a sufficiently small neighborhood of zero for the Hopf-branch statement. No assertion is made that this local branch persists to the finite parameter values used in the article's numerical attractor plots. The codimension-two candidate surface
\[
8\alpha^2-13\alpha+15\gamma-1=0
\]
is excluded from the nondegenerate Hopf conclusion; determining its higher-order type requires a higher-order normal-form calculation.

The first Lyapunov coefficient uses the standard multilinear-form convention
\[
\dot X=AX+\frac12B(X,X)+\frac16C(X,X,X)+\cdots,
\]
with
\[
l_1=\frac12\operatorname{Re}\left\langle p,
C(q,q,\bar q)-2B\!\left(q,A^{-1}B(q,\bar q)\right)
+B\!\left(\bar q,(2iI-A)^{-1}B(q,q)\right)
\right\rangle
\]
at Hopf frequency \(1\), normalized by \(\langle p,q\rangle=1\).

## Proof
Shift the equilibrium to the origin by \(u=x+\beta\), \(v=y\), and \(w=z\). Then
\[
\dot u=v,\qquad \dot v=w,\qquad
\dot w=-u-(1+\beta)v-w-\alpha w^2+uv+\gamma w^3.
\]
The characteristic polynomial at the origin is
\[
p_\beta(\lambda)=\lambda^3+\lambda^2+(1+\beta)\lambda+1.
\]
For this monic cubic, the Routh first column is \(1,1,\beta,1\). Hence \(\beta>0\) gives three open-left-half-plane eigenvalues, whereas \(\beta<0\) gives exactly two open-right-half-plane eigenvalues. At \(\beta=0\),
\[
p_0(\lambda)=(\lambda+1)(\lambda^2+1),
\]
so the spectrum is \(-1,\pm i\). Implicit differentiation of \(p_\beta(\lambda)=0\) along the branch through \(i\) gives
\[
\lambda'(0)=-\frac{i}{-2+2i}=-\frac14+\frac{i}{4},
\]
so the crossing is transversal with \(d\operatorname{Re}\lambda/d\beta=-1/4\).

At \(\beta=0\), take
\[
A=\begin{pmatrix}0&1&0\\0&0&1\\-1&-1&-1\end{pmatrix},\qquad
q=\begin{pmatrix}-1\\-i\\1\end{pmatrix},
\]
and
\[
p=\begin{pmatrix}-1/4-i/4\\-i/2\\1/4-i/4\end{pmatrix}.
\]
Then \(Aq=iq\), \(A^Tp=-ip\), and \(\bar p^Tq=1\). The only nonzero components of the multilinear forms are
\[
B_3(X,Y)=-2\alpha X_3Y_3+X_1Y_2+X_2Y_1,
\qquad
C_3(X,Y,Z)=6\gamma X_3Y_3Z_3.
\]
Direct solution of the two linear systems in the Hopf formula gives
\[
A^{-1}B(q,\bar q)=\begin{pmatrix}2\alpha\\0\\0\end{pmatrix},
\]
and
\[
(2iI-A)^{-1}B(q,q)=
\begin{pmatrix}
2(1-2i)(\alpha-i)/15\\
4(2+i)(\alpha-i)/15\\
8(1-2i)(-\alpha+i)/15
\end{pmatrix}.
\]
Substitution yields the exact complex normal-form contraction
\[
G=\left(\frac1{10}-\frac{i}{30}\right)
\left(8\alpha^2+(-12-3i)\alpha+(9+18i)\gamma-1\right),
\]
and therefore
\[
l_1=\frac12\operatorname{Re}G
=\frac{8\alpha^2-13\alpha+15\gamma-1}{20}.
\]
The radial normal form has leading part
\[
\dot r=-\frac{\beta}{4}r+l_1r^3+\text{higher-order terms}.
\]
Thus a nonzero small branch satisfies \(r^2=\beta/(4l_1)+o(|\beta|)\). Its leading radial derivative is \(\beta/2\): it is unstable when \(l_1>0\), \(\beta>0\), and stable when \(l_1<0\), \(\beta<0\).

## Verification
The accompanying `verify.py` performs exact rational-complex checks of the eigenvectors, adjoint normalization, multilinear contractions, closed-form coefficient, and the source parameter substitutions. It returns `VERIFY_OK` when all identities agree. The proof above is symbolic and does not infer an infinite-parameter statement from numerical sampling.

For the source's Case A nonlinearities,
\[
l_1=\frac{8(23/10)^2-13(23/10)+15(1/20)-1}{20}
=\frac{1217}{2000}>0.
\]
For its second displayed cubic coefficient \(\gamma=1/100\) with \(\alpha=23/10\), the corresponding value is \(1157/2000>0\).

## Relationship to prior work
Vaidyanathan et al. introduce the cubic jerk flow, identify its unique stable equilibrium for positive sample values of \(\beta\), and numerically study periodic and chaotic regimes while varying \(\alpha\), \(\beta\), and \(\gamma\). Their displayed \(\beta\)-scan stays strictly positive and the inspected article does not state the local Hopf normal form or the coefficient above.

The cited 2021 predecessor of Vijayakumar et al. is the \(\gamma=0\) quadratic member, written with a forcing parameter whose sign is opposite to \(\beta\). Its equilibrium linearization already implies the stability exchange at zero forcing. Accordingly, the stability boundary itself is not presented here as original. The added result is the nonlinear Hopf classification for the cubic family: the explicit \(\alpha\)- and \(\gamma\)-dependent first Lyapunov coefficient, the side and stability of the local cycle, and the associated degenerate surface.

Targeted searches of the published-finding index and ordinary literature searches for this exact system, its title, the \(\beta=0\) boundary, and a first Lyapunov coefficient did not return a statement implying this formula. The closest published-finding matches concerned different oscillator families and therefore do not cover this claim.

## Limitations
The result is local near \(E_0\) and \(\beta=0\). It does not determine the global continuation of the small periodic orbit, the global hidden-attractor basin geometry, or whether the local branch reaches the article's finite positive \(\beta\) examples. On \(8\alpha^2-13\alpha+15\gamma-1=0\), higher-order terms must be computed before assigning a bifurcation type. A residual originality risk remains that later or poorly indexed citing literature may contain an equivalent center-manifold calculation; no such coverage was found in the sources inspected.

## References
1. S. Vaidyanathan et al., “Bifurcation Analysis, Synchronization and FPGA Implementation of a New 3-D Jerk System with a Stable Equilibrium,” *Mathematics* 11 (2023), 2623. DOI: 10.3390/math11122623.
2. M. Vijayakumar, A. Karthikeyan, J. Zivcak, O. Krejcar, and H. Namazi, “Dynamical Behavior of a New Chaotic System with One Stable Equilibrium,” *Mathematics* 9 (2021), 3217. DOI: 10.3390/math9243217.
3. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Springer, 2004; standard first-Lyapunov-coefficient convention for Hopf bifurcation.
