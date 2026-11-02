# Universal supercritical Hopf onset and exact critical relaxation in a three-cubic-term jerk flow

## Finding
For each real \(b>0\), consider the smooth polynomial system
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=-az-x(x^2+xy+y^2-b),\qquad a>0.
\]
The equilibria \(E_\pm=(\pm\sqrt b,0,0)\) are asymptotically stable for \(a>2\), have a two-dimensional unstable space for \(0<a<2\), and undergo simultaneous **nondegenerate supercritical Hopf bifurcations** at exactly \(a=2\). In the eigenvector normalization specified in the proof, the first Lyapunov coefficient and spectral crossing speed are
\[
\boxed{\ell_1=-\frac{b+1}{\sqrt b\,(b+4)}<0},\qquad
\boxed{\left.\frac{d\operatorname{Re}\lambda}{da}\right|_{a=2}=-\frac{b}{2(b+4)}}.
\]
For each fixed \(b>0\), let \(\delta=2-a\downarrow0^+\). There are two distinct, locally unique, orbitally asymptotically stable cycles near \(E_+\) and \(E_-\), related by reflection. With \(A\) the half-difference between maximum and minimum of the \(x\)-coordinate along either cycle, and \(T\) its least period,
\[
\boxed{A=\sqrt{\frac{2b}{b+1}}\sqrt\delta+O_b(\delta)},\qquad
\boxed{T=\frac{2\pi}{\sqrt b}\left(1+\frac{4b+15}{12(b+1)}\delta\right)+O_b(\delta^2)}.
\]
At the critical parameter \(a=2\), both nonzero equilibria are locally asymptotically stable, but not exponentially stable. In a smooth local complex Hopf coordinate \(u=re^{i\theta}\) whose leading physical displacement is \((x-x_E,y,z)=u q+\bar u\bar q+O(|u|^2)\) with \(q=(1,i\sqrt b,-b)\), every sufficiently close trajectory not in the one-dimensional strong-stable manifold obeys
\[
\boxed{r(t)\sim\sqrt{\frac{b+4}{2(b+1)t}}}\qquad(t\to\infty).
\]
Trajectories in that strong-stable manifold converge exponentially. The same transition occurs at both equilibria by the exact reflection symmetry.

## Assumptions and scope
The parameters are real with \(b>0\), \(a>0\). The limits for the born cycles fix \(b\) and take \(\delta\to0^+\); no uniformity as \(b\to0\) or \(b\to\infty\) is asserted. Cycle uniqueness means in sufficiently small, pairwise disjoint equilibrium neighborhoods, not global uniqueness. The invariant manifolds and critical amplitude concern trajectories initially sufficiently close to the corresponding equilibrium. The origin is also an equilibrium but is not part of the local Hopf claim.

The normal-form convention is \(\dot U=AU+\frac12B(U,U)+\frac16C(U,U,U)+\cdots\), with right Hopf eigenvector \(q_1=1\), conjugate-normalized adjoint eigenvector \(p\) satisfying \(\langle p,q\rangle=1\), and \(\ell_1=\operatorname{Re}G/(2\omega)\) for the standard Kuznetsov multilinear contraction \(G\) below. The physical-time radial cubic coefficient is \(\operatorname{Re}G/2\), so these two numerical conventions are distinguished explicitly.

## Proof
Put \(w=\sqrt b>0\). At either nonzero equilibrium the characteristic polynomial is
\[
P(\lambda)=\lambda^3+a\lambda^2+b\lambda+2b.
\]
For \(a>2\), the Routh-Hurwitz inequalities \(a>0\), \(b>0\), \(2b>0\), and \(ab>2b\) give asymptotic stability. For \(0<a<2\), the Routh array has two sign changes, hence exactly two unstable eigenvalues. At \(a=2\), \(P(\lambda)=(\lambda+2)(\lambda^2+b)\). Implicit differentiation of this cubic at \(\lambda=iw\) yields
\[
\lambda'(2)=\frac{w^2}{-2w^2+4iw}
=-\frac{b}{2(b+4)}-i\frac{w}{b+4}.
\]
The crossing is simple and transversal for every \(b>0\).

At \(E_+\), shift \(X=x-w\), \(Y=y\), \(Z=z\). Then
\[
\dot X=Y,\quad \dot Y=Z,\quad
\dot Z=-2bX-bY-aZ-3wX^2-2wXY-wY^2-X^3-X^2Y-XY^2.
\]
At \(a=2\), set
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\-2b&-b&-2\end{pmatrix},
\quad q=(1,iw,-b)^\mathsf T,
\quad L=\frac{(2iw,\,2+iw,\,1)}{-2b+4iw}.
\]
Then \(Mq=iwq\) and \(Lq=1\). The only nonzero component of the symmetric quadratic and cubic tensors is component three, explicitly
\[
B_3(U,V)=-6wU_1V_1-2w(U_1V_2+U_2V_1)-2wU_2V_2,
\]
\[
C_3(U,V,W)=-6U_1V_1W_1
-2(U_1V_1W_2+U_1V_2W_1+U_2V_1W_1)
-2(U_1V_2W_2+U_2V_1W_2+U_2V_2W_1).
\]
These tensors are derivatives of the displayed cubic vector field and have no hidden scaling. Evaluate the standard Hopf contraction
\[
G=L\left[C(q,q,\bar q)-2B\!\left(q,M^{-1}B(q,\bar q)\right)
+B\!\left(\bar q,(2iwI-M)^{-1}B(q,q)\right)\right].
\]
Direct exact rational-function simplification yields
\[
\boxed{G=-\frac{2(b+1)}{b+4}
-i\frac{4b^2+43b+72}{3\sqrt b\,(b+4)}}.
\]
Thus \(\ell_1=\operatorname{Re}G/(2w)=-(b+1)/(w(b+4))<0\) for every \(b>0\). The cubic coefficient in the physical-time Hopf radial equation is \(\operatorname{Re}G/2=-(b+1)/(b+4)\), while the real linear crossing term is \(b\delta/[2(b+4)]\). Therefore the small-cycle radial radius satisfies
\[
r^2=\frac{b}{2(b+1)}\delta+O_b(\delta^2),
\]
and the leading physical coordinate oscillation has half-amplitude \(2r\), giving the stated \(A\). The negative radial cubic term and positive crossing term imply orbital asymptotic stability of the local cycles; standard nondegenerate Hopf theory gives existence and local uniqueness. The reflection \((x,y,z)\mapsto(-x,-y,-z)\) exchanges the two equilibria and cycles without changing these coefficients.

For the sharper period law, the imaginary part of the linear eigenvalue changes by \(+w\delta/(b+4)\) and the imaginary cubic coefficient is \(\operatorname{Im}G/2\). Combining them with the above radius gives the physical frequency
\[
\Omega=w\left(1-\frac{4b+15}{12(b+1)}\delta\right)+O_b(\delta^2).
\]
Inverting proves the period expansion. As an independent route to the same first correction, substitute the Poincare-Lindstedt expansion \(X=\varepsilon\cos(\Omega t)+\varepsilon^2X_2(\Omega t)+\cdots\), \(\delta=\Delta\varepsilon^2\) into the scalar jerk equation. Removing the two resonant Fourier components at order \(\varepsilon^3\) gives exactly \(\Delta=(b+1)/(2b)\) and \(\Omega=w-(4b+15)\varepsilon^2/(24w)+O_b(\varepsilon^4)\). Since \(\varepsilon=2r+O_b(r^2)\), this agrees with the normal-form frequency. The accompanying checker performs both symbolic calculations with exact arithmetic.

Finally, on \(a=2\), the real transverse eigenvalue is \(-2\) and the center-manifold normal form can be chosen so that
\[
\dot r=-\frac{b+1}{b+4}r^3+O_b(r^5),
\qquad \dot\theta=w+O_b(r^2).
\]
The negative cubic term gives local asymptotic stability of the equilibrium and the one-dimensional exponentially convergent strong-stable manifold. Off that manifold, set \(v=r^{-2}\). Then \(\dot v=2(b+1)/(b+4)+O_b(v^{-1})\), hence \(v(t)/t\to2(b+1)/(b+4)\), establishing the stated algebraic amplitude law. The strong-stable foliation transfers this center-manifold asymptotic to all nearby trajectories outside the exceptional strong-stable curve.

## Verification
Run the standalone script `verify.py` using Python 3 and SymPy. It asserts the Hopf spectral identities, matrix eigenvectors and normalization, symbolic multilinear contraction and its real and imaginary parts, first Lyapunov coefficient, and its relation to the physical frequency correction. It separately computes the Fourier solvability conditions from the original scalar jerk equation and checks their unique exact solution. Finite numerical simulations were used only for independent sanity checks at several values of \(b\); no infinite-time claim relies on them.

## Relationship to prior work
Vaidyanathan and coauthors introduced the exact polynomial jerk family in *Electronics* (2023), identified its three equilibria, and numerically explored bifurcation diagrams and coexisting periodic and chaotic attractors at finite parameters such as \(a=1.4\). Their inspected paper does not provide the uniform exact \(a=2\) Hopf normal-form calculation, supercriticality for all \(b>0\), quantitative local amplitude and frequency laws, or nonhyperbolic critical relaxation. The general 2023 paper of Lăzureanu and Cho discusses Hopf bifurcations in jerk systems at the structural level but does not specialize to and imply these model-specific formulas. Previously published results on Sprott quadratic and other polynomial jerk flows involve different vector fields, not equivalent coefficients for this family. Exact spectral crossing alone is a routine consequence of Routh-Hurwitz and is not presented as a standalone original contribution.

## Limitations
The conclusions are local near \(a=2\) and the two nonzero equilibria. They do not prove global boundedness, exclude other attractors or secondary bifurcations, classify the origin, or establish any security properties of a proposed encryption method. The asymptotic constants are not uniform in \(b\) near zero or infinity. Publication-priority risk remains from unindexed or later works using coordinate changes or an unreported first-Lyapunov-coefficient calculation; targeted published-record and primary-literature searches identified no covering claim. Independent validation has not been performed.

## References
1. S. Vaidyanathan, A. S. T. Kammogne, E. Tlelo-Cuautle et al., “A Novel 3-D Jerk System, Its Bifurcation Analysis, Electronic Circuit Design and a Cryptographic Application,” *Electronics* **12** (2023), 2818; published 2023-06-26. DOI: 10.3390/electronics12132818.
2. C. Lăzureanu and G. Cho, “On Hopf and Fold Bifurcations of Jerk Systems,” *Mathematics* **11** (2023), 4295. DOI: 10.3390/math11204295.
3. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Springer, 2004 (Hopf normal-form convention).
