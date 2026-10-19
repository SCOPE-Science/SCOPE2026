# Sharp Kerr-biased stability windows for regular polygonal Stuart–Landau states

## Finding
For every integer \(M\ge3\), every \(k_r>0\), \(k_i,\omega,C_i\in\mathbb R\), and \(C_r\ge0\), \(\beta>MC_r\), consider the globally coupled complex-amplitude flow
\[
\dot z_j=\bigl(\beta+i\omega-(k_r+i k_i)|z_j|^2\bigr)z_j
 +(C_r+i C_i)\sum_{\ell\ne j}(z_\ell-z_j),\qquad j=0,\ldots,M-1.
\]
Write \(a=\beta-MC_r>0\), \(r=\sqrt{a/k_r}\), \(h=k_i/k_r\), \(x=MC_r/a\), \(y=MC_i/a\), and \(\Omega=\omega-MC_i-ah\). The regular polygon is the exact solution
\[
z_j(t)=r\exp\!\left(i\left(\Omega t+\frac{2\pi j}{M}\right)\right).
\]
Its \((M-2)\)-dimensional local manifold of equal-radius, zero-mean rotating solutions is **normally exponentially attracting** at this polygon if and only if
\[
\boxed{0\le x<1,\qquad (1-x)(y-2h)^2>(2-x)^2(x+h^2).} \tag{1}
\]
This criterion is independent of \(M\) after the normalization above. For \(0<x<1\), equivalently \(MC_r<\beta/2\), the two exact critical reactive-coupling values are
\[
\boxed{y_\pm=2h\pm(2-x)\sqrt{\frac{x+h^2}{1-x}}.} \tag{2}
\]
One has \(y_-<0<y_+\); normal attraction holds exactly for \(y<y_-\) or \(y>y_+\). For \(y_-<y<y_+\), one transverse exponent has positive real part. At either endpoint the transverse spectrum contains a simple nonzero imaginary conjugate pair, so strict normal hyperbolicity is lost.

When \(x=0\), the criterion reads \(y(y-4h)>0\). At \(x=y=0\) two additional normal zero exponents occur, and at \(y=4h\ne0\) there is a transverse imaginary pair. For \(x\ge1\), **a positive transverse real-part exponent occurs for every finite real \(y,h\)**. In particular, the nonlinear frequency-shear parameter \(h\) shifts the midpoint of the stable/unstable reactive-coupling gap to \(2h\), breaking its \(y\mapsto-y\) symmetry. At \(h=0\), (1) reduces to the zero-shear threshold.

## Assumptions and scope
The claim concerns the full \(2M\)-real-dimensional continuous-time system above, with finite \(M\ge3\), positive saturation \(k_r\), identical growth rates \(\beta\), arbitrary Kerr coefficient \(k_i\), arbitrary common natural frequency \(\omega\), and nonnegative dissipative mean-field coupling \(C_r\). The requirement \(\beta>MC_r\) guarantees positive polygon radius. Normal attraction is local to the family of equal-radius phase polygons satisfying \(\sum_j e^{i\theta_j}=0\), in the frame rotating at \(\Omega\); it is not stability of a single distinguished phase polygon within that family. If \(\Omega=0\), the original solution is an equilibrium rather than a nonconstant periodic orbit. Nothing is claimed at nonhyperbolic thresholds about nonlinear attraction or repulsion.

## Proof
**1. Exact polygon and tangent directions.** Since \(\sum_{j=0}^{M-1}e^{2\pi i j/M}=0\), each coordinate of the displayed polygon solves the scalar amplitude-frequency balance. More generally, every equal-radius phase vector satisfying \(\sum_j e^{i\theta_j}=0\) defines a co-rotating equilibrium. The derivative of this complex constraint at the regular polygon is \(i\sum_j e^{2\pi i j/M}\delta\theta_j\), a real-linear map of rank two, because the polygon contains at least three noncollinear vertices. The local polygonal equilibrium manifold is therefore smooth of real dimension \(M-2\).

**2. Entire real spectrum.** In the frame \(w_j=e^{-i\Omega t}z_j\), linearization at \(w_j^*=r e^{i\theta_j}\), \(\theta_j=2\pi j/M\), reads
\[
\delta\dot w_j=-A\delta w_j-Ae^{2i\theta_j}\overline{\delta w_j}+q\overline{\delta w},
\quad A=a(1+ih),\quad q=MC_r+iMC_i,
\quad \overline{\delta w}=M^{-1}\sum_j\delta w_j.
\]
Here the overline on \(\overline{\delta w}\) denotes the arithmetic mean **only**, whereas \(\overline{\delta w_j}\) denotes complex conjugation; they are distinguished by the subscript. Expanding \(\delta w_j=\sum_{k\in\mathbb Z/M\mathbb Z}u_k e^{ik\theta_j}\) gives
\[
\dot u_k=-Au_k-A\overline{u_{2-k}}+q u_0\,\mathbf1_{\{k=0\}}.
\]
For every Fourier component outside \(k=0,2\), the associated real-linear involution has eigenvalues \(0\) and \(-2a\); total multiplicities are \(M-2\) each. The exceptional variables \((u_0,\overline{u_2})\) form a complex-linear two-dimensional system with matrix
\[
B=\begin{pmatrix}-A+q&-A\\-\overline A&-\overline A\end{pmatrix},
\qquad
p(\lambda)=\det(\lambda I-B)
=\lambda^2+(2a-q)\lambda-q\overline A.
\]
Its realification adds the two roots of \(p\) and their complex conjugates. Thus the complete characteristic polynomial of the real Jacobian is
\[
\lambda^{M-2}(\lambda+2a)^{M-2}
\,p(\lambda)\overline{p(\overline\lambda)}.
\]
The displayed \(M-2\) zero modes are exactly tangent to the phase-polygon manifold.

**3. Exact transverse crossing equation.** Rescale \(\mu=\lambda/a\). The exceptional polynomial becomes
\[
\mu^2+(2-x-iy)\mu-(x+iy)(1-ih).
\]
For \(x\ne2\), a root \(\mu=is\) on the imaginary axis necessarily satisfies
\[
s=\frac{y-hx}{2-x},\qquad
0=-s^2+ys-x-hy.
\]
Direct substitution and multiplication by \((2-x)^2\) yields exactly
\[
(1-x)(y-2h)^2-(2-x)^2(x+h^2)=0.
\]
When \(0<x<1\), this equation has precisely the two distinct roots (2). At either root, \(s\ne0\): if \(s=0\), the exceptional constant term vanishes, forcing \(q=0\), contradicting \(x>0\). The other root has negative real part because the complex trace has real part \(x-2<0\). Both crossings are simple, since the crossing equation has distinct simple roots and a second imaginary root would contradict the negative trace.

**4. Which side is attracting?** For \(0<x<1\), at \(y=0\) the exceptional block is unstable for every \(h\). Indeed, for \(h=0\) its real characteristic polynomial has negative constant term \(-x\), hence a positive root; changing \(h\) cannot move an eigenvalue across the imaginary axis because the crossing equation at \(y=0\) is strictly negative. As \(|y|\to\infty\), the two exceptional root real parts tend to \(x-1\) and \(-1\), hence both are negative. The two simple crossings are the only possible changes, proving (1) and (2) for \(0<x<1\).

For \(x=0\), the exceptional roots are nonzero and stable on both tails \(|y|\gg1\), and the only possible imaginary crossings satisfy \(y(y-4h)=0\). At \(y=0\), the exceptional block has an additional zero; when \(h\ne0\), its small root has real part \(hy/2+O(y^2)\), establishing the claimed stability sectors. If \(h=0\), the explicit discriminant shows both roots have strictly negative real part for every \(y\ne0\). For \(1\le x<2\), the crossing expression is strictly negative for all \(y,h\), while \(y=0\) has a positive exponent by the preceding continuity argument. For \(x=2\), the imaginary-root equation forces \(y=2h\), but its remaining real equation becomes \(-(s-h)^2-2-h^2=0\), which is impossible. Finally \(x>2\) has positive real trace \(x-2\). This proves all exclusions and boundary classifications.

**5. Nonlinear local attraction in the strict window.** At a strictly stable polygon, the neutral modes are semisimple and coincide with the tangent space to a smooth manifold of equilibria. All complementary eigenvalues have strictly negative real parts. Choose smooth local coordinates \((\xi,\eta)\) with \(\eta=0\) representing that equilibrium manifold. The vector field has \(\dot\xi=O(|\eta|)\) and \(\dot\eta=L(\xi)\eta+O(|\eta|^2)\). A positive-definite quadratic Lyapunov metric for the Hurwitz matrix \(L(0)\) remains contracting in a sufficiently small neighborhood, uniformly for small \(\xi\). Thus \(|\eta(t)|\) decays exponentially while \(\xi(t)\) converges. The orbit consequently converges exponentially to some nearby polygonal equilibrium in the co-rotating frame.

## Verification
Run `python verify.py` from the same extracted directory. The standalone standard-library script checks the complex Fourier Jacobian identity for eight different population sizes and numerous parameter choices, compares the exact root-real-part criterion to the explicit quadratic roots, and verifies five imaginary-axis boundary cases in rational arithmetic. It returns `PASS: 25810 finite checks`. Separately, a direct full real-Jacobian eigenspectrum calculation for population sizes 3, 4, 5, 8 and 12 and varied parameters agreed with the predicted block spectrum. These calculations test the algebra but are not substitutes for the all-parameter proof above.

## Relationship to prior work
Zhao and Uchida (arXiv:2610.08239v1, §§2,5) provide the mean-field oscillator equation, the polygonal zero-order-parameter manifold, and numerical transverse stability sampling, specializing their dynamics to vanishing Kerr coefficient. Zou and Zhan (2009, §§2,4.3, Appendix B) analyze the splay spectrum with **real** diffusive coupling; their global stability window requires a repulsive real interaction and does not include complex reactive/Kerr competition. Lee, Ott and Antonsen (2013) investigate nonlinear frequency shifts in large populations, principally mean-field collective transitions; an exhaustive implication comparison with their full text remains a priority risk. The zero-Kerr sharp complex-coupling window had also been established previously; the present statement concerns the genuinely nonzero Kerr parameter and its shifted, asymmetric full stability boundary. In particular, it does not present the zero-Kerr specialization as new.

## Limitations
The result assumes identical growth rates, complete-graph mean-field coupling, cubic Stuart–Landau nonlinearities, a regular polygon, and positive radius. It is not a universal stability theorem for every nonregular balanced polygon, heterogeneous growth rates, nonuniform networks, or finite perturbations at critical equality. The local convergence conclusion does not establish a global basin size. The mathematical priority of the Kerr-dependent shift requires independent literature review, especially against older amplitude-phase oscillator theories.

## References
1. L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239v1 (first posted 2026-10-06), https://arxiv.org/html/2610.08239v1, especially §§2,5.
2. W. Zou and M. Zhan, *Splay States in a Ring of Coupled Oscillators: From Local to Global Coupling*, SIAM J. Appl. Dyn. Syst. 8 (2009), 1324–1340, DOI: 10.1137/09075398X, especially §§2,4.3, Appendix B.
3. W. S. Lee, E. Ott, and T. M. Antonsen Jr., *Phase and Amplitude Dynamics in Large Systems of Coupled Oscillators: Growth Heterogeneity, Nonlinear Frequency Shifts and Cluster States*, Chaos 23 (2013), 033116, arXiv:1304.3974.
